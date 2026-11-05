# T4 - Password Strength Checker

while True:

    # Ask user for password
    password = input("\nPassword: ")

    # Exit program
    if password == "quit":
        print("Program Closed!")
        break

    # Starting score
    score = 0
    missing = []

    # Rule 1: Check password length
    if len(password) >= 8:
        score += 1
    else:
        missing.append("at least 8 characters")

    # Rule 2: Check lowercase letter
    if any(ch.islower() for ch in password):
        score += 1
    else:
        missing.append("a lowercase letter")

    # Rule 3: Check uppercase letter
    if any(ch.isupper() for ch in password):
        score += 1
    else:
        missing.append("an uppercase letter")

    # Rule 4: Check digit
    if any(ch.isdigit() for ch in password):
        score += 1
    else:
        missing.append("a digit")

    # Rule 5: Check symbol
    if any(not ch.isalnum() and not ch.isspace() for ch in password):
        score += 1
    else:
        missing.append("a symbol")

    # Check password strength
    match score:

        case 0 | 1 | 2:
            strength = "Weak"

        case 3 | 4:
            strength = "Medium"

        case 5:
            strength = "Strong"

    # Display result
    print(f"Strength: {strength} ({score}/5)")

    # Show missing rules
    if missing:
        print("Missing:", ", ".join(missing))