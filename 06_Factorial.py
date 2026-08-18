# Write a Python program to take a number and calculate its factorial.

n=int(input("Enter a Number :"))

for i in range(1,n):
    n=n*i

    
print("Factorial of Given Number is :",n)