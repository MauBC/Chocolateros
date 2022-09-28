import logging
import mimetypes
from operator import imod
import re
from tabnanny import check
from flask import Flask, request, jsonify,Response, render_template,redirect,session,url_for
from flask_pymongo import PyMongo
from bson import json_util 
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash,check_password_hash


#SQLALCHEMY_DATABASE_URI = f'{db_type}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'


"""
db_type     = 'postgresql'
db_host     = 'localhost'
db_port     = '5432'
db_name     = 'utecscheduler'
db_user     = 'postgres'
db_password = input('Password: ')
#username = contabilidad
#password = 12345
"""

app = Flask(__name__)
app.secret_key = "141822147109"
#app.config['MONGO_URI'] = 'mongodb://localhost:27017/Contabilidad'
#app.config['MONGO_URI'] = 'mongodb+srv://contabilidad:12345@cluster0.d4tcnhd.mongodb.net/test'
#app.config['MONGO_URI'] = "mongodb+srv://contabilidad:12345@cluster0.d4tcnhd.mongodb.net/?retryWrites=true&w=majority/Contabilidad"
app.config['MONGO_URI'] = 'mongodb+srv://contabilidad:12345@cluster0.d4tcnhd.mongodb.net/Contabilidad'


mongo = PyMongo(app)
db = mongo.db

"""
@app.route("/users", methods=['GET'])
def get_users(): 
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype='application/json')

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one({'_id':ObjectId(id)})
    response = json_util.dumps(user)
    return Response(response, mimetype = "application/json")

"""

@app.route('/')
def index():
    if 'username' in session:
        return "You are logged in as " + session['username']
    return render_template('index.html')
    
@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({"username" : request.form['username']})

    
    if login_user:
        if check_password_hash(login_user['password'],request.form['password']):
            session['username'] = request.form['username']
            return redirect(url_for('index'))
    
        return "Invalid Username or password"
        
    return "NO SE ENCONTRO EL USUARIO"

def generate_user_account(nombre,apellido,dni):
    name = nombre+" " + apellido+" " + dni
    passw = "12345"
    hashpassw = generate_password_hash(passw)
    users = mongo.db.users
    users.insert_one({'username':name,'password':hashpassw})
    

if __name__ == "__main__":
    band = False
    #generate_user_account("Mauro","Bobadilla","73328933")
    if(not band):
        #generate_user_account("Mauro","Bobadilla","73328933")
        band = True;
    app.run(debug=True)
