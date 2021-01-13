from flask import Flask, request, render_template, url_for
from view import index
from DB import db

'''
mongo = pymongo.MongoClient("mongodb://localhost:27017/") # mongodb의 port의 기본값은 27017
print("MongoDB database list : ", mongo.list_database_names())
mongo_tutorial = mongo["mongo_tutorial"] # mongo_tutorial database
scof_collection = mongo_tutorial["scof"]
scof_documents = scof_collection.find()
for i in scof_documents:
    print(i)
'''
'''
print("ddd", myclient.list_database_names())
mydb = myclient["mydb"] # db
mycol = mydb["customers"] # collection
x = mycol.find_one()
print(x)
list = mycol.find()
for i in list:
    print(i)
'''
app = Flask(__name__)
app.register_blueprint(index.BP)

if __name__== '__main__':
    app.run(debug=True)