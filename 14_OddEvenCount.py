# Write a Python program to take a number and count how many even and odd digits it contains.

n = int(input("Enter Number: "))
n = abs(n)

even = 0
odd = 0

while n > 0:
    digit = n % 10

    if digit == 0:
        n //= 10
        continue

    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

    n //= 10

print(f"Even: {even}")
print(f"Odd: {odd}")