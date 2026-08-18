# Write a Python program to take a number and check whether it is prime.

n=int(input("Enter a Number :"))

if(n<2):
    print("Not Prime")

elif(n%2==0):
    print("Not Prime")

else:
    print("Prime")