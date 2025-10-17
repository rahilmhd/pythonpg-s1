n = int(input("enter min of 4 digits number"))

def rev(m):
    if m<1000:
        print("enter value greater than 1000")
        return
    new = 0
    while m>0:
        d = m%10
        new = new*10+d
        m=m//10
    return new

print(rev(n))
    

