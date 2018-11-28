import tkinter
from sys import stdout


class ShowStrategyAbstract:
    @staticmethod
    def get_size():
        raise NotImplementedError

    @staticmethod
    def create_field():
        raise NotImplementedError

    @staticmethod
    def player_move():
        raise NotImplementedError


class ShowConsoleStrategy(ShowStrategyAbstract):
    @staticmethod
    def get_size(min_size, max_size, default_length, default_height):
        __length = default_length if input("Soll die Standard-Breite verwendet werden? ").lower() == "ja" else 0
        __height = default_height if input("Soll die Standard-Länge verwendet werden? ").lower() == "ja" else 0
        while __length < min_size or __length > max_size:
            __length = int(input("Wie breit soll das Feld sein? "))
            if __length < min_size:
                print("Das Feld ist zu klein.")
            elif __length > max_size:
                print("Das Feld ist zu groß.")
        while __height < min_size or __height > max_size:
            __height = int(input("Wie hoch soll das Feld sein? "))
            if __height < min_size:
                print("Das Feld ist zu klein.")
            elif __height > max_size:
                print("Das Feld ist zu groß.")
        return [__length, __height]

    @staticmethod
    def create_field(field):
        for i in range(len(field)):
            for j in range(len(field[0])):
                if field[i][j] is 0:
                    stdout.write('\u25cc')
                if field[i][j] is 1:
                    stdout.write('\u25cb')
                if field[i][j] is 2:
                    stdout.write('\u25cf')
            stdout.write("\n")
        print(len(field))

    def player_move(self):
        pass


class ShowWindowStrategy(ShowStrategyAbstract):
    def get_size(self, min_size, max_size, default_length, default_height):
        self.run()
        lbl_length = tkinter.Label(self.root, text="Length")
        spn_length = tkinter.Spinbox(self.root, from_=min_size, to=max_size, width=2, state='disabled')
        lbl_height = tkinter.Label(self.root, text="Height")
        spn_height = tkinter.Spinbox(self.root, from_=min_size, to=max_size, width=2, state='disabled')
        rad_size1 = tkinter.Radiobutton(self.root, text="Default", value=0, command=
                                        lambda default_length=default_length, default_height=default_height,
                                        spn_length=spn_length, spn_height=spn_height:
                                        self.rad_size1_check(default_length, default_height, spn_length, spn_height))
        rad_size2 = tkinter.Radiobutton(self.root, text="Custom", value=1, command=
                                        lambda spn_length=spn_length, spn_height=spn_height:
                                        self.rad_size2_check(spn_length, spn_height))
        btn_set = tkinter.Button(self.root, text="Set", height=3, width=5)
        btn_set.configure(command=lambda spn_length=spn_length, spn_height=spn_height, btn_set=btn_set,
                                         rad_size1=rad_size1, rad_size2=rad_size2, lbl_height=lbl_height,
                                         lbl_length=lbl_length: self.btn_set_click(spn_length, spn_height, btn_set,
                                         rad_size1, rad_size2, lbl_height, lbl_length))

        lbl_length.grid(row=1, column=1)
        spn_length.grid(row=1, column=2)
        rad_size1.grid(row=1, column=3)
        rad_size1.select()
        lbl_height.grid(row=2, column=1)
        spn_height.grid(row=2, column=2)
        rad_size2.grid(row=2, column=3)
        btn_set.grid(row=1, column=4, rowspan=2)

        self.rad_size1_check(default_length, default_height, spn_length, spn_height)

        self.root.mainloop()

        return [self.length, self.height]

    @staticmethod
    def rad_size1_check(default_length, default_height, spn_length, spn_height):
        spn_length.configure(state='normal')
        spn_height.configure(state='normal')
        spn_length.delete(0, "end")
        spn_height.delete(0, "end")
        spn_length.insert(0, default_length)
        spn_height.insert(0, default_height)
        spn_length.configure(state='disabled')
        spn_height.configure(state='disabled')

    @staticmethod
    def rad_size2_check(spn_length, spn_height):
        spn_length.configure(state='readonly')
        spn_height.configure(state='readonly')

    def btn_set_click(self, spn_length, spn_height, btn_set, rad_size1, rad_size2, lbl_height, lbl_length):
        self.length = int(spn_length.get())
        self.height = int(spn_height.get())
        spn_length.destroy()
        spn_height.destroy()
        rad_size1.destroy()
        rad_size2.destroy()
        lbl_height.destroy()
        lbl_length.destroy()
        btn_set.destroy()
        self.root.quit()
        #self.root.destroy()

    def create_field(self, field):
        #self.run()
        btn_start = tkinter.Button(self.root, text="Start", height=3)
        btn_start.configure(command=lambda btn_start=btn_start : self.btn_start_click(btn_start))
        circle_empty = tkinter.PhotoImage(file="circle.gif")  # Only GIF or PGM/PPM
        circle_yellow = tkinter.PhotoImage(file="circle_yellow.gif")  # Only GIF or PGM/PPM
        circle_green = tkinter.PhotoImage(file="circle_green.gif")  # Only GIF or PGM/PPM
        row = 3
        for i in range(0, self.height):
            column = 1
            for j in range(0, self.length):
                if field[i][j] is 0:
                    #field[i][j] = self.__player_turn
                    btn_circle = tkinter.Button(self.root, image=circle_empty)
                                                     #, command=lambda x_pos=j, y_pos=i: self.btn_circle_click(field, x_pos, y_pos))
                elif field[i][j] is 1:
                    #field[i][j] = self.__player_turn
                    btn_circle = tkinter.Button(self.root, image=circle_yellow)
                                                     #, command=lambda x_pos=j, y_pos=i: self.btn_circle_click(field, x_pos, y_pos))
                    #field[i][j] = self.__player_turn
                else:
                    #field[i][j] = self.__player_turn
                    btn_circle = tkinter.Button(self.root, image=circle_green)
                                                     #, command=lambda x_pos=j, y_pos=i: self.btn_circle_click(field, x_pos, y_pos))

                btn_circle.grid(row=row, column=column)
                column += 1
            row += 1
        btn_start.configure(width=8*column)
        btn_start.grid(row=row, column=1, columnspan=column)
        self.root.mainloop()

    def btn_circle_click(self, field, x_pos, y_pos):
        field[y_pos][x_pos] = 1
        #field = self.player_move()
        self.create_field(field)

    def btn_start_click(self, btn_start):
        pass
        #btn_start.destroy()
        #self.root.quit()

    def player_move(self):
        print("MY TURN")

    def run(self):
        self.root = tkinter.Tk()
        self.root.resizable(width=False, height=False)
        self.root.title("Connect Four")
        img = tkinter.Image("photo", file="ball.gif")
        self.root.tk.call('wm', 'iconphoto', self.root._w, img)
