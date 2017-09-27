from random import randint, uniform, shuffle
from enum import Enum
import math

class PlayerStyle(Enum):
    IMPULSIVE = 1
    EXIGENT = 2
    CAUTIOUS = 3
    RANDOM = 4

class Player:
    funds = 300
    style = None
    current_field = None
    lost_game = False

    def __init__(self, style, initial_field):
        self.lost_game = False
        if style is None:
            raise Exception('this player has no style!')
        self.style = style
        self.current_field = initial_field

    def wants_to_buy(self):
        if self.style == PlayerStyle.IMPULSIVE:
            return True
        elif self.style == PlayerStyle.EXIGENT:
            if self.current_field.rent_price > 50:
                return True
            else:
                return False
        elif self.style == PlayerStyle.CAUTIOUS:
            if self.funds - self.current_field.selling_price >= 80:
                return True
            else: 
                return False
        elif self.style == PlayerStyle.RANDOM:
            if uniform(0,1) > 0.5:
                return True
            else: 
                return False
        else: 
            raise Exception('Player did not choose whether to buy or not!')


class Field:
    selling_price = None
    rent_price = None
    owner = None

    def __init__(self, selling_price, rent_price):
        self.selling_price = selling_price
        self.rent_price = rent_price

    def pay_rent(self, player):
        if self.owner is not None and self.owner is not player:
            player.funds -= self.rent_price
            self.owner.funds += self.rent_price

    def buy(self, player):
        # tries to buy, but only succeeds if it is possible
        if self.owner is None and player.funds >= self.selling_price:
            player.funds -= self.selling_price
            self.owner = player

class Board:
    fields = []

    # expects to receive an array of exactly 20 arrays containing two elements, each one represents a field
    def __init__(self, fields):
        self.fields = []
        for field in fields:
            self.fields.append(
                Field(
                    int(field[0]), 
                    int(field[1])
                )
            )
        if len(self.fields) != 20:
            raise Exception('wrong number of fields unable to build board')

    def walk_on_board(self, player, steps):
        current_idx = self.fields.index(player.current_field)
        if current_idx + steps < 20:
            player.current_field = self.fields[current_idx + steps]
        else:
            # made a full lap on the board
            player.funds += 100
            idx = current_idx + steps - 20
            player.current_field = self.fields[idx]

    def print(self):
        print('---------------------------')
        for field in self.fields:
            print('{}: {} {} {}'.format(
                self.fields.index(field),
                field.selling_price,
                field.rent_price,
                field.owner.style if field.owner else 'None'
                ))
        print('---------------------------')

class Game:
    board = None
    players = None
    round_count = None
    winner = None

    def __init__(self, board):
        self.board = board
        self.players = [
            Player(PlayerStyle.IMPULSIVE, board.fields[0]),
            Player(PlayerStyle.EXIGENT, board.fields[0]),
            Player(PlayerStyle.CAUTIOUS, board.fields[0]),
            Player(PlayerStyle.RANDOM, board.fields[0])
        ]
        shuffle(self.players)
        self.round_count = 0

    def game_ended(self):
        total = len(self.players)
        in_game = 0
        possible_winner = None
        for player in self.players:
            if player.funds >= 0:
                possible_winner = player
                in_game += 1
        
        if in_game == 1:
            self.winner = possible_winner
            return True
        else:
            return False

    def best_player(self):
        best_player = None
        best_wallet = -math.inf
        for player in self.players:
            if player.funds > best_wallet:
                best_player = player
                best_wallet = player.funds
        return best_player

    def clean_player_properties(self, player):
        for field in self.board.fields:
            if field.owner is player:
                field.owner = None

    def print_funds(self):
        print('------------------------')
        for player in self.players:
            print('{}: {}, {}'.format(player.style, player.funds, self.board.fields.index(player.current_field)))
        print('------------------------')

    def play_game(self):
        fin = False
        while self.round_count < 1000 and not fin:
            for player in self.players:
                dice_value = randint(1,6)
                self.board.walk_on_board(player, dice_value)
                if player.wants_to_buy():
                    player.current_field.buy(player)
                player.current_field.pay_rent(player)
                if player.funds < 0:
                    player.lost_game = True
                    self.clean_player_properties(player)
                if self.game_ended():
                    fin = True
            # uncomment to see the live game
            # print('round: {}'.format(self.round_count))
            # self.board.print()
            # self.print_funds()
            aux_players = self.players
            in_game = []
            for player in self.players:
                if not player.lost_game:
                    in_game.append(player)
            self.players = in_game
            self.round_count += 1
        
        if fin:
            return (False, self.winner.style, self.round_count)
        else:
            self.winner = self.best_player()
            return (True, self.winner.style, self.round_count)
                