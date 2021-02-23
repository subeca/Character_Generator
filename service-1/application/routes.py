from application import app, db
from application.models import Cars
from flask import render_template
from sqlalchemy import desc
import requests

@app.route('/')
def index():
