# Program start
# --------------------------------------------------------------------------------------------------
# Imports
import sys
# from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from functools import *
# import numpy as np
# --------------------------------------------------------------------------------------------------
#                                       Class CController start
# --------------------------------------------------------------------------------------------------


class CController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tic Tac Toe')
        self.setFixedSize(300, 300)
        self.__center()
        self.setWindowIcon(QIcon('tic_tac_toe_icon.png'))
        self.__init_user_interface()

    def __init_user_interface(self):
        self.__field = CField()
        self.__create_field(self.field.field)
        self.__get_enemy()
        self.show()

    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def __create_field(self, field):
        self.__buttons = []
        __counter = 0
        for i in range(0, len(field[1])):
            for j in range(0, len(field)):
                self.__buttons.append(QPushButton(self))
                self.__buttons[__counter].setIcon(QIcon())
                self.__buttons[__counter].resize(100, 100)
                self.__buttons[__counter].move(100 * i, 100 * j)
                self.__buttons[__counter].setText("  ")
                self.__buttons[__counter].clicked.connect(self.__set_token)
                self.__buttons[__counter].setVisible(False)
                self.__buttons[__counter].setIconSize(QSize(100, 100))
                __counter += 1

    def __set_token(self):
        button = self.sender()
        if button.text() == "  ":
            if self.__field.player:
                button.setIcon(QIcon('tic_tac_toe_x.png'))
                button.setText("")
            else:
                button.setIcon(QIcon('tic_tac_toe_o.png'))
                button.setText(" ")
            self.__field.swap_player()
            if self.field.check_field(self.__buttons):
                self.__reset()
            else:
                self.__enemy_turn()
                if self.field.check_field(self.__buttons):
                    self.__reset()

    def __reset(self):
        QMessageBox.about(self, "Game result", self.field.get_game_result())
        for button in self.__buttons:
            button.setText("  ")
            button.setIcon(QIcon(None))
        self.__enemy_turn()

    def __get_enemy(self):
        self.__btn_human = QPushButton(self)
        self.__btn_human.move(50, 100)
        self.__btn_human.resize(100, 100)
        self.__btn_human.setIcon(QIcon('tic_tac_toe_human.png'))
        self.__btn_human.setIconSize(QSize(100, 100))
        self.__btn_human.clicked.connect(lambda: self.__set_enemy("human"))
        self.__btn_computer = QPushButton(self)
        self.__btn_computer.move(150, 100)
        self.__btn_computer.resize(100, 100)
        self.__btn_computer.setIcon(QIcon('tic_tac_toe_computer.png'))
        self.__btn_computer.setIconSize(QSize(100, 100))
        self.__btn_computer.clicked.connect(lambda: self.__set_enemy("computer"))

    def __set_enemy(self, enemy):
        self.__btn_human.deleteLater()
        self.__btn_computer.deleteLater()
        self.__field.enemy = enemy
        self.__start()

    def __start(self):
        for button in self.__buttons:
            button.setVisible(True)

    def __enemy_turn(self):
        if self.__field.enemy == "computer" and self.__field.player is False:
            text = " "
            set_text = " "
            check = True
            counter = 0
            while check:
                if counter == 1:
                    text = ""
            #  vertical
                if self.__buttons[0].text() == text and self.__buttons[1].text() == text and self.__buttons[2].text() == "  ":
                    self.__buttons[2].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[2].setText(set_text)
                    break
                elif self.__buttons[0].text() == text and self.__buttons[2].text() == text and self.__buttons[1].text() == "  ":
                    self.__buttons[1].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[1].setText(set_text)
                    break
                elif self.__buttons[1].text() == text and self.__buttons[2].text() == text and self.__buttons[0].text() == "  ":
                    self.__buttons[0].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[0].setText(set_text)
                    break
                elif self.__buttons[3].text() == text and self.__buttons[4].text() == text and self.__buttons[5].text() == "  ":
                    self.__buttons[5].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[5].setText(set_text)
                    break
                elif self.__buttons[3].text() == text and self.__buttons[5].text() == text and self.__buttons[4].text() == "  ":
                    self.__buttons[4].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[4].setText(set_text)
                    break
                elif self.__buttons[4].text() == text and self.__buttons[5].text() == text and self.__buttons[3].text() == "  ":
                    self.__buttons[3].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[3].setText(set_text)
                    break
                elif self.__buttons[6].text() == text and self.__buttons[7].text() == text and self.__buttons[8].text() == "  ":
                    self.__buttons[8].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[8].setText(set_text)
                    break
                elif self.__buttons[6].text() == text and self.__buttons[8].text() == text and self.__buttons[7].text() == "  ":
                    self.__buttons[7].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[7].setText(set_text)
                    break
                elif self.__buttons[7].text() == text and self.__buttons[8].text() == text and self.__buttons[6].text() == "  ":
                    self.__buttons[6].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[6].setText(set_text)
                    break
                #  horizontal
                elif self.__buttons[0].text() == text and self.__buttons[3].text() == text and self.__buttons[6].text() == "  ":
                    self.__buttons[6].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[6].setText(set_text)
                    break
                elif self.__buttons[0].text() == text and self.__buttons[6].text() == text and self.__buttons[3].text() == "  ":
                    self.__buttons[3].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[3].setText(set_text)
                    break
                elif self.__buttons[3].text() == text and self.__buttons[6].text() == text and self.__buttons[0].text() == "  ":
                    self.__buttons[0].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[0].setText(set_text)
                    break
                elif self.__buttons[1].text() == text and self.__buttons[4].text() == text and self.__buttons[7].text() == "  ":
                    self.__buttons[7].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[7].setText(set_text)
                    break
                elif self.__buttons[1].text() == text and self.__buttons[7].text() == text and self.__buttons[4].text() == "  ":
                    self.__buttons[4].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[4].setText(set_text)
                    break
                elif self.__buttons[4].text() == text and self.__buttons[7].text() == text and self.__buttons[1].text() == "  ":
                    self.__buttons[1].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[1].setText(set_text)
                    break
                elif self.__buttons[2].text() == text and self.__buttons[5].text() == text and self.__buttons[8].text() == "  ":
                    self.__buttons[8].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[8].setText(set_text)
                    break
                elif self.__buttons[2].text() == text and self.__buttons[8].text() == text and self.__buttons[5].text() == "  ":
                    self.__buttons[5].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[5].setText(set_text)
                    break
                elif self.__buttons[5].text() == text and self.__buttons[8].text() == text and self.__buttons[2].text() == "  ":
                    self.__buttons[2].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[2].setText(set_text)
                    break
                #  diagonal
                elif self.__buttons[0].text() == text and self.__buttons[4].text() == text and self.__buttons[8].text() == "  ":
                    self.__buttons[8].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[8].setText(set_text)
                    break
                elif self.__buttons[0].text() == text and self.__buttons[8].text() == text and self.__buttons[4].text() == "  ":
                    self.__buttons[4].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[4].setText(set_text)
                    break
                elif self.__buttons[4].text() == text and self.__buttons[8].text() == text and self.__buttons[0].text() == "  ":
                    self.__buttons[0].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[0].setText(set_text)
                    break
                elif self.__buttons[2].text() == text and self.__buttons[4].text() == text and self.__buttons[6].text() == "  ":
                    self.__buttons[6].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[6].setText(set_text)
                    break
                elif self.__buttons[2].text() == text and self.__buttons[6].text() == text and self.__buttons[4].text() == "  ":
                    self.__buttons[4].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[4].setText(set_text)
                    break
                elif self.__buttons[4].text() == text and self.__buttons[6].text() == text and self.__buttons[2].text() == "  ":
                    self.__buttons[2].setIcon(QIcon('tic_tac_toe_o.png'))
                    self.__buttons[2].setText(set_text)
                    break
                else:
                    counter += 1
                if counter == 2:
                    #  dilemma
                    if self.__buttons[4].text() == "" and self.__buttons[8].text() == "" and self.__buttons[2].text() == "  ":
                        self.__buttons[2].setIcon(QIcon('tic_tac_toe_o.png'))
                        self.__buttons[2].setText(set_text)
                        break
                    elif self.__buttons[4].text() == set_text and self.__buttons[0].text() == "" and self.__buttons[8].text() == "  ":
                        self.__buttons[8].setIcon(QIcon('tic_tac_toe_o.png'))
                        self.__buttons[8].setText(set_text)
                        break
                    elif self.__buttons[4].text() == set_text and self.__buttons[6].text() == "" and self.__buttons[2].text() == "  ":
                        self.__buttons[2].setIcon(QIcon('tic_tac_toe_o.png'))
                        self.__buttons[2].setText(set_text)
                        break
                    elif self.__buttons[4].text() == set_text and self.__buttons[2].text() == "" and self.__buttons[6].text() == "  ":
                        self.__buttons[6].setIcon(QIcon('tic_tac_toe_o.png'))
                        self.__buttons[6].setText(set_text)
                        break
                    elif self.__buttons[4].text() == set_text and self.__buttons[8].text() == "" and self.__buttons[0].text() == "  ":
                        self.__buttons[0].setIcon(QIcon('tic_tac_toe_o.png'))
                        self.__buttons[0].setText(set_text)
                        break
                    elif self.__buttons[4].text() == set_text and self.__buttons[8].text() == set_text and self.__buttons[6].text() == "  " and self.__buttons[7].text() == "  ":
                        self.__buttons[6].setIcon(QIcon('tic_tac_toe_o.png'))
                        self.__buttons[6].setText(set_text)
                        break
                    elif self.__buttons[4].text() == set_text and self.__buttons[8].text() == set_text and self.__buttons[2].text() == "  " and self.__buttons[5].text() == "  ":
                        self.__buttons[2].setIcon(QIcon('tic_tac_toe_o.png'))
                        self.__buttons[2].setText(set_text)
                        break
                    elif self.__buttons[4].text() == set_text and self.__buttons[2].text() == set_text and self.__buttons[5].text() == "  " and self.__buttons[8].text() == "  ":
                        self.__buttons[5].setIcon(QIcon('tic_tac_toe_o.png'))
                        self.__buttons[5].setText(set_text)
                        break
                    elif self.__buttons[4].text() == set_text and self.__buttons[2].text() == set_text and self.__buttons[0].text() == "  " and self.__buttons[1].text() == "  ":
                        self.__buttons[1].setIcon(QIcon('tic_tac_toe_o.png'))
                        self.__buttons[1].setText(set_text)
                        break
                    elif self.__buttons[4].text() == set_text and self.__buttons[0].text() == set_text and self.__buttons[1].text() == "  " and self.__buttons[2].text() == "  ":
                        self.__buttons[1].setIcon(QIcon('tic_tac_toe_o.png'))
                        self.__buttons[1].setText(set_text)
                        break
                    elif self.__buttons[4].text() == set_text and self.__buttons[0].text() == set_text and self.__buttons[3].text() == "  " and self.__buttons[6].text() == "  ":
                        self.__buttons[3].setIcon(QIcon('tic_tac_toe_o.png'))
                        self.__buttons[3].setText(set_text)
                        break
                    elif self.__buttons[4].text() == set_text and self.__buttons[6].text() == set_text and self.__buttons[0].text() == "  " and self.__buttons[3].text() == "  ":
                        self.__buttons[3].setIcon(QIcon('tic_tac_toe_o.png'))
                        self.__buttons[3].setText(set_text)
                        break
                    elif self.__buttons[4].text() == set_text and self.__buttons[6].text() == set_text and self.__buttons[7].text() == "  " and self.__buttons[8].text() == "  ":
                        self.__buttons[7].setIcon(QIcon('tic_tac_toe_o.png'))
                        self.__buttons[7].setText(set_text)
                        break
                    elif self.__buttons[5].text() == "" and self.__buttons[7].text() == "" and self.__buttons[4].text() == set_text and self.__buttons[8].text() == "  ":
                        self.__buttons[8].setIcon(QIcon('tic_tac_toe_o.png'))
                        self.__buttons[8].setText(set_text)
                        break
                    elif self.__buttons[5].text() == "" and self.__buttons[1].text() == "" and self.__buttons[4].text() == set_text and self.__buttons[2].text() == "  ":
                        self.__buttons[2].setIcon(QIcon('tic_tac_toe_o.png'))
                        self.__buttons[2].setText(set_text)
                        break
                    elif self.__buttons[1].text() == "" and self.__buttons[3].text() == "" and self.__buttons[4].text() == set_text and self.__buttons[0].text() == "  ":
                        self.__buttons[0].setIcon(QIcon('tic_tac_toe_o.png'))
                        self.__buttons[0].setText(set_text)
                        break
                    elif self.__buttons[3].text() == "" and self.__buttons[7].text() == "" and self.__buttons[4].text() == set_text and self.__buttons[6].text() == "  ":
                        self.__buttons[6].setIcon(QIcon('tic_tac_toe_o.png'))
                        self.__buttons[6].setText(set_text)
                        break
                    if self.__buttons[4].text() != "  ":
                        for button in self.__buttons:
                            if button.text() == "  ":
                                button.setIcon(QIcon('tic_tac_toe_o.png'))
                                button.setText(set_text)
                                break
                    else:
                        self.__buttons[4].setIcon(QIcon('tic_tac_toe_o.png'))
                        self.__buttons[4].setText(set_text)
                    break
                #  nothing

            self.__field.swap_player()

    @property  # makes method accessible like an attribute
    def token(self):
        return self.__token

    @token.setter
    def token(self, token):
        self.__token = token

    @property  # makes method accessible like an attribute
    def field(self):
        return self.__field

    @field.setter
    def field(self, field):
        self.__field = field

    @property  # makes method accessible like an attribute
    def file(self):
        return self.__file

    @file.setter
    def file(self, file):
        self.__file = file
# --------------------------------------------------------------------------------------------------
#                                    Class CController end
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
#                                    Class CField start
# --------------------------------------------------------------------------------------------------


class CField:
    def __init__(self):
        self.__field = [[0 for x in range(3)] for y in range(3)]
        self.__player = True
        self.__file = open("scoreboard.txt", "r+")
        self.__score_one = 0
        self.__score_two = 0

    def check_field(self, field):
        player = 0
        while player < 2:
            if player == 1:
                text = ""
            else:
                text = " "
            #  vertical
            if field[0].text() == text and field[1].text() == text and field[2].text() == text:
                self.__win(player)
                return True
            elif field[3].text() == text and field[4].text() == text and field[5].text() == text:
                self.__win(player)
                return True
            elif field[6].text() == text and field[7].text() == text and field[8].text() == text:
                self.__win(player)
                return True
            #  horizontal
            elif field[0].text() == text and field[3].text() == text and field[6].text() == text:
                self.__win(player)
                return True
            elif field[1].text() == text and field[4].text() == text and field[7].text() == text:
                self.__win(player)
                return True
            elif field[2].text() == text and field[5].text() == text and field[8].text() == text:
                self.__win(player)
                return True
            #  diagonal
            elif field[0].text() == text and field[4].text() == text and field[8].text() == text:
                self.__win(player)
                return True
            elif field[2].text() == text and field[4].text() == text and field[6].text() == text:
                self.__win(player)
                return True
            player += 1
        for i in range(0, len(field)):
            if field[i].text() == "  ":
                return False
        self.game_result = "Remis!"
        return True

    def get_game_result(self):
        return self.game_result

    def __win(self, player):
        __human_wins = 0
        __enemy_wins = 0
        self.game_result = "X" if player == 1 else "O"
        if self.enemy == "computer":
            if self.player is True and self.enemy == "computer":
                self.winner = "c"
            elif self.player is False and self.enemy == "computer":
                self.winner = "h"
            self.file.write(self.winner)
            self.file.seek(0)
            lines = self.file.readlines()
            for line in lines:
                __human_wins = line.count("h")
                __enemy_wins = line.count("c")
        elif self.player is False:
            self.score_one += 1
            __human_wins = self.score_one
            __enemy_wins = self.score_two
        else:
            self.score_two += 1
            __human_wins = self.score_one
            __enemy_wins = self.score_two
        self.game_result += f" has won!\nYou: {__human_wins}\nEnemy: {__enemy_wins}"

    @property  # makes method accessible like an attribute
    def enemy(self):
        return self.__enemy

    @enemy.setter
    def enemy(self, enemy):
        self.__enemy = enemy

    @property  # makes method accessible like an attribute
    def field(self):
        return self.__field

    @field.setter
    def field(self, field):
        self.__field = field

    @property  # makes method accessible like an attribute
    def game_result(self):
        return self.__game_result

    @game_result.setter
    def game_result(self, game_result):
        self.__game_result = game_result

    @property  # makes method accessible like an attribute
    def player(self):
        return self.__player

    def swap_player(self):
        self.__player = not self.__player

    @property  # makes method accessible like an attribute
    def file(self):
        return self.__file

    @file.setter
    def file(self, file):
        self.__file = file

    @property  # makes method accessible like an attribute
    def winner(self):
        return self.__winner

    @winner.setter
    def winner(self, winner):
        self.__winner = winner

    @property  # makes method accessible like an attribute
    def score_one(self):
        return self.__score_one

    @score_one.setter
    def score_one(self, score_one):
        self.__score_one = score_one

    @property  # makes method accessible like an attribute
    def score_two(self):
        return self.__score_two

    @score_two.setter
    def score_two(self, score_two):
        self.__score_two = score_two
# --------------------------------------------------------------------------------------------------
#                                    Class CField end
# --------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    controller = QApplication(sys.argv)
    ex = CController()
    sys.exit(controller.exec_())
# --------------------------------------------------------------------------------------------------
# Program end
