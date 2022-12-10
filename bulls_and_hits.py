import random
from functools import reduce


class BH:
    def __init__(self, number_of_digits=4,zero=True):
        self.number_of_digits = number_of_digits
        self.number_list = []
        self.start_number = None
        self.guess = 0
        self.number_hits = 0
        self.number_bulls = 0
        self.zero = zero

    def create_list(self):
        for x in range(10 ** (self.number_of_digits - 1), 10 ** self.number_of_digits):
            s1 = str(x)
            s2 = set(s1)
            if not self.zero and "0" in s1:
                continue
            else:
                if len(s1) == len(s2):
                    self.number_list.append(s1)

    def choose_random(self):
        self.start_number = random.choice(self.number_list)
        self.temp_number = self.start_number

    def find_bulls_hits(self):
        self.number_bulls = 0
        self.number_hits = 0
        for i in range(self.number_of_digits):
            c1 = self.guess[i]
            j = self.temp_number.find(c1)
            if i == j:
                self.number_bulls += 1
            else:
                if j >= 0:
                    self.number_hits += 1

    def create_guess(self):
        self.guess = random.choice(self.number_list)
        return self.guess

    def check_temp(self, temp_list):
        for self.guess in self.number_list:
            self.find_bulls_hits()
            if self.nh == self.number_hits and self.number_bulls == self.nb:
                temp_list.append(self.guess)
        return temp_list

    def reduce_table(self):
        temp_list = []
        temp_list = self.check_temp(temp_list)
        self.number_list.clear()
        self.number_list = temp_list.copy()

    def init_game(self):
        self.create_list()
        self.choose_random()


class BullsHitsDB:
    def __init__(self):
        self.number_of_games = 0
        self.games = dict()
        self.number_of_draws = 0
        self.number_of_loses = 0

    def add_game(self, number, table_size, computer_number):
        number_games = self.games[f'Game {self.number_of_games}']['Games Played']
        self.games[f'Game {self.number_of_games}']['Computers'][computer_number]['Games'][f'{number_games}'] = {
            "number": number,
            "guess": [],
            "table size": [table_size],
        }

    def add_computer(self):
        return {
            'Games': {},
            "Won": 0,
            "Lost": 0,

        }

    def create_game(self, number_of_digits,zero):
        self.games[f"Game {self.number_of_games + 1}"] = {
            "Games Played": 0,
            "Computers": [],
            "Number of Digits": number_of_digits,
            "Draws": 0,
            "Zero":zero ,
        }
        self.number_of_games += 1

    def average_calculator(self,game_number,computer_number):
        computer=self.games[f'Game {game_number+1}']['Computers'][computer_number]
        number_of_games=self.games[f'Game {game_number+1}']['Games Played']
        return round(
            reduce(lambda x, y: x + y,
            [len(computer['Games'][f'{game}']["guess"])for game in computer['Games']]) /
            number_of_games, 2)

    def get_winner_loser(self):
        temp_list = []
        number_games = self.games[f'Game {self.number_of_games}']['Games Played']
        number_computers = len(self.games[f'Game {self.number_of_games}']['Computers'])
        for computer in self.games[f'Game {self.number_of_games}']['Computers']:
            temp_list.append(len(computer['Games'][f'{number_games}'].get("guess")))
        number_of_true = [i for i in map(lambda x: x <= reduce(min, temp_list), temp_list)].count(True)
        temp_list = [i for i in enumerate([i for i in map(lambda x: x <= reduce(min, temp_list), temp_list)])]
        if number_of_true == number_computers:
            self.games[f"Game {self.number_of_games}"]["Draws"] += 1
            return "DRAW none win"
        else:
            who_won = []
            for index, winner in temp_list:
                if  winner:
                    self.games[f"Game {self.number_of_games}"]["Computers"][index]['Won'] += 1
                    who_won.append(index+1)
                else:
                    self.games[f"Game {self.number_of_games}"]["Computers"][index]['Lost'] += 1
            text = f"Computers {who_won} Won"
        return text
