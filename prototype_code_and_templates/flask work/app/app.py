from random import randint
import sqlite3
from flask import Flask, jsonify, render_template, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import requests
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

@app.route('/Homepage', methods = ['GET', 'POST'])
def homepage():
    if requests.method == 'POST':
        return render_template("Homepage.html")
    elif request.method == 'GET':
        pass
    else:
        return render_template("Homepage.html")

@app.route('/login page', methods = ['POST'])
def login():
    if requests.method == 'POST':
        Email = request.form.get("Email")
        password = request.form.get("Password")
        Email = info.query.filter_by(Email=Email).first()
        password = info.query.filter_by(password=password).first()
    if Email and password in info:
        login_user()
        return render_template('Home page.html')
    else:
        message = "invalid login, please try again."
    return render_template("login page.html")

@app.route('/createAccount', methods = ['GET', 'POST'])
def createacc():
    if requests.method == 'POST':
        Name = request.form.get("Name")
        Email = request.form.get("Email")
        password = request.form.get("Password")
        if Name and  Email and  password not in User_table:
            cursor.execute("INSERT INTO TBL_users (Name, Email, Password) VALUES(?, ?, ?)", (Name), (Email), (password))
            conn.commit()
            print("you have now created an account")
            return render_template("login page.html")
        else:
            return jsonify({"An account under those credentials is already taken"})
    else:
        return render_template("createAccount.html")

@app.route('/forgotpassword', methods = ['GET', 'POST'])
def forgotpassword():
    if requests.method == 'POST':
        Email = request.method.get("Email")
        currpass = request.emthod.get("currpass")
        newpass = request.method.get("newpass")
        re = request.method.get("re-type")
        if Email not in forgot_password:
            return jsonify({"error": "your email must be in our system try again"})
        elif currpass not in forgot_password:
            return jsonify({"error": "you must get your current password correct to be abel tor eset your password"})
        elif newpass and re-type not in forgot_password:
            forgot_password.append({"New Password": newpass, "re-typed password": re})
        else:
            return jsonify({"message": "your information is all correct, you may reset your password now"})
    else:
        return render_template("forgotpassword.html")

@app.route('/info', methods = ['GET', 'POST'])
def infopage():
    if requests.method == 'POST':
        return render_template("info.html")
    else:
        return render_template("info.html")

@app.route('/booking', methods = ['GET', 'POST'])
@login_required
def bookpage():
    if requests.method == 'POST':
        Time = request.form.get("Time")
        Date = request.form.get("Date")
        if Time and Date not in bookings_table:
            cursor.execute("INSERT INTO TBL_bookings (Time, Date) VALUES(?, ?)", (Time), (Date))
            conn.commit()
            print ("you have now added a booking into our system")
            return render_template("booking.html")
        else:
            return jsonify({"message": "That time and date slot isnt available at the moment, please try another around your needs."})
    else:
        return render_template("booking.html")

@app.route('/calculate', methods = ['GET', 'POST'])
def calculation():
    if requests.method == 'POST':
        return render_template("calculate.html")
    else:
        return render_template("calculate.html")

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if requests.method == 'POST':
        Email = request.form.get("Email")
        Message = request.form.get("Message")
        if not Email or not Message:
            return jsonify({"error": "both of the inputs are required"})

        messages.append({"Email": Email, "Message": Message})

        return render_template("contact.html")
    elif request.method == 'GET':
        pass
    else:
        return render_template("contact.html")

@app.route('/payment', methods = ['GET', 'POST'])
def paypage():
    if requests.method == 'POST':
        cardnum = request.form.get("cardnum")
        expiry = request.form.get("expiry")
        CVV = request.form.get("CVV")
        name = request.form.get("name")
        if cardnum not in payment_table:
            payment_table.append({"Cardnumber": cardnum})
        elif expiry not in payment_table:
            payment_table.append({"Expiration Date": expiry})
        elif CVV not in payment_table:
            payment_table.append({"CVV(3 num on back": CVV})
        elif name not in payment_table:
            payment_table.append({"Name of CardHolder": name})
        else:
            pass
    else:
        return render_template("payment.html")

@app.route('/settings', methods = ['GET', 'POST'])
@login_required
def settings():
    if requests.method == 'POST':
        return render_template("profile page.html")
    else:
        return render_template("profile page.html")



conn = sqlite3.connect("Rolsa technolgies")
cursor = conn.cursor()

def User_table():
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS TBL_users (
                    USERID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Email TEXT,
                    Password TEXT,
                    Name TEXT)
                    """)

def item_table():
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS TBL_Item(
                    ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Amount INTEGER,
                    item_type TEXT)
                    """)

def bookings_table():
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS TBL_bookings(
                BookingID INTEGER PRIMARY KEY AUTOINCREMENT,
                Time DATETIME,
                Date DATETIME)
                """)

def calculate_table():
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS TBL_calculate(
                    CalculateID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Result INTEGER)
                    """)


def payment_table():
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS TBL_payment(
                    PaymentID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Cardnum INTEGER,
                    EXPIRY DATE,
                    CVV INTEGER,
                    name TEXT)
                    """)



def forgot_password():
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS TBL_Forgot(
                    Email TEXT,
                    Currpass TEXT,
                    newpass TEXT,
                    re-type TEXT)
                    """)


def messages():
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS TBL_MESSAGE(
                    Message TEXT,
                    Email TEXT)
                    """)



many_users = ['randint()','Acc', 'Email', 'password']
many_items = ['installation']
many_bookings = ['Date', 'Time']
many_calculations = ['Acc','result']

import uuid
random_id=uuid.uuid4()
def info(Email, Password, Name, USERID=random_id):
    cursor.executemany("INSERT INTO TBL_users (USERID, Email, Password, Name) VALUES(?, ?, ?, ?)", (str(random_id), (Email), (Password),(Name)))
    conn.commit()

def item(Amount, item_type, ItemID = random_id):
    cursor.executemany("INSERT INTO TBL_Item(?, ?, ?)", (str(random_id), (Amount), (item_type)))

def book(Time, Date, BookingID=random_id):
    cursor.executemany("INSERT INTO TBL_bookings VALUES(?, ?, ?)", (str(random_id), (Time), (Date)))

def calculate(Name, Result, calculateID=random_id):
    cursor.executemany("INSERT INTO TBL_calculate VALUES(?, ?, ?)", (str(random_id), (Name), (Result)))

def message(Message, Email):
    cursor.executemany("INSERT INTO TBL_Message VALUES(?, ?)", (Message), (Email))


conn.commit
conn.close()


app.debug = True
app.run()
