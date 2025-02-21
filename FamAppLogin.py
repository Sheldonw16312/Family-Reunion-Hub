import ast
import myenc

#Family Reunion Hub App

#Users who currently have an account
users = {}

#Turns file string into dict and assigns contents to empty dict above
f = open("upw.txt", "r")
string_data = f.read()
users = ast.literal_eval(string_data)
f.close()

#Home/Hub
def home():
    print("welcome to the Family Reunion Hub!")

#Create an account
def create():

    print("|Account Creation|")

    #create email for new account
    def email_create():
        email = input("Email: ")
        confirm = input(f"You entered '{email}'. Is this correct? (Yes/No) ")

        if confirm.casefold() == "Yes".casefold():
            password_create(email)
        else:
            print("Returning to create email")
            email_create()

    #create password for new account
    def password_create(x):
        password = input("Password: ")
        conpassword = input("Confirm Password: ")

        if password == conpassword:
            epw = myenc.encrypt(password)
            print("Account Created. Returning to Login.")
            users[x] = epw

            #Writes dict to .py file to be assigned at new session
            f = open("upw.txt", "w")
            f.write(f"{users}")
            f.close()

            login()
        else:
            print("The passwords do not match.")
            password_create(x)
    

    email_create()

#Login
def login():

    print("|Login|")

    def init_login():
        print("Enter 'Create' to create an account." )
        email = input("Email: ")

        if email.casefold() == "Create".casefold():
            create()
        elif email in users:
            password = input("Password: ")

            encpw = users[email]
            decpw = myenc.decrypt(encpw)
            decpass = "".join(decpw)

            if password != decpass:
                print("The passowrd is incorrect.")
                init_login()
            else:
                home()
        elif email not in users:
            print("Their is not an account associated with this email.")
            init_login()

    init_login()

login()