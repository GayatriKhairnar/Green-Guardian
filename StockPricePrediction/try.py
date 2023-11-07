from flask import Flask, render_template, request, redirect, url_for
#from pymongo import MongoClient
from flask_pymongo import PyMongo

app = Flask(__name__)

#client = pymongo.MongoClient("mongodb://localhost:27017")

#db = client['stockdb']
#collection = db['stockdbcollection']
app.config['MONGO_URI'] = 'mongodb://localhost:27017/stockdb'
mongo=PyMongo(app)

@app.route('/')
def index():
    data = mongo.db.stockdbcollection.find()
    return render_template('index.html',data=data)
    

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        #name = request.form['name']
        #email = request.form['email']
        data = {
        'name': 'JC Doe',
        'email': 'jopphndoe@example.com'
        }
        mongo.db.stockdbcollection.insert_one(data)
    print('Inserted')
    #return redirect(url_for('index'))


print("3")
if __name__ == '__main__':
    app.run(debug=True)

