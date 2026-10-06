import string

username = input("What is your username? ")
password = input("What is your password? ")

print(f'{username}, your password is {len(password)} characters long.')

if len(password) >= 12:
    print("Password is at least 12 characters.")
else:
    print("Password is too short.")

if any(char.isupper() for char in password):
    print("Password has uppercase letters.")
else:
    print("Password needs an uppercase letter.")

if any(char.islower() for char in password):
    print("Password has lowercase letters.")
else:
    print("Password needs a lowercase letter.")

if any(char.isdigit() for char in password):
    print("Password has a number.")
else:
    print("Password needs a number.")

if any(char in string.punctuation for char in password):
    print("Password has a symbol.")
else:
    print("Password needs a symbol.")