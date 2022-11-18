from fltk import *
from PIL import Image
import io
import random


def img_resize(fname, width):  # Mr. Arks Image resizer (http://arkiletian.com/cs2/basics/callback/)
    img = Image.open(fname)
    w, h = img.size
    height = int(width * h / w)
    img = img.resize((width, height), Image.BICUBIC)
    mem = io.BytesIO()
    img.save(mem, format="PNG")
    siz = mem.tell()
    return Fl_PNG_Image(None, mem.getbuffer(), siz)


def but_cb(wid):
    global c1, c2, c22, pairs, ifpair, c, clicks # Putting in all the varibles
    wid.deactivate() # Deactivating so you can not click same button twice
    c += 1
    if clicks <= 2: 
        i = LB.index(wid)
        i2 = OL[i]
        wid.image(IL[i2])
        clicks += 1
        if c1 == -1:
            c1 = i
            c22 = i2
        elif c1 != -1 and c2 == -1: # If it is a pair
            c2 = i
            if c22 == i2: 
                pairs += 1
                ifpair = True
                wid.image().inactive()
                LB[i].image().inactive()
                win.redraw()
                box.label(f"Total pairs: {pairs}/12 found")
        winner()
    elif clicks == 3: # If it is not a pair
        i = LB.index(wid)
        i2 = OL[i]
        wid.image(IL[i2])
        if c1 == -1:
            c1 = i
            c22 == i2
        elif c1 != -1 and c2 == -1:
            c2 = i
        if not ifpair: # Resetting to original image
            LB[c1].image(marvel)
            LB[c2].image(marvel)
            LB[c1].activate()
            LB[c2].activate()
        c1 = i
        c2 = -1
        c22 = i2
        win.redraw()
        clicks = 2
        ifpair = False
        winner()


def winner(): # Check if player has won
    global pairs, c
    if pairs == 12:
        fl_message(f'congratulations! You won in {c} clicks!')


NL = ["dococ.png", "electro.png", "goblin.png", "hulk.png", "ironman.png", "lizard.png",
      # List of image names (Name List)
      "mysterio.png", "rhino2.png", "sandman.png", "spiderman.png", "venom.png", "wolverine.png"]
OL = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11]  # List of the order

random.shuffle(OL)
 
IL = []  # List of actual images
for fname in NL:
    image = img_resize(fname, 150)
    IL.append(image)

marvel = Fl_PNG_Image('marvel.png')

bh = 150  # Dimensions of buttons and window
bw = 150
ww = bw * 6
wh = bh * 4 + 100
LB = []  # List of buttons
c1 = -1  # Clicked button 1
c2 = -1  # Clicked button 2
c22 = -1  # Clicked button 2 before
clicks = 1  #
pairs = 0  # Number of pairs acquired
ifpair = False  # If it is a pair
c = 0  # Number of clicks in the game

# Window creation:
win = Fl_Window(300, 400, ww, wh)  # Window creation

win.begin()

marvel = img_resize('marvel.png', 150)  # Default image

# Button creation:
for col in range(6):
    for row in range(4):
        LB.append(Fl_Button(col * 150, row * 150, 150, 150))
        LB[-1].image(marvel)
        LB[-1].callback(but_cb)  # Call back for when button is clicked
box = Fl_Box(0, wh - 100, ww, 100, f"Total pairs: {pairs}/12 found")

win.end()
win.show()
Fl.run()
