# set the working directory
setwd("C:/Users/Daisy/Downloads/GT Coursework/Spring Semester 2020/ISyE6416 Regression Analysis/Final Project/Data")

# introduce the dataset
data = read.csv("us_101_lane2_foruse.csv")
data = data[data$v_ID == 472,]
attach(data)
data = subset(data, select = -c(v_ID, v_Frame_output))
data = data[data$Time_Headway < 9999,]

# split the dataset into training subset and testing subset
library(tidyverse)
data_train = data %>% filter(Frame_ID > 1564)
data_test = data %>% filter(Frame_ID <= 1564)

## hyperparameter tuning 
# find the optimal span parameter
library(bootstrap)
loess_wrapper_extrapolate = function(x, y, span.vals = seq(0.1,1, by = 0.01), folds = 5){
  # model selection using mean absolute error, which is more robust than squared error
  mean.abs.error = numeric(length(span.vals))
  
  # quantify error for each span using cross validation
  loess.model = function(x, y, span){
    loess(y ~ x, degree = 2, span = span, control = loess.control(surface = "direct"))
  }
  
  loess.predict = function(fit, newdata){
    predict(fit, newdata = newdata)
  }
  span.index = 0
  for (each.span in span.vals){
    span.index = span.index + 1
    y.hat.cv = crossval(x, y, theta.fit = loess.model, theta.predict = loess.predict,
                        span = each.span, ngroup = folds)$cv.fit
    non.empty.indices = !is.na(y.hat.cv)
    mean.abs.error[span.index] = mean(abs(y[non.empty.indices] - y.hat.cv[non.empty.indices]))
  }
  # find the span that minimizes the error
  best.span = span.vals[which.min(mean.abs.error)]
  
  # fit and return the best model
  optimal.model = loess(y ~ x, span = best.span, degree = 2, control = loess.control(surface = "direct"))
  return(optimal.model)
}



v_true_train = data_train$v_Vel_output
v_true_test = data_test$v_Vel_output

# with default values
model1_train = loess(data_train$v_Vel_output ~ data_train$v_Vel + data_train$Space_Headway)
model1_test = loess(data_test$v_Vel_output ~ data_test$v_Vel + data_test$Space_Headway)
pred1_train = predict(model1_train, data = data_train[,3:6])
pred1_test = predict(model1_test, data = data_test[,3:6])
comp1_train = data.frame(data_train$Frame_ID, data_train$v_Vel_output, pred1_train)
comp1_test = data.frame(data_test$Frame_ID, data_test$v_Vel_output,pred1_test)
rmse1_train = sqrt(mean((v_true_train - pred1_train)^2))
rmsn1_train = rmse1_train/mean(v_true_train) #0.1450519
rmse1_test = sqrt(mean((v_true_test - pred1_test)^2))
rmsn1_test = rmse1_test/mean(v_true_test) #0.07561231


# with optimized values
model2_train = loess_wrapper_extrapolate(data_train$v_Vel + data_train$Space_Headway, data_train$v_Vel_output)

model2_test = loess(data_test$v_Vel_output ~ data_test$v_Vel + data_test$Space_Headway, span = 0.11, degree = 2, control = loess.control(surface = "direct"))
pred2_train = predict(model2_train, data = data_train[,3:6])
pred2_test = predict(model2_test, data = data_test[,3:6])
comp2_train = data.frame(data_train$Frame_ID, data_train$v_Vel_output ,pred2_train)
comp2_test = data.frame(data_test$Frame_ID, data_test$v_Vel_output,pred2_test)
rmse2_train = sqrt(mean((v_true_train - pred2_train)^2))
rmsn2_train = rmse2_train/mean(data_train$v_Vel_output) #0.2385274
rmse2_test = sqrt(mean((v_true_test - pred2_test)^2))
rmsn2_test = rmse2_test/mean(data_test$v_Vel_output) #0.04720386


# plot the result
library(ggplot2)
tiff("2 inputs.png", units = "in", width = 20, height = 8, res = 300)
fig1 = ggplot()
fig1 = fig1 + geom_point(data = comp1_train, aes(x = data_train.Frame_ID, y = data_train.v_Vel_output), size = 0.5)
# add two lines for training dataset
fig1 = fig1 + geom_line(data = comp1_train, aes(x = data_train.Frame_ID, y = pred1_train), color = "blue") 
fig1 = fig1 + geom_line(data = comp2_train, aes(x = data_train.Frame_ID, y = pred2_train), color = "red")
# add two lines for testing dataset
fig1 = fig1 + geom_point(data = comp1_test, aes(x = data_test.Frame_ID, y = data_test.v_Vel_output), size = 0.5)
fig1 = fig1 + geom_line(data = comp1_test, aes(x = data_test.Frame_ID, y = pred1_test), linetype = "longdash", color = "blue") 
fig1 = fig1 + geom_line(data = comp2_test, aes(x = data_test.Frame_ID, y = pred2_test), linetype = "longdash", color = "red")
fig1 = fig1 + labs(x = "Frame", y = "Vehicle Velocity")
fig1 = fig1 + theme(axis.title.x = element_text(size = 15, face = "bold"))
fig1 = fig1 + theme(axis.title.y = element_text(size = 15, face = "bold"))
fig1
dev.off()