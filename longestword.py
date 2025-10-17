listword=input("enter the words as sentance")
newlist=listword.split()

print(newlist)

for i in range(len(newlist)):
    if(i==0):
        long=newlist[i]
    else:
        if (len(newlist[i])>len(long)):
            long=newlist[i]
      
print(f"the largest of the word is{long}")
