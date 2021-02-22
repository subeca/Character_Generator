from application import app
from flask import request, Response
import random 

@app.route("/house", methods=["GET"])
def house():
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    return Response(str(random.choice(houses)), mimetype="text/plain")