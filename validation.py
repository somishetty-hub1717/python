def password_validation(pas):
    if len(pas)<8:
        return False
    has_upper=False
    has_lower=False
    has_digit=False
    has_special=False
    for char in pas:
        if char.isupper():
            has_upper=True
        elif char.islower():
            has_lower=True
        elif char.isdigit():
            has_digit=True
        elif char in "!@#$%^&*":
            has_special=True
    return has_upper & has_lower & has_digit & has_special
pas="Saisrujana4@"
if password_validation(pas):
    print("valid")
else:
    print("invalid")
    