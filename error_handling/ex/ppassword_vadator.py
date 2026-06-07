class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

def is_alpha(password):
    return password.isalpha()

def is_digit(password):
    return password.isdigit()

def is_symbols(password):
    return all(ch in SPECIAL_SYMBOLS for ch in password)

SPECIAL_SYMBOLS = "@*&%"
while True:

    password = input()

    if password == "Done":
        break

    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")
    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    if is_alpha(password) or is_digit(password) or is_symbols(password):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(ch in SPECIAL_SYMBOLS for ch in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")


    print("Password is valid")

