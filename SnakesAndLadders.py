import random

# ... add your functions here

# DON'T CHANGE THE CODE BELOW
def main():
    # Ensure that games play out deterministically by specifying the random seed.
    # This is needed to ensure that the sequence of die rolls is exactly as expected by the tests in Mimir.
    random.seed(1337)
    snakes, ladders = read_board_layout_from_input()
    player1, player2 = read_player_names_from_input()
    winner = play_game(snakes, ladders, player1, player2)
    declare_winner(winner)


# Make use of this method whenever a player rolls a die
def roll_die() -> int:
    """ Simulate a roll of a 6-sided die """
    return random.randint(1, 6)


main()
