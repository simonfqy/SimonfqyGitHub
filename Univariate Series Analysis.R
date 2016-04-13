#This code uses ARIMA with outlier detection and threshold model to analyze the tourism
#data.
setwd("C:/Users/Simonfqy/Dropbox/Learing materials/2015 Summer Research/Dataset")
library(forecast)
library(TSA)
library(tsoutliers)
library(compiler)
annual<-read.csv('tourism_data.csv')
series<-list(length(annual))

for (i in 1:length(annual)){
  series[[i]]<-ts(annual[i][!is.na(annual[i])], frequency = 1)
  if (i == 1){
    min <- length(series[[i]])
  }
  if (min > length(series[[i]]))
    min <- length(series[[i]])
}

#At this stage all yearly series are contained in each entry of list "series".
qualified <- NULL
for (i in 1:length(series)){
  if (length(series[[i]]) >= min + 4)
    qualified <- c(qualified, i)
}
series<-series[qualified]
#We have now deleted all series with length less than 11.
#Now we start dividing each series into training and test sets.
training<-list(length(series))
test<-list(length(series))
forecast<-list(length(series))
adjusted<-list(length(series))
mase<-list(length(series))
ResultSumm <- NULL
matFull <- matrix(nrow = 2, ncol = 2)
oneMASE<-list(length(series))
aQuarterMASE<-list(length(series))
halfMASE <- list(length(series))
halfResult <- NULL
aQuarterResult <- NULL
oneResult <- NULL
matHalf <- matrix(nrow = 2, ncol = 2)
matQuarter <- matrix(nrow = 2, ncol = 2)
matOne <- matrix(nrow = 2, ncol = 2)

#Function to compute MASE
calcMASE <- function(fore, train, testing, horizon, freq){
  length <- length(train)
  denominator <- 0
  for (j in (freq + 1):length){
    denominator <- denominator + abs(train[j] - train[j-freq])
  }
  denominator <- denominator/(length - freq)
  numerator <- vector(length = horizon)
  numerator <- abs(testing - fore)
  mean(numerator)/denominator
}
calcMASE <- cmpfun(calcMASE)

measure <- function(fore, train, testing, horizon, freq){
  full <- calcMASE(fore, train, testing, horizon, freq)
  half <- calcMASE(fore[1:(horizon/2)], train, testing[1:(horizon/2)],
                   horizon/2, freq)
  one <- calcMASE(fore[1], train, testing[1], 1, freq)
  if (horizon > 4){
    quar <- calcMASE(fore[1:(horizon/4)], train, testing[1:(horizon/4)],
                     horizon/4, freq)
    output <- list(full, half, quar, one)
    names(output) <- c("full", "half", "quar", "one")
  }
  else{
    output <- list(full, half, one)
    names(output) <- c("full", "half", "one")
  }
  output
}
measure <- cmpfun(measure)

logTransform <- function(subject){
  halfSecMin <- 0
  if (min(subject) > 0)
    series <- log(subject)
  else if (min(subject) == 0){
    halfSecMin <- 0.5 * min(subject[subject != 0])
    series <- log(subject + halfSecMin)
  }
  else
    cat("error! ","\n")
  output <- list(halfSecMin, series)    
  names(output) <- c("halfSecMin", "series")
  output
}
logTransform <- cmpfun(logTransform)

decideTrans<-function(){
  word <- readline(prompt = "Are you going to apply log transformation on the data? ")  
  if (substr(word, 1, 1) == "y")
    transform<-TRUE
  else if (substr(word, 1, 1) == 'n')
    transform<-FALSE
  transform
}

transform <- decideTrans()
#Now run auto.arima with tsoutliers from forecast package.
for (i in 1:(length(series))){
  training[[i]]<-ts(series[[i]][1:(length(series[[i]])-4)], frequency = 1)
  test[[i]] <- ts(series[[i]][(length(series[[i]])-3) : length(series[[i]])], 
                  start = length(series[[i]]) -3, end = length(series[[i]]),
                  frequency = 1)
  if(transform){
    transformed <- log(training[[i]])
    #adjusted[[i]] is actually the adjusted log transformed series.
    adjusted[[i]] <- transformed
    outliers <- tsoutliers(transformed)
    if (length(outliers$index) > 0){
      nmbrOut <- length(outliers$index)
      for (j in 1:nmbrOut){
        adjusted[[i]][outliers$index[j]] <- outliers$replacements[j]
      }
    }
    model<-auto.arima(adjusted[[i]], allowdrift = TRUE, allowmean = TRUE)
    forecast[[i]] <- exp(forecast(model, h = 4)$mean)
  }
  else{
    #this case adjusted[[i]] is the adjusted untransformed series
    adjusted[[i]] <- training[[i]]
    outliers <- tsoutliers(training[[i]])
    if (length(outliers$index) > 0){
      nmbrOut <- length(outliers$index)
      for (j in 1:nmbrOut){
        adjusted[[i]][outliers$index[j]] <- outliers$replacements[j]
      }
    }
    model<-auto.arima(adjusted[[i]], allowdrift = TRUE, allowmean = TRUE)
    forecast[[i]] <- forecast(model, h = 4)$mean
  }
  
  if ( i%%50 == 0 )
    cat("Series ", i, " is being analyzed", "\n")
  #Due to the outlier detection, MASE cannot be directly obtained from 
  #existing functions. We need to write from scratch.  
  store<-measure(forecast[[i]], training[[i]], test[[i]], 4, 1)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  oneMASE[[i]] <- store$one
}
cat("MASE of auto arima forecast with outlier detection for h = 4: ", "\n")
print(mean(unlist(mase)))
matFull[2, 1] <- mean(unlist(mase))
matFull[2, 2] <- median(unlist(mase))
matHalf[2, 1] <- mean(unlist(halfMASE))
matHalf[2, 2] <- median(unlist(halfMASE))
matOne[2, 1] <- mean(unlist(oneMASE))
matOne[2, 2] <- median(unlist(oneMASE))

#Now run auto.arima without outlier detection:
for (i in 1:(length(series))){
  if ( i%%50 == 0 )
    cat("Series ", i, " is being analyzed", "\n")
  if(transform){
    transformed <- log(training[[i]])
    model<-auto.arima(transformed, allowdrift = TRUE, allowmean = TRUE)
    forecast[[i]] <- exp(forecast(model, h = 4)$mean)
  }
  else{
    model<-auto.arima(training[[i]], allowdrift = TRUE, allowmean = TRUE)
    forecast[[i]] <- forecast(model, h = 4)$mean
  }    
  store<- measure(forecast[[i]], training[[i]], test[[i]], 4, 1)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  oneMASE[[i]] <- store$one
}
cat("MASE of auto arima forecast for h = 4: ", "\n")
print(mean(unlist(mase)))
matFull[1, 1] <- mean(unlist(mase))
matFull[1, 2] <- median(unlist(mase))
matHalf[1, 1] <- mean(unlist(halfMASE))
matHalf[1, 2] <- median(unlist(halfMASE))
matOne[1, 1] <- mean(unlist(oneMASE))
matOne[1, 2] <- median(unlist(oneMASE))
ResultSumm <- cbind(ResultSumm, matFull)
colnames(ResultSumm)<-c("Auto ARIMA", "MdASE")
rownames(ResultSumm)<-c("ordinary", "with outlier detection")
halfResult <- cbind(halfResult, matHalf)
colnames(halfResult)<-c("Auto ARIMA", "MdASE")
rownames(halfResult)<-c("ordinary", "with outlier detection")
oneResult <- cbind(oneResult, matOne)
colnames(oneResult)<-c("Auto ARIMA", "MdASE")
rownames(oneResult)<-c("ordinary", "with outlier detection")

#Now run theta method forecast:
for (i in 1:(length(series))){
  if ( i%%50 == 0 )
    cat("Series ", i, " is being analyzed", "\n")
  if(transform){
    transformed <- log(training[[i]])    
    forecast[[i]] <- exp(thetaf(transformed, h = 4)$mean)
  }
  else{
    forecast[[i]] <- thetaf(training[[i]], h = 4)$mean
  }
  store<- measure(forecast[[i]], training[[i]], test[[i]], 4, 1)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  oneMASE[[i]] <- store$one
}
cat("MASE of theta method forecast for h = 4: ", "\n")
print(mean(unlist(mase)))
matFull[1, 1] <- mean(unlist(mase))
matFull[1, 2] <- median(unlist(mase))
matHalf[1, 1] <- mean(unlist(halfMASE))
matHalf[1, 2] <- median(unlist(halfMASE))
matOne[1, 1] <- mean(unlist(oneMASE))
matOne[1, 2] <- median(unlist(oneMASE))

#Now run theta method forecast with outlier detection:
for(i in 1:length(series)){  
  if ( i%%50 == 0 ){
    cat("Series ", i, " is being analyzed", "\n")
  }  
  #Due to the outlier detection, MASE cannot be directly obtained from 
  #existing functions. We need to write from scratch.
  if(transform){    
    forecast[[i]] <- exp(thetaf(adjusted[[i]], h = 4)$mean)
  }
  else{
    forecast[[i]] <- thetaf(adjusted[[i]], h = 4)$mean
  }
  store<- measure(forecast[[i]], training[[i]], test[[i]], 4, 1)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  oneMASE[[i]] <- store$one
}
cat("MASE of theta method forecast with outlier detection for h = 4: ", "\n")
print(mean(unlist(mase)))
matFull[2, 1] <- mean(unlist(mase))
matFull[2, 2] <- median(unlist(mase))
matHalf[2, 1] <- mean(unlist(halfMASE))
matHalf[2, 2] <- median(unlist(halfMASE))
matOne[2, 1] <- mean(unlist(oneMASE))
matOne[2, 2] <- median(unlist(oneMASE))
ResultSumm <- cbind(ResultSumm, matFull)
colnames(ResultSumm)[3:4] <- c("Theta method", "MdASE")
halfResult <- cbind(halfResult, matHalf)
colnames(halfResult)[3:4]<-c("Theta method", "MdASE")
oneResult <- cbind(oneResult, matOne)
colnames(oneResult)[3:4]<-c("Theta method", "MdASE")

#Now run naive method forecast:
for (i in 1:(length(series))){
  if ( i%%50 == 0 )
    cat("Series ", i, " is being analyzed", "\n") 
  forecast[[i]] <- naive(training[[i]], h = 4)$mean
  store<- measure(forecast[[i]], training[[i]], test[[i]], 4, 1)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  oneMASE[[i]] <- store$one
}
cat("MASE of naive method forecast for h = 4: ", "\n")
print(mean(unlist(mase)))
matFull[1, 1] <- mean(unlist(mase))
matFull[1, 2] <- median(unlist(mase))
matHalf[1, 1] <- mean(unlist(halfMASE))
matHalf[1, 2] <- median(unlist(halfMASE))
matOne[1, 1] <- mean(unlist(oneMASE))
matOne[1, 2] <- median(unlist(oneMASE))

#Now run naive method with outlier detection:
for(i in 1:length(series)){  
  if ( i%%50 == 0 ){
    cat("Series ", i, " is being analyzed", "\n")
  }  
  #Due to the outlier detection, MASE cannot be directly obtained from 
  #existing functions. We need to write from scratch.
  if (transform)
    forecast[[i]] <- exp(naive(adjusted[[i]], h = 4)$mean)
  else
    forecast[[i]] <- naive(adjusted[[i]], h = 4)$mean
  
  store<- measure(forecast[[i]], training[[i]], test[[i]], 4, 1)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  oneMASE[[i]] <- store$one
}
cat("MASE of naive method forecast with outlier detection for h = 4: ", "\n")
print(mean(unlist(mase)))
matFull[2, 1] <- mean(unlist(mase))
matFull[2, 2] <- median(unlist(mase))
matHalf[2, 1] <- mean(unlist(halfMASE))
matHalf[2, 2] <- median(unlist(halfMASE))
matOne[2, 1] <- mean(unlist(oneMASE))
matOne[2, 2] <- median(unlist(oneMASE))
ResultSumm <- cbind(ResultSumm, matFull)
colnames(ResultSumm)[5:6] <- c("Naive method", "MdASE")
halfResult <- cbind(halfResult, matHalf)
colnames(halfResult)[5:6]<-c("Naive method", "MdASE")
oneResult <- cbind(oneResult, matOne)
colnames(oneResult)[5:6]<-c("Naive method", "MdASE")

#Now run ETS method:
for (i in 1:(length(series))){
  if ( i%%50 == 0 )
    cat("Series ", i, " is being analyzed", "\n")
  if(transform){
    transformed <- log(training[[i]])
    model<-ets(transformed)
    forecast[[i]] <- exp(forecast(model, h = 4)$mean)
  }
  else{
    model<-ets(training[[i]])
    forecast[[i]] <- forecast(model, h = 4)$mean
  }    
  store<- measure(forecast[[i]], training[[i]], test[[i]], 4, 1)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  oneMASE[[i]] <- store$one
  transformed <- log(training[[i]])
}
cat("MASE of ETS forecast for h = 4: ", "\n")
print(mean(unlist(mase)))
matFull[1, 1] <- mean(unlist(mase))
matFull[1, 2] <- median(unlist(mase))
matHalf[1, 1] <- mean(unlist(halfMASE))
matHalf[1, 2] <- median(unlist(halfMASE))
matOne[1, 1] <- mean(unlist(oneMASE))
matOne[1, 2] <- median(unlist(oneMASE))

#Now run ETS with tsoutliers from forecast package.
for (i in 1:(length(series))){
  if ( i%%50 == 0 ){
    cat("Series ", i, " is being analyzed", "\n")
  }  
  if(transform){
    model<-ets(adjusted[[i]])
    forecast[[i]] <- exp(forecast(model, h = 4)$mean)
  }
  else{
    model<-ets(adjusted[[i]])
    forecast[[i]] <- forecast(model, h = 4)$mean
  }  
  store<-measure(forecast[[i]], training[[i]], test[[i]], 4, 1)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  oneMASE[[i]] <- store$one 
}
cat("MASE of ETS forecast with outlier detection for h = 4: ", "\n")
print(mean(unlist(mase)))
matFull[2, 1] <- mean(unlist(mase))
matFull[2, 2] <- median(unlist(mase))
matHalf[2, 1] <- mean(unlist(halfMASE))
matHalf[2, 2] <- median(unlist(halfMASE))
matOne[2, 1] <- mean(unlist(oneMASE))
matOne[2, 2] <- median(unlist(oneMASE))
ResultSumm <- cbind(ResultSumm, matFull)
colnames(ResultSumm)[7:8] <- c("ETS method", "MdASE")
halfResult <- cbind(halfResult, matHalf)
colnames(halfResult)[7:8]<- c("ETS method", "MdASE")
oneResult <- cbind(oneResult, matOne)
colnames(oneResult)[7:8]<- c("ETS method", "MdASE")


#Now run ETS method with Box-Cox transformation:
if(FALSE){
  for (i in 1:(length(series))){
    if ( i%%50 == 0 )
      cat("Series ", i, " is being analyzed", "\n")
    lam<-BoxCox.lambda(training[[i]])
    model<-ets(training[[i]], lambda = lam)
    forecast[[i]] <- forecast(model, h = 4)
    mase[[i]] <- accuracy(forecast[[i]], test[[i]])[2,6]
  }
  cat("MASE of ETS forecast with Box-Cox transformation for h = 4: ", "\n")
  print(mean(unlist(mase)))
}
#Above method showed NA values, not quite applicable.

#Now run Damped trend method:
for (i in 1:(length(series))){
  if ( i%%50 == 0 )
    cat("Series ", i, " is being analyzed", "\n")
  if(transform){
    transformed <- log(training[[i]])
    model<-ets(transformed, model = "AAN", damped = TRUE)
    forecast[[i]] <- exp(forecast(model, h = 4)$mean)
  }
  else{
    model<-ets(training[[i]], model = "AAN", damped = TRUE)
    forecast[[i]] <- forecast(model, h = 4)$mean
  }
  store<- measure(forecast[[i]], training[[i]], test[[i]], 4, 1)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  oneMASE[[i]] <- store$one
  #mase[[i]] <- accuracy(forecast[[i]], test[[i]])[2,6]
}
cat("MASE of Damped trend forecast for h = 4: ", "\n")
print(mean(unlist(mase)))
matFull[1, 1] <- mean(unlist(mase))
matFull[1, 2] <- median(unlist(mase))
matHalf[1, 1] <- mean(unlist(halfMASE))
matHalf[1, 2] <- median(unlist(halfMASE))
matOne[1, 1] <- mean(unlist(oneMASE))
matOne[1, 2] <- median(unlist(oneMASE))

#Now run Damped trend with outlier detection:
for (i in 1:(length(series))){
  if ( i%%50 == 0 ){
    cat("Series ", i, " is being analyzed", "\n")
  }
  if(transform){
    model<-ets(adjusted[[i]], model = "AAN", damped = TRUE)
    forecast[[i]] <- exp(forecast(model, h = 4)$mean)
  }
  else{
    model<-ets(adjusted[[i]], model = "AAN", damped = TRUE)
    forecast[[i]] <- forecast(model, h = 4)$mean
  }
  store<- measure(forecast[[i]], training[[i]], test[[i]], 4, 1)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  oneMASE[[i]] <- store$one  
}
cat("MASE of Damped trend forecast with outlier detection for h = 4: ", "\n")
print(mean(unlist(mase)))
matFull[2, 1] <- mean(unlist(mase))
matFull[2, 2] <- median(unlist(mase))
matHalf[2, 1] <- mean(unlist(halfMASE))
matHalf[2, 2] <- median(unlist(halfMASE))
matOne[2, 1] <- mean(unlist(oneMASE))
matOne[2, 2] <- median(unlist(oneMASE))
ResultSumm <- cbind(ResultSumm, matFull)
colnames(ResultSumm)[9:10] <- c("Damped trend", "MdASE")
halfResult <- cbind(halfResult, matHalf)
colnames(halfResult)[9:10]<- c("Damped trend", "MdASE")
oneResult <- cbind(oneResult, matOne)
colnames(oneResult)[9:10]<- c("Damped trend", "MdASE")

#Now consider the outlier detection method in package tsoutliers
#Applied to auto arima (Only applicable for certain number of regular diffs):
for (i in 1:(length(series))){
  if ( i%%3 == 1 ){
    cat("Series ", i, " is being analyzed", "\n")
  }
  mase[[i]]<-tryCatch({
    detected <- tso(training[[i]], types = c("AO", "IO"), tsmethod = "auto.arima", 
      args.tsmethod = list(allowdrift = TRUE), remove.method = "bottom-up")
    model <- auto.arima(detected$yadj, allowdrift = TRUE)
    forecast[[i]] <- forecast(model, h = 4)$mean
    mas <- calcMASE(forecast[[i]], training[[i]], test[[i]], 4, 1)
  }, warning = function(war){
    model <- auto.arima(training[[i]], allowdrift = TRUE)
    forecast[[i]] <- forecast(model, h = 4)$mean
    mas <- calcMASE(forecast[[i]], training[[i]], test[[i]], 4, 1)
    return(mas)    
  }, error = function(err){
    cat("Not able to find outliers for this case. ", "\n")
    model <- auto.arima(training[[i]], allowdrift = TRUE)
    forecast[[i]] <- forecast(model, h = 4)$mean
    mas <- calcMASE(forecast[[i]], training[[i]], test[[i]], 4, 1)
    return(mas)
  })
  
}
cat("MASE of auto arima forecast with tso function outlier detection 
    for h = 4: ", "\n")
print(mean(unlist(mase)))
#The above method didn't work well.

print(ResultSumm)

#The first part of phase one is finished.
#Now enter the second part: analysis of monthly series 
seasonal<-read.csv('tourism2_revision2.csv')
monthly<-seasonal[regexpr('m', names(seasonal)) > 0]
quarterly<-seasonal[regexpr('q', names(seasonal)) >0]
series<-list(length(monthly))

for (i in 1:length(monthly)){
  series[[i]]<-ts(monthly[i][!is.na(monthly[i])], frequency = 12)
  if (i == 1){
    min <- length(series[[i]])
  }
  if (min > length(series[[i]]))
    min <- length(series[[i]])
}

#At this stage all monthly series are contained in each entry of list "series".
qualified <- NULL
for (i in 1:length(series)){
  if (length(series[[i]]) >= min + 24)
    qualified <- c(qualified, i)
}
series<-series[qualified]
#We have now deleted all series with length less than min + 24.
#Now we start dividing each series into training and test sets.
training<-list(length(series))
test<-list(length(series))
forecast<-list(length(series))
adjusted<-list(length(series))
trainingTrans <- list(length(series))
mase<-list(length(series))
ResultSumm <- NULL
matFull <- matrix(nrow = 2, ncol = 2)
oneMASE<-list(length(series))
aQuarterMASE<-list(length(series))
halfMASE <- list(length(series))
halfResult <- NULL
aQuarterResult <- NULL
oneResult <- NULL
matHalf <- matrix(nrow = 2, ncol = 2)
matQuarter <- matrix(nrow = 2, ncol = 2)
matOne <- matrix(nrow = 2, ncol = 2)

transform<-decideTrans()

#Now run auto.arima with tsoutliers from forecast package.
for (i in 1:(length(series))){
  training[[i]]<-ts(series[[i]][1:(length(series[[i]])-24)], frequency = 12)
  year<-ceiling(length(series[[i]])/12)
  month <- length(series[[i]]) - 12*(year-1)
  if (month < 12)
    test[[i]] <- ts(data = series[[i]][(length(series[[i]])-23) : length(series[[i]])],
                    start = c(year-2, month+1), frequency = 12)    
  else
    test[[i]] <- ts(data = series[[i]][(length(series[[i]])-23) : length(series[[i]])],
                    start = c(year - 1 , 1), frequency = 12)
  if(transform){
    trainingTrans[[i]]<-logTransform(training[[i]])
    #adjusted[[i]] is actually the adjusted log transformed series.
    adjusted[[i]] <- trainingTrans[[i]]$series
    outliers <- tsoutliers(adjusted[[i]])
    if (length(outliers$index) > 0){
      nmbrOut <- length(outliers$index)
      for (j in 1:nmbrOut){
        adjusted[[i]][outliers$index[j]] <- outliers$replacements[j]
      }
    }
    model<-auto.arima(adjusted[[i]], allowdrift = TRUE, allowmean = TRUE)
    forecast[[i]] <- exp(forecast(model, h = 24)$mean) - trainingTrans[[i]]$halfSecMin
  }
  else{
    #this case adjusted[[i]] is the adjusted untransformed series
    adjusted[[i]] <- training[[i]]
    outliers <- tsoutliers(training[[i]])
    if (length(outliers$index) > 0){
      nmbrOut <- length(outliers$index)
      for (j in 1:nmbrOut){
        adjusted[[i]][outliers$index[j]] <- outliers$replacements[j]
      }
    }
    model<-auto.arima(adjusted[[i]], allowdrift = TRUE, allowmean = TRUE)
    forecast[[i]] <- forecast(model, h = 24)$mean
  }
  if ( i%%40 == 0 )
    cat("Series ", i, " is being analyzed", "\n")
  store<-measure(forecast[[i]], training[[i]], test[[i]], 24, 12)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  aQuarterMASE[[i]] <- store$quar  
  oneMASE[[i]] <- store$one  
}
cat("MASE of auto arima forecast with outlier detection for h = 24: ", "\n")
print(mean(unlist(mase)))
matFull[2, 1] <- mean(unlist(mase))
matFull[2, 2] <- median(unlist(mase))
matHalf[2, 1] <- mean(unlist(halfMASE))
matHalf[2, 2] <- median(unlist(halfMASE))
matQuarter[2, 1] <- mean(unlist(aQuarterMASE))
matQuarter[2, 2] <- median(unlist(aQuarterMASE))
matOne[2, 1] <- mean(unlist(oneMASE))
matOne[2, 2] <- median(unlist(oneMASE))

#Now run auto.arima without outlier detection:
for (i in 1:(length(series))){
  if ( i%%40 == 0 )
    cat("Series ", i, " is being analyzed", "\n")   
  if(transform){
    model<-auto.arima(trainingTrans[[i]]$series, allowdrift = TRUE, allowmean = TRUE)
    forecast[[i]] <- exp(forecast(model, h = 24)$mean) - trainingTrans[[i]]$halfSecMin
  }
  else{
    model<-auto.arima(training[[i]], allowdrift = TRUE, allowmean = TRUE)
    forecast[[i]] <- forecast(model, h = 24)$mean
  }    
  store<- measure(forecast[[i]], training[[i]], test[[i]], 24, 12)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  aQuarterMASE[[i]] <- store$quar 
  oneMASE[[i]] <- store$one
}
cat("MASE of auto arima forecast for h = 24: ", "\n")
print(mean(unlist(mase)))
matFull[1, 1] <- mean(unlist(mase))
matFull[1, 2] <- median(unlist(mase))
matHalf[1, 1] <- mean(unlist(halfMASE))
matHalf[1, 2] <- median(unlist(halfMASE))
matQuarter[1, 1] <- mean(unlist(aQuarterMASE))
matQuarter[1, 2] <- median(unlist(aQuarterMASE))
matOne[1, 1] <- mean(unlist(oneMASE))
matOne[1, 2] <- median(unlist(oneMASE))
ResultSumm <- cbind(ResultSumm, matFull)
colnames(ResultSumm)<-c("Auto ARIMA", "MdASE")
rownames(ResultSumm)<-c("ordinary", "with outlier detection")
halfResult <- cbind(halfResult, matHalf)
colnames(halfResult)<-c("Auto ARIMA", "MdASE")
rownames(halfResult)<-c("ordinary", "with outlier detection")
aQuarterResult <- cbind(aQuarterResult, matQuarter)
colnames(aQuarterResult)<-c("Auto ARIMA", "MdASE")
rownames(aQuarterResult)<-c("ordinary", "with outlier detection")
oneResult <- cbind(oneResult, matOne)
colnames(oneResult)<-c("Auto ARIMA", "MdASE")
rownames(oneResult)<-c("ordinary", "with outlier detection")

#Now run theta method forecast:
deseasonalized<-list(length(series))
for (i in 1:(length(series))){
  if ( i%%50 == 0 )
    cat("Series ", i, " is being analyzed", "\n")
  if(transform){
    decomp <- decompose(trainingTrans[[i]]$series, type = "multi")
    deseasonalized[[i]] <- decomp$x/decomp$seasonal
    forecast[[i]] <- thetaf(deseasonalized[[i]], h = 24)$mean
    seasonal <- decomp$seasonal[(length(decomp$seasonal)-23) : length(decomp$seasonal)]
    forecast[[i]] <- exp(forecast[[i]]*seasonal) - trainingTrans[[i]]$halfSecMin
  }
  else{
    decomp <- decompose(training[[i]], type = "multi")
    deseasonalized[[i]] <- decomp$x/decomp$seasonal
    forecast[[i]] <- thetaf(deseasonalized[[i]], h = 24)$mean
    seasonal <- decomp$seasonal[(length(decomp$seasonal)-23) : 
                                  length(decomp$seasonal)]
    forecast[[i]] <- forecast[[i]]*seasonal
  }    
  store<- measure(forecast[[i]], training[[i]], test[[i]], 24, 12)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  aQuarterMASE[[i]] <- store$quar 
  oneMASE[[i]] <- store$one
}
cat("MASE of theta method forecast for h = 24: ", "\n")
print(mean(unlist(mase)))
matFull[1, 1] <- mean(unlist(mase))
matFull[1, 2] <- median(unlist(mase))
matHalf[1, 1] <- mean(unlist(halfMASE))
matHalf[1, 2] <- median(unlist(halfMASE))
matQuarter[1, 1] <- mean(unlist(aQuarterMASE))
matQuarter[1, 2] <- median(unlist(aQuarterMASE))
matOne[1, 1] <- mean(unlist(oneMASE))
matOne[1, 2] <- median(unlist(oneMASE))

#Now run theta method forecast with outlier detection:
for(i in 1:length(series)){  
  if ( i%%50 == 0 ){
    cat("Series ", i, " is being analyzed", "\n")
  }
  if(transform){
    decomp <- decompose(adjusted[[i]], type = "multi")
    deseasonalized[[i]] <- decomp$x/decomp$seasonal
    forecast[[i]] <- thetaf(deseasonalized[[i]], h = 24)$mean
    seasonal <- decomp$seasonal[(length(decomp$seasonal)-23) : length(decomp$seasonal)]
    forecast[[i]] <- exp(forecast[[i]]*seasonal) - trainingTrans[[i]]$halfSecMin
  }
  else{
    decomp <- decompose(adjusted[[i]], type = "multi")
    deseasonalized[[i]] <- decomp$x/decomp$seasonal
    forecast[[i]] <- thetaf(deseasonalized[[i]], h = 24)$mean
    seasonal <- decomp$seasonal[(length(decomp$seasonal)-23) : 
                                  length(decomp$seasonal)]
    forecast[[i]] <- forecast[[i]]*seasonal
  }    
  store<- measure(forecast[[i]], training[[i]], test[[i]], 24, 12)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  aQuarterMASE[[i]] <- store$quar 
  oneMASE[[i]] <- store$one
}
cat("MASE of theta method forecast with outlier detection for h = 24: ", "\n")
print(mean(unlist(mase)))
matFull[2, 1] <- mean(unlist(mase))
matFull[2, 2] <- median(unlist(mase))
matHalf[2, 1] <- mean(unlist(halfMASE))
matHalf[2, 2] <- median(unlist(halfMASE))
matQuarter[2, 1] <- mean(unlist(aQuarterMASE))
matQuarter[2, 2] <- median(unlist(aQuarterMASE))
matOne[2, 1] <- mean(unlist(oneMASE))
matOne[2, 2] <- median(unlist(oneMASE))
ResultSumm <- cbind(ResultSumm, matFull)
colnames(ResultSumm)[3:4]<-c("Theta method", "MdASE")
halfResult <- cbind(halfResult, matHalf)
colnames(halfResult)[3:4]<-c("Theta method", "MdASE")
aQuarterResult <- cbind(aQuarterResult, matQuarter)
colnames(aQuarterResult)[3:4]<-c("Theta method", "MdASE")
oneResult <- cbind(oneResult, matOne)
colnames(oneResult)[3:4]<-c("Theta method", "MdASE")

#Now run theta method forecast with outlier detection (stl decomposition):
for(i in 1:length(series)){  
  if ( i%%50 == 0 ){
    cat("Series ", i, " is being analyzed", "\n")
  }  
  #Due to the outlier detection, MASE cannot be directly obtained from 
  #existing functions. We need to write from scratch.  
  forecast[[i]] <- exp(stlf(transformed[[i]], forecastfunction = thetaf)$mean) - halfSecMin
  mase[[i]] <- calcMASE(forecast[[i]], training[[i]], test[[i]], 24, 12) 
}
cat("MASE of theta method forecast with outlier detection for h = 24: ", "\n")
print(mean(unlist(mase)))

#Now run snaive method forecast:
for (i in 1:(length(series))){
  if ( i%%50 == 0 )
    cat("Series ", i, " is being analyzed", "\n")
  if(transform){
    forecast[[i]] <- exp(snaive(trainingTrans[[i]]$series, h = 24)$mean) - 
      trainingTrans[[i]]$halfSecMin
  }
  else{
    forecast[[i]] <- snaive(training[[i]], h = 24)$mean
  }    
  store<- measure(forecast[[i]], training[[i]], test[[i]], 24, 12)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  aQuarterMASE[[i]] <- store$quar 
  oneMASE[[i]] <- store$one
}
cat("MASE of snaive method forecast for h = 24: ", "\n")
print(mean(unlist(mase)))
matFull[1, 1] <- mean(unlist(mase))
matFull[1, 2] <- median(unlist(mase))
matHalf[1, 1] <- mean(unlist(halfMASE))
matHalf[1, 2] <- median(unlist(halfMASE))
matQuarter[1, 1] <- mean(unlist(aQuarterMASE))
matQuarter[1, 2] <- median(unlist(aQuarterMASE))
matOne[1, 1] <- mean(unlist(oneMASE))
matOne[1, 2] <- median(unlist(oneMASE))

#Now run Snaive method with outlier detection:
for(i in 1:length(series)){  
  if ( i%%50 == 0 ){
    cat("Series ", i, " is being analyzed", "\n")
  }  
  if(transform){
    forecast[[i]] <- exp(snaive(adjusted[[i]], h = 24)$mean) - 
      trainingTrans[[i]]$halfSecMin
  }
  else{
    forecast[[i]] <- snaive(adjusted[[i]], h = 24)$mean
  }    
  store<- measure(forecast[[i]], training[[i]], test[[i]], 24, 12)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  aQuarterMASE[[i]] <- store$quar 
  oneMASE[[i]] <- store$one
}
cat("MASE of snaive method forecast with outlier detection for h = 24: ", "\n")
print(mean(unlist(mase)))
matFull[2, 1] <- mean(unlist(mase))
matFull[2, 2] <- median(unlist(mase))
matHalf[2, 1] <- mean(unlist(halfMASE))
matHalf[2, 2] <- median(unlist(halfMASE))
matQuarter[2, 1] <- mean(unlist(aQuarterMASE))
matQuarter[2, 2] <- median(unlist(aQuarterMASE))
matOne[2, 1] <- mean(unlist(oneMASE))
matOne[2, 2] <- median(unlist(oneMASE))
ResultSumm <- cbind(ResultSumm, matFull)
colnames(ResultSumm)[5:6]<-c("SNaive method", "MdASE")
halfResult <- cbind(halfResult, matHalf)
colnames(halfResult)[5:6]<-c("SNaive method", "MdASE")
aQuarterResult <- cbind(aQuarterResult, matQuarter)
colnames(aQuarterResult)[5:6]<-c("SNaive method", "MdASE")
oneResult <- cbind(oneResult, matOne)
colnames(oneResult)[5:6]<-c("SNaive method", "MdASE")

#Now run ETS method:
for (i in 1:(length(series))){
  if ( i%%50 == 0 )
    cat("Series ", i, " is being analyzed", "\n")
  if(transform){
    model<-ets(trainingTrans[[i]]$series)
    forecast[[i]] <- exp(forecast(model, h = 24)$mean) - 
      trainingTrans[[i]]$halfSecMin
  }
  else{
    model<-ets(training[[i]])
    forecast[[i]] <- forecast(model, h = 24)$mean
  }    
  store<- measure(forecast[[i]], training[[i]], test[[i]], 24, 12)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  aQuarterMASE[[i]] <- store$quar 
  oneMASE[[i]] <- store$one 
}
cat("MASE of ETS forecast for h = 24: ", "\n")
print(mean(unlist(mase)))
matFull[1, 1] <- mean(unlist(mase))
matFull[1, 2] <- median(unlist(mase))
matHalf[1, 1] <- mean(unlist(halfMASE))
matHalf[1, 2] <- median(unlist(halfMASE))
matQuarter[1, 1] <- mean(unlist(aQuarterMASE))
matQuarter[1, 2] <- median(unlist(aQuarterMASE))
matOne[1, 1] <- mean(unlist(oneMASE))
matOne[1, 2] <- median(unlist(oneMASE))


#Now run ETS with tsoutliers from forecast package.
for (i in 1:(length(series))){
  if ( i%%50 == 0 ){
    cat("Series ", i, " is being analyzed", "\n")
  }  
  if(transform){
    model<-ets(adjusted[[i]])
    forecast[[i]] <- exp(forecast(model, h = 24)$mean)-trainingTrans[[i]]$halfSecMin
  }
  else{
    model<-ets(adjusted[[i]])
    forecast[[i]] <- forecast(model, h = 24)$mean
  }    
  store<- measure(forecast[[i]], training[[i]], test[[i]], 24, 12)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  aQuarterMASE[[i]] <- store$quar 
  oneMASE[[i]] <- store$one 
}
cat("MASE of ETS forecast with outlier detection for h = 24: ", "\n")
print(mean(unlist(mase)))
matFull[2, 1] <- mean(unlist(mase))
matFull[2, 2] <- median(unlist(mase))
matHalf[2, 1] <- mean(unlist(halfMASE))
matHalf[2, 2] <- median(unlist(halfMASE))
matQuarter[2, 1] <- mean(unlist(aQuarterMASE))
matQuarter[2, 2] <- median(unlist(aQuarterMASE))
matOne[2, 1] <- mean(unlist(oneMASE))
matOne[2, 2] <- median(unlist(oneMASE))
ResultSumm <- cbind(ResultSumm, matFull)
colnames(ResultSumm)[7:8]<-c("ETS", "MdASE")
halfResult <- cbind(halfResult, matHalf)
colnames(halfResult)[7:8]<-c("ETS", "MdASE")
aQuarterResult <- cbind(aQuarterResult, matQuarter)
colnames(aQuarterResult)[7:8]<-c("ETS", "MdASE")
oneResult <- cbind(oneResult, matOne)
colnames(oneResult)[7:8]<-c("ETS", "MdASE")

#Now run ETS method with Box-Cox transformation:
if(TRUE){
  for (i in 1:(length(series))){
    if ( i%%50 == 0 )
      cat("Series ", i, " is being analyzed", "\n")
    lam<-BoxCox.lambda(training[[i]])
    model<-ets(training[[i]], lambda = lam)
    forecast[[i]] <- forecast(model, h = 24)
    mase[[i]] <- accuracy(forecast[[i]], test[[i]])[2,6]
  }
  cat("MASE of ETS forecast with Box-Cox transformation for h = 24: ", "\n")
  print(mean(unlist(mase)))
}


#Now run Damped trend method:
for (i in 1:(length(series))){
  if ( i%%50 == 0 )
    cat("Series ", i, " is being analyzed", "\n")
  if(transform){
    model<-ets(trainingTrans[[i]]$series, model = "AAA", damped = TRUE)
    forecast[[i]] <- exp(forecast(model, h = 24)$mean) - 
      trainingTrans[[i]]$halfSecMin
  }
  else{
    model<-ets(training[[i]], model = "AAA", damped = TRUE)
    forecast[[i]] <- forecast(model, h = 24)$mean
  }    
  store<- measure(forecast[[i]], training[[i]], test[[i]], 24, 12)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  aQuarterMASE[[i]] <- store$quar 
  oneMASE[[i]] <- store$one 
}
cat("MASE of Damped trend forecast for h = 24: ", "\n")
print(mean(unlist(mase)))
matFull[1, 1] <- mean(unlist(mase))
matFull[1, 2] <- median(unlist(mase))
matHalf[1, 1] <- mean(unlist(halfMASE))
matHalf[1, 2] <- median(unlist(halfMASE))
matQuarter[1, 1] <- mean(unlist(aQuarterMASE))
matQuarter[1, 2] <- median(unlist(aQuarterMASE))
matOne[1, 1] <- mean(unlist(oneMASE))
matOne[1, 2] <- median(unlist(oneMASE))

#Now run Damped trend with outlier detection:
for (i in 1:(length(series))){
  if ( i%%50 == 0 ){
    cat("Series ", i, " is being analyzed", "\n")
  }
  if(transform){
    model<-ets(adjusted[[i]], model = "AAA", damped = TRUE)
    forecast[[i]] <- exp(forecast(model, h = 24)$mean) - 
      trainingTrans[[i]]$halfSecMin
  }
  else{
    model<-ets(adjusted[[i]], model = "AAA", damped = TRUE)
    forecast[[i]] <- forecast(model, h = 24)$mean
  }
  store<- measure(forecast[[i]], training[[i]], test[[i]], 24, 12)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  aQuarterMASE[[i]] <- store$quar 
  oneMASE[[i]] <- store$one   
}
cat("MASE of Damped trend forecast with outlier detection for h = 24: ", "\n")
print(mean(unlist(mase)))
matFull[2, 1] <- mean(unlist(mase))
matFull[2, 2] <- median(unlist(mase))
matHalf[2, 1] <- mean(unlist(halfMASE))
matHalf[2, 2] <- median(unlist(halfMASE))
matQuarter[2, 1] <- mean(unlist(aQuarterMASE))
matQuarter[2, 2] <- median(unlist(aQuarterMASE))
matOne[2, 1] <- mean(unlist(oneMASE))
matOne[2, 2] <- median(unlist(oneMASE))
ResultSumm <- cbind(ResultSumm, matFull)
colnames(ResultSumm)[9:10]<-c("Damped trend", "MdASE")
halfResult <- cbind(halfResult, matHalf)
colnames(halfResult)[9:10]<-c("Damped trend", "MdASE")
aQuarterResult <- cbind(aQuarterResult, matQuarter)
colnames(aQuarterResult)[9:10]<-c("Damped trend", "MdASE")
oneResult <- cbind(oneResult, matOne)
colnames(oneResult)[9:10]<-c("Damped trend", "MdASE")

#Now consider the outlier detection method in package tsoutliers
#Applied to auto arima (Only applicable for certain number of regular diffs):
if(FALSE){
  for (i in 1:(length(series))){
    if ( i%%20 == 1 ){
      cat("Series ", i, " is being analyzed", "\n")
    }
    mase[[i]]<-tryCatch({
      detected <- tso(training[[i]], types = c("AO", "IO"), tsmethod = "auto.arima", 
                      args.tsmethod = list(allowdrift = TRUE), remove.method = "bottom-up")
      model <- auto.arima(detected$yadj, allowdrift = TRUE)
      forecast[[i]] <- forecast(model, h = 24)$mean
      mas <- calcMASE(forecast[[i]], training[[i]], test[[i]], 24, 12) 
    }, warning = function(war){
      model <- auto.arima(detected$yadj, allowdrift = TRUE)
      forecast[[i]] <- forecast(model, h = 24)$mean
      mas <- calcMASE(forecast[[i]], training[[i]], test[[i]], 24, 12) 
      return(mas)    
    }, error = function(err){
      cat("Not able to find outliers for this case. ", "\n")
      model <- auto.arima(training[[i]], allowdrift = TRUE)
      forecast[[i]] <- forecast(model, h = 24)$mean
      mas <- calcMASE(forecast[[i]], training[[i]], test[[i]], 24, 12) 
      return(mas)    
    })
    
  }
  cat("MASE of auto arima forecast with tso function outlier detection 
    for h = 24: ", "\n")
  print(mean(unlist(mase)))
}
#The above method gave rise to many NaN values. Not applicable.

print(ResultSumm)

#The second part of phase one is finished.
#Now enter the third part: analysis of quarterly series 
if(TRUE){
  series<-list(length(quarterly))
  
  for (i in 1:length(quarterly)){
    series[[i]]<-ts(quarterly[i][!is.na(quarterly[i])], frequency = 4)
    if (i == 1){
      min <- length(series[[i]])
    }
    if (min > length(series[[i]]))
      min <- length(series[[i]])
  }
  
  #At this stage all quarterly series are contained in each entry of list "series".
  qualified <- NULL
  for (i in 1:length(series)){
    if (length(series[[i]]) >= min + 8)
      qualified <- c(qualified, i)
  }
  series<-series[qualified]
  #We have now deleted all series with length less than 11.
  #Now we start dividing each series into training and test sets.
  training<-list(length(series))
  test<-list(length(series))
  forecast<-list(length(series))
  adjusted<-list(length(series))
  trainingTrans <- list(length(series))
  mase<-list(length(series))
  ResultSumm <- NULL
  matFull <- matrix(nrow = 2, ncol = 2)
  oneMASE<-list(length(series))
  aQuarterMASE<-list(length(series))
  halfMASE <- list(length(series))
  halfResult <- NULL
  aQuarterResult <- NULL
  oneResult <- NULL
  matHalf <- matrix(nrow = 2, ncol = 2)
  matQuarter <- matrix(nrow = 2, ncol = 2)
  matOne <- matrix(nrow = 2, ncol = 2)
  
  transform<-decideTrans()
  
  #Now run auto.arima with tsoutliers from forecast package.
  for (i in 1:(length(series))){
    training[[i]]<-ts(series[[i]][1:(length(series[[i]])-8)], frequency = 4)
    year<-ceiling(length(series[[i]])/4)
    quarter <- length(series[[i]]) - 4*(year-1)
    if (quarter < 4)
      test[[i]] <- ts(data = series[[i]][(length(series[[i]])-7) : length(series[[i]])],
                      start = c(year-2, quarter+1), frequency = 4)    
    else
      test[[i]] <- ts(data = series[[i]][(length(series[[i]])-7) : length(series[[i]])],
                      start = c(year - 1 , 1), frequency = 4)  
    if(transform){
      trainingTrans[[i]]<-logTransform(training[[i]])
      #adjusted[[i]] is actually the adjusted log transformed series.
      adjusted[[i]] <- trainingTrans[[i]]$series
      outliers <- tsoutliers(adjusted[[i]])
      if (length(outliers$index) > 0){
        nmbrOut <- length(outliers$index)
        for (j in 1:nmbrOut){
          adjusted[[i]][outliers$index[j]] <- outliers$replacements[j]
        }
      }
      model<-auto.arima(adjusted[[i]], allowdrift = TRUE, allowmean = TRUE)
      forecast[[i]] <- exp(forecast(model, h = 8)$mean) - trainingTrans[[i]]$halfSecMin
    }
    else{
      #this case adjusted[[i]] is the adjusted untransformed series
      adjusted[[i]] <- training[[i]]
      outliers <- tsoutliers(training[[i]])
      if (length(outliers$index) > 0){
        nmbrOut <- length(outliers$index)
        for (j in 1:nmbrOut){
          adjusted[[i]][outliers$index[j]] <- outliers$replacements[j]
        }
      }
      model<-auto.arima(adjusted[[i]], allowdrift = TRUE, allowmean = TRUE)
      forecast[[i]] <- forecast(model, h = 8)$mean
    }
    if ( i%%40 == 0 )
      cat("Series ", i, " is being analyzed", "\n")
    store<-measure(forecast[[i]], training[[i]], test[[i]], 8, 4)
    mase[[i]] <- store$full
    halfMASE[[i]] <- store$half
    aQuarterMASE[[i]] <- store$quar  
    oneMASE[[i]] <- store$one      
  }
  cat("MASE of auto arima forecast with outlier detection for h = 8: ", "\n")
  print(mean(unlist(mase)))
  matFull[2, 1] <- mean(unlist(mase))
  matFull[2, 2] <- median(unlist(mase))
  matHalf[2, 1] <- mean(unlist(halfMASE))
  matHalf[2, 2] <- median(unlist(halfMASE))
  matQuarter[2, 1] <- mean(unlist(aQuarterMASE))
  matQuarter[2, 2] <- median(unlist(aQuarterMASE))
  matOne[2, 1] <- mean(unlist(oneMASE))
  matOne[2, 2] <- median(unlist(oneMASE))
  
  #Now run auto.arima without outlier detection:
  for (i in 1:(length(series))){
    if ( i%%30 == 0 )
      cat("Series ", i, " is being analyzed", "\n")
    if(transform){
      model<-auto.arima(trainingTrans[[i]]$series, allowdrift = TRUE, allowmean = TRUE)
      forecast[[i]] <- exp(forecast(model, h = 8)$mean) - trainingTrans[[i]]$halfSecMin
    }
    else{
      model<-auto.arima(training[[i]], allowdrift = TRUE, allowmean = TRUE)
      forecast[[i]] <- forecast(model, h = 8)$mean
    }    
    store<- measure(forecast[[i]], training[[i]], test[[i]], 8, 4)
    mase[[i]] <- store$full
    halfMASE[[i]] <- store$half
    aQuarterMASE[[i]] <- store$quar 
    oneMASE[[i]] <- store$one
    #mase[[i]] <- accuracy(forecast[[i]], test[[i]])[2,6]
  }
  cat("MASE of auto arima forecast for h = 8: ", "\n")
  print(mean(unlist(mase)))
  matFull[1, 1] <- mean(unlist(mase))
  matFull[1, 2] <- median(unlist(mase))
  matHalf[1, 1] <- mean(unlist(halfMASE))
  matHalf[1, 2] <- median(unlist(halfMASE))
  matQuarter[1, 1] <- mean(unlist(aQuarterMASE))
  matQuarter[1, 2] <- median(unlist(aQuarterMASE))
  matOne[1, 1] <- mean(unlist(oneMASE))
  matOne[1, 2] <- median(unlist(oneMASE))
  ResultSumm <- cbind(ResultSumm, matFull)
  colnames(ResultSumm)<-c("Auto ARIMA", "MdASE")
  rownames(ResultSumm)<-c("ordinary", "with outlier detection")
  halfResult <- cbind(halfResult, matHalf)
  colnames(halfResult)<-c("Auto ARIMA", "MdASE")
  rownames(halfResult)<-c("ordinary", "with outlier detection")
  aQuarterResult <- cbind(aQuarterResult, matQuarter)
  colnames(aQuarterResult)<-c("Auto ARIMA", "MdASE")
  rownames(aQuarterResult)<-c("ordinary", "with outlier detection")
  oneResult <- cbind(oneResult, matOne)
  colnames(oneResult)<-c("Auto ARIMA", "MdASE")
  rownames(oneResult)<-c("ordinary", "with outlier detection")
  
  #Now run theta method forecast:
  deseasonalized<-list(length(series))  
  for (i in 1:(length(series))){
    if ( i%%50 == 0 )
      cat("Series ", i, " is being analyzed", "\n")
    if(transform){
      decomp <- decompose(trainingTrans[[i]]$series, type = "multi")
      deseasonalized[[i]] <- decomp$x/decomp$seasonal
      forecast[[i]] <- thetaf(deseasonalized[[i]], h = 8)$mean
      seasonal <- decomp$seasonal[(length(decomp$seasonal)-7) : length(decomp$seasonal)]
      forecast[[i]] <- exp(forecast[[i]]*seasonal) - trainingTrans[[i]]$halfSecMin
    }
    else{
      decomp <- decompose(training[[i]], type = "multi")
      deseasonalized[[i]] <- decomp$x/decomp$seasonal
      forecast[[i]] <- thetaf(deseasonalized[[i]], h = 8)$mean
      seasonal <- decomp$seasonal[(length(decomp$seasonal)-7) : 
                                    length(decomp$seasonal)]
      forecast[[i]] <- forecast[[i]]*seasonal
    }    
    store<- measure(forecast[[i]], training[[i]], test[[i]], 8, 4)
    mase[[i]] <- store$full
    halfMASE[[i]] <- store$half
    aQuarterMASE[[i]] <- store$quar 
    oneMASE[[i]] <- store$one
  }
  cat("MASE of theta method forecast for h = 8: ", "\n")
  print(mean(unlist(mase)))
  matFull[1, 1] <- mean(unlist(mase))
  matFull[1, 2] <- median(unlist(mase))
  matHalf[1, 1] <- mean(unlist(halfMASE))
  matHalf[1, 2] <- median(unlist(halfMASE))
  matQuarter[1, 1] <- mean(unlist(aQuarterMASE))
  matQuarter[1, 2] <- median(unlist(aQuarterMASE))
  matOne[1, 1] <- mean(unlist(oneMASE))
  matOne[1, 2] <- median(unlist(oneMASE))
  
  #Now run theta method forecast with outlier detection:
  for(i in 1:length(series)){  
    if ( i%%50 == 0 ){
      cat("Series ", i, " is being analyzed", "\n")
    }
    if(transform){
      decomp <- decompose(adjusted[[i]], type = "multi")
      deseasonalized[[i]] <- decomp$x/decomp$seasonal
      forecast[[i]] <- thetaf(deseasonalized[[i]], h = 8)$mean
      seasonal <- decomp$seasonal[(length(decomp$seasonal)-7) : length(decomp$seasonal)]
      forecast[[i]] <- exp(forecast[[i]]*seasonal) - trainingTrans[[i]]$halfSecMin
    }
    else{
      decomp <- decompose(adjusted[[i]], type = "multi")
      deseasonalized[[i]] <- decomp$x/decomp$seasonal
      forecast[[i]] <- thetaf(deseasonalized[[i]], h = 8)$mean
      seasonal <- decomp$seasonal[(length(decomp$seasonal)-7) : 
                                    length(decomp$seasonal)]
      forecast[[i]] <- forecast[[i]]*seasonal
    }    
    store<- measure(forecast[[i]], training[[i]], test[[i]], 8, 4)
    mase[[i]] <- store$full
    halfMASE[[i]] <- store$half
    aQuarterMASE[[i]] <- store$quar 
    oneMASE[[i]] <- store$one
  }
  cat("MASE of theta method forecast with outlier detection for h = 8: ", "\n")
  print(mean(unlist(mase)))
  matFull[2, 1] <- mean(unlist(mase))
  matFull[2, 2] <- median(unlist(mase))
  matHalf[2, 1] <- mean(unlist(halfMASE))
  matHalf[2, 2] <- median(unlist(halfMASE))
  matQuarter[2, 1] <- mean(unlist(aQuarterMASE))
  matQuarter[2, 2] <- median(unlist(aQuarterMASE))
  matOne[2, 1] <- mean(unlist(oneMASE))
  matOne[2, 2] <- median(unlist(oneMASE))
  ResultSumm <- cbind(ResultSumm, matFull)
  colnames(ResultSumm)[3:4]<-c("Theta method", "MdASE")
  halfResult <- cbind(halfResult, matHalf)
  colnames(halfResult)[3:4]<-c("Theta method", "MdASE")
  aQuarterResult <- cbind(aQuarterResult, matQuarter)
  colnames(aQuarterResult)[3:4]<-c("Theta method", "MdASE")
  oneResult <- cbind(oneResult, matOne)
  colnames(oneResult)[3:4]<-c("Theta method", "MdASE")
  
  #Now run theta method forecast with outlier detection (stl decomposition):
  for(i in 1:length(series)){  
    if ( i%%50 == 0 ){
      cat("Series ", i, " is being analyzed", "\n")
    }  
    #Due to the outlier detection, MASE cannot be directly obtained from 
    #existing functions. We need to write from scratch.
    forecast[[i]] <- stlf(adjusted[[i]], forecastfunction = thetaf)$mean
    mase[[i]] <- calcMASE(forecast[[i]], training[[i]], test[[i]], 8, 4) 
  }
  cat("MASE of theta method forecast with outlier detection for h = 8: ", "\n")
  print(mean(unlist(mase)))
  
  #Now run snaive method forecast:
  for (i in 1:(length(series))){
    if ( i%%50 == 0 )
      cat("Series ", i, " is being analyzed", "\n")
    if(transform){
      forecast[[i]] <- exp(snaive(trainingTrans[[i]]$series, h = 8)$mean) - 
        trainingTrans[[i]]$halfSecMin
    }
    else{
      forecast[[i]] <- snaive(training[[i]], h = 8)$mean
    }    
    store<- measure(forecast[[i]], training[[i]], test[[i]], 8, 4)
    mase[[i]] <- store$full
    halfMASE[[i]] <- store$half
    aQuarterMASE[[i]] <- store$quar 
    oneMASE[[i]] <- store$one
  }
  cat("MASE of snaive method forecast for h = 8: ", "\n")
  print(mean(unlist(mase)))
  matFull[1, 1] <- mean(unlist(mase))
  matFull[1, 2] <- median(unlist(mase))
  matHalf[1, 1] <- mean(unlist(halfMASE))
  matHalf[1, 2] <- median(unlist(halfMASE))
  matQuarter[1, 1] <- mean(unlist(aQuarterMASE))
  matQuarter[1, 2] <- median(unlist(aQuarterMASE))
  matOne[1, 1] <- mean(unlist(oneMASE))
  matOne[1, 2] <- median(unlist(oneMASE))
  
  #Now run Snaive method with outlier detection:
  for(i in 1:length(series)){  
    if ( i%%50 == 0 ){
      cat("Series ", i, " is being analyzed", "\n")
    }  
    if(transform){
      forecast[[i]] <- exp(snaive(adjusted[[i]], h = 8)$mean) - 
        trainingTrans[[i]]$halfSecMin
    }
    else{
      forecast[[i]] <- snaive(adjusted[[i]], h = 8)$mean
    }    
    store<- measure(forecast[[i]], training[[i]], test[[i]], 8, 4)
    mase[[i]] <- store$full
    halfMASE[[i]] <- store$half
    aQuarterMASE[[i]] <- store$quar 
    oneMASE[[i]] <- store$one
  }
  cat("MASE of snaive method forecast with outlier detection for h = 8: ", "\n")
  print(mean(unlist(mase)))
  matFull[2, 1] <- mean(unlist(mase))
  matFull[2, 2] <- median(unlist(mase))
  matHalf[2, 1] <- mean(unlist(halfMASE))
  matHalf[2, 2] <- median(unlist(halfMASE))
  matQuarter[2, 1] <- mean(unlist(aQuarterMASE))
  matQuarter[2, 2] <- median(unlist(aQuarterMASE))
  matOne[2, 1] <- mean(unlist(oneMASE))
  matOne[2, 2] <- median(unlist(oneMASE))
  ResultSumm <- cbind(ResultSumm, matFull)
  colnames(ResultSumm)[5:6]<-c("SNaive method", "MdASE")
  halfResult <- cbind(halfResult, matHalf)
  colnames(halfResult)[5:6]<-c("SNaive method", "MdASE")
  aQuarterResult <- cbind(aQuarterResult, matQuarter)
  colnames(aQuarterResult)[5:6]<-c("SNaive method", "MdASE")
  oneResult <- cbind(oneResult, matOne)
  colnames(oneResult)[5:6]<-c("SNaive method", "MdASE")
  
  #Now run ETS method:
  for (i in 1:(length(series))){
    if ( i%%50 == 0 )
      cat("Series ", i, " is being analyzed", "\n")
    if(transform){
      model<-ets(trainingTrans[[i]]$series)
      forecast[[i]] <- exp(forecast(model, h = 8)$mean) - 
        trainingTrans[[i]]$halfSecMin
    }
    else{
      model<-ets(training[[i]])
      forecast[[i]] <- forecast(model, h = 8)$mean
    }    
    store<- measure(forecast[[i]], training[[i]], test[[i]], 8, 4)
    mase[[i]] <- store$full
    halfMASE[[i]] <- store$half
    aQuarterMASE[[i]] <- store$quar 
    oneMASE[[i]] <- store$one 
  }
  cat("MASE of ETS forecast for h = 8: ", "\n")
  print(mean(unlist(mase)))
  matFull[1, 1] <- mean(unlist(mase))
  matFull[1, 2] <- median(unlist(mase))
  matHalf[1, 1] <- mean(unlist(halfMASE))
  matHalf[1, 2] <- median(unlist(halfMASE))
  matQuarter[1, 1] <- mean(unlist(aQuarterMASE))
  matQuarter[1, 2] <- median(unlist(aQuarterMASE))
  matOne[1, 1] <- mean(unlist(oneMASE))
  matOne[1, 2] <- median(unlist(oneMASE))  
  
  #Now run ETS with tsoutliers from forecast package.
  for (i in 1:(length(series))){
    if ( i%%50 == 0 ){
      cat("Series ", i, " is being analyzed", "\n")
    }  
    if(transform){
      model<-ets(adjusted[[i]])
      forecast[[i]] <- exp(forecast(model, h = 8)$mean)-trainingTrans[[i]]$halfSecMin
    }
    else{
      model<-ets(adjusted[[i]])
      forecast[[i]] <- forecast(model, h = 8)$mean
    }    
    store<- measure(forecast[[i]], training[[i]], test[[i]], 8, 4)
    mase[[i]] <- store$full
    halfMASE[[i]] <- store$half
    aQuarterMASE[[i]] <- store$quar 
    oneMASE[[i]] <- store$one 
  }
  cat("MASE of ETS forecast with outlier detection for h = 8: ", "\n")
  print(mean(unlist(mase)))
  matFull[2, 1] <- mean(unlist(mase))
  matFull[2, 2] <- median(unlist(mase))
  matHalf[2, 1] <- mean(unlist(halfMASE))
  matHalf[2, 2] <- median(unlist(halfMASE))
  matQuarter[2, 1] <- mean(unlist(aQuarterMASE))
  matQuarter[2, 2] <- median(unlist(aQuarterMASE))
  matOne[2, 1] <- mean(unlist(oneMASE))
  matOne[2, 2] <- median(unlist(oneMASE))
  ResultSumm <- cbind(ResultSumm, matFull)
  colnames(ResultSumm)[7:8]<-c("ETS", "MdASE")
  halfResult <- cbind(halfResult, matHalf)
  colnames(halfResult)[7:8]<-c("ETS", "MdASE")
  aQuarterResult <- cbind(aQuarterResult, matQuarter)
  colnames(aQuarterResult)[7:8]<-c("ETS", "MdASE")
  oneResult <- cbind(oneResult, matOne)
  colnames(oneResult)[7:8]<-c("ETS", "MdASE")
  
  #Now run ETS method with Box-Cox transformation:
  if(TRUE){
    for (i in 1:(length(series))){
      if ( i%%50 == 0 )
        cat("Series ", i, " is being analyzed", "\n")
      lam<-BoxCox.lambda(training[[i]])
      model<-ets(training[[i]], lambda = lam)
      forecast[[i]] <- forecast(model, h = 8)
      mase[[i]] <- accuracy(forecast[[i]], test[[i]])[2,6]
    }
    cat("MASE of ETS forecast with Box-Cox transformation for h = 8: ", "\n")
    print(mean(unlist(mase)))
  }  
  
  #Now run Damped trend method:
  for (i in 1:(length(series))){
    if ( i%%50 == 0 )
      cat("Series ", i, " is being analyzed", "\n")
    if(transform){
      model<-ets(trainingTrans[[i]]$series, model = "AAA", damped = TRUE)
      forecast[[i]] <- exp(forecast(model, h = 8)$mean) - 
        trainingTrans[[i]]$halfSecMin
    }
    else{
      model<-ets(training[[i]], model = "AAA", damped = TRUE)
      forecast[[i]] <- forecast(model, h = 8)$mean
    }    
    store<- measure(forecast[[i]], training[[i]], test[[i]], 8, 4)
    mase[[i]] <- store$full
    halfMASE[[i]] <- store$half
    aQuarterMASE[[i]] <- store$quar 
    oneMASE[[i]] <- store$one 
  }
  cat("MASE of Damped trend forecast for h = 8: ", "\n")
  print(mean(unlist(mase)))
  matFull[1, 1] <- mean(unlist(mase))
  matFull[1, 2] <- median(unlist(mase))
  matHalf[1, 1] <- mean(unlist(halfMASE))
  matHalf[1, 2] <- median(unlist(halfMASE))
  matQuarter[1, 1] <- mean(unlist(aQuarterMASE))
  matQuarter[1, 2] <- median(unlist(aQuarterMASE))
  matOne[1, 1] <- mean(unlist(oneMASE))
  matOne[1, 2] <- median(unlist(oneMASE))
  
  #Now run Damped trend with outlier detection:
  for (i in 1:(length(series))){
    if ( i%%50 == 0 ){
      cat("Series ", i, " is being analyzed", "\n")
    }
    if(transform){
      model<-ets(adjusted[[i]], model = "AAA", damped = TRUE)
      forecast[[i]] <- exp(forecast(model, h = 8)$mean) - 
        trainingTrans[[i]]$halfSecMin
    }
    else{
      model<-ets(adjusted[[i]], model = "AAA", damped = TRUE)
      forecast[[i]] <- forecast(model, h = 8)$mean
    }
    store<- measure(forecast[[i]], training[[i]], test[[i]], 8, 4)
    mase[[i]] <- store$full
    halfMASE[[i]] <- store$half
    aQuarterMASE[[i]] <- store$quar 
    oneMASE[[i]] <- store$one   
  }
  cat("MASE of Damped trend forecast with outlier detection for h = 8: ", "\n")
  print(mean(unlist(mase)))
  matFull[2, 1] <- mean(unlist(mase))
  matFull[2, 2] <- median(unlist(mase))
  matHalf[2, 1] <- mean(unlist(halfMASE))
  matHalf[2, 2] <- median(unlist(halfMASE))
  matQuarter[2, 1] <- mean(unlist(aQuarterMASE))
  matQuarter[2, 2] <- median(unlist(aQuarterMASE))
  matOne[2, 1] <- mean(unlist(oneMASE))
  matOne[2, 2] <- median(unlist(oneMASE))
  ResultSumm <- cbind(ResultSumm, matFull)
  colnames(ResultSumm)[9:10]<-c("Damped trend", "MdASE")
  halfResult <- cbind(halfResult, matHalf)
  colnames(halfResult)[9:10]<-c("Damped trend", "MdASE")
  aQuarterResult <- cbind(aQuarterResult, matQuarter)
  colnames(aQuarterResult)[9:10]<-c("Damped trend", "MdASE")
  oneResult <- cbind(oneResult, matOne)
  colnames(oneResult)[9:10]<-c("Damped trend", "MdASE")
  
  #Now consider the outlier detection method in package tsoutliers
  #Applied to auto arima (Only applicable for certain number of regular diffs):
  for (i in 1:(length(series))){
    if ( i%%20 == 1 ){
      cat("Series ", i, " is being analyzed", "\n")
    }
    mase[[i]]<-tryCatch({
      detected <- tso(training[[i]], types = c("AO", "IO"), tsmethod = "auto.arima", 
                      args.tsmethod = list(allowdrift = TRUE), remove.method = "bottom-up")
      model <- auto.arima(detected$yadj, allowdrift = TRUE)
      forecast[[i]] <- forecast(model, h = 8)$mean
      mas <- calcMASE(forecast[[i]], training[[i]], test[[i]], 8, 4) 
    }, warning = function(war){
      model <- auto.arima(detected$yadj, allowdrift = TRUE)
      forecast[[i]] <- forecast(model, h = 8)$mean
      mas <- calcMASE(forecast[[i]], training[[i]], test[[i]], 8, 4) 
      return(mas)    
    }, error = function(err){
      cat("Not able to find outliers for this case. ", "\n")
      model <- auto.arima(training[[i]], allowdrift = TRUE)
      forecast[[i]] <- forecast(model, h = 8)$mean
      mas <- calcMASE(forecast[[i]], training[[i]], test[[i]], 8, 4) 
      return(mas)    
    })
    
  }
  cat("MASE of auto arima forecast with tso function outlier detection 
    for h = 8: ", "\n")
  print(mean(unlist(mase)))
  
  print(ResultSumm)
}

#The following code is not necessary due to the incorporation of tsoutliers() function.
if(FALSE){
  #capture.output(ao<-detectAO(model))
  #capture.output(io<-detectIO(model))
  #AODetected <- FALSE
  #IODetected <- FALSE
  #No outliers detected, go on to the next series
  #if(length(ao$lambda2) == 0 && length(io$lambda1) == 0 )
  #  next
  #if(length(ao$lambda2) > 0){
  #  detectAO(model)
  # AODetected <- TRUE
  #}
  #if(length(io$lambda1) > 0){
  #  detectIO(model)
  #  IODetected <- TRUE
  #}
  #AOIndex <- vector()
  #IOIndex <- vector()
  while(AODetected || IODetected){
    cat("Series ", i, " is being analyzed", "\n")
    orders<-model$arma
    ar <- orders[1]
    ma <- orders[2]
    sar <- orders[3]
    sma <- orders[4]
    prd <- orders[5]
    diff <- orders[6]
    sdiff <- orders[7]
    cat("Forecast before outliers are included: ", "\n")
    print(forecast(model, h=4))
    #predict(model, n.ahead = 4, se.fit = TRUE)
    
    if (AODetected && !IODetected){
      AOIndex<-c(AOIndex, ao$ind[which.max(abs(ao$lambda2))])
      cat("New model after only an addtive outlier is taken into account. ", '\n')
    }
    
    if (IODetected && !AODetected){
      IOIndex<-c( IOIndex,io$ind[which.max(abs(io$lambda1))])
      cat("New model after only an innovative outlier is taken into account. ", '\n')
    }
    
    if (IODetected && AODetected){
      MaxAbsIO <- max(abs(io$lambda1))
      MaxAbsAO <- max(abs(ao$lambda2))
      if (MaxAbsIO > MaxAbsAO){
        IOIndex<-c( IOIndex,io$ind[which.max(abs(io$lambda1))])
        #browser()        
      }
      else{
        AOIndex<-c(AOIndex, ao$ind[which.max(abs(ao$lambda2))])
        #browser()
      }
      
      cat("New model after outlier is taken into account. ", '\n')
    }
    if (length(IOIndex) > 0){
      if(length(AOIndex > 0)){
        model2 <- arimax(training[[i]], order = c(ar, diff, ma), seasonal = list(
          order = c(sar, sdiff, sma), period = prd), io = list(IOIndex), 
          xreg = data.frame(AO = seq(training[[i]]) == AOIndex))          
      }
      else
        model2 <- arimax(training[[i]], order = c(ar, diff, ma), seasonal = list(
          order = c(sar, sdiff, sma), period = prd), io = list(IOIndex)) 
    }
    else{
      model2 <- arimax(training[[i]], order = c(ar, diff, ma), seasonal = list(
        order = c(sar, sdiff, sma), period = prd), xreg = data.frame(AO = seq(
          training[[i]]) == AOIndex)) 
    }
    if(i == 18)
      browser()
    
    if (model2$aic >= model$aic){
      #browser()
      break
    }
    model<-model2
    print(model2)
    #model <- model2
    
    capture.output(ao<-detectAO(model))
    capture.output(io<-detectIO(model))
    AODetected <- FALSE
    IODetected <- FALSE
    if(length(ao$lambda2) > 0){
      detectAO(model)
      AODetected <- TRUE
    }
    if(length(io$lambda1) > 0){
      detectIO(model)
      IODetected <- TRUE
    }
  }
  #cat("After changes in model: ", "\n")
  #predict(model, n.ahead = 4, se.fit=TRUE)
  #forecast(model, h=4)
  
  #The following code is erroneously written. I am too thrifty to delete them.
  
  #Create two vectors to store indices with IO and AO.
  AOIndices<-vector()
  IOIndices<-vector()
  samePos<-TRUE
  for (j in 1:leng){
    if (io$ind[j] != ao$ind[j]){
      samePos<-FALSE
      break
    }
  }
  #Only process the case when AOs and IOs are on the same positions.
  if (samePos){
    for (j in 1:leng){
      if (io$lambda1[j] > ao$lambda2[j])
        IOIndices<-c(IOIndices, io$ind[j])
      else
        AOIndices<-c(AOIndices, ao$ind[j])
    }
    orders<-model$arma
    ar <- orders[1]
    ma <- orders[2]
    sar <- orders[3]
    sma <- orders[4]
    prd <- orders[5]
    diff <- orders[6]
    sdiff <- orders[7]
    adtvOut <- rep(0, length(training[[i]]))
    adtvOut[AOIndices] <- 1
    if ( length(IOIndices) > 0 ){     
      #browser()
      model <- arimax(training[[i]], order = c(ar, diff, ma), seasonal = list(
        order = c(sar, sdiff, sma), period = prd), xreg = data.frame(adtvOut), 
        io = IOIndices)      
    }
    else{
      #vector IOIndices is empty.
      model <- arimax(training[[i]], order = c(ar, diff, ma), seasonal = list(
        order = c(sar, sdiff, sma), period = prd), xreg = data.frame(adtvOut))
    }
    cat("New model after outliers are taken into consideration. ", '\n')
    print(model)
    next
  }
  #Handle the cases where IO and AO detection results are not so 'regular'
  cat("Please decide the indices of addtive outliers and innovative outliers", "\n")
  AOIndices <- readline(prompt = "Indices of Additive Outliers, separate with comma: ")
  IOIndices <- readline(prompt = "Indices of Innovative Outliers, separate with comma: ")
  AOIndices <- as.numeric(unlist(strsplit(AOIndices, split = ",")))
  IOIndices <- as.numeric(unlist(strsplit(IOIndices, split = ",")))
  if ( length(IOIndices) > 0 ){
    newModel <- arimax(training[[i]], order = c(ar, diff, ma), seasonal = list(
      order = c(sar, sdiff, sma), period = prd), xreg = data.frame(adtvOut), 
      io = IOIndices)      
  }
  else{
    #vector IOIndices is empty.
    newModel <- arimax(training[[i]], order = c(ar, diff, ma), seasonal = list(
      order = c(sar, sdiff, sma), period = prd), xreg = data.frame(adtvOut))
  }
}