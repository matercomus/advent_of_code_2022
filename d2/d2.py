#rock     - A,X 1 
#paper    - B,Y 2
#scissors - C,Z 3
#lost 0
#tied 3
#won  6
with open("d2/input.txt","r") as input:
    rounds = input.read().split('\n')[:-1]
    rounds = [i.split() for i in rounds]
    #replace opponents xyz for abc respectively for comparisons.
    for round in rounds:
        round[1] = round[1].replace('X', 'A')
        round[1] = round[1].replace('Y', 'B')
        round[1] = round[1].replace('Z', 'C')

    #[rock,paper,scissors] each kills the index below it (negative indexies will start from end)
    n_points = 0 
    def point_counter(round):
        global n_points
        rules = ['A','B','C']
        opponent = round[0]
        player = round[1]

        #tie
        if opponent == player:
            n_points += rules.index(player) +1
            n_points += 3

        #player wins
        if opponent == rules[rules.index(player)-1]:
            n_points += rules.index(player) +1
            n_points += 6

        #Opponent wins
        if player == rules[rules.index(opponent)-1]:
            n_points += rules.index(player) +1
    for round in rounds:
        point_counter(round)

    print(f'Total Points: {n_points}')

    