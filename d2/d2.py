with open("d2/input.txt","r") as input:
    rounds = input.read().split('\n')[:-1]
    rounds = [i.split() for i in rounds]

    #[rock,paper,scissors] each kills the index below it (negative indexies will start from end)
    n_points = 0 
    def point_counter(round):
        global n_points
        rules_oponent = ['A','B','C']
        rules_player = ['X','Y','Z']
        opponent = round[0]
        player = round[1]

        #tie
        if opponent == rules_oponent[rules_player.index(player)]:
            n_points += rules_player.index(player) +1
            n_points += 3

        #player wins
        if opponent == rules_oponent[rules_player.index(player)-1]:
            n_points += rules_player.index(player) +1
            n_points += 6

        #Opponent wins
        if player == rules_player[rules_oponent.index(opponent)-1]:
            n_points += rules_player.index(player) +1
    
    def p1():
        for round in rounds:
            point_counter(round)
        print(f'Total Points: {n_points}')
    
    def p2():
        pass

    p1()
    p2()

    