import random
import string

def generate_captcha(length=6):
    characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(characters) for _ in range(length))
    return captcha

def captcha_system():
    captcha = generate_captcha()
    print("CAPTCHA:", captcha)

    user_input = input("Enter the CAPTCHA: ")

    if user_input == captcha:
        print("Access Granted. You are Human!")
    else:
        print("Access Denied. Incorrect CAPTCHA.")

captcha_system()