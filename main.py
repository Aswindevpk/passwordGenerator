# libraries needed
import pyperclip
import random
import string


class PasswordGenerator:

    def __init__(self, pass_length):
        self.pass_length = pass_length

    @classmethod
    def shuffle_pass(cls, p):
        """ shuffle the password and copy to clipboard if c in en needed"""
        password = ''.join(random.sample(p, len(p)))
        print(f"Generated password is:{password}")
        pyperclip.copy(password)
        print(f"Your {len(password)} Digit Password is copied to clipboard!")

    def generate(self):
        """ the password must contain lowercase, uppercase, digits, and punctuations"""

        four_digits = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + \
                    random.choice(string.digits) + random.choice(string.punctuation)

        if self.pass_length == 4:

            # if password is 4 letter long
            self.shuffle_pass(four_digits)
        else:

            # if password length is higher than 4 it add some printable letter and add to the four_digit variable
            diff = self.pass_length - 4
            password_long = ''
            i = 1
            while i <= diff:
                i += 1
                p = random.choice(string.printable)
                password_long += p
            self.shuffle_pass(four_digits + password_long)



password = PasswordGenerator(pass_length=10)  # creating an instance
password.generate()      # generating a password