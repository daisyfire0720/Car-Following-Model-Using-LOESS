# set the working directory
setwd("C:/Users/Daisy/Downloads/GT Coursework/Spring Semester 2020/ISyE6416 Regression Analysis/Final Project/Data")

# rmsn comparison plot
# default model
series = c("Data Series 2092-3161","Data Series 2092-3161","Data Series 2092-3161","Data Series 2092-3161",
          "Data Series 1081-1539","Data Series 1081-1539","Data Series 1081-1539","Data Series 1081-1539")
model = c("Model 1","Model 2", "Model 3", "Model 4", "Model 1","Model 2", "Model 3", "Model 4")
rmsn = c(1.587,2.337,0.141,0.145,0.465,1.045,0.078,0.076)
model_default = data.frame(series, model, rmsn)

# improved model
series1 = c("Data Series 2092-3161","Data Series 2092-3161","Data Series 2092-3161","Data Series 2092-3161",
          "Data Series 1081-1539","Data Series 1081-1539","Data Series 1081-1539","Data Series 1081-1539")
model1 = c("Model 1","Model 2", "Model 3", "Model 4", "Model 1","Model 2", "Model 3", "Model 4")
rmsn1 = c(0.327,0.29,0.283,0.239,0.037,0.040,0.064,0.047)
model_improved = data.frame(series1, model1, rmsn1)

model_final = data.frame(series, model, rmsn, rmsn1)
colnames(model_final) = c("Series", "Model", "rmsn_default", "rmsn_improved")


library(ggplot2)
# one combined dataframe
tiff("rmsn comparison1.png", units = "in", width = 20, height = 10, res = 300)
fig = ggplot(data=model_final, aes(group = Series, color = Series)) +
  geom_line(aes(x = factor(Model), y = rmsn_default),linetype="dotted", size=2)+
  geom_point(aes(x = factor(Model), y = rmsn_default), size=4, shape = 16)+
  #geom_text(aes(x = factor(Model), y = rmsn_default,label = rmsn_default)) +
  geom_line(aes(x = factor(Model), y = rmsn_improved),linetype="solid", size=2)+
  geom_point(aes(x = factor(Model), y = rmsn_improved), size=5, shape = 18)+
  #geom_text(aes(x = factor(Model), y = rmsn_improved, label = rmsn_improved)) +
  theme(legend.position = "top") +
  labs(x = "Model", y = "Normalzied Root Mean Square Error")+
  scale_y_continuous(breaks = seq(0,3,0.2)) +
  theme(axis.title.x = element_text(size = 15))+
  theme(axis.title.y = element_text(size = 15))+
  theme(axis.text= element_text(size = 10))
  
fig
dev.off()

