import re


def check_password_strength(password):
    minimum_password_length = 12

    if len(password) < minimum_password_length:
        return "Password is too short"

    if not re.search(r'[A-Z]', password):
        return "Password must include at least one uppercase letter"

    if not re.search(r'[a-z]', password):
        return "Password must include at least one lowercase letter"

    if not re.search(r'[0-9]', password):
        return "Password must include at least one digit"

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password must include at least one special character"

    return "All Good"


password = input("Please Enter Your Password: ")
result = check_password_strength(password)
print(result)
