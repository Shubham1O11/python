# Write a Python program to take the price of an item. 
# If the price is greater than ₹1000, give a 10% discount; otherwise, give no discount. Print the final price.

item=int(input("Enter the price of item :"))

if(item > 1000):
    discount=item*0.1
    Fp=item-discount
    print(f"You got {Fp}$ ")

else:
    print("No discount")