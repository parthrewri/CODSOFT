import random
import string

def generate_password(length):
    # Define possible characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password using random.choices (Python 3.6+)
    password = ''.join(random.choices(characters, k=length))

    return password

def main():
    print("Welcome to the Password Generator!")

    # Get desired password length from the user
    while True:
        try:
            length = int(input("Enter the length of the password you want to generate: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Generate and display the password
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()