#python3 battleship.py [type] [IP] [port]
#[type] = server OR client
from fltk import *
import socket
import sys


''' 
#TCP Connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#For the person connecting
if sys.argv[1] == 'client':
	host = sys.argv[2]
	port = int(sys.argv[3])
	s.connect((host, port))
	
#For the person hosting
if sys.argv[1] == 'server':
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	host = sys.argv[2]
	post = int(sys.argv[3])
	s.bind((host, port))
	s.listen(1)
	conn, addr = s.accept()
'''

class Battle_Ship(Fl_Window):
	def __init__(self, x, y, w, h, label="Battle_Ship"):
		Fl_Window.__init__(self, x, y, w, h, label)
		self.begin()
		
		gridsize=5
		self.ships=5
		self.myship_list=[]
		self.opponentship_list=[(0,0),(1,1),(2,2),(3,3),(4,4)]
		self.hits=0
		self.misses=0
		self.squares_shot=[]

		self.blank = Fl_PNG_Image("blank.png")
		self.hit = Fl_PNG_Image("hit.png")
		self.miss = Fl_PNG_Image("miss.png")
		self.ship = Fl_PNG_Image("ship.png")
		
		self.blank = self.blank.copy(100,100)
		self.hit = self.hit.copy(100,100)
		self.miss = self.miss.copy(100,100)
		self.ship = self.ship.copy(100,100)
		
		# Players Grid
		
		self.my_grid=[]
		for x in range(gridsize):
			temp=[]
			for y in range(gridsize):
				button=Fl_Button(x*100+50, y*100+50, 100, 100)
				button.callback(self.place_ships)
				button.image(self.blank)
				button.box(FL_UP_BOX)
				temp.append(button)
			self.my_grid.append(temp)
			
		# Opponents Grid
		
		self.opponents_grid=[]
		for x in range(gridsize):
			temp=[]
			for y in range(gridsize):
				button=Fl_Button(x*100+580, y*100+50, 100, 100)
				button.callback(self.shoot)
				button.image(self.blank)
				button.box(FL_UP_BOX)
				temp.append(button)
			self.opponents_grid.append(temp)
			
		#Game chat
		self.chat_brow=Fl_Multi_Browser(50,560,500,150)
		
		self.chat_input=Fl_Input(50,720,500,40,"Chat")
		self.chat_input.align(FL_ALIGN_LEFT)
		
		#Computer helper
		self.console_brow=Fl_Multi_Browser(580, 560, 500, 150)
		#self.console_brow.add(f'Connection established with {addr}')
		
		#Ready button
		self.ready_button=Fl_Button(580,720,200,40,'Ready!')
		self.ready_button.callback(self.ready)
		
		self.end()
			
	def place_ships(self, w): #When you get to place your ships
		
		if w not in self.myship_list:
			if self.ships < 1:
				
				return
			self.myship_list.append(w)
			self.ships = self.ships - 1
			
			w.image(self.ship)
			w.redraw()
			return
			
		else:
			self.myship_list.remove(w)
			self.ships +=1
			w.image(self.blank)
			w.redraw()
			
		return
		
	def ready(self,w):
		if self.ships == 0:
			self.console_brow.add('Ready!')
			self.ready_button.deactivate()
		else:
			self.console_brow.add('You need to place all ships to be ready!')
			
	def shoot(self, w): #When you shoot
		#check if its my turn
		for x in self.opponents_grid:

			if w in x:

				i = x.index(w)
				ind = (self.opponents_grid.index(x), i)
		if ind in self.squares_shot:
			return
		self.squares_shot.append(ind)
		
		if ind in self.opponentship_list:
			self.hit_ship(ind,'player')
		else:
			self.miss_ship(ind,'player')
        
        
		
		#send ind
		#recive ind
		#display
		
		return
		
	def gameover(self,win): #When the game is won/lost
		if win == 'win':
			fl_message(f'Congrats you won!\n You shot {self.misses+self.hits} missles!')
		else:
			fl_message(f'Oh no! You ran out of vessels, Better luck next time!\n You shot {self.misses+self.hits} missles!')
		
	def miss_ship(self, ind, player): #When you miss
		if player == 'player':
			self.opponents_grid[ind[0]][ind[1]].image(self.miss)
			self.misses += 1
		else:
			self.my_grid[ind[0]][ind[1]].image(self.miss)
		
	def hit_ship(self, ind, player): #When you hit a ship
		if player == 'player':
			self.opponents_grid[ind[0]][ind[1]].image(self.hit)
			self.hits+=1
			if self.hits == 5:
				self.gameover('win')
		else:
			self.my_grid[ind[0]][ind[1]].image(self.hit)
			
	def chat(self): #Chat function
		return

size = 800
app = Battle_Ship(0, 0, size+300, size)
Fl.scheme('plastic')
app.show()
Fl.run()

1
#556755 556755 556754 456766 667877 54
#`121`21232131232132343243454354575475787868986978987989098090-09

