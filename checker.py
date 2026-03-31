import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include numbers")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Use special characters")

    return score, feedback

def main():
    password = input("Enter your password: ")
    score, feedback = check_password_strength(password)

    print("\nPassword Strength:", end=" ")
    
    if score <= 2:
        print("Weak")
    elif score <= 4:
        print("Medium")
    else:
        print("Strong")

    if feedback:
        print("\nSuggestions:")
        for tip in feedback:
            print("-", tip)

if __name__ == "__main__":
    main()
