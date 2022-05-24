import random
print("Simple version of the game Black&Jack\n")
budget = float(input("Enter amount of money for the game: \n"))
list_cards = ["A_", "K_", "Q_", "J_", "10_", "9_", "8_", "7_", "6_", "5_", "4_", "3_", "2_"]
list_types = ["Hearts", "Spades", "Clubs", "Diamonds"]
command = input("Enter command to continue (bet/quit): \n")
# Трябва да изберете една от командите. С "bet" започва раздаването на карти.
# С командата "quit" спираш да играеш.
your_money = budget
over_21 = False
open_bank_card = "|"
while command != "quit":
    if command != "bet":
        print("Wrong command!Please, repeat your choice.")
        command = input("Enter command to continue (bet/quit): \n")
        continue
    your_bet = your_money * 0.20
    random.shuffle(list_cards)
    random.shuffle(list_types)
    counter = 0
    points_bank = 0
    points_player = 0
    bank_cards = "|"
    player_cards = "|"
    for _ in range(2):
        pick_card_bank = random.choice(list_cards) + random.choice(list_types)
        pick_card_player = random.choice(list_cards) + random.choice(list_types)
        if pick_card_bank[0].isdigit():
            points_bank += int(pick_card_bank[0])
            if pick_card_bank[1].isdigit():
                points_bank += 9
        elif pick_card_bank[0] == "A":
            points_bank += 11
        else:
            points_bank += 10
        if pick_card_player[0].isdigit():
            points_player += int(pick_card_player[0])
            if pick_card_player[1].isdigit():
                points_player += 9
        elif pick_card_player[0] == "A":
            points_player += 11
        else:
            points_player += 10
        open_bank_card = pick_card_bank
        bank_cards += pick_card_bank + "|"
        player_cards += pick_card_player + "|"
    print(f"Your cards: {player_cards}")
    print(f"Dealer`s opened card: {open_bank_card}|")
    print(f"Your bet is : {your_bet:.2f} \n")
    if not player_cards.isdigit() and points_player == 21:
        your_money += your_bet * 1.5
        print(f"Black&Jack!!! You won.\nYour money for betting: {your_money:.2f}\n")
        command = input("Enter command to continue (bet/quit): \n")
        if command != "bet" or command != "quit":
            print("Wrong command!Please, repeat your choice.")
            command = input("Enter command to continue (bet/quit): \n")
        continue
    command_input = input("Enter command to continue (hit/stand)? \n")
    # Трябва да изберете една от командите. С "card" получавате допълнителна карта.
    # С команда "stay" оставаш да играеш с текущите ти карти.
    while command_input != "stand":
        if command_input != "hit":
            print("Wrong command!Please, repeat your choice.")
            command_input = input("Enter command to continue hit/stand)? \n")
            continue
        pick_card_player = random.choice(list_cards) + random.choice(list_types)
        if pick_card_player[0].isdigit():
            points_player += int(pick_card_player[0])
            if pick_card_player[1].isdigit():
                points_player += 9
        elif pick_card_player[0] == "A":
            points_player += 11
        else:
            points_player += 10
        player_cards += pick_card_player + "|"
        if player_cards.count("A") < counter and points_player > 21:
            counter += 1
            points_player -= 10
        if points_player > 21:
            your_money -= your_bet
            print(f"Your cards: {player_cards}")
            print(f"You lose your bet : {your_bet:.2f}!\nYour money for betting: {your_money:.2f}")
            print(f"Dealer`s cards: {bank_cards}\n")
            over_21 = True
            break
        else:
            print(f"Your cards: {player_cards}")
            command_input = input("Enter command to continue (hit/stand)? \n")
            if command_input != "hit" or command != "stand":
                print("Wrong command!Please, repeat your choice.")
                command_input = input("Enter command to continue (hit/stand): \n")
            continue
    if over_21:
        command = input("Enter command to continue (bet/quit): \n")
        if command != "bet" or command != "quit":
            print("Wrong command!Please, repeat your choice.")
            command = input("Enter command to continue (bet/quit): \n")
        continue
    while points_bank < 17:
        pick_card_bank = random.choice(list_cards) + random.choice(list_types)
        if pick_card_bank[0].isdigit():
            points_bank += int(pick_card_bank[0])
            if pick_card_bank[1].isdigit():
                points_bank += 9
        elif pick_card_bank[0] == "A":
            points_bank += 11
        else:
            points_bank += 10
        bank_cards += pick_card_bank + "|"
        if bank_cards.count("A") < counter and points_bank > 21:
            counter += 1
            points_bank -= 10
        if points_bank > 21:
            your_money += your_bet
            print(f"You win the bet: {your_bet:.2f}\nYour money for betting: {your_money:.2f}")
            print(f"Dealer`s cards: {bank_cards}\n")
            over_21 = True
            break
    if over_21:
        command = input("Enter command to continue (bet/quit): \n")
        if command != "bet" or command != "quit":
            print("Wrong command!Please, repeat your choice.")
            command = input("Enter command to continue (bet/quit): \n")
        continue
    if points_bank > points_player:
        your_money -= your_bet
        print(f"Your cards: {player_cards}")
        print(f"Dealer`s cards: {bank_cards}")
        print(f"You lose your bet: {your_bet:.2f}\nYour money for betting:{your_money:.2f}\n")
    elif points_player > points_bank:
        your_money += your_bet
        print(f"Your cards: {player_cards}")
        print(f"Dealer`s cards: {bank_cards}")
        print(f"You win the bet: {your_bet:.2f}\nYour money for betting: {your_money:.2f}\n")
    else:
        print(f"Your cards: {player_cards}")
        print(f"Dealer`s cards: {bank_cards}")
        print(f"You save your bet: {your_bet:.2f}\nYour money for betting: {your_money:.2f}\n")
    if your_money <= 10:
        print("Your money is over!\nYou have only for taxi!\n")
        break
    command = input("Enter command to continue (bet/quit): \n")
    if command != "bet" or command != "quit":
        print("Wrong command!Please, repeat your choice.")
        command = input("Enter command to continue (bet/quit): \n")
        continue
print(f"Good game! You have {your_money:.2f} money after the game.")
