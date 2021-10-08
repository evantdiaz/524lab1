from flask import Flask, request
from flask import Blueprint, render_template
import hashlib
import csv
import time

app = Flask(__name__)


def create_hash(plain_pw): 
    salted = plain_pw + "potato"
    encoded = salted.encode()
    result = hashlib.sha256(encoded)
    return result.hexdigest()

def get_secret_code():
    return "7GTgk3dtR7U@wCAH"

def get_hashed_pw_from_db(user):
    with open('user_db2.csv') as inf:
        reader = csv.DictReader(inf)
        for row in reader:
            if row['username'] == user:
                return create_hash(row['password'])
    return False

@app.route("/")
def hello_world():
        return "<p>Hello, World!</p>"


@app.route("/login", methods=['POST'])
def login_post():
    user = request.form.get('user')
    password = request.form.get('password')
    attempted_hash = create_hash(password)
    hashed_pw = get_hashed_pw_from_db(user)
    print(hashed_pw)
    print(attempted_hash)
    if hashed_pw and hashed_pw == attempted_hash:
    	return get_secret_code()
    return "Invalid Credentials\n"