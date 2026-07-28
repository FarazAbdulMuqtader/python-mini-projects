def evaluate_password(password):
    length=len(password)>=8
    uppercase=any(char.isupper() for char in password)
    digit=any(char.isdigit() for char in password)
    special_chars = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/"
    special=any(char in special_chars for char in password)

    if length and uppercase and digit and special:
        return "Strong: Password is greater or equal to 8 characters long and contains uppercase letters, digits, special characters."
    elif length and (uppercase or digit or special):
        return "Medium: Password is greater or equal to 8 characters long and contains at least one of the following: uppercase letters, digits, or special characters."
    else:
        return "Weak: Password does not meet the criteria."

password=str(input("Enter candidates password: "))
print(evaluate_password(password))