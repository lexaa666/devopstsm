from flask import Flask, jsonify, render_template, request
import json
from markupsafe import Markup

app = Flask(__name__)
jData = json.loads(open('./restaurants.json').read())
data=jData["Restaurants"]

# Intial request Ex: http://192.168.99.100:5000/
@app.route('/')
def route_main():
    return "RESTful Webservice Started. Request data with proper URL"

# Returns JSON which containes all restaurants
@app.route('/getrestaurants/')
def restaurants_all():
    return render_template("index.html",items=data)

# Returns restaurants JSON which matches the id
@app.route('/getrestaurants/<string:id>/')
def restaurants_by_id(id=''):
    myList=[]
    for element in data:
        if element["id"] == id:
            myList.append(element)
    return render_template("index.html",items=myList)

# Returns the restaurants JSON with particualr food type
@app.route('/getrestaurants/type/<string:type_of_food>/')
def restaurants_by_type(type_of_food=''):
    myList=[]
    for element in data:
        if element["type_of_food"].lower() == type_of_food.lower():
            myList.append(element)
    return render_template("index.html",items=myList)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
