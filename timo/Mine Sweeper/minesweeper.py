from fltk import *
import random
import time


class Mine_Sweeper(Fl_Window):
    def __init__(self, x, y, w, h, label="Mine Sweeper"):

        Fl_Window.__init__(self, x, y, w, h, label)
        self.begin()

        fl_color(FL_WHITE)

        self.flags = 0  # Total flags used

        self.flag_list = []
        self.button_list = []
        self.bomb_list = []
        self.bomb_index = []
        self.revealed_list = []

        row = 0
        col = 0

        self.bomb = Fl_JPEG_Image("bomb.jpg")
        self.bomb = self.bomb.copy(50, 50)
        self.flag = Fl_PNG_Image("flag.png")
        self.flag = self.flag.copy(50, 50)

        # Button Creation (2D List)
        for row in range(10):

            temp = []

            for col in range(10):

                button = Fl_Button(row * 52, col * 52, 50, 50)
                button.callback(self.reveal)
                button.box(FL_UP_BOX)
                temp.append(button)
            self.button_list.append(temp)

        # Bomb Creation
        y = random.sample(range(10), 10)
        z = random.sample(range(10), 10)

        for x in range(10):

            self.bomb_list.append(self.button_list[y[x]][z[x]])
            self.bomb_index.append(self.find_ind(self.bomb_list[-1]))

        # Number of flags used
        self.flag_box = Fl_Box(210, 520, 100, 25, f"Flags used: {self.flags}")

        self.end()

        self.resizable(self)

        self.start = time.time()

    def gameover(self):  # When the game is lost
        for x in range(10):
            if self.bomb_list[x] not in self.flag_list:
                self.bomb_list[x].image(self.bomb)
                self.bomb_list[x].redraw()

        for x in range(len(self.flag_list)):
            if self.flag_list[x] not in self.bomb_list:
                self.flag_list[x].image(None)
                self.flag_list[x].label("@+41+")
                self.flag_list[x].labelcolor(FL_RED)

        fl_message("Game Over!")

    def find_ind(self, wid):  # Finds where a widget is in the 2d Button list
        for x in self.button_list:

            if wid in x:

                i = x.index(wid)
                return self.button_list.index(x), i

    def reveal(self, wid):  # When a button is clicked

        if Fl.event_button() == FL_RIGHT_MOUSE:  # If right click

            self.flagged(wid)
            return

        if wid in self.flag_list:  # If its a flag

            return

        if wid in self.bomb_list:  # If a bomb
            self.gameover()
            return

        coord = self.find_ind(wid)

        self.num(coord[0], coord[1])
           
         # Sends to a recursive function to reveal more buttons if it can

        wid.value(1)

        if len(set(self.revealed_list)) == 90:  # Win check

            self.win()

    def flagged(self, wid):  # Flag function

        if wid in self.flag_list:  # If button is already a flag

            wid.image(None)
            self.flag_list.remove(wid)
            self.flags -= 1
            wid.redraw()

            self.flag_box.label(f"Flags used: {self.flags}")

            return

        if wid.value() == 1:  # If not already clicked
            return

        self.flag_list.append(wid)
        wid.image(self.flag)
        self.flags += 1
        wid.redraw()

        self.flag_box.label(f"Flags used: {self.flags}")

    def num( self, row, col): # Recursive function for setting the number for a button and revealing more buttons
       
        bombs = 0

        for x in range(-1, 2):  # 1 Button around the selected button

            for y in range(-1, 2):

                if (0 <= (row + x) < 10 and 0 <= (col + y) < 10): # If its in a corner/edge
                    
                    self.revealed_list.append((row, col))
                    self.button_list[row][col].value(1)

                    if (row + x, col + y) in self.bomb_index:  # Finds total bombs

                        bombs += 1

        # Changes color of number:

        if bombs == 1:

            color = FL_BLUE

        if bombs == 2:
            color = FL_BLACK

        if bombs >= 3:
            color = FL_RED

        if bombs > 0:

            if self.button_list[row][col] not in self.flag_list:
                self.button_list[row][col].label(str(bombs))
                self.button_list[row][col].labelcolor(color)
                return

        for x in range(-1, 2):
            for y in range(-1, 2):

                if 0 <= (row + x) < 10 and 0 <= (col + y) < 10:

                    if (row + x, col + y) not in self.revealed_list:  # Mmakes it so it does not recurse infintely
                        if self.button_list[row + x][col + y] not in self.flag_list:
                            self.num(row + x, col + y)  # Recurse

    def win(self):  # Win function
        timetaken = time.time() - self.start
        timetaken = round(timetaken, 1)

        fl_message(f"Congratulations, You won!\n It took you {timetaken}s!")
        return


size = 550
app = Mine_Sweeper(0, 0, size - 30, size)
app.show()
Fl.run()
