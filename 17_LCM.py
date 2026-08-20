# Write a Python program to take two numbers and calculate their LCM.

a=int(input("Enter number :"))
b=int(input("Enter number :"))

a=abs(a)
b=abs(b)

x=a
y=b

while y!=0:
    x,y=y,x%y

lcm=(a*b)//x

print(lcm)
