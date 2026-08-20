# Write a Python program to take a string and count the number of vowels in it.

a=str(input("Enter a string :"))
count=0
for i in a.lower():
    if (i in "aeiou"):
        count+=1


print(count)