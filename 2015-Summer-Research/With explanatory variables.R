setwd("C:/Users/Simonfqy/Dropbox/Learing materials/2015 Summer Research/Dataset")
library(forecast)
library(KFAS)
library(compiler)
library(vars)
library(dynlm)
multi <- read.csv("multivariate.csv")
hkcpi <- multi$CPI_HK[1:66]
tourist <-list(length = 6)
cpi <- list(length = 6)
exchange <- list(length = 6)
realGDP <- list(length = 6)
storage <-vector(length = 22)
sndStorage <- list()
ownPrice <- list(length = 6)
income <- list(length = 6)
logTraining <- list(length = 6)

for (i in 1:66){
  if (i%%3==1)
  storage[ceiling(i/3)] <- ave(hkcpi[i:(i+2)])[1]
}
hkcpi <- storage

#Now load the data into the created lists.
for (i in 2:25){
  if (i%%4 ==2){
    sndStorage <- multi[,i][1:78]
    storage <- vector(length = 26)
    for (j in 1:78){
      if (j%%3 == 1)
        storage[ceiling(j/3)] <- ave(sndStorage[j:(j+2)])[1]
    }
    tourist[[ceiling(i/4)]] <- storage
  }
  if (i%%4 == 3){
    sndStorage <- multi[,i][1:66]
    storage <- vector(length = 22)
    for (j in 1:66){
      if (j%%3 == 1)
        storage[ceiling(j/3)] <- ave(sndStorage[j:(j+2)])[1]
    }
    cpi[[ceiling(i/4)]] <- storage
  }
  if (i%%4 == 0){
    storage <- multi[,i][!is.na(multi[, i])]
    exchange[[ceiling(i/4)]] <- storage
  }
  if (i%%4 == 1){
    realGDP[[floor(i/4)]] <- multi[,i][!is.na(multi[, i])]
  }
}

#Functions to be used for measuring performance
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

decideTrans<-function(){
  word <- readline(prompt = "Are you going to apply log transformation on the data? ")  
  if (substr(word, 1, 1) == "y")
    transform<-TRUE
  else if (substr(word, 1, 1) == 'n')
    transform<-FALSE
  transform
}

test<-list()
training<-list()
forecast <- list()
adjusted<-list()
trainingTrans <- list()
mase<-list()
ResultSumm <- NULL
matFull <- matrix(nrow = 2, ncol = 2)
oneMASE<-list()
halfMASE <- list()
halfResult <- NULL
oneResult <- NULL
matHalf <- matrix(nrow = 2, ncol = 2)
matOne <- matrix(nrow = 2, ncol = 2)

for (i in 1:6){
  training[[i]]<-ts(tourist[[i]][1:(length(tourist[[i]])-4)], frequency = 4)
  year<-ceiling(length(tourist[[i]])/4)
  quarter <- length(tourist[[i]]) - 4*(year-1)
  if (quarter < 4)
    test[[i]] <- ts(data = tourist[[i]][(length(tourist[[i]])-3) : length(tourist[[i]])],
                    start = c(year-1, quarter+1), frequency = 4)    
  else
    test[[i]] <- ts(data = tourist[[i]][(length(tourist[[i]])-3) : length(tourist[[i]])],
                    start = c(year, 1), frequency = 4)
}

#Compute the own price variable series.
for (i in 1:6){
  ownPrice[[i]] <- log(hkcpi*exchange[[i]]/cpi[[i]])
  income[[i]] <- log(realGDP[[i]])
  logTraining[[i]] <- log(training[[i]])
}

#Now start the multivariate analysis.
#First apply Vector Autoregressive model.
matFull <- matrix(nrow = 1, ncol = 2)
matHalf <- matrix(nrow = 1, ncol = 2)
matOne <- matrix(nrow = 1, ncol = 2)
for ( i in 1:6){
  aggregate <- cbind(logTraining[[i]],ownPrice[[i]], income[[i]])
  order <- VARselect(aggregate, lag.max = 4, season = 4, type = "both")$selection[3]
  var <- VAR(aggregate, p = order, season = 4, type = "both")
  forecast[[i]] <- exp(forecast(var, h = 4)$mean$logTraining)
  store<-measure(forecast[[i]], training[[i]], test[[i]], 4, 4)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half 
  oneMASE[[i]] <- store$one 
}
matFull[, 1]<-mean(unlist(mase))
matFull[, 2] <- median(unlist(mase))
ResultSumm <- cbind(ResultSumm, matFull)
matHalf[, 1] <- mean(unlist(halfMASE))
matHalf[, 2] <- median(unlist(halfMASE))
halfResult <- cbind(halfResult, matHalf)
matOne[, 1] <- mean(unlist(oneMASE))
matOne[, 2] <- median(unlist(oneMASE))
oneResult <- cbind(oneResult, matOne)
colnames(ResultSumm)[1:2] <- c("VAR", "MdASE")
colnames(halfResult)[1:2] <- c("VAR", "MdASE")
colnames(oneResult)[1:2] <- c("VAR", "MdASE")

#Apply ADLM 
for (i in 1:6){
  lag4Price <- lag(ownPrice[[i]], k = -4)
  lag3Price <- lag(ownPrice[[i]], k = -3)
  lag2Price <- lag(ownPrice[[i]], k = -2)
  lag1Price <- lag(ownPrice[[i]], k = -1)
  Price <- ownPrice[[i]]
  lag4Inc <- lag(income[[i]], k = -4)
  lag3Inc <- lag(income[[i]], k = -3)
  lag2Inc <- lag(income[[i]], k = -2)
  lag1Inc <- lag(income[[i]], k = -1)
  Inc<- income[[i]]
  y <- logTraining[[i]]
  fit <- dynlm(y~lag4Price + lag3Price + lag2Price + lag1Price + Price + lag4Inc + 
            lag3Inc + lag2Inc + lag1Inc + Inc + L(y, 1) + L(y, 2) + L(y, 3) + L(y, 4))
  xnew <- list()
  newPrice <- predict(HoltWinters(ts(Price, frequency = 4)), n.ahead = 4)
  newPrice <- c(Price[(length(Price)-3) : length(Price)],newPrice)
  newInc <- predict(HoltWinters(ts(Inc, frequency = 4)), n.ahead = 4)
  newInc <- c(Inc[(length(Inc)-3) : length(Inc)],newInc)
  for(j in 1:10){
    if(j <= 5){
      xnew[[j]] <- newPrice[j:(j+3)]
    }
    else{
      xnew[[j]] <- newInc[(j-5):(j-2)]
    }
  }
  
}

#Apply time varying parameter model
for ( i in 1:6){
  lag4Price <- lag(ownPrice[[i]], k = -4)
  lag3Price <- lag(ownPrice[[i]], k = -3)
  lag2Price <- lag(ownPrice[[i]], k = -2)
  lag1Price <- lag(ownPrice[[i]], k = -1)
  Price <- ownPrice[[i]]
  lag4Inc <- lag(income[[i]], k = -4)
  lag3Inc <- lag(income[[i]], k = -3)
  lag2Inc <- lag(income[[i]], k = -2)
  lag1Inc <- lag(income[[i]], k = -1)
  Inc<- income[[i]]
  y <- logTraining[[i]]
  model <- SSModel(y~lag4Price + lag3Price + lag2Price + lag1Price + Price + lag4Inc + 
                     lag3Inc + lag2Inc + lag1Inc + Inc)
  kfs <- KFS(model)
  xnew <- list()
  newPrice <- predict(HoltWinters(ts(Price, frequency = 4)), n.ahead = 4)
  newPrice <- c(Price[(length(Price)-3) : length(Price)],newPrice)
  newInc <- predict(HoltWinters(ts(Inc, frequency = 4)), n.ahead = 4)
  newInc <- c(Inc[(length(Inc)-3) : length(Inc)],newInc)
  for(j in 1:10){
    if(j <= 5){
      xnew[[j]] <- newPrice[j:(j+3)]
    }
    else{
      xnew[[j]] <- newInc[(j-5):(j-2)]
    }
  }
  newdata <- SSModel(rep(NA, length(xnew[[1]]))~xnew[[1]]+xnew[[2]]+xnew[[3]]+xnew[[4]]+
      xnew[[5]]+xnew[[6]]+xnew[[7]]+xnew[[8]]+xnew[[9]]+xnew[[10]])
  forecast[[i]]<-exp(predict(model, newdata = newdata))
  store<-measure(forecast[[i]], training[[i]], test[[i]], 4, 4)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half 
  oneMASE[[i]] <- store$one 
}
matFull[, 1]<-mean(unlist(mase))
matFull[, 2] <- median(unlist(mase))
ResultSumm <- cbind(ResultSumm, matFull)
matHalf[, 1] <- mean(unlist(halfMASE))
matHalf[, 2] <- median(unlist(halfMASE))
halfResult <- cbind(halfResult, matHalf)
matOne[, 1] <- mean(unlist(oneMASE))
matOne[, 2] <- median(unlist(oneMASE))
oneResult <- cbind(oneResult, matOne)
colnames(ResultSumm)[3:4] <- c("TVP", "MdASE")
colnames(halfResult)[3:4] <- c("TVP", "MdASE")
colnames(oneResult)[3:4] <- c("TVP", "MdASE")

#Apply auto arima without outlier detection
for (i in 1:6){
  if (transform){
    trainingTrans[[i]] <- log(training[[i]])
    model<-auto.arima(trainingTrans[[i]], allowdrift = TRUE, allowmean = TRUE)
    forecast[[i]] <- exp(forecast(model, h = 4)$mean)
  }
  else{
    model<-auto.arima(training[[i]], allowdrift = TRUE, allowmean = TRUE)
    forecast[[i]] <- forecast(model, h = 4)$mean
  }
  store<-measure(forecast[[i]], training[[i]], test[[i]], 4, 4)
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

#apply auto.arima with outlier detection
for (i in 1:6){
  if (transform){
    adjusted[[i]] <- log(training[[i]])
    outliers <- tsoutliers(adjusted[[i]])
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
  store<-measure(forecast[[i]], training[[i]], test[[i]], 4, 4)
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
deseasonalized<-list()  
for (i in 1:6){
  if(transform){
    decomp <- decompose(trainingTrans[[i]], type = "multi")
    deseasonalized[[i]] <- decomp$x/decomp$seasonal
    forecast[[i]] <- thetaf(deseasonalized[[i]], h = 4)$mean
    seasonal <- decomp$seasonal[(length(decomp$seasonal)-3) : length(decomp$seasonal)]
    forecast[[i]] <- exp(forecast[[i]]*seasonal)
  }
  else{
    decomp <- decompose(training[[i]], type = "multi")
    deseasonalized[[i]] <- decomp$x/decomp$seasonal
    forecast[[i]] <- thetaf(deseasonalized[[i]], h = 4)$mean
    seasonal <- decomp$seasonal[(length(decomp$seasonal)-3) : 
                                  length(decomp$seasonal)]
    forecast[[i]] <- forecast[[i]]*seasonal
  }    
  store<- measure(forecast[[i]], training[[i]], test[[i]], 4, 4)
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
for(i in 1:6){  
  if(transform){
    decomp <- decompose(adjusted[[i]], type = "multi")
    deseasonalized[[i]] <- decomp$x/decomp$seasonal
    forecast[[i]] <- thetaf(deseasonalized[[i]], h = 4)$mean
    seasonal <- decomp$seasonal[(length(decomp$seasonal)-3) : length(decomp$seasonal)]
    forecast[[i]] <- exp(forecast[[i]]*seasonal)
  }
  else{
    decomp <- decompose(adjusted[[i]], type = "multi")
    deseasonalized[[i]] <- decomp$x/decomp$seasonal
    forecast[[i]] <- thetaf(deseasonalized[[i]], h = 4)$mean
    seasonal <- decomp$seasonal[(length(decomp$seasonal)-3) : 
                                  length(decomp$seasonal)]
    forecast[[i]] <- forecast[[i]]*seasonal
  }    
  store<- measure(forecast[[i]], training[[i]], test[[i]], 4, 4)
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
colnames(ResultSumm)[3:4]<-c("Theta method", "MdASE")
halfResult <- cbind(halfResult, matHalf)
colnames(halfResult)[3:4]<-c("Theta method", "MdASE")
oneResult <- cbind(oneResult, matOne)
colnames(oneResult)[3:4]<-c("Theta method", "MdASE")

#Now run snaive method forecast:
for (i in 1:6){
  if(transform){
    forecast[[i]] <- exp(snaive(trainingTrans[[i]], h = 4)$mean) 
  }
  else{
    forecast[[i]] <- snaive(training[[i]], h = 4)$mean
  }    
  store<- measure(forecast[[i]], training[[i]], test[[i]], 4, 4)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  oneMASE[[i]] <- store$one
}
cat("MASE of snaive method forecast for h = 4: ", "\n")
print(mean(unlist(mase)))
matFull[1, 1] <- mean(unlist(mase))
matFull[1, 2] <- median(unlist(mase))
matHalf[1, 1] <- mean(unlist(halfMASE))
matHalf[1, 2] <- median(unlist(halfMASE))
matOne[1, 1] <- mean(unlist(oneMASE))
matOne[1, 2] <- median(unlist(oneMASE))

#Now run Snaive method with outlier detection:
for(i in 1:6){ 
  if(transform){
    forecast[[i]] <- exp(snaive(adjusted[[i]], h = 4)$mean) 
  }
  else{
    forecast[[i]] <- snaive(adjusted[[i]], h = 4)$mean
  }    
  store<- measure(forecast[[i]], training[[i]], test[[i]], 4, 4)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half 
  oneMASE[[i]] <- store$one
}
cat("MASE of snaive method forecast with outlier detection for h = 4: ", "\n")
print(mean(unlist(mase)))
matFull[2, 1] <- mean(unlist(mase))
matFull[2, 2] <- median(unlist(mase))
matHalf[2, 1] <- mean(unlist(halfMASE))
matHalf[2, 2] <- median(unlist(halfMASE))
matOne[2, 1] <- mean(unlist(oneMASE))
matOne[2, 2] <- median(unlist(oneMASE))
ResultSumm <- cbind(ResultSumm, matFull)
colnames(ResultSumm)[5:6]<-c("SNaive method", "MdASE")
halfResult <- cbind(halfResult, matHalf)
colnames(halfResult)[5:6]<-c("SNaive method", "MdASE")
oneResult <- cbind(oneResult, matOne)
colnames(oneResult)[5:6]<-c("SNaive method", "MdASE")

#Now run ETS method:
for (i in 1:6){
  if(transform){
    model<-ets(trainingTrans[[i]])
    forecast[[i]] <- exp(forecast(model, h = 4)$mean)
  }
  else{
    model<-ets(training[[i]])
    forecast[[i]] <- forecast(model, h = 4)$mean
  }    
  store<- measure(forecast[[i]], training[[i]], test[[i]], 4, 4)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  oneMASE[[i]] <- store$one 
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
for (i in 1:6){
  if(transform){
    model<-ets(adjusted[[i]])
    forecast[[i]] <- exp(forecast(model, h = 4)$mean)
  }
  else{
    model<-ets(adjusted[[i]])
    forecast[[i]] <- forecast(model, h = 4)$mean
  }    
  store<- measure(forecast[[i]], training[[i]], test[[i]], 4, 4)
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
colnames(ResultSumm)[7:8]<-c("ETS", "MdASE")
halfResult <- cbind(halfResult, matHalf)
colnames(halfResult)[7:8]<-c("ETS", "MdASE")
oneResult <- cbind(oneResult, matOne)
colnames(oneResult)[7:8]<-c("ETS", "MdASE")

#Now run Damped trend method:
for (i in 1:6){
  if(transform){
    model<-ets(trainingTrans[[i]], model = "AAA", damped = TRUE)
    forecast[[i]] <- exp(forecast(model, h = 4)$mean)
  }
  else{
    model<-ets(training[[i]], model = "AAA", damped = TRUE)
    forecast[[i]] <- forecast(model, h = 4)$mean
  }    
  store<- measure(forecast[[i]], training[[i]], test[[i]], 4, 4)
  mase[[i]] <- store$full
  halfMASE[[i]] <- store$half
  oneMASE[[i]] <- store$one 
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
for (i in 1:6){
  if(transform){
    model<-ets(adjusted[[i]], model = "AAA", damped = TRUE)
    forecast[[i]] <- exp(forecast(model, h = 4)$mean) 
  }
  else{
    model<-ets(adjusted[[i]], model = "AAA", damped = TRUE)
    forecast[[i]] <- forecast(model, h = 4)$mean
  }
  store<- measure(forecast[[i]], training[[i]], test[[i]], 4, 4)
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
colnames(ResultSumm)[9:10]<-c("Damped trend", "MdASE")
halfResult <- cbind(halfResult, matHalf)
colnames(halfResult)[9:10]<-c("Damped trend", "MdASE")
oneResult <- cbind(oneResult, matOne)
colnames(oneResult)[9:10]<-c("Damped trend", "MdASE")


