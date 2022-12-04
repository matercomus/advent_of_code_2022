# Split the input into a list of rounds
with open("input.txt","r") as input:
    rounds = input.read().split('\n')[:-1]
    rounds = [i.split() for i in rounds]

# [rock, paper, scissors] each kills the index below it (negative indexies will start from end)
def point_counter(round):
    # Define the rules for the game
    rules_opponent = ['A','B','C']
    rules_player = ['X','Y','Z']

    # Get the opponent and player moves
    opponent = round[0]
    player = round[1]
    opponent_index = rules_opponent.index(opponent)
    player_index = rules_player.index(player)

    # Calculate the points earned in this round
    points = player_index + 1
    if opponent == rules_opponent[player_index]:
        # Tie
        points += 3
    elif opponent == rules_opponent[player_index-1]:
        # Player wins
        points += 6
    else:
        # Opponent wins
        points += 0

    return points

# Calculate the total points earned in all rounds
def p1():
    # Initialize the total points to 0
    total_points = 0

    # Iterate through the rounds and calculate the points earned in each round
    for round in rounds:
        points = point_counter(round)
        total_points += points

    print(f'Total Points: {total_points}')

def p2():
    # Define the rules for the game
    rules_opponent = ['A','B','C']
    rules_player = ['X','Y','Z']

    # Initialize the total points to 0
    total_points = 0

    # Iterate through the rounds and calculate the points earned in each round
    for round in rounds:
        # Get the opponent and result moves
        opponent = round[0]
        result = round[1]

        # Get the index of the opponent move in the rules
        opponent_index = rules_opponent.index(opponent)

        # Choose the player move based on the result move
        if result == 'X':
            player_index = opponent_index - 1
        elif result == 'Y':
            player_index = opponent_index
        else:
            player_index = opponent_index + 1

        # Adjust the index of the player move if it is out of range
        if player_index < 0:
            player_index += 3
        elif player_index > 2:
            player_index -= 3

        # Calculate the points earned in this round
        points = player_index + 1
        if opponent == rules_opponent[player_index]:
            # Tie
            points += 3
        elif opponent == rules_opponent[player_index-1]:
            # Player wins
            points += 6
        else:
            # Opponent wins
            points += 0

        total_points += points

    print(f'Total Points: {total_points}')

p1()
p2()