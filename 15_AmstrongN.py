# Write a Python program to take a number and check whether it is an Armstrong number.

n=int(input("Enter Number :"))
# n=abs(n)

Tdigit=len(str(n))
while n>0:
    digit=n%10 
    for i in range(Tdigit):
        ams+=digit**Tdigit
        print(ams)
    n//=10
    

print(Tdigit)
