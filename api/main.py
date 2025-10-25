import numpy
import pandas
import math
from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__, static_folder='static')

players = [
    ["Roger Federer", 0.7193697480417766, 0.2806302519582235, 8.261405672009865, 1.5487053020961776],
    ["Novak Djokovic", 0.6919147804332736, 0.3080852195667264, 5.656934306569343, 2.239051094890511],
    ["Rafael Nadal", 0.6848565116264265, 0.3151434883735736, 3.3141025641025643, 1.732905982905983],
    ["Andy Murray", 0.6612316817164237, 0.3387683182835763, 6.993932038834951, 2.4308252427184467],
    ["Andy Roddick", 0.712895230721064, 0.2871047692789361, 12.33090909090909, 1.7563636363636363],
    ["Stan Wawrinka", 0.6636913299390815, 0.33630867006091847, 7.432795698924731, 2.3763440860215055],
    ["Lleyton Hewitt", 0.6314656604029686, 0.36853433959703136, 6.245901639344262, 3.7540983606557377],
    ["Gilles Simon", 0.622119630659578, 0.377880369340422, 4.354706684856753, 2.4038199181446114],
    ["Marat Safin", 0.6393398337713139, 0.3606601662286861, 8.976190476190476, 2.9404761904761907],
    ["Juan Martin del Potro", 0.6798649318577962, 0.3201350681422039, 7.835564053537285, 2.2447418738049714],
    ["Marin Cilic", 0.6706063513200101, 0.3293936486799899, 9.57590361445783, 3.004819277108434],
    ["Alexander Zverev", 0.672503248397905, 0.327496751602095, 8.390444810543658, 3.647446457990115],
    ["Grigor Dimitrov", 0.6673108269074414, 0.3326891730925586, 7.090014064697609, 3.4472573839662446],
    ["David Ferrer", 0.6453788747448157, 0.35462112525518436, 2.835357624831309, 2.6005398110661266],
    ["Nick Kyrgios", 0.6978643227244247, 0.3021356772755753, 15.19732441471572, 3.531772575250836],
    ["Daniil Medvedev", 0.6650707486594905, 0.3349292513405095, 7.818367346938776, 3.76734693877551],
    ["Jannik Sinner", 0.6809844943953158, 0.31901550560468417, 6.041935483870968, 2.0516129032258066],
    ["Frances Tiafoe", 0.6522051575631265, 0.34779484243687353, 7.702412868632708, 2.525469168900804],
    ["Carlos Alcaraz", 0.6707661480813749, 0.32923385191862514, 3.9655172413793105, 2.21455938697318],
]



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

            return render_template('results.html', winner = match[0], player_a = player_a, player_b = player_b, 
                                score_1a = scores[0] if len(scores) >= 1 else "", 
                                score_2a = scores[2] if len(scores) >= 3 else "",
                                score_3a = scores[4] if len(scores) >= 5 else "",
                                score_4a = scores[6] if len(scores) >= 7 else "",
                                score_5a = scores[8] if len(scores) >= 9 else "",

                                score_1b = scores[1] if len(scores) >= 2 else "",
                                score_2b = scores[3] if len(scores) >= 4 else "",
                                score_3b = scores[5] if len(scores) >= 6 else "",
                                score_4b = scores[7] if len(scores) >= 8 else "",
                                score_5b = scores[9] if len(scores) >= 10 else "",
                                )

    return render_template('index.html', winner = "None")


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
        
        if (a_points >= 6 or b_points >= 6) and abs(a_points - b_points) >= 2:
            if a_points > b_points:
                return list((a_player, 6, b_points))
            else:
                return list((b_player, a_points, 6))
        
        total_points += 1
        if total_points == 1 or total_points % 2 == 1:
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
                print(a_score)
            elif winner == 'return':
                b_score += 1
                print(b_score)
        else: 
            normalized_win_rate = b_win_rate
            winner = run_game(normalized_win_rate)

            if winner == 'server':
                b_score += 1
                print(b_score)
            elif winner == 'return':
                a_score += 1
                print(a_score)
            

        if (a_score >= 6 or b_score >= 6) and abs(a_score - b_score) >= 2:
            if a_score > b_score:
                print(f'{a_player} scored: {a_score} and {b_player} scored: {b_score}')
                return list((a_player, a_score, b_score))
            elif b_score > a_score:
                print(f'{b_player} scored: {b_score} and {a_player} scored: {a_score}')
                return list((b_player, a_score, b_score))
            
        if a_score == 6 and b_score == 6:
            return run_tiebreak(a_win_rate, b_win_rate, a_player, b_player)

            
        if server == 1:
            server = 2
        elif server == 2:
            server = 1


def run_match(a, b):
    player_a_win = 0
    player_b_win = 0
    player_a_lose = 0
    player_b_lose = 0

    player_a_set_score = 0
    player_b_set_score = 0

    player_a = a
    player_b = b

    for p in players:
        if player_a.lower() in p[0].lower():
            player_a_win = p[1]
            player_b_lose = p[2]
            a_ace = p[3]
            a_df = p[4]


    for p in players:
        if player_b.lower() in p[0].lower():
            player_b_win = p[1]
            player_a_lose = p[2]
            b_ace = p[3]
            b_df = p[4]

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

    
    normalized_a_win_rate = ((player_a_win + player_a_lose) / (player_a_win + player_b_win)) + (player_a_adj)
    normalized_b_win_rate = ((player_b_win + player_b_lose) / (player_a_win + player_b_win)) + (player_b_adj)
    print(normalized_a_win_rate)
    print(normalized_b_win_rate)


    scores = []

    while True:
        winner = run_set(normalized_a_win_rate, normalized_b_win_rate, player_a, player_b)
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
 





if __name__ == '__main__':
    app.run()
