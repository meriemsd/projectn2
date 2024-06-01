from flask import Flask

app = Flask(__name__)

DB = "dojos_and_ninjas"
app.secret_key = "Secret Key"
