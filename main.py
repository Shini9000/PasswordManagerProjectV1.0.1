import string
import random
import time

project_version = '1.0.3'
admin_signedin = False

print(f"Welcome to the PasswordManager Application version: " + project_version +
      f"\nFor more information please go to the github @"
      f"\nhttps://github.com/Shini9000/PasswordManagerProject"
      f"\nAnd thank you for downloading and testing my application :)\n\n")

""" safe keeping module
def savepassword(result_string):
    print(result_string)
    if input(f'Do you wish to save this password?').capitalize() == 'Y':
       print(f'Not implemented as of V1.0.3')#
       admin_signedin = not False
        admin_signon(admin_signedin)
    else:
        print(f'Returning to main menu!')


def admin_signon(admin_signedin):
    print(admin_signedin)
    input('A')
"""

# Function to generate the password
def generatepassword():
    print(f"Generate a new password")
    password_type_select = input(f"\n\nSelect an type: "
                                 f"\n   1. Uppercase "  # ABC
                                 f"\n   2. Lowercase "  # abc
                                 f"\n   3. Numbers "  # 123
                                 f"\n   4. Mix "  # Ab3
                                 f"\n   5. GenericPassword (Cap,Num and Sym"  # Yz1!
                                 f"\nEnter selection: ")
    try:
        selection = int(password_type_select)
    except ValueError:
        print(f"not a digit")
    if selection not in (1, 2, 3, 4, 5):
        print(f'Please select a valid option!')
        generatepassword()
    match selection:
        case 1:
            # Uppercase password generator
            letters = string.ascii_uppercase
            result_string = ''.join(
                (random.choice(letters) for i in range(int(input("Select a password length: ")))))
            result_string.startswith("\n")
            print("\n" + result_string + "\n")
            print(f'Returning to main menu!')
        case 2:
            # Lowercase password generator
            letters = string.ascii_lowercase
            result_string = ''.join(
                (random.choice(letters) for i in range(int(input("Select a password length: ")))))
            result_string.startswith("\n")
            print("\n" + result_string + "\n")
            print(f'Returning to main menu!')
        case 3:
            # Number password generator
            numbers = string.digits
            result_string = ''.join(
                (random.choice(numbers) for i in range(int(input("Select a password length: ")))))
            result_string.startswith("\n")
            print("\n" + result_string + "\n")
            print(f'Returning to main menu!')
        case 4:
            # Mix password generator
            generic_letters = string.ascii_letters
            numbers = string.digits
            string_line = numbers + generic_letters
            result_string = ''.join(
                (random.choice(string_line) for i in range(int(input("Select a password length: ")))))
            result_string.startswith("\n")
            print("\n" + result_string + "\n")
            print(f'Returning to main menu!')
        case 5:
            # Generic password generator
            string_letters = string.ascii_letters
            string_numbers = string.digits
            string_symbols = string.punctuation
            string_line = string_letters + string_symbols + string_numbers
            result_string = ''.join(
                (random.choice(string_line) for i in range(int(input("Select a password length: ")))))
            result_string.startswith("\n")
            print("\n" + result_string + "\n")
            print(f'Returning to main menu!')
    savepassword(result_string)


def savepassword(result_string):
    print(result_string)
    if input(f'Do you wish to save this password?').capitalize() == 'Y':
        print(f'Not implemented as of V1.0.3')
        admin_signedin = not False
        admin_signon(admin_signedin)
    else:
        print(f'Returning to main menu!')

def admin_signon(admin_signedin):
    print(admin_signedin)
    input('A')

# true loop
while True:
    time.sleep(2.5)
    # Main menu loop
    user_input = input(f"Choose an option: "
                       f"\n     1. Generate Password "
                       f"\n     2. View Passwords "
                       f"\n     3. View Accounts "
                       f"\n     4. Add Account "
                       f"\n     5. Delete Account "
                       f"\n     6. Help menu"  # Help menu
                       f"\n     7. Exit Application "
                       f"\nEnter Input: ")
    try:
        val = int(user_input)
    except ValueError:
        print(f"not a digit")
    # Check if input is valid
    if val not in (1, 2, 3, 4, 5, 6, 7):
        print(f'Please select a valid option!')
        continue
    match val:
        # Proceed to generate a password
        case 1:
            generatepassword()
        # Not implemented as of V1.0.1
        case 2:
            print(f'Password management not available in version: ' + project_version)
        case 3:
            print(f'Account management not available in version: ' + project_version)
        case 4:
            print(f'Test 4')
        case 5:
            print(f'Account management not available in version: ' + project_version)
        case 6:
            print(f'Help menu')
            file = open("help.txt")
            print(file.read())
            input('Press enter to continue... ')
            file.close()
            print(f'Returning to main menu please wait.')
            continue

        # Exit the programme
        case 7:
            print(f'Test 7')
            quit('Quit programme')
