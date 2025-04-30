from random import randint
import sqlite3
from flask import Flask, jsonify, render_template, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import requests
from flask_cors import CORS


app = Flask(__name__) # connects app to a flask command which allows connection between the languages
CORS(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"# allows for this varibale to be used under login which goes onto coding the users login sequence

@app.route('/Homepage', methods = ['GET', 'POST'])
def homepage(): # creates a function which shows methods for the home page and redirects the user back to the home page if they click on the title card
    if requests.method == 'POST':
        return render_template("Homepage.html")
    elif request.method == 'GET':
        pass
    else:
        return render_template("Homepage.html")

@app.route('/login page', methods = ['POST'])
def login(): # creates a function that allows navigation through the login sequence
    if requests.method == 'POST':
        Email = request.form.get("Email")
        password = request.form.get("Password")
        Email = info.query.filter_by(Email=Email).first()# filters through all emails in database and uses first one that matches the filter
        password = info.query.filter_by(password=password).first()# filters through all password in database and uses first one that matches the filter
    if Email and password in info:
        login_user()
        return render_template('Homepage.html')# if the password and email are in the table then the user is logged in and the user is returned back to the home page
    else:
        message = "invalid login, please try again."
    return render_template("login page.html") # if it isnt then is shows a message saying its invalid and return them to the login page for another attempt

@app.route('/createAccount', methods = ['GET', 'POST'])
def createacc(): # creates a function for creating an account for the user
    if requests.method == 'POST':
        Name = request.form.get("Name")
        Email = request.form.get("Email")
        password = request.form.get("Password")# gets all needed inputs from the user and puts them in variables
        if Name and  Email and  password not in User_table:
            cursor.execute("INSERT INTO TBL_users (Name, Email, Password) VALUES(?, ?, ?)", (Name), (Email), (password))
            conn.commit()
            print("you have now created an account")
            return render_template("login page.html")# if the inputs arent in the table then it inserts them into the table and creates their account and redirects them to the login page
        else:
            return jsonify({"An account under those credentials is already taken"})#if its in the table then it shows a message saying that an account is already made using those inputs
    else:
        return render_template("createAccount.html") # else it reloads the page

@app.route('/forgotpassword', methods = ['GET', 'POST'])
def forgotpassword(): # creates a function for resetting a password
    if requests.method == 'POST':
        Email = request.method.get("Email")
        currpass = request.emthod.get("currpass")
        newpass = request.method.get("newpass")
        re = request.method.get("re-type")# gets all inputs from the user and adds tem to a variable
        if Email not in forgot_password:
            return jsonify({"error": "your email must be in our system try again"}) # if their email isnt in the table then an error message is displayed
        elif currpass not in forgot_password:
            return jsonify({"error": "you must get your current password correct to be abel tor eset your password"}) # if the current password isnt in the table then an error message is displayed
        elif newpass and re not in forgot_password:
            forgot_password.append({"New Password": newpass, "re-typed password": re})# if the new password arent in the database then it adds them to the database
        else:
            return jsonify({"message": "your information is all correct, you may reset your password now"})# if its all good then it allows the user to reset their password
    else:
        return render_template("forgotpassword.html") # else it reloads the page

@app.route('/info', methods = ['GET', 'POST'])
def infopage(): #creates a fucntion to load the info page 
    if requests.method == 'POST':
        return render_template("info.html")
    else:
        return render_template("info.html")

@app.route('/booking', methods = ['GET', 'POST'])
@login_required# requires login for access to the page
def bookpage(): # creates a fucntion to load the booking page
    if requests.method == 'POST':
        Time = request.form.get("Time")
        Date = request.form.get("Date")# gets inputs and assings them to variables
        if Time and Date not in bookings_table:
            cursor.execute("INSERT INTO TBL_bookings (Time, Date) VALUES(?, ?)", (Time), (Date))
            conn.commit()# if their not in the table then it inserts them into it
            print ("you have now added a booking into our system")
            return render_template("booking.html")
        else:
            return jsonify({"message": "That time and date slot isnt available at the moment, please try another around your needs."})# if they are then the user is tld they cant book that time and date
    else:
        return render_template("booking.html")#else it reload the page

@app.route('/calculate', methods = ['GET', 'POST'])
def calculation():# creates a function for loading the calculation page
    if requests.method == 'POST':
        return render_template("calculate.html")
    else:
        return render_template("calculate.html")

@app.route('/contact', methods = ['GET', 'POST'])
def contact():# creates a function for the contact page
    if requests.method == 'POST':
        Email = request.form.get("Email")
        Message = request.form.get("Message")# gets the inputs and assigns variables to them
        if not Email or not Message:
            return jsonify({"error": "both of the inputs are required"})# if any are blank then it returns an error message

        messages.append({"Email": Email, "Message": Message})#adds the email and message to the messages array

        return render_template("contact.html")
    elif request.method == 'GET':
        pass
    else:
        return render_template("contact.html")

@app.route('/payment', methods = ['GET', 'POST'])
def paypage():# creates a function for payment page
    if requests.method == 'POST':
        cardnum = request.form.get("cardnum")
        expiry = request.form.get("expiry")
        CVV = request.form.get("CVV")
        name = request.form.get("name")# gets all inputs and assigns variables to them
        if cardnum not in payment_table:
            payment_table.append({"Cardnumber": cardnum})# adds cardnum if its not in the table
        elif expiry not in payment_table:
            payment_table.append({"Expiration Date": expiry})# adds expiry date to the table if its not in it
        elif CVV not in payment_table:
            payment_table.append({"CVV(3 num on back": CVV})# add CVV to the table if it not in the table
        elif name not in payment_table:
            payment_table.append({"Name of CardHolder": name})# adds the name if not in the table
        else:
            pass
    else:
        return render_template("payment.html")

@app.route('/settings', methods = ['GET', 'POST'])
@login_required#requires login to get on the page
def settings():# creates a function for the settings page
    if requests.method == 'POST':
        return render_template("profile page.html")
    else:
        return render_template("profile page.html")



conn = sqlite3.connect("Rolsa technolgies")
cursor = conn.cursor()#connects to the database "Rolsa technologies" 

def User_table():#made a table for users info so i can use it in the code above for differnet areas
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS TBL_users (
                    USERID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Email TEXT,
                    Password TEXT,
                    Name TEXT)
                    """)

def item_table():#made a table for item info so i can use it in the code above for differnet areas
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS TBL_Item(
                    ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Amount INTEGER,
                    item_type TEXT)
                    """)

def bookings_table():#made a table for booking info so i can use it in the code above for differnet areas
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS TBL_bookings(
                BookingID INTEGER PRIMARY KEY AUTOINCREMENT,
                Time DATETIME,
                Date DATETIME)
                """)

def calculate_table():#made a table for calculation info so i can use it in the code above for differnet areas
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS TBL_calculate(
                    CalculateID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Result INTEGER)
                    """)


def payment_table():#made a table for payment info so i can use it in the code above for differnet areas
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS TBL_payment(
                    PaymentID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Cardnum INTEGER,
                    EXPIRY DATE,
                    CVV INTEGER,
                    name TEXT)
                    """)



def forgot_password():#made a table for the forgot password area so i can use it in the code above for differnet areas
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS TBL_Forgot(
                    Email TEXT,
                    Currpass TEXT,
                    newpass TEXT,
                    re-type TEXT)
                    """)


def messages(): #made a table for message info so i can use it in the code above for differnet areas
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS TBL_MESSAGE(
                    Message TEXT,
                    Email TEXT)
                    """)


import uuid
random_id=uuid.uuid4()# allows em to generate random id's
def info(Email, Password, Name, USERID=random_id):
    cursor.executemany("INSERT INTO TBL_users (USERID, Email, Password, Name) VALUES(?, ?, ?, ?)", (str(random_id), (Email), (Password),(Name)))# inserts data into users for their info being inputted into the table for functions in the code above
    conn.commit()

def item(Amount, item_type, ItemID = random_id):
    cursor.executemany("INSERT INTO TBL_Item(?, ?, ?)", (str(random_id), (Amount), (item_type)))# inserts data into items for their info being inputted into the table for functions in the code above

def book(Time, Date, BookingID=random_id):
    cursor.executemany("INSERT INTO TBL_bookings VALUES(?, ?, ?)", (str(random_id), (Time), (Date)))# inserts data into bookings for their info being inputted into the table for functions in the code above

def calculate(Name, Result, calculateID=random_id):
    cursor.executemany("INSERT INTO TBL_calculate VALUES(?, ?, ?)", (str(random_id), (Name), (Result)))# inserts data into calculations for their info being inputted into the table for functions in the code above

def message(Message, Email):
    cursor.executemany("INSERT INTO TBL_Message VALUES(?, ?)", (Message), (Email))# inserts data into messages for their info being inputted into the table for functions in the code above


conn.commit
conn.close()#commits the changes and closes the sql area


app.debug = True
app.run()#runs the app

