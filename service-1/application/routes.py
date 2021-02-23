from application import app, db
from application.models import Houses
from flask import render_template
from sqlalchemy import desc
import requests

@app.route('/')
def index():
