from bson import json_util
import json
import pymongo
from flask import Flask,request,render_template

app = Flask(__name__)

#connecting to mongodb database
client = pymongo.MongoClient("mongodb://localhost:27017/")

#creating databse
db = client['SENSOR_DATABASE']

#creating list
values = db['SENSOR_VALUE']

#getting json data nand sending to mongodb database
@app.route("/", methods=['POST'])
def insert_document():
    req_data = json.dumps(request.get_json())
    print(req_data)
#     data = request.data
#     print(data)
#     database = values.insert_one(json.loads(request.get_json()))

#     database = values.insert_one(json.load(data))
    values.insert_one(request.get_json())
    print("data aded successfully")
    for row in values.find():
        print(row)
    return "json posted"



# #sending json data to webpage via mongodb database
# @app.route("/webpage",methods = ["GET","POST"])
# def display():
#      return render_template("json.html",data=req_data);
    
#running api
if __name__ == '__main__':
    app.run(host="0.0.0.0",port = 2777) #chnage port according to cloud
