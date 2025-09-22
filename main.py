import numpy
import pandas
import math
from flask import Flask, render_template
import random

players = [["Roger Federer", 0.6135066337949038], 
           ["Novak Djokovic", 0.5878653429435347], 
           ["Rafael Nadal", 0.5878653429435347], 
           ["Andy Murray", 0.563521946242299], 
           ["Andy Roddick", 0.6412803307850137], 
           ["Stan Wawrinka", 0.5387102621495471], 
           ["Lleyton Hewitt", 0.5038985875058043], 
           ["Gilles Simon", 0.49887316576666085],
           ["Marat Safin", ], 
           ["Juan Martin del Potro", ], 
           ["Marin Cilic", ], 
           ["Alexander Zverev", ], 
           ["Grigor Dimitrov", ], 
           ["David Ferrer", ], 
           ["Nick Kyrgios", ], 
           ["Daniil Medvedev", ], 
           ["Jannik Sinner", ], 
           ["Frances Tiafoe", ], 
           ["Carlos Alcaraz", ], 
           ]

def run_game(server_win_rate):
    server_points = 0
    return_points = 0

    while True:
        if random.random() < server_win_rate:
            server_points += 1
        else:
            return_points += 1
        
        if server_points >= 4 and (server_points - return_points == 2):
            return 'server'
        elif return_points >= 4 and (return_points - server_points == 2):
            return 'return'
        


def run_set(a_win_rate, b_win_rate, a_player: str, b_player: str):
    a_score = 0
    b_score = 0
    server = random.randint(1, 2)

    while True:
        if server == 1:
            normalized_win_rate = a_win_rate
        else: 
            normalized_win_rate = b_win_rate

        winner = run_game(normalized_win_rate)

        if winner == 'server':
            a_score += 1
        elif winner == 'return':
            b_score += 1
            

        if a_score >= 6 or b_score >= 6:
            if (a_score - 2) >= b_score:
                print(f'{a_player} scored: {a_score} and {b_player} scored: {b_score}')
                return a_player
            elif (b_score - 2) >= a_score:
                print(f'{b_player} scored: {b_score} and {a_player} scored: {a_score}')
                return b_player
            
        if server == 1:
            server = 2
        elif server == 2:
            server = 1


def run_match():
    player_a_win = 0
    player_b_win = 0

    player_a_set_score = 0
    player_b_set_score = 0

    player_a = str(input("Enter the 1st player: "))
    player_b = str(input("Enter the 2nd player: "))

    for p in players:
        if player_a.lower() in p[0].lower():
            player_a_win =  p[1]

    for p in players:
        if player_b.lower() in p[0].lower():
            player_b_win =  p[1]


    normalized_a_win_rate = ((player_a_win + (1 - player_b_win)) / 2)
    normalized_b_win_rate = ((player_b_win + (1 - player_a_win)) / 2)

    server = random.randint(1, 2)

    while True:
        winner = run_set(normalized_a_win_rate, normalized_b_win_rate, player_a, player_b)

        if winner == player_a:
            player_a_set_score += 1
        elif winner == player_b:
            player_b_set_score += 1

        if player_a_set_score == 3:
            print(f'Winner of the match is {player_a}')
            print(f'{player_a}: {player_a_set_score}')
            print(f'{player_b}: {player_b_set_score}')
            return
        elif player_b_set_score == 3:
            print(f'Winner of the match is {player_b}')
            print(f'{player_a}: {player_a_set_score}')
            print(f'{player_b}: {player_b_set_score}')
            return
            
        if server == 1:
            server = 2
        elif server == 2:
            server = 1


run_match()

