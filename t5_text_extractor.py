import re
from datetime import datetime

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

# Convert emails to lowercase and remove duplicates
emails = list(dict.fromkeys(email.lower() for email in emails))


# Step 3: Extract phone numbers
phones = re.findall(r'\b03\d{2}[- ]?\d{7}\b', text)

# Remove duplicates and use same format
phones = list(dict.fromkeys(
    phone.replace(" ", "").replace("-", "")
    for phone in phones
))

phones = [phone[:4] + "-" + phone[4:] for phone in phones]


# Step 4: Extract dates
dates = re.findall(
    r'\b\d{2}/\d{2}/\d{4}\b|\b\d{4}-\d{2}-\d{2}\b',
    text
)

valid_dates = []

for date in dates:

    try:
        if "/" in date:
            new_date = datetime.strptime(date, "%d/%m/%Y")
        else:
            new_date = datetime.strptime(date, "%Y-%m-%d")

        final_date = new_date.strftime("%Y-%m-%d")

        if final_date not in valid_dates:
            valid_dates.append(final_date)

    except ValueError:
        continue


# Step 5: Print final report
print("===== CONTACT EXTRACTOR REPORT =====")

print(f"\nEmails ({len(emails)}):")
for email in emails:
    print(email)

print(f"\nPhones ({len(phones)}):")
for phone in phones:
    print(phone)

print(f"\nDates ({len(valid_dates)}):")
for date in valid_dates:
    print(date)

print("\n===== REPORT COMPLETED =====")