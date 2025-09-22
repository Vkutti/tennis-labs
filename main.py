import numpy
import pandas
import math
from flask import Flask, render_template
import random

players = [["Roger Federer", 0.6181684623962715], 
           ["Novak Djokovic", 0.5947536538180075], 
           ["Rafael Nadal", 0.5866196318068458], 
           ["Andy Murray", 0.5639304650385061], 
           ["Andy Roddick", 0.6390888166198604], 
           ["Stan Wawrinka", 0.5412835681262631], 
           ["Lleyton Hewitt", 0.5012052757076787], 
           ["Gilles Simon", 0.4936153298057834],
           ["Marat Safin", 0.5278027410227841], 
           ["Juan Martin del Potro", 0.6000366515792587], 
           ["Marin Cilic", 0.5631289364226771], 
           ["Alexander Zverev", 0.6132135038078368], 
           ["Grigor Dimitrov", 0.5919210039749763], 
           ["David Ferrer", 0.5369534140019233], 
           ["Nick Kyrgios", 0.6325506471767043], 
           ["Daniil Medvedev", 0.5905048030648645], 
           ["Jannik Sinner", 0.5654574943566698], 
           ["Frances Tiafoe", 0.5564689245239004], 
           ["Carlos Alcaraz", 0.5685097899035272], 
           ]

def run_game(server_win_rate):
    server_points = 0
    return_points = 0

    max_points = 7

    while True:
        if random.random() <= server_win_rate:
            server_points += 1
        else:
            return_points += 1
        
        if server_points >= 4 and (server_points - return_points == 2):
            return 'server'
        elif return_points >= 4 and (return_points - server_points == 2):
            return 'return'
        
        if server_points + return_points > max_points:
            # Safety fallback: give win to whoever is ahead
            return 'server' if server_points > return_points else 'return'
        


def run_set(a_win_rate, b_win_rate, a_player: str, b_player: str):
    a_score = 0
    b_score = 0
    server = random.randint(1, 2)

    while True:
        if server == 1:
            normalized_win_rate = a_win_rate
            winner = run_game(normalized_win_rate)

            if winner == 'server':
                a_score += 1
            elif winner == 'return':
                b_score += 1
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
            player_a_win = p[1]

    for p in players:
        if player_b.lower() in p[0].lower():
            player_b_win = p[1]


    normalized_a_win_rate = ((player_a_win + (1 - player_b_win)) / 2)
    normalized_b_win_rate = ((player_b_win + (1 - player_a_win)) / 2)

    server = random.randint(1, 2)

    while True:
        winner = run_set(normalized_a_win_rate, normalized_b_win_rate, player_a, player_b)

        if winner == player_a:
            player_a_set_score += 1
        elif winner == player_b:
            player_b_set_score += 1

        if player_a_set_score >= 3:
            print(f'Winner of the match is {player_a}')
            print(f'{player_a}: {player_a_set_score}')
            print(f'{player_b}: {player_b_set_score}')
            return
        elif player_b_set_score >= 3:
            print(f'Winner of the match is {player_b}')
            print(f'{player_a}: {player_a_set_score}')
            print(f'{player_b}: {player_b_set_score}')
            return
 


run_match()

