def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

a=int(input("Enter Number :"))
b=int(input("Enter Number :"))
c=int(input("Enter Number :"))


print(greatest(a,b,c))