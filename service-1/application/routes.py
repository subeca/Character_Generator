from application import app, db
from application.models import Cars
from flask import render_template
from sqlalchemy import desc
import requests

@app.route('/')
def index():  
  
    
    return render_template("index.html", car_name=car_make.text, colour=car_colour.text, cars=cars, price=price.text)

