t<-c(1:10)
for(i in t){
l<-list('Iteration number: ',i)
print(l)
u<-c(1:50)
for(j in u){
x<-runif(3,min=1,max=6)%/%1
print(x)
}

}

ctr<-0
v<-c(1:50000)
for(j in v){
x<-sum(rnorm(3,mean=3.5,sd=2.5))%/%1
z<-c(14:16)
if(x %in% z){
ctr<-ctr+1
}
}
print('Probability:')
print(round(ctr/50000,digits=3))


