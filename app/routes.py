# app/routes.py

from flask import Blueprint, render_template, redirect, url_for, request
from .game import players, simulate_game

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', players=players)

@main.route('/simulate', methods=['POST'])
def simulate():
    player1_name = request.form['player1']
    player2_name = request.form['player2']
    player1 = next(player for player in players if player.name == player1_name)
    player2 = next(player for player in players if player.name == player2_name)
    
    winner = simulate_game(player1, player2)
    return render_template('result.html', player1=player1, player2=player2, winner=winner)

