# The value of a mask is 5 euros, if purchased from 10 units each costs 4 euros. The product quantity must be entered, and the amount to be paid printed on the screen. If the number entered is less than or equal to 0, “invalid operation” should appear.
quantity = int(input("Please enter the quantity of masks: "))

# default
price = 5
if (quantity >= 10):
    price = 4

total = price * quantity
print(F"Total price is EUR {total} (Price {price} x Qty {quantity})")
