"""
get number_of_items
while number_of_items < 0
    display invalid message
    get number_of_items
total = 0
total_price = 0
for each item in number_of_items
    get price
    total = total + price
if total > 100
    total_price = total - (total * 0.1)
else
    total_price = total
display total_price
"""

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
total = 0
total_price = 0
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total += price
if total > 100:
    total_price = total - (total * 0.1)
else:
    total_price = total
print(f"Total price for {number_of_items} items is ${total_price:.2f}")