class NameTooShortError(Exception):
    pass
class MustContainAtSymbolError(Exception):
    pass
class InvalidDomainError(Exception):
    pass

VALID_DOMAIN = [".com", ".bg", ".org", ".net"]
MIN_SYMBOLS = 4
while True:
    email = input()
    if email == 'End':
        break
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    if len(email.split('@')[0]) <= MIN_SYMBOLS:
        raise NameTooShortError("Name must be more than 4 characters")

    if not any(email.endswith(domain) for domain in VALID_DOMAIN):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")


    print("Email is valid")