import re

def check_password_strength(password):
    length_score = len(password) >= 8
    uppercase_score = bool(re.search(r'[A-Z]', password))
    lowercase_score = bool(re.search(r'[a-z]', password))
    digit_score = bool(re.search(r'\d', password))
    special_char_score = bool(re.search(r'[^A-Za-z0-9]', password))

    total_score = sum([length_score, uppercase_score, lowercase_score, digit_score, special_char_score])

    if total_score == 5:
        return "Very Strong"
    elif total_score >= 3:
        return "Strong"
    elif total_score >= 2:
        return "Moderate"
    elif total_score >= 1:
        return "Weak"
    else:
        return "Very Weak"

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print("Password strength:", strength)

if __name__ == "__main__":
    main()
