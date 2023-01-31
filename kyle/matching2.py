
from fltk import*
from PIL import Image
import io
import random

def img_resize(fname,width): #resize image for button size
    '''resizes any image type using high quality PIL library'''
    img = Image.open(fname) #opens all image formats supported by PIL
    w,h = img.size
    height = int(width*h/w)  #correct aspect ratio
    img = img.resize((width, height), Image.BICUBIC) #high quality resizing
    mem = io.BytesIO()  #byte stream memory object
    img.save(mem, format="PNG") #converts image type to PNG byte stream
    siz = mem.tell() #gets size of image in bytes without reading again
    return Fl_PNG_Image(None, mem.getbuffer(), siz)

def reset(): #reset widgets back to original cover and clear lists
        widlist[0].activate()
        widlist[1].activate()
        widlist[0].image(cover)
        widlist[1].image(cover)
        clicked.clear()
        widlist.clear()

def but_cb(wid): #callback for widgets
    global cnum, pair, hs
    if len(clicked) ==2:
        if clicked[0] != clicked[1] or numindex[0] == numindex[1]: #different image name or same button
            reset()
    wid.deactivate()
    x=LB.index(wid) #find widget index number
    wid.image(il[x]) #item in list that corresponds to index number
    cnum +=1
    clicked.append(nl[x])
    numindex.append(x)
    widlist.append(wid)
    if len(clicked) == 2: #check if 2 widgets are clicked
        if clicked[0] == clicked[1] and numindex[0] != numindex[1]: #same image name, different buttons
            widlist[0].image().inactive()
            widlist[1].image().inactive()
            widlist[0].redraw()
            widlist[1].redraw()
            pair+=1
            clicked.clear()
            widlist.clear()
    if pair == 12:
            try:
                f = open("Highscore.txt", "r+") #open highscore file
                hs = f.read()
                hs = hs.strip('\x00') #remove unneeded characters
                hs = hs.strip('\n') #remove new line
                hs = int(float(hs))
                if hs > cnum:
                    hs = cnum
                    f.truncate(0) #reset the file
                    f.write(str(hs))
                    f.close()
            except:
                print('no file found')
            fl_message(f"You win with {cnum} clicks. \nHighscore: {hs}", fl_message_title("Congratulations!!"))
            

    

clicked = [] #list for clicked image names
numindex=[] #list for clicked image indexes
widlist=[] #last 2 widgets used to reset in case of no match
cnum = 0 #num of clicks
pair = 0 #num of pairs
hs = 'no highscore file found'
nl = ['dococ.png', 'electro.png', 'goblin.png', 'hulk.png', 'ironman.png', 
'lizard.png', 'mysterio.png', 'rhino2.png', 'sandman.png', 'spiderman.png', 
'venom.png', 'wolverine.png']
il = []
nl = nl*2
#random.shuffle(nl)

for fname in nl: #resize all images
    image = img_resize(fname, 128)
    il.append(image)


win = Fl_Window(0, 0, 768, 512, "Marvel Matching Game")
LB = []
win.begin()
cover = img_resize('marvel.png', 128)

for col in range(6): #make the board
    for row in range(4):
        LB.append(Fl_Button(col*128,row*128,128,128)) #dimensions of each button
        LB[-1].image(cover)
        LB[-1].callback(but_cb)

win.end()

win.show()
Fl.run()

