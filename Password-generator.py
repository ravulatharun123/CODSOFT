import random

# Define character sets
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

def generate_password(min_length, max_length):
    # Get the range for each character type
    range_letters = random.randint(min_length, max_length)
    range_numbers = random.randint(min_length, max_length)
    range_symbols = random.randint(min_length, max_length)

    # Generate the password
    password = ''.join([random.choice(letters) for _ in range(range_letters)] +
                       [random.choice(numbers) for _ in range(range_numbers)] +
                       [random.choice(symbols) for _ in range(range_symbols)])

    # Shuffle the password for added security
    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)

    print(f"Your generated password is: {shuffled_password}")

# Get minimum and maximum lengths for each character type from the user
try:
    min_length = int(input("Enter the minimum length for each character type: "))
    max_length = int(input("Enter the maximum length for each character type: "))
except ValueError:
    print("Please enter valid numbers for minimum and maximum lengths.")
else:
    generate_password(min_length, max_length)
