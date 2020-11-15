#!/usr/bin/env python3
from time import time
from math import floor
from ago import human
from datetime import timedelta
from flask import Flask
from os import environ

app = Flask(__name__)

rares = ['Noth the Plaguebringer', 'Patchwerk', "Blood Queen Lana'thel", 'Professor Putricide', 'Lady Deathwhisper', 'Skadi the Ruthless', 'Ingvar the Plunderer', 'Prince Keleseth', 'The Black Knight', 'Bronjahm', 'Scourgelord Tyrannus', 'Forgemaster Garfrost', 'Marwyn', 'Falric', "The Prophet Tharonja", 'Novos the Summoner', 'Trollgore', "Krikthir the Gatewatcher", 'Prince Taldaram', 'Elder Nadox']
wp = ['31.6, 70.5', '36.5, 67.4', '49.7, 32.7', '57.1, 30.3', '51.1, 78.5', '57.8, 56.1', '52.4, 52.6', '54.0, 44.7', '64.8, 22.1', '70.7, 38.4', '47.2, 66.1', '58.6, 72.5', '58.2, 83.4', '50.2, 87.9', '80.1, 61.2', '77.8, 66.1', '58.3, 39.4', '67.5, 58.0', '29.6, 62.2', '44.2, 49.1']
epoch = 1605412993

def a(x):
    return human(timedelta(seconds=-x))


@app.route('/')
def index():
    t = time()
    n=t-epoch
    out = f"/way {wp[floor(n/1200)%20]} for {rares[floor(n/1200)%20]} {a(1200-floor(n%1200))}"
    return out

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=environ["PORT"])
