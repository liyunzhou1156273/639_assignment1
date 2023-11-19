
import mysql.connector, MySQLdb.cursors, git, os, smtplib, db.query as query,bcrypt

from flask import Flask, render_template, request, redirect, url_for, session, flash
from db import db,query

#from features.staff.staff import staff
#from features.student.student import student
#from features.mentor.mentor import mentor
from common.user import *
from ci import ci
from dotenv import load_dotenv
#from common.login_required import student_login_required
from itsdangerous import URLSafeTimedSerializer
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = "I'm a secret unique key"

# app.config['MYSQL_HOST']='localhost'
# app.config['MYSQL_USER']='root'
# app.config['MYSQL_PASSWORD']='1234'

@app.route("/")
def home():
    return render_template("login.html")

users = []
# @app.route('/login',methods=['GET','POST'])
# def login():
#     msg=''
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
#         username= request.form['username']
#         user_password = request.form['password']
#         cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('SELCET* FROM ')
#         account= cursor.fetchone()
#         if account is not None:
#             password = account['password']
#             if bcrypt.checkpw(user_password.encode('utf-8'),password.encode('utf-8'),username.encode('utf-8')):
#                 session['loggedin']=True
#                 session['id']=account['id']
#                 session['username']=account['username']
#                 return redirect(url_for('home'))
#             else:
#                 msg='Incorrect username'
#         else:
#             msg='Incorrect username.'
#     return render_template('index.html',msg=msg)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.clear()
        return render_template("login.html")
    
    email = request.form['email'].strip()
    password = request.form['password'].strip()
    params=["email"]

    # privode convient port under development
    if os.getenv("ENV") == "DEVELOPMENT":
        if email == "arlette@email.com" and password == "13579":
            session['user'] = {
            'email': email,
            'role': user_type,
            'id': user_id,
            'name': name,
            'role_id': user_id
            print(user)
            return redirect(url_for("staff.dashboard"))
        if email == "mentor1@example.com" and password == "13579":
            user = User(
                name="Scott Allen",
                email="mentor1@example.com",
                role="industry_mentor",
                id="6",
                role_id="6",
            )
            print(user)
            return redirect(url_for("mentor.dashboard"))
        if email == "student1@example.com" and password == "13579":
            user = User(
                name="John for recommend",
                email="student1@example.com",
                role="student",
                id="1",
                role_id="1",
            )
            print(user)
            return redirect(url_for("student.dashboard"))



    # if user and bcrypt.check_password_hash(user['password'], password):
    #         flash('Login successful!', 'success')
    #         return redirect(url_for('home'))
    #     else:
    #         flash('Login failed. Check your username and password.', 'danger')

    # return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        user = {
            'username': username,
            'password': hashed_password
        }

        users.append(user)

        flash('Registration successful! You can now login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')