# gameConfig: first column is selling price, second is rent price
# initial funds: 300 coins
# number of properties: 20
# dice: D6
# gains 100 coins when making a full lap on the board

# first player: IMPULSIVE buys anything
# second player: EXIGENT buys properties whose rent is higher than 50 coins
# third player: CAUTIOUS only buys if it has at least 80 coins left
# fourth player: RANDOM 50% chance of buying

# limit of 1000 rounds
# wins the player with more coins, to break the tie use the players order (first is higher than second ...)

# SIMULATION CONSTRAINTS AND ASSUMPTIONS
# players start in the first field
# players order is randomized at the beginning of match

# ---------------------------------------------------------------------------------------------------------

from models import Board, Field, Player, Game

entry = open('app/res/gameConfig.txt', 'r')

fields = []

for line in entry:
    fields.append(line.split())

print('max_rounds,player_style,rounds')

for i in range(0,300):
    game = Game(Board(fields))
    game.play_game()
    
