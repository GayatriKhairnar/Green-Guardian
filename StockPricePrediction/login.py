from flask import Flask, render_template, request, redirect, url_for
#from pymongo import MongoClient
from flask_pymongo import PyMongo
import json

app = Flask(__name__)

#client = pymongo.MongoClient("mongodb://localhost:27017")

#db = client['stockdb']
#collection = db['stockdbcollection']
app.config['MONGO_URI'] = 'mongodb://localhost:27017/stockdb'
mongo=PyMongo(app)
data = mongo.db.stockdbcollection.find()

@app.route('/')
def index():
    data = mongo.db.stockdbcollection.find()
    return render_template('index.html',data=data)

    
@app.route('/add', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        data_to_insert = {
            'username': username,
            'password': password
        }
        mongo.db.stockdbcollection.insert_one(data_to_insert)
    return redirect(url_for('index'))


print("3")
if __name__ == '__main__':
    app.run(debug=True)

