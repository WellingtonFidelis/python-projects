import pyrebase
import firebase_config

firebase_config = firebase_config.Firebase().firebase_config
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()


def signup():
    print("Signing up...")
    email = input("Enter your e-mail:\n")
    password = input("Enter your password:\n")

    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("Successfully, acount added.")

        ask = input("Do you want to login now? [y/n]")
        if ask == "y":
            login()

    except:
        print("E-mail already exists.")


def login():
    print("Login ...")
    email = input("Enter your e-mail:\n")
    password = input("Enter your password:\n")

    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Logged in!")
    except:
        print("Invalid e-mail or password!")


answer = input("Are you a new user? [y/n]")
if answer == "y":
    signup()
else:
    login()
