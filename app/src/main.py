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

from models import Board, Field, Player, Game, PlayerStyle

entry = open('app/res/gameConfig.txt', 'r')

fields = []

for line in entry:
    fields.append(line.split())

player_styles = {
    PlayerStyle.IMPULSIVE: 0,
    PlayerStyle.EXIGENT: 0,
    PlayerStyle.CAUTIOUS: 0,
    PlayerStyle.RANDOM: 0,
}

count_max_rounds = 0

sum_round_count = 0

for i in range(0,300):
    game = Game(Board(fields))
    max_rounds, player_style, round_count = game.play_game()

    player_styles[player_style] += 1
    if max_rounds:
        count_max_rounds += 1

    sum_round_count += round_count
print('{} games ends in a  timeout, representing {:.2f}%'.format(count_max_rounds, count_max_rounds/300 * 100))
print('the mean duration of a game is {:.2f} rounds'.format(sum_round_count/300))
best_behavior = None
max_victories = 0
for player_style in player_styles:
    if player_styles[player_style] > max_victories:
        max_victories = player_styles[player_style]
        best_behavior = player_style
    print('{} wins {:.2f}% of games'.format(player_style, player_styles[player_style] / 300 * 100))

print('The behavior that wins most of games is {}'.format(best_behavior))




    
