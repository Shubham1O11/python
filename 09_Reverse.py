# Write a Python program to take a number and print its reverse.

n=int(input("Enter a Number :"))
reverse=0
while n > 0:
    digit=n%10
    reverse=reverse*10+digit
    n//=10

print(reverse)

