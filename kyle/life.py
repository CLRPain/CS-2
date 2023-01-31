from fltk import *
	
class Cell(Fl_Button):
	alive=False
	def __init__(self,x,y,w,h,label=None):
		Fl_Button.__init__(self,x,y,w,h,label)
		
		
class Grid(Fl_Double_Window):
    
    running=False #running = True if simulation is running
    
    
    '''Creates the cells'''
    def borncb(self, wid):
        wid.color(FL_BLUE)
    Cell.alive=True
    self.startbut.activate() 
    if Grid.running==False: 
    self.lexbut.deactivate()
    
    '''Start button'''	
    def startcb(self, wid):
    wid.label('Pause') #changes startbut to pausebut
    Grid.running=True
    self.clicks+=1
    if self.clicks % 2 == 0: #if click num is even, change back to startbut
    self.pausecb()
    Grid.running=False #pauses simulation
    
    
    contact=0 #number of cells the selected cell in 2d list is touching 
    born=[] #the locations of where cells will be birthed
    kill=[] #the locations of where cells will be killed
    livecells=[] #list of currently live cells on grid
    
    while Grid.running == True:
    born=[] 
    kill=[]
    livecells=[]
    for row in range(len(self.bl)): #iterates over each row
    for column in range(len(self.bl)): #iterates over each column
    
    if self.bl[row][column].color()==216: #if cell is alive
    
    contact=0
    livecells.append(self.bl[row][column])
    
    
    for r,c in self.area: 
    
    if row+r < 0 or row+r > 79 or column+c < 0 or column+c > 79: #edge cases
    continue
    
    if self.bl[row+r][column+c].color()==216: #if a cell within the range of main cell is alive,
    contact+=1 #then it is a cell in contact with the main cell
    
    
    '''Kill rule'''	
    if contact < 2 or contact >= 4: 
    kill.append(self.bl[row][column]) #adds the cell to be killed
    
    
    else: #if cell is not alive
    
    contact=0
    
    
    
    for r,c in self.area:
    
    if row+r < 0 or row+r > 79 or column+c < 0 or column+c > 79:
    continue
    
    if self.bl[row+r][column+c].color()==FL_BLUE:
    contact+=1	
    
    '''Birthing rule'''	
    if contact == 3:
    born.append(self.bl[row][column])
    
    
    for cell in born:
    cell.color(FL_BLUE)
    
    self.redraw()
    
    
    for cell in kill:
    cell.color(FL_BACKGROUND_COLOR)
    livecells.remove(cell) 
    
    self.redraw()
    
    '''Resets everything'''	
    if len(livecells) == 0:
    self.clearcb(wid)
    
    Fl.check()	
    
    '''Pause button'''	
    def pausecb(self):
    self.startbut.label('Start')
    self.startbut.value(0)
    
    '''Clears all cells and resets everything'''
    def clearcb(self, wid):
    Grid.running=False #simulation ends when all cells are cleared
    self.clicks=0
    self.pausecb()
    self.lexbut.activate()
    self.startbut.deactivate()
    for row in range(len(self.bl)): 
    for column in range(len(self.bl)):
    self.bl[row][column].color(FL_BACKGROUND_COLOR)
    
    self.redraw()
    
    '''Creates glider in middle of grid'''	
    def lexcb(self, wid):
    self.clearcb(wid)
    for r,c in self.lexcords:
    self.bl[r][c].color(FL_BLUE)
    
    self.redraw()
    self.startbut.activate()
    Cell.alive=True
    
    '''Draws grid'''	
    def draw(self):
    Fl_Double_Window.draw(self)
    sep=10
    fl_color(FL_BLACK)
    for x in range(0, 801, sep):
    fl_line(x,0,x,800)
    for y in range(0, 801, sep):
    fl_line(0,y,800,y)
    
    def __init__(self,x,y,w,h,label=None):
    Fl_Double_Window.__init__(self, x, y, w, h, label)
    self.area=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)] #list of positions relative to selected cell to know whether selected cell is in contact with any
    self.lexcords=[(38,40),(39,41),(40,39),(40,40),(40,41)] #glider coords
    self.width=10
    self.clicks=0
    self.bl=[]
    self.begin()
    
    for y in range(80):
    self.xcord=[]
    for x in range(80):
    self.but=Cell(x*self.width, y*self.width, self.width,self.width)
    self.but.box(FL_FLAT_BOX)
    self.xcord.append(self.but)
    self.xcord[-1].callback(self.borncb)
    
    self.bl.append(self.xcord)
    
    
    self.startbut=Fl_Light_Button(800,0,200,80, 'Start')
    self.startbut.callback(self.startcb)
    self.clearbut=Fl_Button(800,100,200,80, 'Clear')
    self.clearbut.callback(self.clearcb)
    self.lexbut=Fl_Button(800,200,200,80, 'Glider')
    self.lexbut.callback(self.lexcb)
    self.startbut.deactivate()
    
    
    self.end()
    self.show()
    
    
x=Fl.w()//2-400
y=Fl.h()//2-400	
w=1000
h=800	

game=Grid(x,y,w,h)

Fl_scheme('gtk+')

Fl.run()