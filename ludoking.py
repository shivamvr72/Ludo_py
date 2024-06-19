import random


ludo_cordinated = []
for i in range(15):
    for j in range(15):
        ludo_cordinated.append({(j, i): ""})

# for the dynamic player position
players_position = {}
# was for static
# players_position = {"blue": {"B1": -1, "B2": -1, "B3": -1, "B4": -1}, "red": {"R1": -1, "R2": -1, "R3": -1, "R4": -1}, "green": {"G1": -1, "G2": -1, "G3": -1, "G4": -1}, "yellow": {"Y1": -1, "Y2": -1, "Y3": -1, "Y4": -1}}

# to put kukis in the home while printing the board
home_coordinated = {"red": {"R1": (2, 2), "R2": (2, 3), "R3": (3, 2), "R4": (3, 3)}, "blue": {"B1": (2, 11), "B2": (2, 12), "B3": (3, 11), "B4": (3, 12)}, "green": {"G1": (11, 2), "G2": (11, 3), "G3": (12, 2), "G4": (12, 3)}, "yellow": {"Y1": (11, 11), "Y2": (11, 12), "Y3": (12, 11), "Y4": (12, 12)}}

# to print the destination
destination_cordinates = ((7, 6), (6, 7), (8, 7), (7, 8))

# for home side borders
home_side_borders = ((6, 6), (8, 6), (7, 7), (6, 8), (8, 8),)

# safe cordinates
safe_cordinates = ((7, 6), (6, 7), (8, 7), (7, 8), (8, 12), (6, 2), (12, 6), (2, 8), (1, 6), (6, 13), (8, 1), (13, 8))

# for borders
border_cordinates = ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (0, 2), (1, 2), (4, 2), (5, 2), (9, 2), (10, 2), (13, 2), (14, 2), (0, 3), (1, 3), (4, 3), (5, 3), (9, 3), (10, 3), (13, 3), (14, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (9, 4), (10, 4), (11, 4), (12, 4), (13, 4), (14, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (9, 5), (10, 5), (11, 5), (12, 5), (13, 5), (14, 5), (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (9, 9), (10, 9), (11, 9), (12, 9), (13, 9), (14, 9), (0, 10), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (9, 10), (10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (0, 11), (1, 11), (4, 11), (5, 11), (9, 11), (10, 11), (13, 11), (14, 11), (0, 12), (1, 12), (4, 12), (5, 12), (9, 12), (10, 12), (13, 12), (14, 12), (0, 13), (1, 13), (2, 13), (3, 13), (4, 13), (5, 13), (9, 13), (10, 13), (11, 13), (12, 13), (13, 13), (14, 13), (0, 14), (1, 14), (2, 14), (3, 14), (4, 14), (5, 14), (9, 14), (10, 14), (11, 14), (12, 14), (13, 14), (14, 14))

# for all
path_cordinates = ((6, 0), (7, 0), (8, 0), (6, 1), (7, 1), (8, 1), (6, 2), (7, 2), (8, 2), (6, 3), (7, 3), (8, 3), (6, 4), (7, 4), (8, 4), (6, 5), (7, 5), (8, 5), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (7, 6), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (8, 7), (9, 7), (10, 7), (11, 7), (12, 7), (13, 7), (14, 7), (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (7, 8), (9, 8), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (6, 9), (7, 9), (8, 9), (6, 10), (7, 10), (8, 10), (6, 11), (7, 11), (8, 11), (6, 12), (7, 12), (8, 12), (6, 13), (7, 13), (8, 13), (6, 14), (7, 14), (8, 14))

# blue path
blue_path_cordiantes = ((6, 13), (6, 12), (6, 11), (6, 10), (6, 9), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), (0, 8), (0, 7), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 5), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0), (7, 0), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6), (14, 7), (14, 8), (13, 8), (12, 8), (11, 8), (10, 8), (9, 8), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (7, 14), (7, 13), (7, 12), (7, 11), (7, 10), (7, 9), (7, 8))

# red path
red_path_cordinates = ((1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 5), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0), (7, 0), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6), (14, 7), (14, 8), (13, 8), (12, 8), (11, 8), (10, 8), (9, 8), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (7, 14), (6, 14), (6, 13), (6, 12), (6, 11), (6, 10), (6, 9), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), (0, 8), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7))

# yellow path
yellow_path_cordinates = ((13, 8), (12, 8), (11, 8), (10, 8), (9, 8), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (7, 14), (6, 14), (6, 13), (6, 12), (6, 11), (6, 10), (6, 9), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), (0, 8), (0, 7), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 5), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0), (7, 0), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6), (14, 7), (13, 7), (12, 7), (11, 7), (10, 7), (9, 7), (8, 7))

# green path
green_path_cordinates = ((8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6), (14, 7), (14, 8), (13, 8), (12, 8), (11, 8), (10, 8), (9, 8), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (7, 14), (6, 14), (6, 13), (6, 12), (6, 11), (6, 10), (6, 9), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), (0, 8), (0, 7), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 5), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6))

# safe zones for printing
safe_zone = ((8, 12), (6, 2), (12, 6), (2, 8))

# start cordinates for printing 
start_cordinates = ((1, 6), (6, 13), (8, 1), (13, 8))

# red homes
redhome = ((2, 2), (3, 2), (2, 3), (3, 3))
bluehome = ((2, 11), (3, 11), (2, 12), (3, 12))
greenhome = ((11, 2), (12, 2), (11, 3), (12, 3))
yellowhome = ((11, 11), (12, 11), (11, 12), (12, 12))

# dynamic winner list
winners = []

# home position
def set_home(ludo, player_color, home_cordinates, dictionary):
    try:
        # for setting up the empty homes
        for emptyhome in home_cordinates:
            if emptyhome == ludo:
                index = ludo_cordinated.index(dictionary)
                ludo_cordinated[index][ludo] = "{:>7}".format("[X]")

        # for the players home
        for player, coins in players_position.items():
            if player == player_color:
                for cordinate, color in zip(coins.items(), home_cordinates):
                    if color == ludo and cordinate[1] == -1:
                        index = ludo_cordinated.index(dictionary)
                        ludo_cordinated[index][ludo] = "{:>7}".format(cordinate[0])
                    elif color == ludo:
                        index = ludo_cordinated.index(dictionary)
                        ludo_cordinated[index][ludo] = "{:>7}".format("[ ]")

    except Exception as e:
        print("something went wrong!")
        return False

def set_path_ways(ludo, cordinates, dictionary, set_with):
    # for priting path and boards postions
    try:
        for cords in cordinates:
            if ludo == cords:
                index = ludo_cordinated.index(dictionary)
                if set_with == "*":
                    ludo_cordinated[index][ludo] = f"   {set_with}   "
                else:
                    ludo_cordinated[index][ludo] = " {:>5} ".format(set_with)

    except Exception as e:
        print("something went wrong!")
        return False


def is_home(ludo, dictionary):
    set_home(ludo, "red", redhome, dictionary)
    set_home(ludo, "blue", bluehome, dictionary)
    set_home(ludo, "green", greenhome, dictionary)
    set_home(ludo, "yellow", yellowhome, dictionary)


def pathways(ludo, dictionary):
    set_path_ways(ludo, home_side_borders, dictionary, "*")
    set_path_ways(ludo, border_cordinates, dictionary, "#")
    set_path_ways(ludo, path_cordinates, dictionary, "|  |")
    set_path_ways(ludo, destination_cordinates, dictionary, "| H |")
    set_path_ways(ludo, safe_zone, dictionary, "| s |")
    set_path_ways(ludo, start_cordinates, dictionary, "| S |")


def set_coin_operation(ludo, dictionary, coin_dict, cordinates):
    try:
        for coin, value in coin_dict.items():
            if value != -1 and value <= 56:
                cordinate = cordinates[value]
                if cordinate == ludo:
                    index = ludo_cordinated.index(dictionary)
                    ludo_cordinated[index][ludo] = " {:>5} ".format(
                        f"| {coin} |")
    except Exception as e:
        print("something went wrong!")
        return False


# main control
def display():
    try:
        i = 0
        for positions in ludo_cordinated:
            for key, position in positions.items():
                print(position, end=" ")
            i += 1
            if i == 15:
                print("\n\n")
                i = 0
    except Exception as e:
        print("something went wrong!")
        return False


def start_boarding(c_player, dice, player_upcoming):
    try:
        print("\nAll Players Position")
        for pl, vl in players_position.items():
            print("{:<6} {:<20}".format(f"{pl}", f"{vl}") )

        print("\nCurrent Player: ", players_position[c_player])
        print(f"Dice: {dice}")

        for ludo_dict in ludo_cordinated:
            for ludo in ludo_dict:
                # setting coins on home index
                is_home(ludo, ludo_dict)
            # for setting up the path, safe zones and destination
            pathways(ludo, ludo_dict)

            # for setting up the player
            for player, coin_dict in players_position.items():
                if player == "blue":
                    set_coin_operation(ludo, ludo_dict, coin_dict, blue_path_cordiantes)
                elif player == "red":
                    set_coin_operation(ludo, ludo_dict, coin_dict, red_path_cordinates)
                elif player == "yellow":
                    set_coin_operation(ludo, ludo_dict, coin_dict, yellow_path_cordinates)
                elif player == "green":
                    set_coin_operation(ludo, ludo_dict, coin_dict, green_path_cordinates)
        display()
    except Exception as e:
        print("something went wrong!")
        return False


def game_play(player, coin, dice):
    try:
        # for killing the coins
        cord = None
        flag = False
        if (players_position[player][coin] + dice) < 56:
            if player == "blue":
                cord = blue_path_cordiantes[players_position[player][coin] + dice]
            elif player == "red":
                cord = red_path_cordinates[players_position[player][coin] + dice]
            elif player == "green":
                cord = green_path_cordinates[players_position[player][coin] + dice]
            elif player == "yellow":
                cord = yellow_path_cordinates[players_position[player][coin] + dice]

        # print("cord...", cord)
        for dics in ludo_cordinated:
            for dt in dics:
                if dt == cord:
                    killable = dics[cord]
                    # print(killable, "thi killabel might be")
                    nkills = killable.strip(" | ")

                    if len(nkills) == 2 and cord not in safe_cordinates:
                        if nkills[0] == "R" and coin[0] != "R":
                            players_position["red"][nkills] = -1
                            print("Red executed", players_position["red"][nkills])
                            flag = True
                            break
                        elif nkills[0] == "B" and coin[0] != "B":
                            players_position["blue"][nkills] = -1
                            print("Blue executed", players_position["blue"][nkills])
                            flag = True
                            break
                        elif nkills[0] == "G" and coin[0] != "G":
                            players_position["green"][nkills] = -1
                            print("Green executed", players_position["green"][nkills])
                            flag = True
                            break
                        elif nkills[0] == "Y" and coin[0] != "Y":
                            players_position["yellow"][nkills] = -1
                            print("Yellow executed", players_position["yellow"][nkills])
                            flag = True
                            break
                    break

        if players_position[player][coin] + dice <= 56:
            players_position[player][coin] = players_position[player][coin] + dice
            player_upcoming = players_position[player][coin]
            start_boarding(player, dice, player_upcoming)
            if flag == True:
                return "killed"
            else:
                return False
        else:
            return True
        
    except Exception as e:
        print("something went wrong!")
        return False


def ask_roll_dice():
    try:
        ## manual mode
        # n = input("Roll The Dice or For Exit N: ").strip(" ").capitalize()
        # x = n
        ## automatic mode
        x = input("\nRoll The Dice or For Exit N: ").strip(" ").capitalize()
        n = random.randint(1, 6)

        if x == "N":
            return "N"
        else:
            print("Dice: ", n)
            return int(n)
        
    except Exception as e:
        print("something went wrong!")
        return False


def ask_coin_to_move(player, coins, n):
    try:
        players_coins_on_path = [player[0].capitalize()]
        all_at_home = all(value == -1 for value in coins.values())

        for rcoin, value in coins.items():
            if (value != -1 and value != 56 and (value + n) <= 56) or (value == -1 and n == 6):
                players_coins_on_path.append(rcoin[1])

        print(players_coins_on_path)
        if len(players_coins_on_path) == 1:
            return False
        while True:
            coin = input("\nEnter coin to move: ").strip(" ").capitalize()
            if coin in players_coins_on_path:
                if coin.isdigit():
                    prefix = player[0].capitalize()
                    coin = prefix + str(coin)
                    return coin
                else:
                    print("\nInvalid Choice. Try Again!")
    except Exception as e:
        print("something went wrong!")
        return False


def move_piece(player, coin, steps):
    try:
        current_position = players_position[player][coin]

        if current_position == -1:
            if steps == 6:
                players_position[player][coin] = 0
                game_play(player, coin, 0)
                return True
            else:
                return False
        else:
            if current_position + steps <= 56:
                new_position = current_position + steps
            else:
                overshoot = current_position + steps - 56
                new_position = 56 - overshoot

            iskill = game_play(player, coin, steps)
            if iskill =="killed":
                return "killed"
            
            if new_position == 56:
                print(f"\n*** {player}'s {coin} has reached the finish! ***\n")
                return "reached"
            return True

    except Exception as e:
        print("something went wrong!")
        return False


def game_over():
    for player in players_position:
        iswin = all(position == 56 for position in players_position[player].values())
        if not iswin:
            return False
    return True


def check_win(player):
    try:
        iswin = all(position == 56 for position in players_position[player].values())
        if iswin:
            winners.append(player)
            if game_over():
                print("over1")
                return "over"
            
        return iswin
    
    except Exception as e:
        print("something went wrong! Check win")
        return False


def on_the_way(player, coins):
    try:
        if player in winners:
            return False
        
        print(f"\nTurn: {player.capitalize()}")
        while True:
            n = ask_roll_dice()

            if n == "N":
                return "N"

            if all(value == -1 for value in coins.values()) and n != 6:
                print("\nDidn't get 6...! Try Again in Next Turn\n")
                return False

            coin = ask_coin_to_move(player, coins, n)
            if not coin:
                return False
            
            ans = move_piece(player, coin, n)
            if ans == "killed" or ans == "reached":
                winover = check_win(player)
                if winover == "over":
                    print("\n!! Game Over !!\n")
                    return "N"
                
                if winover:
                    print(f"\n\n**|** {player.capitalize()} wins the game! **|**\n\n")
                continue
                
            if ans:
                print(f"\nMoved {coin} for {player}. New Position: {players_position[player][coin]}")
                if n != 6:
                    return True
            else:
                print("\nCouldn't move the selected piece! Try again")
                if n == 6:
                    continue

    except Exception as e:
        print("something went wrong!", e)
        return False


def start_game():
    try:
        flag = True
        while flag:
            try:
                nply = int(input("\nEnter number of players: ").strip(" "))
                if nply >= 2 and nply <= 4:
                    flag = False
                else:
                    print("\nplease enter 2 or less then 5 players!")
                    continue
            except:
                continue

        plyer_color = ["blue", "red", "green", "yellow"]
        for n in range(nply):
            players_position[plyer_color[n]] = {f"{plyer_color[n][0].capitalize()}1": -1, f"{plyer_color[n][0].capitalize()}2": -1,
                                                f"{plyer_color[n][0].capitalize()}3": -1, f"{plyer_color[n][0].capitalize()}4": -1}
        
        # print(players_position, "Run time list")
        start_boarding("blue", "0", "0")
        flag = True
        while flag:
            for player, coins in players_position.items():
                ans = on_the_way(player, coins)
                if ans == "N":
                    flag = False
                    break
    except Exception as e:
        print("something went wrong!")
        return False

# print(players_position)
if __name__ == "__main__":
    start_game()
