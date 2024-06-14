import random 

board_num = [range(1,11), range(20, 10, -1), range(21, 31), range(40, 30, -1), range(41, 51), range(60, 50, -1), range(61, 71), range(80, 70, -1), range(81, 91), range(100, 90, -1)][::-1]

snake_mouth = [30, 38, 43, 49, 55, 58, 63, 69, 72, 79, 84, 87, 93, 98, 99]
snake_tails = [9, 19, 15, 29, 37, 24, 40, 39, 27, 51, 21, 7, 59, 52, 7]

ladder_start = [8, 18, 13, 23, 34, 41, 60]
ladder_end = [28, 36, 27, 51, 63, 90, 83][::-1]


snake_bit = {30: 9, 38: 19, 43: 15, 49: 29, 55: 37, 58: 24, 63: 40, 69: 39, 72: 27, 79: 51, 84: 21, 87: 7, 93: 59, 98: 52, 99: 7}
ladders = {8: 28, 18: 36, 13: 27, 23: 51, 34: 63, 41: 90, 60: 83}

player = {"( p1 )": 0, "( p2 )": 0, "( p3 )":0, "( p4 )":0, "( p5 )":0}

def create_board(n, p):

    st = -1
    sd = -1
    
    player[p] = player.get(p) + n
    print("Dice: ", n)
    print(player)
    print(p in player.keys())
    print(p+": ", player[p])
    
    for i in board_num:
        for j in i: 
    
            if j in snake_mouth:
                st += 1
                j = f"{str(j)}>~~{snake_tails[st]}"
                jsnake = j.split(">~~")[0]
                if int(jsnake) <= player[p]:
                    if int(jsnake) == player[p]:
                        player[p] = snake_bit[int(jsnake)]
                        j = f"{player[p]}>~~{snake_tails[st]}"
            
            if j in ladder_start:
                sd += 1
                j = f"{ladder_end[sd]}|=|{str(j)}"
                jladder = j.split("|=|")[1]
                if int(jladder) <= player[p]:
                    if int(jladder) == player[p]:
                        player[p] = ladders[int(jladder)]
                        # j = f"{ladders[sd]}|=|{player[p]}"
            
            if j == player[p]:
                j = f"{str(j)} {p}"
                
            if p in player.keys():
                for px in player.keys():
                    if j == player[px]:
                        j = f"{str(j)}{px}"
            
            print(" {:<10} ".format(str(j)), end=" ")

        print("\n\n")
    print("\n\n")

def dice():
    n = random.choice(range(1,7))
    return n


i = 0
play = ["( p1 )", "( p2 )", "( p3 )", "( p4 )", "( p5 )"]


while player[play[i]] <= 100:
    py = play[i]
    x = input("Roll The Dice: ").strip(" ")
    if x == "":
        n = dice()
        
        create_board(n, py)
        i+=1
        if i == 5:
            i = 0
    