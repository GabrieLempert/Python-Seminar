import random
from functools import reduce


class BH:
    def __init__(self, number_of_digits=4):
        self.number_of_digits = number_of_digits
        self.number_list = []
        self.start_number = None
        self.guess = 0
        self.number_hits = 0
        self.number_bulls = 0

    def create_list(self):
        for x in range(10 ** (self.number_of_digits - 1), 10 ** self.number_of_digits):
            s1 = str(x)
            s2 = set(s1)
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
    def __init__(self, player):
        self.number_of_games = 0
        self.player = f"Computer {player}"
        self.number_of_wins = 0
        self.games = dict()
        self.number_of_draws = 0

    def add_game(self, number, table_size):
        self.games[f"Game {self.number_of_games + 1}"] = {
            "number": number,
            "guess": [],
            "table size": [table_size]
        }
        self.number_of_games += 1

    def average_calculator(self):
        return round(reduce(lambda x, y: x + y, [len(self.games[game]["guess"]) for game in self.games]) / \
               self.number_of_games,2)
