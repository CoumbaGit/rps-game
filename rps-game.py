

import random


class Player:
    score = 0
# Method

    def __init__(self):
        self.my_move = None
        self.their_move = None

# remember moves
    def remember(self, my_turn, their_turn):
        self.my_turn = my_turn
        self.their_turn = their_turn


class RandomPlayer(Player):
    # chooses its moves at random
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    # ask human user what move to make
    def __init__(self):
        super().__init__()
        self.selection = 'Primary Player'

    def move(self):
        while True:
            move = input(
                'Which move do you make? Rock, Paper or Scissors? ').lower()
            if move in moves:
                return move
            else:
                print("Try again")


class ReflectPlayer(Player):
    # remembers what move the opponent played last
    # round and plays that move this round

    def move(self):
        # random play if no move made
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class EchoPlayer(Player):
    # always plays rock
    def move(self):
        return 'rock'


class CyclePlayer(Player):
    # cycles through the three moves or remember
    #what moves it played last round and cycles through
    #different moves
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            index = moves.index(self.my_move) + 1
            if index == len(moves):
                index = 0
            return moves[index]

# winning options


def player1_victory(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def player2_victory(one, two):
    return((one == 'rock' and two == 'paper') or
           (one == 'paper' and two == 'scissors') or
           (one == 'scissors' and two == 'rock')
           )


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play_round(self):
        move1 = self.player1.move()
        move2 = self.player2.move()
        print(f'player1: {move1} player2: {move2}')

        if player1_victory(move1, move2) is True and player2_victory is False:
            self.player1.score += 1
            print('You Won')
        elif player2_victory(move1, move2) is True and player1_victory(move1, move2) is False:
            self.player2.score += 1
            print('Player 2 Won!')

        else:
            print('It is a tie!')

            self.player1.remember(move1, move2)
            self.player2.remember(move1, move2)

        print('This is the score: ')
        print(f'Player1: {self.player1.score} Player2:{self.player2.score}')

    def play_game(self):
        print('Time to Play!')
        for round in range(3):
            print(f'Round {round+1}: ')
            self.play_round()
        print("Game over!")
        self.player1.score = 0
        self.player2.score = 0


if __name__ == '__main__':
    moves = ['rock', 'paper', 'scissors']
    selection = {'human': HumanPlayer(),
                 'reflect': ReflectPlayer(),
                 'random': RandomPlayer(),
                 'cycle': CyclePlayer(),
                 'echo': EchoPlayer()}


while True:
    print('Time to play Rock, Paper, Scissors!')
    print(
        'Best out of 3 rounds wins! Remember Rock smashes Scissors',
        'Paper covers Rock and Scissors cut Paper.')

    choice = input(
        'Choose your player:(random, echo, reflect, cycle) ')
    if choice in selection:
        game = Game(selection['human'], selection[choice])
        game.play_game()
    else:
        print('Incorrect player! Try again!')
