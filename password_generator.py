import random
from string import  ascii_lowercase, \
    ascii_uppercase, digits, punctuation

def generate_password():
    chars = ascii_lowercase + ascii_uppercase + digits + punctuation
    password = ''

    # building a password step by step
    while True:
        password += random.choice(chars)
        if len(password) == 16:
            break

    return 'Your strong password: ' + password

if __name__ == '__main__':
    print(generate_password())