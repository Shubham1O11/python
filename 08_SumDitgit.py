# Write a Python program to take a number and calculate the sum of its digits.

n=int(input('Enter Number :'))
count=0

while n > 0:
    digit=n%10
    count=count+digit
    n//=10

print(count)
