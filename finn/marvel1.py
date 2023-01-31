from fltk import*
import random
from PIL import Image
import io

def img_resize(fname,width):
    '''resizes any image type using high quality PIL library'''
    img = Image.open(fname) #opens all image formats supported by PIL
    w,h = img.size
    height = int(width*h/w)  #correct aspect ratio
    img = img.resize((width, height), Image.BICUBIC) #high quality resizing
    mem = io.BytesIO()  #byte stream memory object
    img.save(mem, format="PNG") #converts image type to PNG byte stream
    siz = mem.tell() #gets size of image in bytes without reading again
    return Fl_PNG_Image(None, mem.getbuffer(), siz)

def reveal(wid):
	times = 0
	global pairs, truetimes
	widlist.append(wid)
	wid.deactivate()		# saving button index, corresponding picture, and number of buttons clicked
	number = LB.index(wid)
	wid.image(pnglist[number])
	clicklist.append(piclist[number])
	truetimes += 1
	
	for x in clicklist:
		times += 1
		if times >= 2:
			if clicklist[0] == clicklist[1]: #checking for pairs
				widlist[0].image().inactive()
				widlist[1].image().inactive()
				widlist[0].redraw()
				widlist[1].redraw()
				clicklist.clear()
				widlist.clear()
				times = 0
				pairs += 1
			else:
				if times == 3:
					widlist[0].image(goodstartpic)
					widlist[0].activate()
					widlist[1].image(goodstartpic)
					widlist[1].activate()
					temp = widlist[2]
					temps = clicklist[2]
					clicklist.clear()
					widlist.clear()
					widlist.append(temp) #resetting if a pair is not found
					clicklist.append(temps)
					times = 1
	if pairs == 12:
		fl_message(f"You Won in {truetimes} clicks!", fl_message_title("Hooray!"))
		
	wid.redraw()

goodstartpic = img_resize("marvel.png", 160)

piclist = ["dococ.png", "goblin.png", "hulk.png", "ironman.png", "lizard.png", "electro.png", "rhino2.png", "sandman.png", "mysterio.png", "venom.png", "wolverine.png", "spiderman.png"]
piclist = piclist*2
random.shuffle(piclist)

clicklist = []
widlist = []
LB=[]
pnglist = []
pairs = 0
truetimes = 0

for pic in piclist:
	pic = img_resize(pic, 160)
	pnglist.append(pic)

win = Fl_Window(0,0,960,640,"MemoryGame") #making window
win.begin()

for row in range(4): #making buttons
	for col in range(6):
		LB.append(Fl_Button(col*160, row*160,160,160))
		LB[-1].callback(reveal)
		LB[-1].image(goodstartpic)
win.end()
win.show()
Fl.run()
