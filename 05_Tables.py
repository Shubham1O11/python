# Write a Python program to take a number from the user and print its multiplication table from 1 to 10.

n=int(input("Enter a number :"))

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")