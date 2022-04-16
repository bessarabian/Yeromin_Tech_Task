import random
from string import  ascii_lowercase, \
    ascii_uppercase, digits, punctuation
from checker import check_password

def generate_password():
    chars = ascii_lowercase + ascii_uppercase + digits + punctuation
    password = ''

    # building a password step by step
    while True:
        password += random.choice(chars)
        if len(password) == 16:
            if check_password(password) == True:
                return 'Your strong password: ' + password
            else:
                password = ''
                continue

    
    

if __name__ == '__main__':
    print(generate_password())