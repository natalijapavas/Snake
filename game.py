#!/usr/bin/env python3
# snake
from typing import Dict, Union
import random
from flask import Flask

import json

moves = ["up", "down", "left", "right"]

Snake = {}

app = Flask(__name__)

@app.route("/start", methods=["POST"])
def start(req):
    move = {
    "move": random.choice(moves),
    "taunt": "r4ndom"
    }
    move_json = json.dumps(move)
    print(req)
    return move_json

@app.route("/move", methods=["POST"])
def move(req):
    move = {
    "move": random.choice(moves),
    "taunt": "r4ndom"
    }
    move_json = json.dumps(move)
    print(req)
    return move_json



@app.route("/start", methods=["GET"])
def start_g(req):
    return Snake.__repr__()


@app.route("/move", methods=["GET"])
def move_g(req):
    return Snake.__repr__()


app.run()