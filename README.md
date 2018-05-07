# data_storage
#codes

####PLot the relation between rape and kidnapping of women and girls for the state where no of 
#####murder cases is more than 70 from 2001 to 2012
library(dplyr)
library(ggplot2)
crime<-read.csv("E:/data visualization/Data Set/rajanand-crime-in-india/01_District_wise_crimes_committed_IPC_2001_2012.csv")
names(crime)
View(crime)
crime_data<-crime%>%group_by(STATE.UT,YEAR)%>%filter(DISTRICT=="TOTAL"&MURDER>70)%>%select(STATE.UT,YEAR,MURDER,RAPE,KIDNAPPING.AND.ABDUCTION.OF.WOMEN.AND.GIRLS)
p1<-ggplot(crime_data, aes(x=RAPE,y=KIDNAPPING.AND.ABDUCTION.OF.WOMEN.AND.GIRLS))+geom_point(aes(col=STATE.UT,size=MURDER))
p2<-ggplot(crime_data, aes(x=RAPE,y=KIDNAPPING.AND.ABDUCTION.OF.WOMEN.AND.GIRLS,frame = YEAR))+geom_point(aes(col=STATE.UT,size=MURDER))
install.packages("plotly")
library(plotly)
ggplotly(p1)
ggplotly(p2)
## plot manufacturer wise, class wise count of cars
mpg
mpg1<-mpg%>%group_by(manufacturer,class)%>%count()
stack_bar=ggplot(mpg1,aes(x=manufacturer,y=n,fill=class))+geom_bar(position = "fill",stat="identity")
ggplot(mpg1,aes(x=manufacturer,y=n))+geom_bar(stat="identity")+facet_wrap("class")
ggplot(mpg1,aes(x=manufacturer,y=n))+geom_point(aes(col=class))
stack_bar+geom_text(data=mpg1,aes(x=manufacturer,y=n,label=n),position=position_stack(vjust=0.5))
stack_bar

library(data.table)
###major reason being people kidnapped in each state
kid<-fread("E:/data visualization/Data Set/rajanand-crime-in-india/39_Specific_purpose_of_kidnapping_and_abduction.csv")
kid1<-kid%>%group_by(Area_Name,Sub_Group_Name)%>%select(K_A_Grand_Total)%>%count()
names(kid)
kid1
ggplot(kid1,aes(x=Area_Name,y=n,fill=Sub_Group_Name))+geom_bar(position = "fill",stat="identity")+
  coord_flip()
ggplot(data=kid1,aes(x=Sub_Group_Name,y=Area_Name))+
  geom_tile(aes(fill=n),color="white")+theme(axis.text.x = element_text(angle=90))+
  scale_fill_gradient(low="green",high = "red")

###plot with city mileage grouped by classes of each cylinder
s1<-mpg%>%group_by(class,cyl)
ggplot(s1,aes(x=cyl,y=sum,fill=class))+geom_bar(stat = "identity",position = "fill")
ggplot(s1,aes(x=class,y=sum,fill=factor(cyl)))+geom_bar(stat="identity",position = "fill")
ggplot(s1,aes(x=class,y=cty,fill=as.factor(cyl)))+geom_boxplot(varwidth = T)

####to create a histogram of displacement of various cars classsss
ggplot(mpg,aes(x=displ,fill=class))+geom_histogram(binwidth = 0.5)

ggplot(mpg,aes(x=manufacturer,fill=class))+geom_histogram(stat = "count")
