from datetime import datetime

from datetime import datetime

from flask import Flask, render_template, request
from . import app
from .koodi import PelaajaLuettelo, Sovellus


#players = PelaajaLuettelo()

players_sovellus = Sovellus()
@app.route('/player/')
def get_single_player():
    name = request.args.get('name')
    print (name)    
    return players_sovellus.hae_pelaaja(name)
@app.route('/player/joukkueet')
def get_joukkueet():
    return players_sovellus.hae_joukkueet()

@app.route('/player/maat')
def get_maat():
    return players_sovellus.hae_maat()