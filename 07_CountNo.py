# Write a Python program to take a number and count how many digits it contains.

n=int(input("Enter a Number :"))

count=0
for i in range(len(str(n))):
    count=count+1

print(count)
