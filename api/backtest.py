import numpy as np
import pandas as pd
import math
import random
import json

players = ['Tommy Haas', 'Juan Balcells', 'Alberto Martin', 'Juan Carlos Ferrero', 'Michael Chang', 'Magnus Gustafsson', 'Thomas Johansson', 'Sjeng Schalken', 'Tomas Behrend',
            'Gaston Gaudio', 'Jiri Novak', 'Marc Rosset', 'John Van Lottum', 'Jan Michael Gambill', 'Magnus Norman', 'Andrea Gaudenzi', 'Albert Portas', 'Galo Blanco', 
            'Markus Hantschk', 'Andrei Medvedev', 'Christophe Rochus', 'Andrei Pavel', 'Juan Antonio Marin', 'Markus Hipfl', 'Stefan Koubek', 'Andrew Ilie', 'Sergi Bruguera', 
            'Thomas Enqvist', 'Ivan Ljubicic', 'Slava Dosedel', 'Bohdan Ulihrach', 'Jonas Bjorkman', 'Fernando Meligeni', 'Max Mirnyi', 'Franco Squillari', 'Richard Fromberg', 
            'Younes El Aynaoui', 'Antony Dupuis', 'Gianluca Pozzi', 'Greg Rusedski', 'Julien Boutter', 'Justin Gimelstob', 'Fabrice Santoro', 'Mark Philippoussis', 
            'Goran Ivanisevic', 'Karol Kucera', 'Byron Black', 'Sebastien Grosjean', 'Davide Sanguinetti', 'Todd Martin', 'Andre Sa', 'Michael Llodra', 'Andre Agassi', 
            'Marat Safin', 'Cedric Pioline', 'Lleyton Hewitt', 'Pete Sampras', 'Alex Corretja', 'Vincent Spadea', 'George Bastl', 'Marcelo Rios', 'Francisco Clavet', 
            'Jerome Golmard', 'Albert Costa', 'Mariano Puerta', 'Felix Mantilla', 'Nicolas Kiefer', 'Chris Woodruff', 'Mardy Fish', 'Wayne Arthurs', 'Peter Wessels', 
            'David Prinosil', 'Jason Stoltenberg', 'Paul Goldstein', 'Scott Draper', 'Jiri Vanek', 'Nicolas Massu', 'Andreas Vinciguerra', 'Guillermo Canas', 'Dominik Hrbaty', 
            'Adrian Voinea', 'Alex Calatrava', 'Raemon Sluiter', 'Arnaud Di Pasquale', 'Sergio Roitman', 'Jan Siemerink', 'Nikolay Davydenko', 'Sargis Sargsian', 'Paul Henri Mathieu', 
            'Michel Kratochvil', 'Agustin Calleri', 'Federico Luzzi', 'Fernando Gonzalez', 'Yevgeny Kafelnikov', 'Nicolas Lapentti', 'Mariano Zabaleta', 'Rainer Schuettler', 
            'Karim Alami', 'David Sanchez', 'Olivier Rochus', 'Alexander Popp', 'Mikael Tillstrom', 'Hicham Arazi', 'Carlos Moya', 'Nicolas Escude', 'Roger Federer', 
            'Richard Krajicek', 'Arnaud Clement', 'Tim Henman', 'Leander Paes', 'Takao Suzuki', 'Cecil Mamiit', 'Harel Levy', 'Hyung Taik Lee', 'Wayne Black', 'Gustavo Kuerten', 
            'Patrick Rafter', 'Kevin Kim', 'Fernando Vicente', 'Jean Rene Lisnard', 'Wayne Ferreira', 'Juan Ignacio Chela', 'Tomas Zib', 'Paradorn Srichaphan', 'Magnus Larsson', 
            'Andy Roddick', 'Cyril Saulnier', 'Xavier Malisse', 'Michal Tabara', 'Guillermo Coria', 'Taylor Dent', 'Vladimir Voltchkov', 'Gouichi Motomura', 'Mikhail Youzhny', 
            'Lars Burgsmuller', 'Attila Savolt', 'Andrei Stoliarov', 'Ivo Heuberger', 'Martin Lee', 'Michael Russell', 'Ramon Delgado', 'Kristian Pless', 'Jose De Armas', 'Luis Horna', 
            'Jarkko Nieminen', 'Danai Udomchoke', 'Marcel Felder', 'Aisam Ul Haq Qureshi', 'Alexey Kedryuk', 'Mario Ancic', 'Gilles Muller', 'Marko Tkalec', 'Jan Frode Andersen', 
            'Ivo Karlovic', 'Konstantinos Economidis', 'Giovanni Lapentti', 'Ivan Miranda', 'Flavio Saretta', 'Gilles Elseneer', 'James Blake', 'Kenneth Carlsen', 'Jose Acasuso', 
            'Tommy Robredo', 'Olivier Mutis', 'Alexander Peya', 'Jan Vacek', 'Oliver Marach', 'Marc Lopez', 'David Nalbandian', 'Jurgen Melzer', 'Bjorn Phau', 'Julien Benneteau', 
            'Noam Okun', 'Dmitry Tursunov', 'Robby Ginepri', 'Albert Montanes', 'Robin Soderling', 'Irakli Labadze', 'Nicolas Mahut', 'Feliciano Lopez', 'Ricardo Mello', 
            'Ruben Ramirez Hidalgo', 'Lukasz Kubot', 'Victor Estrella', 'Jimmy Wang', 'Yen Hsun Lu', 'Alejandro Falla', 'Mohammad Ghareeb', 'Aqeel Khan', 'Janko Tipsarevic', 
            'Filippo Volandri', 'Radek Stepanek', 'Jeff Morrison', 'Brian Vahaly', 'Martin Verkerk', 'David Ferrer', 'Alexander Waske', 'Stefano Galvani', 'Richard Gasquet', 
            'Frank Dancevic', 'Alex Bogomolov Jr', 'Joachim Johansson', 'Victor Hanescu', 'Fernando Verdasco', 'Marc Gicquel', 'Gregory Carraz', 'Karol Beck', 'Rafael Nadal', 
            'Miguel Gallardo Valles', 'Andis Juska', 'Rik De Voest', 'Wesley Moodie', 'Thierry Ascione', 'Philipp Kohlschreiber', 'Peter Luczak', 'Chris Guccione', 'Stan Wawrinka', 
            'Oscar Hernandez', 'Nicolas Almagro', 'Robert Kendrick', 'Kristof Vliegen', 'Philipp Petzschner', 'Rajeev Ram', 'Prakash Amritraj', 'Amer Delic', 'Igor Andreev', 
            'Marcos Daniel', 'Tomas Berdych', 'Frederik Nielsen', 'Boris Pashanski', 'Daniel Koellerer', 'Olivier Patience', 'Potito Starace', 'Florian Mayer', 'Brian Baker', 
            'Juan Monaco', 'Santiago Ventura', 'Andreas Seppi', 'Martin Vassallo Arguello', 'Ivo Minar', 'Andreas Beck', 'Marco Chiudinelli', 'Guillermo Garcia Lopez', 
            'Florent Serra', 'Gael Monfils', 'Jo-Wilfried Tsonga', 'Jan Hernych', 'Nicolas Devilder', 'Igor Kunitsyn', 'Daniele Bracciali', 'Marcos Baghdatis', 'Stephane Robert', 
            'Novak Djokovic', 'Paul Capdeville', 'Alessio Di Mauro', 'Malek Jaziri', 'Frederico Gil', 'Lamine Ouahab', 'Pablo Cuevas', 'Denis Gremelmayr', 'Andy Murray', 
            'Robin Vik', 'Gilles Simon', 'Michael Berrer', 'Sergiy Stakhovsky', 'Bobby Reynolds', 'Teymuraz Gabashvili', 'Lukas Dlouhy', 'Ivan Navarro', 'Dudi Sela', 'Denis Istomin', 
            'Go Soeda', 'Grega Zemlja', 'Rui Machado', 'Benjamin Balleret', 'Michal Przysiezny', 'Ryan Sweeting', 'Jose Rubin Statham', 'Benjamin Becker', 'Mischa Zverev', 
            'Marin Cilic', 'Simon Greul', 'Sam Querrey', 'Evgeny Korolev', 'Thiemo De Bakker', 'Fabio Fognini', 'Andreas Haider Maurer', 'Juan Martin del Potro', 'Diego Hartfield', 
            'Jan Hajek', 'Viktor Troicki', 'Carlos Berlocq', 'Daniel Gimeno Traver', 'Jeremy Chardy', 'Ernests Gulbis', 'Lukas Lacko', 'Robin Haase', 'Santiago Giraldo', 
            'Blaz Kavcic', 'Matthias Bachinger', 'Daniel Brands', 'Steve Darcis', 'Andrey Golubev', 'Donald Young', 'John Isner', 'Simone Bolelli', 'Kei Nishikori', 
            'Martin Klizan', 'Wayne Odesnik', 'Paolo Lorenzi', 'Pablo Andujar', 'Pere Riba', 'Jesse Levine', 'Flavio Cipolla', 'Marcel Granollers', 'Yuichi Sugita', 'Gastao Elias', 
            'Kevin Anderson', 'Edouard Roger-Vasselin', 'Eduardo Schwank', 'Leonardo Mayer', 'Lukas Rosol', 'Adrian Mannarino', 'Somdev Devvarman', 'Mikhail Kukushkin', 'Maximo Gonzalez', 
            'Joao Sousa', 'Thomaz Bellucci', 'Ryan Harrison', 'Sam Groth', 'Marsel Ilhan', 'Ivan Dodig', 'Grigor Dimitrov', 'Illya Marchenko', 'Horacio Zeballos', 'Andrey Kuznetsov', 
            'Alexandr Dolgopolov', 'Bernard Tomic', 'James Ward', 'Marius Copil', 'Jerzy Janowicz', 'Christopher Rungkat', 'Ricardas Berankis', 'Henri Laaksonen', 'Ze Zhang', 'Attila Balazs', 
            'Radu Albot', 'Tatsuma Ito', 'Yuki Bhambri', 'Matthew Ebden', 'Dustin Brown', 'Joao Souza', 'Igor Sijsling', 'Di Wu', 'Jurgen Zopp', 'Aljaz Bedene', 'Marinko Matosevic', 
            'Albert Ramos', 'Filip Krajinovic', 'Tobias Kamke', 'Denis Kudla', 'Marcelo Arevalo', 'Hugo Dellien', 'Damir Dzumhur', 'Tim Smyczek', 'Benoit Paire', 'Milos Raonic', 
            'Adrian Ungur', 'Ruben Bemelmans', 'Evgeny Donskoy', 'David Goffin', 'Marton Fucsovics', 'Dusan Lajovic', 'Vasek Pospisil', 'Rogerio Dutra Silva', 'Federico Delbonis', 
            'Cedrik Marcel Stebe', 'Jack Sock', 'Dominic Thiem', 'James Duckworth', 'Daniel Evans', 'Darian King', 'Ricardo Rodriguez', 'Facundo Bagnis', 'Roberto Bautista Agut', 
            'Inigo Cervantes Huegun', 'Kenny De Schepper', 'Marco Trungelliti', 'Steve Johnson', 'Emilio Gomez', 'John Millman', 'Cristian Garin', 'Guido Pella', 'Diego Schwartzman', 
            'Egor Gerasimov', 'Pablo Carreno Busta', 'Lucas Pouille', 'Nick Kyrgios', 'Mirza Basic', 'Kyle Edmund', 'Jan Lennard Struff', 'Peter Gojowczyk', 'Andrej Martin', 
            'Karen Khachanov', 'Pierre Hugues Herbert', 'Ramkumar Ramanathan', 'Jiri Vesely', 'Thanasi Kokkinakis', 'Taro Daniel', 'Alejandro Gonzalez', 'Borna Coric', 'Norbert Gombos', 
            'Roberto Carballes Baena', 'Jason Kubler', 'Elias Ymer', 'Renzo Olivo', 'Alexander Zverev', 'Andrey Rublev', 'Hyeon Chung', 'Nikoloz Basilashvili', 'Nicolas Jarry', 
            'Gerald Melzer', 'Jared Donaldson', 'Yoshihito Nishioka', 'Taylor Fritz', 'Liam Broady', 'Daniel Elahi Galan', 'Jaume Munar', 'Dennis Novak', 'Frances Tiafoe', 'Zhizhen Zhang', 
            'Aslan Karatsev', 'Thomas Fabbiano', 'Jordan Thompson', 'Quentin Halys', 'Thiago Monteiro', 'Ilya Ivashka', 'Casper Ruud', 'Lloyd Harris', 'Juan Pablo Varillas', 
            'Hubert Hurkacz', 'Marco Cecchinato', 'Jozef Kovalik', 'Bjorn Fratangelo', 'Tommy Paul', 'Daniil Medvedev', 'Ernesto Escobedo', 'Nicolas Kicker', 'Denis Shapovalov', 
            'Reilly Opelka', 'Kamil Majchrzak', 'Alexander Bublik', 'Mikael Ymer', 'Alex De Minaur', 'Yibing Wu', 'Laslo Djere', 'Yannick Hanfmann', 'Benjamin Bonzi', 'Daniel Altmaier', 
            'Cameron Norrie', 'Sebastian Ofner', 'Christopher Eubanks', 'Tennys Sandgren', 'Stefano Travaglia', 'Stefanos Tsitsipas', 'Michael Mmoh', 'Matteo Berrettini', 'Mackenzie Mcdonald', 
            'Maximilian Marterer', 'Lorenzo Sonego', 'Marc Andrea Huesler', 'Emil Ruusuvuori', 'Corentin Moutet', 'Tallon Griekspoor', 'Felix Auger Aliassime', 'Holger Rune', 
            'Bernabe Zapata Miralles', 'Federico Coria', 'Marcos Giron', 'Dominik Koepfer', 'Ugo Humbert', 'Yosuke Watanuki', 'Constant Lestienne', 'Oscar Otte', 'Alexei Popyrin', 
            'Miomir Kecmanovic', 'Juan Ignacio Londero', 'Pedro Cachin', 'Gregoire Barrere', 'Thiago Seyboth Wild', 'Jannik Sinner', 'Alejandro Davidovich Fokina', 'Soon Woo Kwon', 
            'Jenson Brooksby', 'Gianluca Mager', 'Tomas Machac', 'Max Purcell', 'Jack Draper', 'Arthur Rinderknech', 'Zizou Bergs', 'Hugo Gaston', 'Maxime Cressy', 'Pedro Martinez', 
            'Dominic Stricker', 'Carlos Alcaraz', 'Sebastian Korda', 'Lorenzo Musetti', 'Aleksandar Vukic', 'Brandon Nakashima', 'Alejandro Tabilo', 'Alex Molcan', 'Sebastian Baez', 
            'Botic Van De Zandschulp', 'Francisco Cerundolo', 'Roman Safiullin', 'Alexandre Muller', 'Christopher Oconnell', 'Nuno Borges', 'Juan Manuel Cerundolo', 'Tomas Martin Etcheverry', 
            'Flavio Cobolli', 'Borna Gojo', 'Jiri Lehecka', 'J J Wolf', 'Pavel Kotov', 'Ben Shelton', 'Rinky Hijikata', 'Juncheng Shang', 'Luciano Darderi', 'Arthur Fils', 
            'Facundo Diaz Acosta', 'Luca Van Assche', 'Matteo Arnaldi', 'Alexander Shevchenko', 'Fabian Marozsan', 'Hamad Medjedovic', 'Alex Michelsen', 'Jakub Mensik', 
            'Giovanni Mpetshi Perricard', 'Mariano Navone', 'Jeff Tarango', 'Mark Nielsen', 'Glenn Weiner', 'Hernan Gumy', 'Jens Knippschild', 'Christian Ruud', 'Orlin Stanoytchev', 
            'Daniel Vacek', 'Gaston Etlis', 'Martin Damm Sr', 'Federico Browne', 'Laurence Tieleman', 'Stephane Huet', 'Sebastien Lareau', 'Ronald Agenor', 'Arvind Parmar', 
            'Daniel Nestor', 'Bob Bryan', 'Nicolas Thomann', 'Neville Godwin', 'Christian Vinck', 'Tuomas Ketola', 'Fredrik Jonsson', 'Dennis Van Scheppingen', 'Adrian Garcia', 
            'Jacobo Diaz', 'Daniel Elsner', 'Jeff Salzenstein', 'Eric Taino', 'Giorgio Galimberti', 'Nicolas Coutelot', 'Michael Kohlmann', 'Frederic Niemeyer', 'Hugo Armando', 
            'Jamie Delgado', 'Eric Prodon', 'Werner Eschauer', 'Alex Kim', 'Razvan Sabau', 'Vadim Kutsenko', 'Alexandre Simoni', 'Dick Norman', 'Nenad Zimonjic', 'Julian Knowle', 
            'Zack Fleishman', 'Yuri Schukin', 'Thiago Alves', 'Sebastien De Chaunac', 'Gilles Kremer', 'Zeljko Krajan', 'Alex Bogdanovic', 'Juan Pablo Guzman', 'Todd Reid', 'Rohan Bopanna', 
            'Michael Lammer', 'Roko Karanusic', 'Jerome Haehnel', 'Stephane Bohli', 'Alex Kuznetsov', 'Michael Ryderstedt', 'Ti Chen', 'Juan Pablo Brzezicki', 'Ilija Bozoljac', 
            'Victor Crivoi', 'Farrukh Dustov', 'Aleksandr Nedovyesov', 'Jamie Baker', 'Diego Junqueira', 'Julian Reister', 'Martin Fischer', 'Peter Polansky', 'Konstantin Kravchuk', 
            'Jesse Huta Galung', 'Pedro Sousa', 'Kittipong Wachiramanowong', 'Franko Skugor', 'Josselin Ouanna', 'Brian Dabul', 'Antonio Veic', 'Daniel Munoz de la Nava', 'Austin Krajicek', 
            'Vincent Millot', 'Guillaume Rufin', 'Mohamed Safwat', 'Tsung Hua Yang', 'Martin Cuevas', 'Laurynas Grigelis', 'Bradley Klahn', 'Dimitar Kuzmanov', 'Alessandro Giannessi', 
            'Rhyne Williams', 'Adrian Menendez Maceiras', 'Guido Andreozzi', 'John Patrick Smith', 'Stefan Kozlov', 'Blaz Rola', 'Viktor Durasovic', 'Yasutaka Uchiyama', 'Mitchell Krueger', 
            'Brayden Schnur', 'Noah Rubin', 'Luca Vanni', 'Cem Ilkel', 'Alex Bolt', 'Salvatore Caruso', 'Sumit Nagal', 'Jason Jung', 'Prajnesh Gunneswaran', 'Carlos Taberner', 'Jurij Rodionov', 
            'Chun Hsin Tseng', 'Lukas Klein', 'Arthur Cazaux', 'Shintaro Mochizuki', 'Hugo Grenier', 'Luca Nardi', 'Aleksandar Kovacevic']





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

court_types = ['Hard', 'Clay', 'Grass', 'Carpet']

player_stats = {
    p: {
        surface: {
            "serve": 0,
            "return": 0,
            "aces": 0,
            "df": 0,
            "matches": 0,
        }
        for surface in court_types
    }
    for p in players
}

def build_stats(row):
    w_all_data = []
    l_all_data = []


    winner = str(row.winner_name).strip()
    loser = str(row.loser_name).strip()
    court_surface = str(row.surface)

    if court_surface not in court_types:
        return

    try:
        w_serve_to_points = float(row.w_svpt)
        w_first_serves = float(row.w_1stWon)
        w_second_serves = float(row.w_2ndWon)
        w_aces = float(row.w_ace)
        w_df = float(row.w_df)

        if w_serve_to_points > 0:

            w_serves_to_points = (w_first_serves + w_second_serves) / w_serve_to_points

            l_return_accuracy = (w_serve_to_points - (w_first_serves + w_second_serves)) / w_serve_to_points

            w_all_data.append([
                winner,
                court_surface,
                w_serves_to_points,
                l_return_accuracy,
                w_aces,
                w_df,
                1
            ])

    except (ValueError, TypeError):
        return


    try:
        l_serve_to_points = float(row.l_svpt)
        l_first_serves = float(row.l_1stWon)
        l_second_serves = float(row.l_2ndWon)
        l_aces = float(row.l_ace)
        l_df = float(row.l_df)

        if l_serve_to_points > 0:

            l_serves_to_points = (l_first_serves + l_second_serves) / l_serve_to_points

            w_return_accuracy = (l_serve_to_points - (l_first_serves + l_second_serves)) / l_serve_to_points


            l_all_data.append([
                loser,
                court_surface,
                l_serves_to_points,
                w_return_accuracy,
                l_aces,
                l_df,
                1
            ])

    except (ValueError, TypeError):
        return

    total_all_data = w_all_data + l_all_data

    for i in total_all_data:

        player = i[0]
        surface = i[1]
        serve_value = i[2]
        return_value = i[3]
        aces = i[4]
        df = i[5]
        matches = i[6]


        if (
            player in player_stats 
            and surface in court_types
            and not math.isnan(serve_value)
            and not math.isnan(return_value)
        ):

            player_stats[player][surface]["serve"] += serve_value
            player_stats[player][surface]["return"] += return_value
            player_stats[player][surface]["aces"] += aces
            player_stats[player][surface]["df"] += df
            player_stats[player][surface]["matches"] += matches
    
    # print(total_all_data_dict)

player_elo = {}

data = (
        pd.read_csv("atp_matches_2008.csv")
        .drop_duplicates()
        .sort_values("tourney_date")
    )


def new_player():
    return {
        "Hard": [1500],
        "Grass": [1500],
        "Clay": [1500],
        "Carpet": [1500],
    }

for row in data.itertuples(index=False):
    if row.winner_name not in player_elo:
        player_elo[row.winner_name] = new_player()
    if row.loser_name not in player_elo:
        player_elo[row.loser_name] = new_player()

def build_elo(row):
    K_multiplier = 40

    predictions = []
    losses = []

    court_type = row.surface
    winner_rating = player_elo[row.winner_name][court_type][-1]
    loser_rating = player_elo[row.loser_name][court_type][-1]

    expected_a = (1 / (1 + (10 ** (((loser_rating) - (winner_rating)) / 400))))   
    expected_b = 1 - expected_a

    
    if expected_a >= 0.5:
        predictions.append(1)
    else:
        predictions.append(0)

    loss = -np.log(expected_a)
    losses.append(loss)

    # print(expected_a + expected_b)

    result_a = winner_rating + (K_multiplier * (1 - expected_a))
    result_b = loser_rating + (K_multiplier * (0 - expected_b))

    # print(result_a, result_b)

    player_elo[row.winner_name][court_type].append((result_a))
    player_elo[row.loser_name][court_type].append((result_b))

losses = []

def calculate_elo(player_a, player_b, court_type):
    k = 32
    elo_a = player_elo[player_a][court_type][-1] if player_elo[player_a][court_type] else 1500
    elo_b = player_elo[player_b][court_type][-1] if player_elo[player_b][court_type] else 1500

    expected_a = 1 / (1 + 10 ** ((elo_b - elo_a) / 400))
    expected_b = 1 / (1 + 10 ** ((elo_a - elo_b) / 400))

    loss = -np.log(expected_a)
    losses.append(loss)

    # print(expected_a, expected_b)

    return expected_a, expected_b

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
    player_a_lose = player_a_stats["return"] / player_a_stats["matches"]
    a_ace = player_a_stats["aces"] / player_a_stats["matches"]
    a_df = player_a_stats["df"] / player_a_stats["matches"]


    player_b_win = player_b_stats["serve"] / player_b_stats["matches"]
    player_b_lose = player_b_stats["return"] / player_b_stats["matches"]
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

    expected_a_prob, expected_b_prob = calculate_elo(player_a, player_b, court_type)

    normalized_a_win_rate = (0.4 * ((player_a_win + player_a_lose) / total_strength) + player_a_adj) + (0.6 * expected_a_prob)

    normalized_b_win_rate = (0.4 * ((player_b_win + player_b_lose) / total_strength) + player_b_adj) + (0.6 * (expected_b_prob))

    # normalized_a_win_rate = ((player_a_win + player_a_lose) / (player_a_win + player_b_win)) + (player_a_adj)
    # normalized_b_win_rate = ((player_b_win + player_b_lose) / (player_a_win + player_b_win)) + (player_b_adj)
    # print(normalized_a_win_rate)
    # print(normalized_b_win_rate)

    normalized_a_win_rate = min(max(normalized_a_win_rate,0.02),0.98)
    normalized_b_win_rate = min(max(normalized_b_win_rate,0.02),0.98)


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
            # print(f'Winner of the match is {player_a}')
            # print(f'{player_a}: {player_a_set_score}')
            # print(f'{player_b}: {player_b_set_score}')
            # print(list((player_a, player_b, scores)))
            return list((player_a, player_b, scores))
        elif player_b_set_score >= 3:
            # print(f'Winner of the match is {player_b}')
            # print(f'{player_a}: {player_a_set_score}')
            # print(f'{player_b}: {player_b_set_score}')
            # print(list((player_b, player_a, scores)))
            return list((player_b, player_a, scores))
 

player_names = set(players)

def run_monte_carlo_simulation(iterations):
    correct_predictions = 0
    incorrect_predictions = 0

    data.columns = data.columns.str.strip()

    # data = data[["surface", "winner_name", "loser_name"]].dropna()

    


    for row in data.itertuples(index=False):
        winner = row.winner_name
        loser = row.loser_name
        
        if winner not in player_names or loser not in player_names:
            continue

        actual_winner_wins = 0
        actual_loser_wins = 0

        for i in range(iterations):
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

        build_stats(row)
        build_elo(row)


    print(correct_predictions)
    print(incorrect_predictions)
    print(f"Accuracy: {correct_predictions / (correct_predictions + incorrect_predictions) * 100:.2f}%")

 
run_monte_carlo_simulation(51)

print(np.mean(losses))

