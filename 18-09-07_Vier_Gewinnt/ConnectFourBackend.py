import tkinter
from sys import stdout, stderr
import ConnectFourFrontendStrategy
from abc import ABC


class Controller:
    def __init__(self):
        #self.__frontend_strategy = ConnectFourFrontendStrategy
        self.__view = ConnectFourFrontendStrategy.ShowConsoleStrategy()
        #self.__view = ConnectFourFrontendStrategy.ShowWindowStrategy()
        #self.__frontend = self.__view  # Use chosen view

    def start(self):
        field1 = Field()
        player1 = Player()
        field1.set_size()
        field1.set_field()
        field1.create_field()
        #player1.player_move(field)

    @property  # makes method accessible like an attribute
    def view(self):
        return self.__view

    @view.setter
    def view(self, view):
        self.__view = view


class Field(Controller):
    def __init__(self):
        super().__init__()
        self.__min_size = 4
        self.__max_size = 10
        self.__default_length = 7
        self.__default_height = 6

    def set_size(self):
        self.field_size = self.view.get_size(self.min_size, self.max_size, self.default_length, self.default_height)
        print(self.field_size)  # temp

    def set_field(self):
        self.field = [[0 for i in range(self.field_size[0])] for j in range(self.field_size[1])]  # set 0 filled 2D Field (better?)
        print(self.field)  # temp

    def create_field(self):
        self.view.create_field(self.field)

    def check_move(self, column, row, field):
        pass

    def move(self, column, player_turn):
        pass

    def check_round(self, field):
        pass

    def end(self):
        pass

    @property  # makes method accessible like an attribute
    def field(self):
        return self.__field

    @field.setter
    def field(self, field):
        self.__field = field

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

    @property  # makes method accessible like an attribute
    def field_size(self):
        return self.__field_size

    @field_size.setter
    def field_size(self, field_size):
        self.__field_size = field_size


class Player(Controller):
    def player_move(self):
        self.view.player_move()


controller1 = Controller()
controller1.start()

# -------------------------------------------------------------------------------------------------------------------- #


class ConnectFourWindow:
    def __init__(self, **additional_parameters):

        self.root = tkinter.Tk()
        self.root.title("Connect Four")

        if 'field_length' in additional_parameters:
            self.__field_length = additional_parameters['field_length']
        else:
            self.__field_length = 7

        if 'field_height' in additional_parameters:
            self.__field_height = additional_parameters['field_height']
        else:
            self.__field_height = 6

        self.__field = [[0 for x in range(self.__field_length)] for y in range(self.__field_height)]

        self.__player_turn = 1

        self.draw_playing_field()

    def click(self, x_pos, y_pos):
        print("Button " + str(x_pos) + " " + str(y_pos) + " clicked!")
        if self.__player_turn is 1:
            self.__player_turn = 2
        else:
            self.__player_turn = 1
        self.draw_playing_field()

    def create_playing_field(self, length, height):
        for i in range(0, length):
            for j in range(0, height):
                self.__field[i][j] = 0

    def draw_playing_field(self):
        btn_start = tkinter.Button(self.root, text="Start")
        #btn_start.pack()

        btn_end = tkinter.Button(self.root, text="End")
        #btn_end.pack()

        btn_start.grid(row=1, column=1)
        btn_end.grid(row=1, column=3)

        self.img_ball = tkinter.PhotoImage(file="ball.gif")  # Only GIF or PGM/PPM
        lbl_ball = tkinter.Label(self.root, image=self.img_ball)
        #lbl_ball.pack()
        lbl_ball.grid(row=1, column=2)

        for i in range(0, 6):
            for j in range(0, 7):
                stdout.write(str(self.__field[i][j]))
            stdout.write("\n")

        self.circle = tkinter.PhotoImage(file="circle.gif")  # Only GIF or PGM/PPM
        self.circle_yellow = tkinter.PhotoImage(file="circle_yellow.gif")  # Only GIF or PGM/PPM
        self.circle_green = tkinter.PhotoImage(file="circle_green.gif")  # Only GIF or PGM/PPM

        row = 3
        for i in range(0, 6):
            column = 1
            for j in range(0, 7):
                if self.__field[i][j] is 0:
                    self.__field[i][j] = self.__player_turn
                    btn_circle = tkinter.Button(self.root, image=self.circle, command=lambda x_pos = j, y_pos = i : self.click(x_pos, y_pos))
                elif self.__field[i][j] is 1:
                    self.__field[i][j] = self.__player_turn
                    btn_circle = tkinter.Button(self.root, image=self.circle_yellow, command=lambda x_pos = j, y_pos = i : self.click(x_pos, y_pos))
                    self.__field[i][j] = self.__player_turn
                else:
                    self.__field[i][j] = self.__player_turn
                    btn_circle = tkinter.Button(self.root, image=self.circle_green, command=lambda x_pos = j, y_pos = i : self.click(x_pos, y_pos))

                btn_circle.grid(row=row, column=column)
                column += 1
            row += 1

    def run(self):
        self.root.mainloop()
