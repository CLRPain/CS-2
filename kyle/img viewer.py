
from fltk import *
from PIL import Image
import io


def filter(fname): #resize image for button size
    try:
        img = Image.open(fname) 
        mem = io.BytesIO() 
        img.save(mem, format="PNG") 
        siz = mem.tell()
        return Fl_PNG_Image(None, mem.getbuffer(), siz)
    except:
        return

def but_cb(wid, num):
    win.image(pngs[0])
    win.redraw()

#fl_dir_chooser
img = ['dococ.png', 'electro.png', 'goblin.png', 'hulk.png', 'ironman.png', 
'lizard.png', 'mysterio.png', 'rhino2.png', 'sandman.png', 'spiderman.png', 
'venom.png', 'wolverine.png', 'Highscore.txt' ]
pngs=[]
for pic in img:
    pic = filter(pic)
    pngs.append(pic)

ww = 400
wh = 500


win = Fl_Window(0,0,ww,wh, "img viewer")
win.begin()

p= Fl_Pack(0, 0, ww, wh)
p.type(Fl_Pack.HORIZONTAL)
p.begin()

b1=Fl_Button(0,0, 100, 0,'@<')
b2=Fl_Button(0,0, 100, 0,'@>')
p.spacing(win.w()-200)
b1.callback(but_cb, -1)
b2.callback(but_cb, 1)

p.end()

win.end()
win.resizable(p)
win.show()
Fl.run()