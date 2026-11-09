# T3 - Bill Splitter

from decimal import Decimal, ROUND_HALF_UP

# Step 1: Get bill amount
while True:

    bill_input = input("Bill amount (Rs): ")

    # Check valid number
    if bill_input.replace(".", "", 1).isdigit():

        bill = Decimal(bill_input)

        if bill >= 0:
            break
        else:
            print("Bill cannot be negative!")

    else:
        print("Invalid input! Enter a valid bill amount.")


# Step 2: Get tip percentage
while True:

    tip_input = input("Tip %: ")

    # Check valid number
    if tip_input.replace(".", "", 1).isdigit():

        tip = Decimal(tip_input)

        if tip >= 0:
            break
        else:
            print("Tip cannot be negative!")

    else:
        print("Invalid input! Enter a valid tip percentage.")


# Step 3: Get number of people
while True:

    people_input = input("People: ")

    # Check valid whole number
    if people_input.isdigit():

        people = int(people_input)

        if people > 0:
            break
        else:
            print("People must be greater than zero!")

    else:
        print("Invalid input! Enter a whole number.")


# Step 4: Round bill to 2 decimal places
bill = bill.quantize(
    Decimal("0.01"),
    rounding=ROUND_HALF_UP
)


# Step 5: Calculate tip
tip_amount = (bill * tip / Decimal("100")).quantize(
    Decimal("0.01"),
    rounding=ROUND_HALF_UP
)


# Step 6: Calculate total amount
total = bill + tip_amount


# Step 7: Convert total into paisa
total_paisa = int(total * 100)


# Step 8: Calculate each person's share
share = total_paisa // people


# Step 9: Calculate last person's share
last_share = total_paisa - (share * (people - 1))


# Step 10: Print results
print("-------------------------")

print(f"Tip:       Rs {tip_amount:,.2f}")
print(f"Total:     Rs {total:,.2f}")


# Step 11: Print each person's amount
for person in range(1, people + 1):

    if person == people:
        amount = Decimal(last_share) / Decimal("100")

    else:
        amount = Decimal(share) / Decimal("100")

    print(f"Person {person}:  Rs {amount:,.2f}")