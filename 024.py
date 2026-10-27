"""Problem 024: Login Validator : Check whether a username and password combination is valid."""

# Example credentials for practice
valid_username = "admin"
valid_password = "python123"
username = input("Username: ")
password = input("Password: ")
if username == valid_username and password == valid_password:
    print("Login successful")
else:
    print("Invalid username or password")
