import numpy as np
import pandas as pd
import math
from flask import Flask, render_template, request, redirect, url_for
import random
import json

app = Flask(__name__, static_folder='static')
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.jinja_env.auto_reload = True


def build_set_rows(scores, max_sets=5):
    player_a_sets = scores[0::2]
    player_b_sets = scores[1::2]
    set_rows = []

    for i in range(max_sets):
        played = i < len(player_a_sets) and i < len(player_b_sets)
        set_rows.append(
            {
                "a": player_a_sets[i] if played else "",
                "b": player_b_sets[i] if played else "",
                "played": played,
            }
        )

    return set_rows




"""

@app.route('/')
def index():    
    return render_template('index.html', winner = "")


@app.route('/simulate', methods=['POST'])
def run_app():
    if request.method == 'POST':
        player_a = request.form.get('tennis_players_a')
        player_b = request.form.get('tennis_players_b')

        if player_a == "empty" or player_b == "empty":
            return render_template('index.html', winner = "None")
        else:
            match = run_match(player_a, player_b)
            scores = match[2]
            set_rows = build_set_rows(scores)

            return render_template(
                'results.html',
                winner=match[0],
                player_a=player_a,
                player_b=player_b,
                set_rows=set_rows,
            )

    return render_template('index.html', winner = "None")

"""

def run_tiebreak(a_win_rate, b_win_rate, a_player: str, b_player: str):
    a_points = 0
    b_points = 0
    total_points = 0
    server = 1
    
    while True:
        if server == 1:
            win_rate = a_win_rate
            winner = 'a' if random.random() <= win_rate else 'b'
        else:
            win_rate = b_win_rate
            winner = 'b' if random.random() <= win_rate else 'a'
        
        if winner == 'a':
            a_points += 1
        else:
            b_points += 1
        
        if (a_points >= 7 or b_points >= 7) and abs(a_points - b_points) >= 2:
            if a_points > b_points:
                return list((a_player, 7, b_points))
            else:
                return list((b_player, a_points, 7))
        
        total_points += 1

        if total_points >= 1 and total_points % 2 == 1:
            server = 2 if server == 1 else 1



def run_game(server_win_rate):
    server_points, return_points = 0, 0
    
    while True:
        if random.random() <= server_win_rate:
            server_points += 1
        else:
            return_points += 1
        
        if server_points >= 4 or return_points >= 4:
            if abs(server_points - return_points) >= 2:
                return 'server' if server_points > return_points else 'return'

        


def run_set(a_win_rate, b_win_rate, a_player: str, b_player: str, server: int):
    a_score = 0
    b_score = 0

    while True:
        if server == 1:
            normalized_win_rate = a_win_rate
            winner = run_game(normalized_win_rate)

            if winner == 'server':
                a_score += 1
                # print(a_score)
            elif winner == 'return':
                b_score += 1
                # print(b_score)
        else: 
            normalized_win_rate = b_win_rate
            winner = run_game(normalized_win_rate)

            if winner == 'server':
                b_score += 1
                # print(b_score)
            elif winner == 'return':
                a_score += 1
                # print(a_score)
            

        if (a_score >= 6 or b_score >= 6) and abs(a_score - b_score) >= 2:
            if a_score > b_score:
                # print(f'{a_player} scored: {a_score} and {b_player} scored: {b_score}')
                return list((a_player, a_score, b_score))
            elif b_score > a_score:
                # print(f'{b_player} scored: {b_score} and {a_player} scored: {a_score}')
                return list((b_player, a_score, b_score))
            
        if a_score == 6 and b_score == 6:
            return run_tiebreak(a_win_rate, b_win_rate, a_player, b_player)

            
        if server == 1:
            server = 2
        elif server == 2:
            server = 1


with open("player_surface_stats.json", "r") as file:
    player_stats = json.load(file)

def run_match(a, b, court_type):
    player_a_win = 0
    player_b_win = 0
    player_a_lose = 0
    player_b_lose = 0

    player_a_set_score = 0
    player_b_set_score = 0

    player_a = a
    player_b = b

    player_a_stats = player_stats[player_a][court_type]
    player_b_stats = player_stats[player_b][court_type]

    if player_a_stats["matches"] == 0 or player_b_stats["matches"] == 0:
        return None

    player_a_win = player_a_stats["serve"] / player_a_stats["matches"]
    player_b_lose = player_b_stats["return"] / player_a_stats["matches"]
    a_ace = player_a_stats["aces"] / player_a_stats["matches"]
    a_df = player_a_stats["df"] / player_a_stats["matches"]


    player_b_win = player_b_stats["serve"] / player_b_stats["matches"]
    player_a_lose = player_b_stats["return"] / player_b_stats["matches"]
    b_ace = player_b_stats["aces"] / player_b_stats["matches"]
    b_df = player_b_stats["df"] / player_b_stats["matches"]

    SCALING_FACTOR = 0.025

    a_ace_adv = (a_ace - b_ace)
    a_df_adv  = (a_df - b_df)

    ace_scale = (a_ace + b_ace) / 2
    df_scale  = (a_df + b_df) / 2

    ace_scale = ace_scale if ace_scale != 0 else 1
    df_scale  = df_scale if df_scale != 0 else 1

    ace_effect = (a_ace_adv / ace_scale)
    df_effect  = -(a_df_adv / df_scale) 

    player_a_adj = SCALING_FACTOR * (ace_effect + df_effect)
    player_b_adj = -player_a_adj 

    total_strength = (player_a_win + player_a_lose + player_b_win + player_b_lose)

    normalized_a_win_rate = (player_a_win + player_a_lose) / total_strength

    normalized_b_win_rate = (player_b_win + player_b_lose) / total_strength
    
    # normalized_a_win_rate = ((player_a_win + player_a_lose) / (player_a_win + player_b_win)) + (player_a_adj)
    # normalized_b_win_rate = ((player_b_win + player_b_lose) / (player_a_win + player_b_win)) + (player_b_adj)
    # print(normalized_a_win_rate)
    # print(normalized_b_win_rate)

    normalized_a_win_rate = min(max(normalized_a_win_rate,0.05),0.95)
    normalized_b_win_rate = min(max(normalized_b_win_rate,0.05),0.95)


    scores = []

    while True:
        server = 1 if random.random() < 0.5 else 2
        winner = run_set(normalized_a_win_rate, normalized_b_win_rate, player_a, player_b, server)
        scores.append(winner[1])
        scores.append(winner[2])

        if winner[0] == player_a:
            player_a_set_score += 1
        elif winner[0] == player_b:
            player_b_set_score += 1

        if player_a_set_score >= 3:
            print(f'Winner of the match is {player_a}')
            print(f'{player_a}: {player_a_set_score}')
            print(f'{player_b}: {player_b_set_score}')
            print(list((player_a, player_b, scores)))
            return list((player_a, player_b, scores))
        elif player_b_set_score >= 3:
            print(f'Winner of the match is {player_b}')
            print(f'{player_a}: {player_a_set_score}')
            print(f'{player_b}: {player_b_set_score}')
            print(list((player_b, player_a, scores)))
            return list((player_b, player_a, scores))
 

correct_predictions = 0
incorrect_predictions = 0

data = pd.read_csv("atp_matches_2008.csv", low_memory=False, na_values=[' ', ''])

data.columns = data.columns.str.strip()

data = data[["surface", "winner_name", "loser_name"]].dropna()

player_names = set(player_stats.keys())


for row in data.itertuples(index=False):
    winner = row.winner_name
    loser = row.loser_name
    
    if winner not in player_names or loser not in player_names:
        continue

    actual_winner_wins = 0
    actual_loser_wins = 0

    for i in range(25):
        match = run_match(winner, loser, row.surface)

        if match is None:
            continue

        if match[0] == winner:
            actual_winner_wins += 1
        else:
            actual_loser_wins += 1
    

    if actual_winner_wins > actual_loser_wins:
        correct_predictions += 1
    else:
        incorrect_predictions += 1


print(correct_predictions)
print(incorrect_predictions)



# if __name__ == '__main__':
    # app.run()
