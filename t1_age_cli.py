import sys
from datetime import datetime, date

# Step 1: Check arguments
# Total 3 arguments hone chahiye
if len(sys.argv) != 3:
    print("Usage: python t1_age_cli.py <name> <YYYY-MM-DD>")
    sys.exit()

# Step 2: Get name and birth date
name = sys.argv[1]
dob_input = sys.argv[2]

# Step 3: Check date format
# Date ka format YYYY-MM-DD hona chahiye
parts = dob_input.split("-")

valid = True

if len(parts) != 3:
    valid = False
else:
    for part in parts:
        if not part.isdigit():
            valid = False

    if len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
        valid = False

# Step 4: Check invalid format
if not valid:
    print(f"Error: '{dob_input}' is not a valid date.")
    print("Usage: python t1_age_cli.py <name> <YYYY-MM-DD>")
    sys.exit()

# Step 5: Convert date parts into numbers
year = int(parts[0])
month = int(parts[1])
day = int(parts[2])

# Step 6: Check month and day
if year < 1 or month < 1 or month > 12 or day < 1:
    valid = False
else:
    # Days in each month
    days_in_month = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

    # Check leap year
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        days_in_month[1] = 29

    # Check maximum days in selected month
    if day > days_in_month[month - 1]:
        valid = False

# Step 7: Show error if date is invalid
if not valid:
    print(f"Error: '{dob_input}' is not a valid date.")
    print("Usage: python t1_age_cli.py <name> <YYYY-MM-DD>")
    sys.exit()

# Step 8: Create birth date
dob = date(year, month, day)

# Step 9: Get today's date
today = date.today()

# Step 10: Check future birth date
if dob > today:
    print(f"Error: '{dob_input}' is not a valid birth date.")
    print("Usage: python t1_age_cli.py <name> <YYYY-MM-DD>")
    sys.exit()

# Step 11: Calculate age
age = today.year - dob.year

# Check if birthday has passed
if (today.month, today.day) < (dob.month, dob.day):
    age = age - 1

# Step 12: Find birth weekday
birth_day = dob.strftime("%A")

# Step 13: Format today's date
today_formatted = today.strftime("%A, %d %B %Y")

# Step 14: Print final output
print(f"Hi {name}! Today is {today_formatted}.")
print(f"You are {age} years old and were born on a {birth_day}.")