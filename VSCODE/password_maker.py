import random
import string

def generate_password(length):
    if length < 4:
        return "Password ki length kam se kam 4 honi chahiye!"

    # letters, numbers, symbols sab include karenge
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # kam se kam 1 letter, 1 digit, 1 symbol pakka rahe
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # baki ki length random se fill karo
    all_chars = letters + digits + symbols
    password += random.choices(all_chars, k=length - 3)

    # shuffle kar do taaki order random ho
    random.shuffle(password)

    return ''.join(password)

print("==== Strong Password Generator ====")

try:
    n = int(input("Kitne characters ka password chahiye? "))
    result = generate_password(n)
    print("\nTumhara Strong Password:", result)

except ValueError:
    print("Please sirf number daalo!")