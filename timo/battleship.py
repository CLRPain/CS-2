#python3 battleship.py[type][IP][port]
#[type] = server OR client
from fltk import *
import socket, sys, pickle

class Battle_Ship(Fl_Window):
	def __init__(self, x, y, w, h, label=sys.argv[1]):
		Fl_Window.__init__(self, x, y, w, h, label)
		self.begin()

		gridsize=5
		self.ships=5
		self.myship_list=[]
		self.opponentship_list=[]
		self.hits=0
		self.misses=0
		self.squares_shot=[]
		self.turn='client'
		self.am_ready=False

		self.blank = Fl_PNG_Image("blank.png")
		self.hit = Fl_PNG_Image("hit.png")
		self.miss = Fl_PNG_Image("miss.png")
		self.ship = Fl_PNG_Image("ship.png")

		self.blank = self.blank.copy(100,100)
		self.hit = self.hit.copy(100,100)
		self.miss = self.miss.copy(100,100)
		self.ship = self.ship.copy(100,100)

#Players Grid

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

#Opponents Grid

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

#Ready button
		self.ready_button=Fl_Button(580,720,200,40,'Ready!')
		self.ready_button.callback(self.ready)

		self.end()
		self.resizable(self)
		self.connect()
		
	def connect(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.host = sys.argv[2]
		self.port = int(sys.argv[3])

		if sys.argv[1] == 'server':

			self.s.bind((self.host, self.port))
			self.s.listen(1)
			Fl.add_fd(self.s.fileno(), self.acceptConnection)

		elif sys.argv[1] == 'client':
			self.s.connect((self.host, self.port))

			self.fd=self.s.fileno()
			print(self.fd)
			Fl.add_fd( self.fd, self.receive_data)

	def acceptConnection(self, fd):
		self.conn, addr = self.s.accept()
		self.fd=self.conn.fileno()
		print(self.fd)
		Fl.add_fd(self.fd, self.receive_data) 


	def place_ships(self, w): #When you get to place your ships
		if self.am_ready == True:
			return
		for x in self.my_grid:

			if w in x:

				i = x.index(w)
				ind = (self.my_grid.index(x), i)
				
				
		if ind not in self.myship_list:
			if self.ships < 1:

				return
			self.myship_list.append(ind)
			self.ships = self.ships - 1

			w.image(self.ship)
			w.redraw()
			return

		else:
			self.myship_list.remove(ind)
			self.ships +=1
			w.image(self.blank)
			w.redraw()

		return

	def ready(self,w):
		if self.ships == 0:
			self.ready_button.deactivate()
			data=pickle.dumps(self.myship_list)
			if sys.argv[1] == 'client':
				print('client')
				self.s.sendall(data)

				
			else:


				
				self.conn.sendall(data)
				
			self.opponentship_list = pickle.loads(data)	
			self.am_ready = True
			self.placed = True

			
		
			

	def shoot(self, w): #When you shoot
		if self.am_ready == False:
			return
		
		if sys.argv[1] == self.turn:
			for x in self.opponents_grid:

				if w in x:

					i = x.index(w)
					
					ind = (self.opponents_grid.index(x), i)
					
					print('ind',ind)
			if ind in self.squares_shot:
				return
				
			
			
			if ind in self.opponentship_list:
				self.hit_ship(ind,'player')
			else:
				self.miss_ship(ind,'player')
			print('hi')
			data = pickle.dumps(ind)
			if sys.argv[1] == 'client':
				self.s.sendall(data)
			elif sys.argv[1] == 'server':
				self.conn.sendall(data)
			
			self.squares_shot.append(ind)
			
			if self.turn == 'client':
				self.turn = 'server'
			else:
				self.turn = 'client'

#data = self.conn.recv(1024)
		


	def miss_ship(self, ind, player): #When you miss
		if player == 'player':
			self.opponents_grid[ind[0]][ind[1]].image(self.miss)
			self.misses += 1
			self.opponents_grid[ind[0]][ind[1]].redraw()
		else:
			self.my_grid[ind[0]][ind[1]].image(self.miss)
			self.opponents_grid[ind[0]][ind[1]].redraw()
			
	def hit_ship(self, ind, player): #When you hit a ship
		if player == 'player':
			self.opponents_grid[ind[0]][ind[1]].image(self.hit)
			self.opponents_grid[ind[0]][ind[1]].redraw()
			self.hits+=1
			if self.hits == 5:
				self.gameover('win')
		else:
			self.my_grid[ind[0]][ind[1]].image(self.hit)
			self.my_grid[ind[0]][ind[1]].redraw()

	def receive_data(self, fd): #When you receive data
		if sys.argv[1] == 'server':
			data = self.conn.recv(1024)
		elif sys.argv[1] == 'client':
			data = self.s.recv(1024)
		data = pickle.loads(data)
		print('data:',data)


	def gameover(self,win): #When the game is won/lost
		for x in range(len(opponents_grid)):
			for y in range(len(opponents_grid[x])):
				opponents_grid[x][y].deactivate()
		for x in range(len(my_grid)):
			for y in range(len(my_grid[x])):
				my_grid[x][y].deactivate()
		if win == 'win':
			fl_message(f'Congrats you won!\n You shot {self.misses+self.hits} missles!')
		else:
			fl_message(f'Oh no! You ran out of vessels, Better luck next time!\n You shot {self.misses+self.hits} missles!')

size = 800
app = Battle_Ship(0, 0, size+300, size)
Fl.scheme('plastic')
app.show()
Fl.run()
