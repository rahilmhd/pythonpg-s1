dict1={"suzuki":"grand vitara","toyota":"hyryder"}
dict2={"hyundai":"creta"}

dict1.update(dict2)
print(dict1)



n=15
d=dict()
for x in range(1,n+1):
       d[x]=x*x
print(d)


car={"suzuki":1,"toyota":2,"hyundai":3}
sum=0
for i in car.values():
       sum=sum+(i)
print("The sum of values : ",sum)



car={"suzuki":3,"toyota":4,"hyundai":5}
mul=1
for i in car.values():
    mul=mul*i
print("product: ",mul)
