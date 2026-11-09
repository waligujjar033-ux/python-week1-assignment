import re

# Step 1: Given text
text = """
Meeting notes 12/03/2026 -- call Sara at 0300-1234567 or email sara.khan@example.com.
Ali's new number: 0321 7654321 (old one 0300-1234567 is still active).
Invoice sent to billing@acme.co on 2026-03-15; reminder due 01/04/2026.
Contact: support@hp-built.org, ALI.R@Mail.com, not-an-email@, 12345, 2026-13-45
"""

# Step 2: Extract emails
emails = re.findall(
    r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
    text
)

unique_emails = []

for email in emails:
    email = email.lower()

    if email not in unique_emails:
        unique_emails.append(email)


# Step 3: Extract phone numbers
phones = re.findall(r'\b03\d{2}[- ]?\d{7}\b', text)

unique_phones = []

for phone in phones:
    phone = phone.replace("-", "").replace(" ", "")
    phone = phone[:4] + "-" + phone[4:]

    if phone not in unique_phones:
        unique_phones.append(phone)


# Step 4: Extract dates
dates = re.findall(
    r'\b\d{2}/\d{2}/\d{4}\b|\b\d{4}-\d{2}-\d{2}\b',
    text
)

valid_dates = []

for date in dates:

    if "/" in date:
        day, month, year = date.split("/")
    else:
        year, month, day = date.split("-")

    day = int(day)
    month = int(month)
    year = int(year)

    # Check leap year
    leap = False

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        leap = True

    # Find maximum days in month
    max_days = 31

    if month == 4 or month == 6 or month == 9 or month == 11:
        max_days = 30

    if month == 2:
        if leap:
            max_days = 29
        else:
            max_days = 28

    # Check valid date
    if year >= 1 and month >= 1 and month <= 12 and day >= 1 and day <= max_days:

        final_date = f"{year:04d}-{month:02d}-{day:02d}"

        if final_date not in valid_dates:
            valid_dates.append(final_date)


# Step 5: Print report
print("===== CONTACT EXTRACTOR REPORT =====")

print(f"\nEmails ({len(unique_emails)}):")
for email in unique_emails:
    print(email)

print(f"\nPhones ({len(unique_phones)}):")
for phone in unique_phones:
    print(phone)

print(f"\nDates ({len(valid_dates)}):")
for date in valid_dates:
    print(date)

print("\n===== REPORT COMPLETED =====")