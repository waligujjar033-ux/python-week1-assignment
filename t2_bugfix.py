# t2_bugfix.py - legacy shop receipt script

items = ["pen", "notebook", "bag"]
prices = [20, 150, 1200]

qty = input("Quantity of each item (e.g. 2,1,1): ").split(",")

total = 0

for i in range(1, len(items)):
    line = prices[i] * qty[i]
    print(items[i], "x", qty[i], "=", line)
    total = line

if total > 500:
    discount = total * 10 / 100

elif total > 1000:
    discount = total * 20 / 100

else:
    discount = 0

final = total - discount

print("Total:", total)
print("Discount:", discount)
print("Pay: Rs " + final)