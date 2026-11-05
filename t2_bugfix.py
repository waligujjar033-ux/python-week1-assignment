# t2_bugfix.py - legacy shop receipt script

items = ["pen", "notebook", "bag"]
prices = [20, 150, 1200]

qty = list(map(int, input("Quantity of each item (e.g. 2,1,1): ").split(",")))

total = 0

for i in range(0, len(items)):  # Bug 1 0 sy start karna chahiye tha, 1 sy nahi
    line = prices[i] * qty[i]
    print(items[i], "x", qty[i], "=", line)
    total += line

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