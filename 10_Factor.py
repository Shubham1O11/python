# Write a Python program to take a number and print all of its factors.


n=int(input("Enter a Number :"))

for i in range(1,n+1):
    if(n%i==0):
        print(i)