list1=[1,2,3,4,5,6,7]
list2=[10,20,30,40,50,60]

if len(list1) == len(list2):
    print("The Lists are of same size")
else:
    print("Not same")



sum1=0
for i in list1:
    sum1=sum1+i
print("list1 sum = ",sum1)
sum2=0
for i in list2:
    sum2=sum2+i
print("list2 sum = ",sum2)
if sum1 == sum2:
    print("The sum are of same size")
else:
    print("Not same")


common=[]
for i in list1:
    for j in list2:
        if i == j :
            common.append(i)
print(common)            
    
