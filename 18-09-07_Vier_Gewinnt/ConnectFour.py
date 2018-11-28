import ConnectFourStrategy
import numpy


class Controller:
    def __init__(self, strategy):
        self.__view = strategy
        self.__players_range = [2, 7]
        self.__player_amount = 2
        self.__player_list = []
        self.__default_player_amount = 2
        self.__color_list = {"rot": "\033[1;38;31m", "blau": "\033[1;38;34m", "grün": "\033[1;38;32m",
                             "gelb": "\033[1;38;33m", "lila": "\033[1;38;35m",  "türkis": "\033[1;38;36m",
                             "weiß": "\033[1;30;29m"}
        self.__player_colors = {}
        self.__playing = True

    def start(self):
        field = Field()
        self.player_amount = self.view.set_players(self.players_range, self.default_player_amount, field.default_color)
        self.create_players()
        self.prepare_player()
        while self.playing:
            field.prepare_field()
            __game_result = self.player_turn(field, self.player_amount)
            self.playing = self.game_end(__game_result, field.default_color)

    def create_players(self):
        for player in range(0, self.player_amount):
            self.player_list.append(Player())

    def prepare_player(self):
        __counter = 0
        for player in self.player_list:
            __color = player.prepare_player(__counter + 1, self.color_list)
            self.player_colors.update({__color: self.color_list.get(__color)})
            del self.color_list[__color]
            __counter += 1

    def player_turn(self, field_instance, player_amount):
        field_instance.show_field(self.player_colors)
        __game_running = True
        __game_state = "running"
        while __game_running:
            for player in self.player_list:
                field_instance.field = player.make_turn(field_instance.field, field_instance.field_size,
                                                        self.player_colors, field_instance.default_color, player_amount)
                field_instance.show_field(self.player_colors)
                __game_state = self.check_field(field_instance.field, self.player_amount)
                if __game_state != "running":
                    __game_running = False
                    break
        return __game_state

    @staticmethod
    def check_field(field, player_amount):
        __result = "running"
        for height in range(0, len(field)):
            for length in range(0, len(field[0])):
                for player in range(1, player_amount + 1):
                    if all(all(x != 0 for x in v) for v in field):  # check for draw
                        __result = "draw"
                    if height < (len(field) - 3):
                        if field[height][length] == player and field[height+1][length] == player and field[height+2][length] == player and field[height+3][length] == player:  # check height
                            __result = player
                    if length < (len(field[0]) - 3):
                        if field[height][length] == player and field[height][length+1] == player and field[height][length+2] == player and field[height][length+3] == player:  # check length
                            __result = player
                    if length < (len(field[0]) - 3) and height < (len(field) - 3):
                        if field[height][length] == player and field[height+1][length+1] == player and field[height+2][length+2] == player and field[height+3][length+3] == player:  # check diagonal
                            __result = player
                    if length < (len(field[0]) + 3) and height < (len(field) - 3):
                        if field[height][length] == player and field[height+1][length-1] == player and field[height+2][length-2] == player and field[height+3][length-3] == player:  # check diagonal
                            __result = player
        return __result

    def game_end(self, game_result, default_color):
        if game_result != "draw":
            self.player_list[game_result - 1].score += 1
        return self.view.game_end(game_result, self.player_list, self.player_colors, default_color)

    @property  # makes method accessible like an attribute
    def view(self):
        return self.__view

    @view.setter
    def view(self, view):
        self.__view = view

    @property  # makes method accessible like an attribute
    def players_range(self):
        return self.__players_range

    @players_range.setter
    def players_range(self, players_range):
        self.__players_range = players_range

    @property  # makes method accessible like an attribute
    def player_amount(self):
        return self.__player_amount

    @player_amount.setter
    def player_amount(self, player_amount):
        self.__player_amount = player_amount

    @property  # makes method accessible like an attribute
    def player_list(self):
        return self.__player_list

    @player_list.setter
    def player_list(self, player_list):
        self.__player_list = player_list

    @property  # makes method accessible like an attribute
    def default_player_amount(self):
        return self.__default_player_amount

    @default_player_amount.setter
    def default_player_amount(self, default_player_amount):
        self.__default_player_amount = default_player_amount

    @property  # makes method accessible like an attribute
    def color_list(self):
        return self.__color_list

    @color_list.setter
    def color_list(self, color_list):
        self.__color_list = color_list

    @property  # makes method accessible like an attribute
    def color_list(self):
        return self.__color_list

    @color_list.setter
    def color_list(self, color_list):
        self.__color_list = color_list

    @property  # makes method accessible like an attribute
    def player_colors(self):
        return self.__player_colors

    @player_colors.setter
    def player_colors(self, player_colors):
        self.__player_colors = player_colors

    @property  # makes method accessible like an attribute
    def playing(self):
        return self.__playing

    @playing.setter
    def playing(self, playing):
        self.__playing = playing


class Field(Controller):
    def __init__(self):
        super().__init__(gui)
        self.__min_length = 4
        self.__max_length = 20
        self.__min_height = 4
        self.__max_height = 20
        self.__default_length = 7
        self.__default_height = 6
        self.__field_size = [7, 6]
        self.__field = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.__min_size = [self.__min_length, self.__min_height]
        self.__max_size = [self.__max_length, self.__max_height]
        self.__default_size = [self.__default_length, self.__default_height]
        self.__default_color = '\033[3;33;39m'

    def prepare_field(self):
        self.field_size = self.view.prepare_field(self.min_size, self.max_size, self.default_size)
        self.field = [[0 for x in range(self.field_size[0])] for y in range(self.field_size[1])]

    def show_field(self, player_colors):
        self.view.show_field(self.field, self.field_size, player_colors, self.default_color)

    @property  # makes method accessible like an attribute
    def field(self):
        return self.__field

    @field.setter
    def field(self, field):
        self.__field = field

    @property  # makes method accessible like an attribute
    def field_size(self):
        return self.__field_size

    @field_size.setter
    def field_size(self, field_size):
        self.__field_size = field_size

    @property  # makes method accessible like an attribute
    def default_color(self):
        return self.view.get_default_color()

    @default_color.setter
    def default_color(self, default_color):
        self.__default_color = default_color

    @property  # makes method accessible like an attribute
    def min_length(self):
        return self.__min_length

    @min_length.setter
    def min_length(self, min_length):
        self.__min_length = min_length

    @property  # makes method accessible like an attribute
    def max_length(self):
        return self.__max_length

    @max_length.setter
    def max_length(self, max_length):
        self.__max_length = max_length

    @property  # makes method accessible like an attribute
    def min_height(self):
        return self.__min_height

    @min_height.setter
    def min_height(self, min_height):
        self.__min_height = min_height

    @property  # makes method accessible like an attribute
    def max_height(self):
        return self.__max_height

    @max_height.setter
    def max_height(self, max_height):
        self.__max_height = max_height

    @property  # makes method accessible like an attribute
    def default_length(self):
        return self.__default_length

    @default_length.setter
    def default_length(self, default_length):
        self.__default_length = default_length

    @property  # makes method accessible like an attribute
    def default_height(self):
        return self.__default_height

    @default_height.setter
    def default_height(self, default_height):
        self.__default_height = default_height

    @property  # makes method accessible like an attribute
    def default_size(self):
        return self.__default_size

    @default_size.setter
    def default_size(self, default_size):
        self.__default_size = default_size

    @property  # makes method accessible like an attribute
    def min_size(self):
        return self.__min_size

    @min_size.setter
    def min_size(self, min_size):
        self.__min_size = min_size

    @property  # makes method accessible like an attribute
    def max_size(self):
        return self.__max_size

    @max_size.setter
    def max_size(self, max_size):
        self.__max_size = max_size


class Player(Controller):
    def __init__(self):
        super().__init__(gui)
        self.__turn = 1
        self.__name = "Player 1"
        self.__color = "green"
        self.__score = 0
        self.__difficulty = "human"

    def prepare_player(self, turn, color_list):
        self.turn = turn
        __player_information = self.view.prepare_player(color_list)
        self.name = __player_information[0]
        self.color = __player_information[1]
        self.__difficulty = __player_information[2]
        return self.color

    def make_turn(self, field, field_size, player_colors, default_color, player_amount):
        return self.view.make_turn(self, field, field_size, player_colors, default_color, player_amount)

    @property  # makes method accessible like an attribute
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property  # makes method accessible like an attribute
    def turn(self):
        return self.__turn

    @turn.setter
    def turn(self, turn):
        self.__turn = turn

    @property  # makes method accessible like an attribute
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    @property  # makes method accessible like an attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property  # makes method accessible like an attribute
    def difficulty(self):
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        self.__difficulty = difficulty


gui = ConnectFourStrategy.Console()
#  gui = ConnectFourStrategy.Tkinter()
#  gui = ConnectFourStrategy.PyQt5()
#  gui = ConnectFourStrategy.PGZero()
game = Controller(gui)
game.start()
