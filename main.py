import string
import random

# true loop
while True:
    # Main menu loop
    user_input = input(f"Choose an option: "
                       f"\n\n1. Generate Password "
                       f"\n2. View Passwords "
                       f"\n3. View Accounts "
                       f"\n4. Add Account "
                       f"\n5. Delete Account "
                       f"\n6. Exit Application "
                       f"\n\nEnter Input: ")
    try:
        val = int(user_input)
    except ValueError:
        print(f"not a digit")
    # Check if input is valid
    if val in (1, 2, 3, 4, 5, 6):
        match val:
            # Proceed to generate a password
            case 1:
                print(f"Generate a new password")
                password_type_select = input(f"Select an type: "
                                             f"\n1. Uppercase "  # ABC
                                             f"\n2. Lowercase "  # abc
                                             f"\n3. Numbers "  # 123
                                             f"\n4. Mix "  # Ab3
                                             f"\n5. GenericPassword (Cap,Num and Sym"  # Ab3!
                                             f"\n6. Debug(Unsafe size) "  # Size of 200000
                                             f"\n\nEnter selection: ")
                try:
                    selection = int(password_type_select)
                except ValueError:
                    print(f"not a digit")
                match selection:
                    case 1:
                        letters = string.ascii_uppercase
                        result_string = ''.join(
                            (random.choice(letters) for i in range(int(input("Select a password length: ")))))
                        result_string.startswith("\n")
                        print("\n" + result_string + "\n")
                        print(f'Returning to main menu!')
                    case 2:
                        letters = string.ascii_lowercase
                        result_string = ''.join(
                            (random.choice(letters) for i in range(int(input("Select a password length: ")))))
                        result_string.startswith("\n")
                        print("\n" + result_string + "\n")
                        print(f'Returning to main menu!')
                    case 3:
                        numbers = string.digits
                        result_string = ''.join(
                            (random.choice(numbers) for i in range(int(input("Select a password length: ")))))
                        result_string.startswith("\n")
                        print("\n" + result_string + "\n")
                        print(f'Returning to main menu!')
                    case 4:
                        generic_letters = string.ascii_letters
                        result_string = ''.join(
                            (random.choice(generic_letters) for i in range(int(input("Select a password length: ")))))
                        result_string.startswith("\n")
                        print("\n" + result_string + "\n")
                        print(f'Returning to main menu!')
                    case 5:
                        string_letters = string.ascii_letters
                        string_numbers = string.digits
                        string_symbols = string.punctuation
                        string_line = string_letters + string_symbols + string_numbers
                        result_string = ''.join(
                            (random.choice(string_line) for i in range(int(input("Select a password length: ")))))
                        result_string.startswith("\n")
                        print("\n" + result_string + "\n")
                        print(f'Returning to main menu!')
            # Not implemented as of V1.0.1
            case 2:
                print(f'Test 2')
            case 3:
                print(f'Test 3')
            case 4:
                print(f'Test 4')
            case 5:
                print(f'Test 5')
            # Exit the programme
            case 6:
                print(f'Test 6')
                quit('Quit programme')
    else:
        print("Enter a valid number")
