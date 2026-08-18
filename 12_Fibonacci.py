# Write a Python program to take a number n and print the first n terms of the Fibonacci series.

n=int(input("Enter Number :"))

a=0
b=1

for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c




