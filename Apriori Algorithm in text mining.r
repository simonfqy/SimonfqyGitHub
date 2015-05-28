library(readr)
library(ggvis)
library(tm)
library(compiler)
train<-read_csv("train.csv")

#Now start the Apriori Algorithm, mining the frequently appearing words in 
#product_titles.
goodTrain<-train[which(train$median_relevance>=2.5), ]

inThisLine<-function(corporaLine, words){
  length(intersect(corporaLine, words))==length(words)
}

inThisLineCmpd<-cmpfun(inThisLine)

#requirement: length is an integer greater than or equal to 2.
CoocurringWords<-function(length, corpora, thesaura, lowerbound){
  lengthOfPhrases<-vapply(regmatches(names(thesaura), gregexpr(',', names(thesaura))), length,
                          1)+1
  oneLessWord<-names(thesaura[lengthOfPhrases==length-1])
  words<-vapply(oneLessWord, strsplit, list("brand"), 
                split=',')
  lengthOneLess<-length(oneLessWord)
  
  frequentList<-list()
  wordsAtLevel<-vector()
  linesWithFreq<-list()  
  
  InnerPermutation<-function(wordLista, wordListb, length, corpora, lowerbound){
    #construct a new phrase and test whether it is frequent.
    if(length(intersect(wordLista, wordListb)) != length - 2)
      return(subList<-NULL) #the two words don't share the common part as desired, move for
    # the next word.
    
    # now the two vector of words have length-2 words in common.
    wordsInPhrase<-union(wordLista, wordListb)
    duplicate<-FALSE
    if(length>=3){
      if(length(wordsAtLevel)!=0){            
        #wordsInPrevious<-vapply(wordsAtLevel, strsplit, list("string"), split=',')
        if(any(vapply(wordsAtLevel, setequal, TRUE, 
                      wordsInPhrase))){
          duplicate <- TRUE
          return(subList<-NULL)
        }
      }
    }
    
    phrase<-paste(wordsInPhrase, collapse=',')
    whetherInLine<-vapply(corpora,inThisLineCmpd, TRUE, words=wordsInPhrase)
    if (length >= 3)
      wordsAtLevel<<-c(wordsAtLevel, list(wordsInPhrase))  
    #after iterating through the whole corpora, we could count it.
    if(sum(whetherInLine) < lowerbound)
      return (subList<-NULL)
    positionsTrue<-which(whetherInLine)
    linesWithFreq <<- union(linesWithFreq, positionsTrue)
    subList<-list()
    subList[[phrase]]<-sum(whetherInLine)     
    subList
  }
  
  if (lengthOneLess >= 1){    
    for (i in 1:(lengthOneLess-1)){
      cat(" finding under ", oneLessWord[i], '\t')
      subList<- sapply(words[-(1:i)], InnerPermutation,
                       wordListb=words[[i]], length=length, corpora=corpora, 
                       lowerbound, simplify = FALSE,USE.NAMES=TRUE)
      subList<-unlist(unname(subList))
      freqSubList<-subList[subList >= lowerbound]      
      frequentList<-c(frequentList, freqSubList)   
    }    
  }
  wordsAtLevel<-NULL
  #prune the corpora, keeping lines with frequent itemsets only.
  corporaGlobal<<-corpora[unlist(linesWithFreq)]
  diff<-length(corpora)-length(linesWithFreq)
  cat('\n', diff," lines pruned.\n" )
  frequentList    
}

CoocurringWordsCmpd<-cmpfun(CoocurringWords)

getFreqWords<-function(document){
  corpus<-Corpus(VectorSource(tolower(document)))
  corpus<-tm_map(corpus, removePunctuation)
  corpus<-tm_map(corpus, removeWords, stopwords("english"))
  
  #thesaurus<-vector(mode="character")
  #count<-vector(mode="numeric")
  thesaurus<-list()
  size<-length(corpus)
  corpora<-list()
  for (corpi in corpus){
    #corpi <- corpus[[i]]
    corpi <- unlist(strsplit(corpi, split = ' '))
    trash <- corpi %in% ''
    corpi <- unique(corpi[!trash])
    corpora<-c(corpora, list(corpi))
    titleLength <- length(corpi)
    for (corpij in corpi){
      if (is.null(thesaurus[[corpij]])){
        thesaurus[[corpij]] <- 1
        #count <- c(count, 1)
      }
      else{
        #position <- match(corpi[j], thesaurus)
        #count[position] <- count[position]+1
        thesaurus[[corpij]]<-thesaurus[[corpij]]+1
      }
    }
    #if (i%%100==0)
      #print(i)
  }
    
  thesaurus<-unlist(thesaurus)
  threshold<-length(document)*0.007
  thesaurus<-thesaurus[thesaurus >= threshold]
  #count<-count[which(count >= length(document)*0.008)]
  thesaurus<-thesaurus[order(thesaurus, decreasing=TRUE)]
  #count<-count[order(count, decreasing=TRUE)]  
  thesaurus<-as.list(thesaurus)  
  
  #Now we optimize the algorithm by transaction reduction.
  wordsInThesaurus<-names(thesaurus)
  for(i in 1:size){
    line<-corpora[[i]]
    if(length(intersect(line, wordsInThesaurus))==0){
      if(!exists("garbage"))
        garbage<-i
      else
        garbage<-c(garbage, i)
    }
  }
  corporaGlobal<<-corpora[-garbage]
  cat("\n", length(garbage), "lines pruned.\n")
    
  #Now we should start the recursive part of the Apriori Algorithm.
  for (length in 2:15){
    cat("\nlength ", length, "is under search", '\n')
    append<-CoocurringWordsCmpd(length, corporaGlobal, thesaurus, threshold)
    if ( length(append) == 0 ) break
    if (length(append) ==1 ){
      thesaurus<-c(thesaurus, append)
      break
    }
    thesaurus<-c(thesaurus, append)
  }
  
  thesaurus<-unlist(thesaurus)
  thesaurus<-thesaurus[order(thesaurus, decreasing=TRUE)]
  thesaurus<-as.list(thesaurus)  
  thesaurus
  
#  doc_terms<-DocumentTermMatrix(corpus)
#  removeSparseTerms(doc_terms, 0.008)
#  doc_terms<-as.data.frame(as.matrix(doc_terms))
#  word_counts<-data.frame(Words=colnames(doc_terms), Counts=colSums(doc_terms))
  #Sort from most frequent words to least frequent words
  #word_counts<-word_counts[order(word_counts$Counts, decreasing = TRUE), ]
#  frequentWords<-word_counts[word_counts$Counts>=length(document)*0.008, ]
  #for (length in 2:300){
  #  freqMultiWords<-CoocurringWords(length, frequentWords, doc_terms)
  #  if(length(freqMultiWords$Counts)==0) break
  #  frequentWords<-c(frequentWords, freqMultiWords)
  #}  
  #frequentWords<-frequentWords[order(frequentWords$Counts, decreasing=TRUE), ]
  #print(frequentWords)
#  frequentWords
}
getFreqWordsCompiled<-cmpfun(getFreqWords)
system.time(freqWords<-getFreqWordsCompiled(goodTrain$product_title))
