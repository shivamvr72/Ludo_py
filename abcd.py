players = {"red":{"R1": 0, "R2": 0, "R3": 1, "R4": 0}, "blue":{"B1": 0, "B2": 0, "B3": 4, "B4": 0}, "green":{"G1": 0, "G2": 0, "G3": 0, "G4": 0}, "yellow":{"Y1": 0, "Y2": 0, "Y3": 0, "Y4": 0}}

home_coordinated = {"red":{"R1":(2, 2), "R2":(2, 3), "R3":(3, 2), "R4":(3, 3)}, "green":{"G1":(2, 11), "G2":(2, 12), "G3":(3, 11), "G4":(3, 12)},"blue": {"B1":(11, 2), "B2":(11, 3), "B3":(12, 2), "B4":(12, 3)}, "yellow":{"Y1":(11, 11), "Y2":(11, 12), "Y3":(12, 11), "Y4":(12, 12)}}


def show_board(player, kuki):
    rowcolpath = (6,7,8)
    homepath = (2,3,11,12)
    for column in range(15):
        for row in range(15):
            if row in homepath and column in homepath:
                for player, kukis in players.items():
                    for player_key in home_coordinated.keys():
                        if player_key == player:
                            for kuki in kukis.keys():
                                if players[player][kuki] == 0:
                                    if home_coordinated[player][kuki][0] == column and home_coordinated[player][kuki][1] == row:
                                        print("{:>3}".format(kuki), end="  ")
                                elif home_coordinated[player][kuki][0] == column and home_coordinated[player][kuki][1] == row:
                                    print("{:>3}".format("[ ]"), end="  ")
                            
                        
            else:
                if row in rowcolpath or column in rowcolpath:
                    if row in rowcolpath and column in rowcolpath:
                        print("{:>3}".format("[X]"), end="  ")
                    else:
                        if row == 12 and column == 6 or row == 13 and column == 8 or row == 2 and column == 8 or row==1 and column == 6 or row==6 and column == 2 or row == 8 and column == 1 or column == 13 and row == 6 or column == 12 and row == 8:
                            print("{:>3}".format("(S)"), end="  ")
                        else:
                            print("{:>3}".format("| |"), end="  ")
                else:
                    print("{:>3}".format(" 0 "), end="  ")
            
        print("\n")

show_board("blue", "B3")