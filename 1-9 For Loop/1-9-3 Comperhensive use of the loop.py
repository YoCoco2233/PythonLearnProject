# 2024-7-24 23:09 start, 2024-7-24 23:29 end  @YoCoco2233 1-9-3 Comprehensive use of the loop.
import time

# Set correct username and password
correct_username = "YoCoco"
correct_password = "2233"

# Login attempt limit
attempt_limit = 3


def login(username, password):
    """
    Checks if the username and password are correct.
    """
    if username == correct_username and password == correct_password:
        return True
    elif username == correct_username:
        return "Username is correct,Password is incorrect."
    else:
        return "Username is incorrect."


while True:
    for attempt in range(attempt_limit):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        result = login(username, password)

        if result is True:
            print(f"Welcome {username}!")
            break  # Breakout of the loop if login is successful.
        else:
            print(result)

        if attempt == attempt_limit - 1:
            print("Too many login failures. Please wait 30 seconds before trying again.")
            time.sleep(30)  # Wait for 30 seconds.
        # Ask if the user wants to continue trying to login
        continue_login = input("Would you like to continue (y/n): ")
        if continue_login.lower() != "y":
            break
