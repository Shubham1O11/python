# Write a Python program to take a number and find the largest digit in it.

n=int(input("Enter Number :"))
n=abs(n)
largest=0
smallest=float('inf')

while n>0:
   digit=n%10 
   if(digit>largest ):
      largest=digit
   n//=10
    

print(largest)