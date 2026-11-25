while True:
    password = input("Enter password (stop to exit): ")

    if password.lower() == "stop":
        break

    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)

    if len(password) >= 8 and upper and lower and digit:
        print("Strong Password")
    else:
        print("Weak Password")