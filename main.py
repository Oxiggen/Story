import os
from time import sleep
is_game_over = False
is_already_used = False
is_correct_option = False
picks_list = []
logo_values = {
    "A1": " ",
    "A2": " ",
    "A3": " ",
    "B1": " ",
    "B2": " ",
    "B3": " ",
    "C1": " ",
    "C2": " ",
    "C3": " ",
}

def draw_field(logo_values):
    logo = f"""
       A   B   C
     -------------
    1| {logo_values['A1']}  | {logo_values['B1']}  | {logo_values['C1']}  |
     |------------
    2| {logo_values['A2']}  | {logo_values['B2']}  | {logo_values['C2']}  |
     |------------
    3| {logo_values['A3']}  | {logo_values['B3']}  | {logo_values['C3']}  |
    """
    return print(logo)

def check_winner(logo_values):

    if (logo_values['A1'] == logo_values['A2'] == logo_values['A3']) and logo_values['A1'] != " ":
        return True
    elif (logo_values['B1'] == logo_values['B2'] == logo_values['B3']) and logo_values['B1'] != " ":
        return True
    elif (logo_values['C1'] == logo_values['C2'] == logo_values['C3']) and logo_values['C1'] != " ":
        return True
    elif (logo_values['A1'] == logo_values['B1'] == logo_values['C1']) and logo_values['A1'] != " ":
        return True
    elif (logo_values['A2'] == logo_values['B2'] == logo_values['C2']) and logo_values['A2'] != " ":
        return True
    elif (logo_values['A3'] == logo_values['B3'] == logo_values['C3']) and logo_values['A3'] != " ":
        return True
    elif (logo_values['A1'] == logo_values['B2'] == logo_values['C3']) and logo_values['A1'] != " ":
        return True
    elif (logo_values['A3'] == logo_values['B2'] == logo_values['C1']) and logo_values['A3'] != " ":
        return True

    else:
        return False


def check_draw(logo_values):
    if ' ' in logo_values.values():
        return False
def check_already_used(picks_list, pick):
    if pick in picks_list:
        print("This position is already occupied please try again:")
        return False
    else:
        return True

def check_option(logo_values, pick):
    if pick in logo_values:
        return True
    else:
        print("Incorrect value pick again:")
        return False


player1 = input("Player 1 what would you like to have X or O :")
os.system('cls')
if player1 == "X":
   player2 = "O"
else:
    player2 = "X"

draw_field(logo_values)
player = player1



while not is_game_over:

    while not is_already_used:
            pick = input(f"Player {player} pick the field eg.A1 ... :")
            print(pick)
            is_correct_option = check_option(logo_values, pick)
            if is_correct_option == True:
               is_already_used = check_already_used(picks_list, pick)

            else:
                is_already_used = False
            picks_list.append(pick)



    logo_values[pick] = player
    sleep(1)
    os.system('cls')
    draw_field(logo_values)
    winner = check_winner(logo_values)
    draw = check_draw(logo_values)
    if winner == True or draw == True:
        print(f"Player {player} won")
        is_game_over = True
    if player == player1:
        player = player2
    else:
        player = player1
    is_correct_option = False
    is_already_used = False
