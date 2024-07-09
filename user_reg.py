# import Decor

print("""
Validate User Registration Data Using simple if/elif/else
Objective: To validate the registration data entered by the user, ensuring that it meets specific criteria
before it’s processed. You will use Python string. User should input the following:
    Username
    Email
    Phone
    Password
    Password repeat
Requirements:
    Username Validation:
        Should be between 5 and 20 characters long.
        Can only contain alphanumeric characters.
        Should not be a reserved name (e.g., ‘admin’, ‘root’, etc.).
    Email Validation:
        Should have a valid email format (e.g., user@example.com).
    Phone Number Validation:
        Should be in a valid format (+37499123456 or 099123456).
        The number should only contain digits, with optional ‘+’ at the beginning.
    Password Validation:
        Should be at least 8 characters long.
        Must contain at least one uppercase letter, one lowercase letter, one digit, 
            and one special character (e.g., !@#$%^&*).
    Password Repeat Validation:
        Should match the initially provided password.
        Ensure the password and its reply are checked together.
        """)

username = ""
email = ""
phone = ""
password = ""
repeat_password = ""

reserved_usernames = ["admin", "root", "user"]
usernames = ["BlackPanther", "Karen", "James"]
emails = ["blackpanter@example.com",
          "karen@example.com",
          "james@example.com"]
phones = ["37496708623",
          "37455417890",
          "37433121212"]


# Validate username
def check_username(username, usernames):
    if username.lower() in reserved_usernames:
        print("Username is reserved.")
        return False
    if username in usernames:
        print("Username already exists.")
        return False
    if not username.isalnum():
        print("Username can only contain alphanumeric characters.")
        return False
    if len(username) < 5 or len(username) > 20:
        print("Username should be between 5 and 20 characters long.")
        return False
    return username


# Validate email
def check_email(email, emails):
    email = email.lower()
    if email in emails:
        print("Email already exists.")
        return False
    if len(email) < 6:
        print("Email should have a valid format (e.g., user@example.com).")
        return False
    if "@" not in email or "." not in email or email.index(".") <= email.index("@") + 1:
        print("Email should have a valid format (e.g., user@example.com).")
        return False
    return email


# Validate phone
def check_phone(phone, phones):
    phone_codes = ['33',
                   '41',
                   '43',
                   '44',
                   '55',
                   '77',
                   '91',
                   '92',
                   '93',
                   '94',
                   '95',
                   '96',
                   '97',
                   '98',
                   '99']
    if len(phone) < 8 or len(phone) > 12:
        print("Phone number should be in a valid format (+37412345678 or 012345678).")
        return False
    if phone[0:4] == "+374" and len(phone) == 12:
        phone = phone[4:]
    elif phone[0:3] == "374" and len(phone) == 11:
        phone = phone[3:]
    elif phone[0] == "0" and len(phone) == 9:
        phone = phone[1:]

    if not phone.isdecimal():
        print("Phone number should only contain digits.")
        return False
    if phone[:2] not in phone_codes:
        print("Phone number does not exist")
        return False

    phone = "374" + phone

    if phone in phones:
        print("Phone number already exists.")
        return False
    return phone


# Validate password
def check_password(password):
    if len(password) < 8:
        print("Password should be at least 8 characters long.")
        return False
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        return False
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        return False
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        return False
    if not any(char in "!@#$%^&*" for char in password):
        print("Password must contain at least one special character.")
        return False
    return password


# Validate repeat password
def check_repeat_password(password, repeat_password):
    if password != repeat_password:
        print("Passwords do not match.")
        return False
    return True


###############################################################
def input_registration_data(username, email, phone, password, repeat_password):
    while True:
        try:
            username = input("Enter username: ")
            if check_username(username, usernames):
                username = check_username(username, usernames)
                print("Username is valid.")
                break
        except ValueError:
            print(ValueError)

    while True:
        try:
            email = input("Enter email: ")
            if check_email(email, emails):
                email = check_email(email, emails)
                print("Email is valid.")
                break
        except ValueError:
            print(ValueError)

    while True:
        try:
            phone = input("Enter phone number: ")
            if check_phone(phone, phones):
                phone = check_phone(phone, phones)
                print("Phone is valid.")
                break
        except ValueError:
            print(ValueError)

    while True:
        try:
            password = input("Enter password: ")
            if check_password(password):
                print("Password is valid.")
                break
        except ValueError:
            print(ValueError)

    while True:
        try:
            repeat_password = input("Repeat password: ")
            if check_repeat_password(password, repeat_password):
                print("Repeat password is valid.")
                break
        except ValueError:
            print(ValueError)

    user_data = dict(username=username, email=email, phone=phone, password=password)

    return user_data

user = input_registration_data(username, email, phone, password, repeat_password)


print("Username:", user["username"],
      "\nEmail:", user["email"],
      "\nPhone:", user["phone"],
      "\nPassword:", user["password"])
