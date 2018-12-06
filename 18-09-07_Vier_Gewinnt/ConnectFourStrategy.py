from sys import stdout
import random
import time
import tkinter
import sys
from PyQt5.QtWidgets import QApplication
from ConnectFourPyQt5 import App


class View:
    @staticmethod
    def prepare_field():
        raise NotImplementedError

    @staticmethod
    def set_players():
        raise NotImplementedError

    @staticmethod
    def prepare_player():
        raise NotImplementedError

    @staticmethod
    def show_field():
        raise NotImplementedError

    @staticmethod
    def make_turn():
        raise NotImplementedError

    @staticmethod
    def game_end():
        raise NotImplementedError

    @staticmethod
    def get_default_color():
        raise NotImplementedError


class Console(View):
    @staticmethod
    def prepare_field(min_size, max_size, default_size):
        __field_size = [-1, -1]
        while __field_size == [-1, -1]:
            __player_decision = input("Soll das Standardfeld verwendet werden? ").lower()
            if __player_decision == "ja" or __player_decision == "j":
                __field_size = default_size
            elif __player_decision == "nein" or __player_decision == "n":
                __field_size = [0, 0]
            else:
                print("Ungültige Eingabe. Antworten Sie mit Ja (J) oder Nein (N).")
        while __field_size[0] < min_size[0] or __field_size[0] > max_size[0]:
            try:
                __field_size[0] = int(input("Wie breit soll das Feld sein? "))
                if __field_size[0] < min_size[0]:
                    print("Das Feld ist zu schmal.")
                elif __field_size[0] > max_size[0]:
                    print("Das Feld ist zu breit.")
            except ValueError:
                print("Ungültige Eingabe. Verwenden Sie eine ganze Zahl.")
            except Exception as ex:
                print("Unerwarteter Fehler: " + ex)
        while __field_size[1] < min_size[1] or __field_size[1] > max_size[1]:
            try:
                __field_size[1] = int(input("Wie hoch soll das Feld sein? "))
                if __field_size[1] < min_size[1]:
                    print("Das Feld ist zu tief.")
                elif __field_size[1] > max_size[1]:
                    print("Das Feld ist zu hoch.")
            except ValueError:
                print("Ungültige Eingabe. Verwenden Sie eine ganze Zahl.")
            except Exception as ex:
                print("Unerwarteter Fehler: " + ex)
        return __field_size

    @staticmethod
    def set_players(players_range, default_player_amount, default_color):
        print(default_color)
        __player_amount = -1
        while __player_amount < 0:
            __player_decision = input("Sollen zwei Spieler beteiligt sein? ").lower()
            if __player_decision == "ja" or __player_decision == "j":
                __player_amount = default_player_amount
            elif __player_decision == "nein" or __player_decision == "n":
                __player_amount = 0
            else:
                print("Ungültige Eingabe. Antworten Sie mit Ja (J) oder Nein (N).")
        while __player_amount < players_range[0] or __player_amount > players_range[1]:
            try:
                __player_amount = int(input("Wie viele Spieler soll es geben? "))
                if __player_amount < players_range[0]:
                    print("Es gibt zu wenig Spieler.")
                elif __player_amount > players_range[1]:
                    print("Es gibt zu viele Spieler.")
            except ValueError:
                print("Ungültige Eingabe. Verwenden Sie eine ganze Zahl.")
            except Exception as ex:
                print("Unerwarteter Fehler: " + ex)
        return __player_amount

    @staticmethod
    def prepare_player(color_list):
        __name = ""
        __color = ""
        __color_keys = []
        __difficulty = ""
        __sorted_color_list = sorted(color_list)
        while __difficulty != "ja" and __difficulty != "j" and __difficulty != "nein" and __difficulty != "n":
            __difficulty = str(input("Künstliche Intelligenz? ")).lower()
            if __difficulty != "ja" and __difficulty != "j" and __difficulty != "nein" and __difficulty != "n":
                print("Ungültige Eingabe. Antworten Sie mit Ja (J) oder Nein (N).")
        if __difficulty == "ja" or __difficulty == "j":
            while __difficulty != "random" and __difficulty != "smart":
                __difficulty = str(input("Smart oder random? ")).lower()
                if __difficulty != "smart" and __difficulty != "random":
                    print("Ungültige Eingabe. Antworten Sie mit smart oder random.")
        else:
            __difficulty = "human"
        for key in color_list:
            __color_keys.append(key.lower())
        while len(__name) < 1 or len(__name) > 20:
            __name = str(input("Name: "))
            if len(__name) < 1:
                print("Name ist zu kurz.")
            elif len(__name) > 20:
                print("Name ist zu lang.")
        while __color not in __color_keys:
            stdout.write("Es gibt folgende Farben: ")
            for color in __sorted_color_list:
                if color != __sorted_color_list[-1]:
                    stdout.write(color + ", ")
                else:
                    stdout.write(color + "\n")
            __color = str(input("Farbe: ")).lower()
            if __color not in __color_keys:
                print("Farbe nicht vorhanden.")
        return [__name, __color, __difficulty]

    @staticmethod
    def show_field(field, field_size, player_colors, default_color):
        __player_colors = []
        for i in range(0, len(player_colors)):
            for key in player_colors.keys():
                if key not in __player_colors:
                    __player_colors.append(player_colors.get(key))
        for i in range(0, field_size[1]):
            for j in range(0, field_size[0]):
                if field[i][j] == 0:
                    stdout.write('\u25cc' + " ")
                else:
                    __counter = 1
                    for k in range(0, len(player_colors) + 1):
                        if field[i][j] == __counter:
                            stdout.write(__player_colors[k] + '\u25cb' + default_color + " ")
                        __counter += 1
            stdout.write("\n")

    @staticmethod
    def make_turn(player, field, field_size, player_colors, default_color, player_amount):
        if player.difficulty == "human":
            player_turn = True
            while player_turn:
                __column = 0
                while __column < 1 or __column > field_size[0]:
                    try:
                        __column = int(input("In welche Spalte soll der Spielstein eingeworfen werden, {}? "
                                             .format(player_colors[player.color] + player.name + default_color)))
                        if __column < 1 or __column > field_size[0]:
                            print("Ungültige Eingabe. Diese Spalte gibt es nicht.")
                    except ValueError:
                        print("Ungültige Eingabe. Verwenden Sie eine ganze Zahl.")
                    except Exception as ex:
                        print("Unerwarteter Fehler: " + ex)
                for i in range(0, field_size[0]):
                    if field[field_size[1] - i - 1][__column - 1] == 0:
                        field[field_size[1] - i - 1][__column - 1] = player.turn
                        player_turn = False
                        break
                    elif i == field_size[0] - 1:
                        print("Die Spalte ist voll.")
        elif player.difficulty == "random":
            #time.sleep(1)
            player_turn = True
            while player_turn:
                __column = 0
                while __column < 1 or __column > field_size[0]:
                    __column = random.randint(1, field_size[0])
                    for i in range(0, field_size[0]):
                        if field[field_size[1] - i - 1][__column - 1] == 0:
                            field[field_size[1] - i - 1][__column - 1] = player.turn
                            player_turn = False
                            print("{} wirft in Spalte {}.".format(player_colors[player.color] + player.name +
                                                                  default_color, __column))
                            break
        else:  # Player difficulty equals smart
            #time.sleep(1)
            #KI should not start first
            player_turn = True
            while player_turn:
                __column = 0
                __risk_field = []
                while __column < 1 or __column > field_size[0]:
                    for height in range(0, len(field)):
                        for length in range(0, len(field[0])):
                            for token in range(1, player_amount + 1):
                                if height < (len(field) - 3):
                                    try:
                                        if field[height + 3][length] == token and field[height + 2][length] == token and field[height + 1][length] == token and field[height][length] == 0:  # check height
                                            __column = length + 1
                                            print("A")
                                            print(__column)
                                    except IndexError:
                                        print("IE")
                                    try:
                                        if field[height + 3][length] == 0 and field[height + 2][length] == token and field[height + 1][length] == token and field[height][length] == token:  # check height nonsense
                                            __column = length - 3
                                            print("B")
                                            print(__column)
                                    except IndexError:
                                        print("IE")
                                if length < (len(field[0]) - 3):
                                    try:
                                        if field[height][length] == token and field[height][length + 1] == token and field[height][length + 2] == token and field[height][length + 3] == 0:  # check length
                                            if height != len(field) - 1:
                                                if field[height + 1][length + 3] != 0:
                                                    __column = length + 4
                                                    print("C")
                                                    print(__column)
                                                elif field[height + 2][length + 3] != 0:
                                                    __risk_field.append(length + 4)
                                                    print("C+")
                                            else:
                                                __column = length + 4
                                                print("C-")
                                    except IndexError:
                                        print("IE")
                                    try:
                                        if field[height][length] == 0 and field[height][length + 1] == token and field[height][length + 2] == token and field[height][length + 3] == token:  # check length
                                            if height != len(field) - 1:
                                                if field[height + 1][length] != 0:
                                                    __column = length + 1
                                                    print("D")
                                                    print(__column)
                                                elif field[height + 2][length] != 0:
                                                    __risk_field.append(length + 1)
                                                    print("D+")
                                            else:
                                                __column = length + 1
                                                print("D-")
                                    except IndexError:
                                        print("IE")
                                    try:
                                        if field[height][length] == token and field[height][length + 1] == 0 and field[height][length + 2] == token and field[height][length + 3] == token:  # check length
                                            if height != len(field) - 1:
                                                if field[height + 1][length + 1] != 0:
                                                    __column = length + 2
                                                    print("Z")
                                                    print(__column)
                                                elif field[height + 2][length + 1] != 0:
                                                    __risk_field.append(length + 2)
                                                    print("Z+")
                                            else:
                                                __column = length + 2
                                                print("Z-")
                                    except IndexError:
                                        print("IE")
                                    try:
                                        if field[height][length] == token and field[height][length + 1] == token and field[height][length + 2] == 0 and field[height][length + 3] == token:  # check length
                                            if height != len(field) - 1:
                                                if field[height + 1][length + 2] != 0:
                                                    __column = length + 3
                                                    print("Y")
                                                    print(__column)
                                                elif field[height + 2][length + 2] != 0:
                                                    __risk_field.append(length + 3)
                                                    print("Y+")
                                            else:
                                                __column = length + 3
                                                print("Y-")
                                    except IndexError:
                                        print("IE")
                                if length < (len(field[0]) - 3) and height < (len(field) - 3):
                                    try:
                                        if field[height][length] == token and field[height + 1][length + 1] == token and field[height + 2][length + 2] == token and field[height + 3][length + 3] == 0:  # check diagonal
                                            if field[height + 4][length + 3] != 0:
                                                __column = length + 4
                                                print("E")
                                                print(__column)
                                            elif field[height + 5][length + 3] != 0:
                                                __risk_field.append(length + 4)
                                                print("E+")
                                    except IndexError:
                                        print("IE")
                                    try:
                                        if field[height][length] == 0 and field[height + 1][length + 1] == token and field[height + 2][length + 2] == token and field[height + 3][length + 3] == token:  # check diagonal
                                            if field[height + 1][length] != 0:
                                                __column = length + 1
                                                print("F")
                                                print(__column)
                                            elif field[height + 2][length] != 0:
                                                __risk_field.append(length + 1)
                                                print("F+")
                                    except IndexError:
                                        print("IE")
                                    try:
                                        if field[height][length] == token and field[height + 1][length + 1] == 0 and field[height + 2][length + 2] == token and field[height + 3][length + 3] == token:  # check diagonal
                                            if field[height + 2][length + 1] != 0:
                                                __column = length + 2
                                                print("G")
                                                print(__column)
                                            elif field[height + 3][length + 1] != 0:
                                                __risk_field.append(length + 2)
                                                print("G+")
                                    except IndexError:
                                        print("IE")
                                    try:
                                        if field[height][length] == token and field[height + 1][length + 1] == token and field[height + 2][length + 2] == 0 and field[height + 3][length + 3] == token:  # check diagonal
                                            if field[height + 3][length + 2] != 0:
                                                __column = length + 3
                                                print("H")
                                                print(__column)
                                            elif field[height + 4][length + 2] != 0:
                                                __risk_field.append(length + 3)
                                                print("H+")
                                    except IndexError:
                                        print("IE")
                                if length > 2 and height < (len(field) - 3):
                                    try:
                                        if field[height][length] == token and field[height + 1][length - 1] == token and field[height + 2][length - 2] == token and field[height + 3][length - 3] == 0:  # check diagonal
                                            if field[height + 4][length - 3] != 0:
                                                __column = length - 2
                                                print("I")
                                                print(__column)
                                            elif field[height + 5][length - 3] != 0:
                                                __risk_field.append(length - 2)
                                                print("I+")
                                    except IndexError:
                                        print("IE")
                                    try:
                                        if field[height][length] == 0 and field[height + 1][length - 1] == token and field[height + 2][length - 2] == token and field[height + 3][length - 3] == token:  # check diagonal
                                            if field[height + 1][length] != 0:
                                                __column = length + 1
                                                print("J")
                                                print(__column)
                                            elif field[height + 2][length] != 0:
                                                __risk_field.append(length + 1)
                                                print("J+")
                                    except IndexError:
                                        print("IE")
                                    try:
                                        if field[height][length] == token and field[height + 1][length - 1] == 0 and field[height + 2][length - 2] == token and field[height + 3][length - 3] == token:  # check diagonal
                                            if field[height + 2][length - 1] != 0:
                                                __column = length
                                                print("K")
                                                print(__column)
                                            elif field[height + 3][length - 1] != 0:
                                                __risk_field.append(length)
                                                print("K+")
                                    except IndexError:
                                        print("IE")
                                    try:
                                        if field[height][length] == token and field[height + 1][length - 1] == token and field[height + 2][length - 2] == 0 and field[height + 3][length - 3] == token:  # check diagonal
                                            if field[height + 3][length - 2] != 0:
                                                __column = length - 1
                                                print("L")
                                                print(__column)
                                            elif field[height + 4][length - 2] != 0:
                                                __risk_field.append(length - 1)
                                                print("L+")
                                    except IndexError:
                                        print("IE")
                    print(__risk_field)
                    if __column == 0:
                        __column = random.randint(1, field_size[0])
                        i = 0
                        while __risk_field.__contains__(__column):  # do 100 times?!
                            __column = random.randint(1, field_size[0])
                            i += 1
                            if i > 90:
                                for i in range(0, field_size[0]):
                                    if field[i][0] == 0:
                                        __column = i + 1
                                break
                    for i in range(0, field_size[0]):
                        if field[field_size[1] - i - 1][__column - 1] == 0:
                            field[field_size[1] - i - 1][__column - 1] = player.turn
                            player_turn = False
                            print("{} wirft in Spalte {}.".format(player_colors[player.color] + player.name +
                                                                  default_color, __column))
                            break
        return field

    @staticmethod
    def game_end(game_result, player_list, player_colors, default_color):
        if game_result != "draw":
            print("{} hat gewonnen!".format(player_colors[player_list[game_result - 1].color] +
                                            player_list[game_result - 1].name + default_color))
        else:
            print("Unentschieden!")
        __repeat = ""
        for player in player_list:
            print("{}: {}".format(player_colors[player.color] + player.name + default_color, player.score))
        while __repeat != "ja" and __repeat != "j" and __repeat != "nein" and __repeat != "n":
            __repeat = input("Nochmal? ").lower()
            if __repeat != "ja" and __repeat != "j" and __repeat != "nein" and __repeat != "n":
                print("Ungültige Eingabe. Antworten Sie mit Ja (J) oder Nein (N).")
        return True if __repeat == "ja" or __repeat == "j" else False

    @staticmethod
    def get_default_color():
        return '\033[3;33;39m'


class Tkinter(View):
    def __init__(self):
        self.root = tkinter.Tk()  # start
        self.root.title("Connect Four")
        btn = tkinter.Button(self.root, text="next")
        btn.pack()

    @staticmethod
    def prepare_field():
        pass

    def set_players(self, players_range, default_player_amount, default_color):
        #self.root.resizable(width=False, height=False)
        #img = tkinter.Image("photo", file="ball.gif")
        #self.root.tk.call('wm', 'iconphoto', self.root._w, img)
        #btn_start = tkinter.Button(self.root)
        #btn_start(row=1, column=1)
        #btn_start.pack()
        #btn_start.configure(command=lambda btn_start=btn_start: self.btn_start_click(btn_start))
        #btn_start = tkinter.Button(self.root, text="Start")
        #btn_start.pack()
        self.root.mainloop()  # end
        #btn_start.grid(row=1, column=1)
        #  print(default_color)
        __player_amount = -1
        while __player_amount < 0:
            __player_decision = input("Sollen zwei Spieler beteiligt sein? ").lower()
            if __player_decision == "ja" or __player_decision == "j":
                __player_amount = default_player_amount
            elif __player_decision == "nein" or __player_decision == "n":
                __player_amount = 0
            else:
                print("Ungültige Eingabe. Antworten Sie mit Ja (J) oder Nein (N).")
        while __player_amount < players_range[0] or __player_amount > players_range[1]:
            try:
                __player_amount = int(input("Wie viele Spieler soll es geben? "))
                if __player_amount < players_range[0]:
                    print("Es gibt zu wenig Spieler.")
                elif __player_amount > players_range[1]:
                    print("Es gibt zu viele Spieler.")
            except ValueError:
                print("Ungültige Eingabe. Verwenden Sie eine ganze Zahl.")
            except Exception as ex:
                print("Unerwarteter Fehler: " + ex)
        return __player_amount

    @staticmethod
    def prepare_player():
        pass

    @staticmethod
    def show_field():
        pass

    @staticmethod
    def make_turn():
        pass

    @staticmethod
    def game_end():
        pass

    @staticmethod
    def get_default_color():
        pass


class PyQt5(View):
    @staticmethod
    def prepare_field():
        pass

    @staticmethod
    def set_players(players_range, default_player_amount, default_color):
        app = QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec_())

    @staticmethod
    def prepare_player():
        pass

    @staticmethod
    def show_field():
        pass

    @staticmethod
    def make_turn():
        pass

    @staticmethod
    def game_end():
        pass

    @staticmethod
    def get_default_color():
        pass


class PGZero(View):
    @staticmethod
    def prepare_field():
        pass

    @staticmethod
    def set_players():
        pass

    @staticmethod
    def prepare_player():
        pass

    @staticmethod
    def show_field():
        pass

    @staticmethod
    def make_turn():
        pass

    @staticmethod
    def game_end():
        pass

    @staticmethod
    def get_default_color():
        pass
