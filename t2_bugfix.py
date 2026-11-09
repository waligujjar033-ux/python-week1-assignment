# t2_bugfix.py - legacy shop receipt script

items = ["pen", "notebook", "bag"]
prices = [20, 150, 1200]

# BUG-6: Input validation using Week 1 concepts

valid = False

while not valid:
    user_input = input("Quantity of each item (e.g. 2,1,1): ")
    parts = user_input.split(",")

    if len(parts) != len(items):
        print("Invalid input! Please enter quantities like 2,1,1")
        continue

    qty = []
    valid = True

    for part in parts:
        part = part.strip()

        if part.isdigit():
            qty.append(int(part))
        else:
            valid = False
            break

    if not valid:
        print("Invalid input! Please enter quantities like 2,1,1")
total = 0

for i in range(0, len(items)):  # Bug 1 0 sy start karna chahiye tha, 1 sy nahi
    line = prices[i] * qty[i]
    print(items[i], "x", qty[i], "=", line)
    total += line

if total > 1000:
    discount = total * 20 / 100

elif total > 500:
    discount = total * 10 / 100

else:
    discount = 0

final = total - discount

print("Total:", total)
print("Discount:", discount)
print("Pay: Rs ", final)