#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""
f = float(input("Enter the first price:"))
s = float(input("Enter the second price:"))
t = float(input("Enter the third price:"))
fth = float(input("Enter the fourth price:"))
fv = float(input("Enter the fifth price:"))
s = f+s+t+fth+fv
tx1 = s*0.12
tx = round(tx1,2)
tt = tx + s
print(f"Your subtotal is ${s} and you taxes total ${tx} for a total of ${tt}")