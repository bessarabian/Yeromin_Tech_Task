import sys
from string import  ascii_lowercase, \
    ascii_uppercase, digits, punctuation


def check_password(password: str):
    # Variables zone begins
    low_letters, up_letters, numbs, symbs, length = False, False, False, False, False
    conclusion = ''
    # Variables zone ends

    # Validation password length
    try:
        if len(password) >= 14:
            length = True
        # Looking through symbols
        for i in password:
            if i in ascii_lowercase:
                low_letters = True
            if i in ascii_uppercase:
                up_letters= True
            if i in digits:
                numbs = True
            if i in punctuation:
                symbs = True
    except Exception:
        print('Invalid data was entered x_x')

    # Checking for cons
    if low_letters == False:
        conclusion += '- Password must contain lowercase letters\n'
    if up_letters == False:
        conclusion += '- Password must contain uppercase letters\n'
    if numbs == False:
        conclusion += '- Password must contain digits\n'
    if symbs == False:
        conclusion += '- Password must contain special symbols({0})\n'.format(punctuation)
    if length == False:
        conclusion += '- Password must be at least 14 characters long!'


    # if empty string was entered
    try:
        if not len(password):
            print('Empty string was entered!')
    except Exception:
        print('Invalid data was entered x_x')

    # final result
    if len(conclusion) == 0:
        # if everithing is cool
        return 'Your password is strong enough!'
    else:
        # if our programme have smth to say
        return conclusion
    

if __name__ == '__main__':
    print(check_password(sys.argv[1]))