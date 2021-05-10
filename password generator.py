# libraries needed
import pyperclip
import random
import string


def shuffle_pass(p):
    """ shuffle the password and copy to clipboard if c in en needed"""
    password = ''.join(random.sample(p, len(p)))
    print(f"Generated password is:{password}")
    while True:
        choice = input("To copy password enter 'c' :")
        if choice == 'c':
            pyperclip.copy(password)
            print(f"Your {len(password)} Digit Password is copied to clipboard!")
            break
        else:
            print("Entered value is wrong Try again !")


def password_generator():
    """ the password must contain lowercase, uppercase, digits, and punctuations"""
    four_digits = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + \
                random.choice(string.digits) + random.choice(string.punctuation)

    if pass_len == 4:
        # if password is 4 letter long
        shuffle_pass(four_digits)
    else:
        # if password length is higher than 4 it add some printabe letter and add to the four_digit variable
        diff = pass_len - 4
        password_long = ''
        i = 1
        while i <= diff:
            i += 1
            p = random.choice(string.printable)
            password_long += p
        shuffle_pass(four_digits + password_long)


if __name__ == '__main__':

    pass_len = int(input("Enter length of pass:"))

    # checking the entered value it between 4 and 10
    if int(pass_len) < 4:
        print("length of password should be 4-10")
    elif int(pass_len) > 10:
        print("length of password should be 4-10")
    else:
        password_generator()
