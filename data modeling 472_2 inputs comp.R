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


v_true_train = data_train$v_Vel_output
v_true_test = data_test$v_Vel_output

# with optimized values
model1 = loess(data_train$v_Vel_output ~ data_train$v_Vel + data_train$Space_Headway, span = 0.1, degree = 2, control = loess.control(surface = "direct"))
pred1 = predict(model1, data = data_train[,3:6])
rmse1 = sqrt(mean((v_true_train - pred1)^2))
rmsn1= rmse1/mean(data_train$v_Vel_output) 

model3 = loess(data_train$v_Vel_output ~ data_train$v_Vel + data_train$Space_Headway, span = 0.3, degree = 2, control = loess.control(surface = "direct"))
pred3 = predict(model3, data = data_train[,3:6])
rmse3 = sqrt(mean((v_true_train - pred3)^2))
rmsn3 = rmse3/mean(data_train$v_Vel_output) 

model5 = loess(data_train$v_Vel_output ~ data_train$v_Vel + data_train$Space_Headway, span = 0.5, degree = 2, control = loess.control(surface = "direct"))
pred5 = predict(model5, data = data_train[,3:6])
rmse5 = sqrt(mean((v_true_train - pred5)^2))
rmsn5 = rmse5/mean(data_train$v_Vel_output) 

model7 = loess(data_train$v_Vel_output ~ data_train$v_Vel + data_train$Space_Headway, span = 0.7, degree = 2, control = loess.control(surface = "direct"))
pred7 = predict(model7, data = data_train[,3:6])
rmse7 = sqrt(mean((v_true_train - pred7)^2))
rmsn7 = rmse7/mean(data_train$v_Vel_output) 

model9 = loess(data_train$v_Vel_output ~ data_train$v_Vel + data_train$Space_Headway, span = 0.9, degree = 2, control = loess.control(surface = "direct"))
pred9 = predict(model9, data = data_train[,3:6])
rmse9 = sqrt(mean((v_true_train - pred9)^2))
rmsn9 = rmse9/mean(data_train$v_Vel_output) 



model21 = loess(data_test$v_Vel_output ~ data_test$v_Vel + data_test$Space_Headway, span = 0.1, degree = 2, control = loess.control(surface = "direct"))
pred21 = predict(model21, data = data_train[,3:6])
rmse21 = sqrt(mean((v_true_train - pred21)^2))
rmsn21= rmse21/mean(data_train$v_Vel_output) 

model23 = loess(data_test$v_Vel_output ~ data_test$v_Vel + data_test$Space_Headway, span = 0.3, degree = 2, control = loess.control(surface = "direct"))
pred23 = predict(model23, data = data_train[,3:6])
rmse23 = sqrt(mean((v_true_train - pred23)^2))
rmsn23 = rmse23/mean(data_train$v_Vel_output) 

model25 = loess(data_test$v_Vel_output ~ data_test$v_Vel + data_test$Space_Headway, span = 0.5, degree = 2, control = loess.control(surface = "direct"))
pred25 = predict(model25, data = data_train[,3:6])
rmse25 = sqrt(mean((v_true_train - pred25)^2))
rmsn25 = rmse25/mean(data_train$v_Vel_output) 

model27 = loess(data_test$v_Vel_output ~ data_test$v_Vel + data_test$Space_Headway, span = 0.7, degree = 2, control = loess.control(surface = "direct"))
pred27 = predict(model27, data = data_train[,3:6])
rmse27 = sqrt(mean((v_true_train - pred27)^2))
rmsn27 = rmse27/mean(data_train$v_Vel_output) 

model29 = loess(data_test$v_Vel_output ~ data_test$v_Vel + data_test$Space_Headway, span = 0.9, degree = 2, control = loess.control(surface = "direct"))
pred29 = predict(model29, data = data_train[,3:6])
rmse29 = sqrt(mean((v_true_train - pred29)^2))
rmsn29 = rmse29/mean(data_train$v_Vel_output) 



span = c("0.1","0.3","0.5","0.7","0.9","0.1","0.3","0.5","0.7","0.9")
rmsn = c(rmsn1,rmsn3,rmsn5,rmsn7,rmsn9,rmsn21,rmsn23,rmsn25,rmsn27,rmsn29)
series = c("Data Series 2092-3161","Data Series 2092-3161","Data Series 2092-3161","Data Series 2092-3161","Data Series 2092-3161",
           "Data Series 1081-1539","Data Series 1081-1539","Data Series 1081-1539","Data Series 1081-1539","Data Series 1081-1539")
model_value = data.frame(span, rmsn, series)

library(ggplot2)
tiff("rmsn comparison2.png", units = "in", width = 20, height = 10, res = 300)
fig = ggplot(data = model_value, aes(x = factor(span), y = rmsn, color = series, group = series)) 
fig = fig + geom_line(size = 2) 
fig = fig + geom_point(size = 3.5)
fig = fig + geom_text(aes(x = factor(span), y = rmsn,label = round(rmsn,3)), hjust = 0.5, vjust = 2)
fig = fig + theme(legend.position = "top") +
  labs(x = "Span", y = "Normalzied Root Mean Square Error")+
  scale_y_continuous(breaks = seq(0,1.5,0.1)) +
  theme(axis.title.x = element_text(size = 15))+
  theme(axis.title.y = element_text(size = 15))+
  theme(axis.text= element_text(size = 10))
fig
dev.off()