names= input("Enter the names:")
name = names.split()
print(name)

count=0
for i in name:
    for word in list(i):
        if "a" in word:
            count+=1
print(count)           
