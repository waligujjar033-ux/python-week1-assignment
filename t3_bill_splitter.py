# =====================================
# T3 - BILL SPLITTER
# =====================================

# Import Decimal for correct money calculations
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


# Function to get bill amount
def get_bill():

    while True:

        try:
            bill = Decimal(input("Enter bill amount (Rs): "))

            # Check for invalid numbers
            if not bill.is_finite():
                print("Please enter a valid number.")
                continue

            # Check for negative amount
            if bill < 0:
                print("Bill cannot be negative.")
                continue

            return bill

        except InvalidOperation:
            print("Wrong input! Enter a number.")


# Function to get tip percentage
def get_tip():

    while True:

        try:
            tip = Decimal(input("Enter tip percentage: "))

            # Check for invalid numbers
            if not tip.is_finite():
                print("Please enter a valid number.")
                continue

            # Check for negative tip
            if tip < 0:
                print("Tip cannot be negative.")
                continue

            return tip

        except InvalidOperation:
            print("Wrong input! Enter a number.")


# Function to get number of people
def get_people():

    while True:

        try:
            people = int(input("Enter number of people: "))

            # People must be greater than zero
            if people <= 0:
                print("People must be greater than zero.")
                continue

            return people

        except ValueError:
            print("Wrong input! Enter a whole number.")


# Main function
def main():

    print("===== BILL SPLITTER =====")

    # Step 1: Get bill amount
    bill = get_bill()

    # Step 2: Get tip percentage
    tip = get_tip()

    # Step 3: Get number of people
    people = get_people()

    # Step 4: Round bill to 2 decimal places
    bill = bill.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )

    # Step 5: Calculate tip amount
    tip_amount = (bill * tip / Decimal("100")).quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )

    # Step 6: Calculate total bill
    total = bill + tip_amount

    # Step 7: Convert total into paisa
    total_paisa = int(total * 100)

    # Step 8: Divide bill among people
    share = total_paisa // people

    # Step 9: Calculate last person's share
    last_share = total_paisa - (share * (people - 1))

    # Step 10: Show results
    print("\n-------------------------")

    print(f"Tip:       Rs {tip_amount:,.2f}")

    print(f"Total:     Rs {total:,.2f}")

    # Step 11: Show each person's amount
    for person in range(1, people + 1):

        if person == people:
            amount = Decimal(last_share) / Decimal("100")

        else:
            amount = Decimal(share) / Decimal("100")

        print(f"Person {person}:  Rs {amount:,.2f}")


# Start the program
if __name__ == "__main__":
    main()