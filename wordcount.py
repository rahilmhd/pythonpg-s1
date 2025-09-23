string = input("enter the sentance to check occurence of word : ")

splitstrings = strings.split()
print(splitstrings)

i=0
count =0

while (i<len(splitstrings)):

    j=0
    while (j<len(splitstrings)):
        if(spitstrings[i] == splitstrings[j]):
            splitstrings.pop(j)
            count = count+1
        j=j+1
    print(f"splitstrings[i] - {count}")
    count =0
    i=i+1
        
