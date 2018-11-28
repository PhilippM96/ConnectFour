#  pip3 install PyQt5
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Connect Four'
        self.height = 300
        self.width = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(1, 1, self.width, self.height)
        self.center()

        #self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Connect Four')

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        helpMenu = mainMenu.addMenu('Help')

        file_quit = QAction(QIcon('quit.png'), 'Exit', self)
        file_quit.setShortcut('Ctrl+Q')
        file_quit.triggered.connect(self.close)
        fileMenu.addAction(file_quit)

        file_players = QAction(QIcon('players.png'), 'Players', self)
        file_players.setShortcut('Ctrl+P')
        file_players.triggered.connect(self.players)
        fileMenu.addAction(file_players)

        help_rules = QAction(QIcon('rules.png'), 'Rules', self)
        help_rules.setShortcut('Ctrl+R')
        help_rules.triggered.connect(self.rules)
        helpMenu.addAction(help_rules)

        # create the widget here
        self.setCentralWidget(SetPlayers(self))  # Get Value which widget should auto start

        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def rules(self):
        self.setCentralWidget(Rules(self))

    def players(self):
        self.setCentralWidget(SetPlayers(self))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class SetPlayers(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        #btn_quit = QPushButton('Quit', self)
        #btn_quit.setToolTip('This button <b>closes</b> the game.')
        #btn_quit.clicked.connect(self.close_game)
        #btn_quit.resize(50, 25)
        #btn_quit.move(100, 100)

        self.lbl_players = QLabel('Player Amount', self)

        self.cmbbx_players = QComboBox(self)
        for i in range(2, 8):  # make dynamic
            self.cmbbx_players.addItem(str(i))
            i += 1
        self.cmbbx_players.resize(50, 20)
        self.cmbbx_players.move(200, 20)

        self.btn_set = QPushButton('Set', self)
        self.btn_set.resize(90, 20)
        self.btn_set.move(200, 50)
        self.btn_set.clicked.connect(self.set_players)

        self.layout.addWidget(self.lbl_players)
        self.layout.addWidget(self.cmbbx_players)
        self.layout.addWidget(self.btn_set)
        self.create_players()
        #self.layout.addWidget(btn_quit)
        self.setLayout(self.layout)

    def close_game(self):
        reply = QMessageBox.question(self, 'Message',
        "Are you sure to leave the game?", QMessageBox.Yes |
        QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QApplication.quit()
        else:
            pass

    def on_click(self):
        QMessageBox.question(self, 'Message', "You typed: " + self.txtbx_player1.text(), QMessageBox.Ok, QMessageBox.Ok)
        self.txtbx_player1.setText("")

    def create_players(self):
        self.players_label = []
        self.players_text = []
        for i in range(0, int(self.cmbbx_players.currentText())):
            self.players_label.append(i)
            self.players_label[i] = QLabel('Player ' + str(i + 1), self)
            self.layout.addWidget(self.players_label[i])
            self.players_label[i].resize(50, 20)
            self.players_label[i].move(10, 10 + (i * 20))

            self.players_text.append(i)
            self.players_text[i] = QLineEdit(self)
            self.layout.addWidget(self.players_text[i])
            self.players_text[i].resize(90, 20)
            self.players_text[i].move(60, 10 + (i * 20))

    def set_players(self):
        self.create_players()

            #self.players_list.append

        #self.txtbx_player1 = QLineEdit(self)
        #self.txtbx_player1.resize(90, 20)
        #self.txtbx_player1.move(50, 10)

class Rules(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.initUI()

    def initUI(self):
        rules = "To win Connect Four you must be the first player to get four of your colored checkers in a row " \
                "either horizontally, vertically or diagonally."
        self.lbl_rules = QTextEdit(rules, self)
        #self.layout.addWidget(self.lbl_rules)
        self.lbl_rules.resize(280, 60)
        self.lbl_rules.move(10, 10)
        self.lbl_rules.setEnabled(False)

    def close_rules(self):
        pass
