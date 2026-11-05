import sys  # Terminal se arguments lene ke liye
from datetime import datetime, date  # Date check aur age calculate karne ke liye

# Step 1: Check command-line arguments
# len() arguments ki total quantity check karta hai
# 3 arguments hone chahiye: file name, name, date of birth
if len(sys.argv) != 3:
    print("Usage: python t1_age_cli.py <name> <YYYY-MM-DD>")
    sys.exit()  # Agar arguments galat hon to program band kar dega


# Step 2: Get name and date of birth
# sys.argv[0] = Python file ka naam
# sys.argv[1] = User ka naam
# sys.argv[2] = User ki date of birth

name = sys.argv[1]  # Terminal se user ka naam lena
dob_input = sys.argv[2]  # Terminal se date of birth lena


# Step 3: Validate date of birth
try:
    # strptime() date ko string se date object mein convert karta hai
    # %Y = Year, %m = Month, %d = Day
    dob = datetime.strptime(dob_input, "%Y-%m-%d").date()

    # strftime() date ko dobara YYYY-MM-DD format mein convert karta hai
    # Agar format galat ho to ValueError generate hoga
    if dob.strftime("%Y-%m-%d") != dob_input:
        raise ValueError

except ValueError:
    # Agar date invalid ho to error message show karega
    print(f"Error: '{dob_input}' is not a valid date.")
    print("Usage: python t1_age_cli.py <name> <YYYY-MM-DD>")
    sys.exit()  # Program safely band karna


# Step 4: Get today's date
# date.today() computer ki current date leta hai
today = date.today()


# Step 5: Check future birth date
# Agar birth date aaj ki date se aage ho to error show karega
if dob > today:
    print(f"Error: '{dob_input}' is not a valid birth date.")
    print("Usage: python t1_age_cli.py <name> <YYYY-MM-DD>")
    sys.exit()


# Step 6: Calculate exact age
# Current year mein se birth year minus karna
age = today.year - dob.year

# Check karna ke is saal birthday aa chuka hai ya nahi
# Agar birthday abhi nahi aaya to age mein se 1 minus hoga
if (today.month, today.day) < (dob.month, dob.day):
    age -= 1


# Step 7: Get birth weekday
# strftime("%A") date ka weekday name batata hai
# Example: Monday, Tuesday, Wednesday, Sunday
birth_day = dob.strftime("%A")


# Step 8: Format today's date
# %A = Weekday name
# %d = Day
# %B = Month name
# %Y = Year
today_formatted = today.strftime("%A, %d %B %Y")


# Step 9: Print final result
# f-string variables ki values text ke andar show karta hai

print(f"Hi {name}! Today is {today_formatted}.")

print(f"You are {age} years old and were born on a {birth_day}.")


# --------------------------------------------------
# TERMINAL TEST COMMANDS
# --------------------------------------------------

# Test 1: Correct Input
# python t1_age_cli.py Ali 2005-08-14

# Test 2: Missing Argument
# python t1_age_cli.py Ali

# Test 3: Invalid Date
# python t1_age_cli.py Ali 2005-13-40

# Test 4: Extra Argument
# python t1_age_cli.py Ali 2005-08-14 Lahore

# Test 5: Future Birth Date
# python t1_age_cli.py Ali 2030-05-10