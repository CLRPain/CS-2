from fltk import *
import random


D={0:"seven.png",
1:"cherry.png",
2:"grapes.png",
3:"lemon.png",
4:"watermelon.png",
5:"bell.png"
}

pic1 = Fl_PNG_Image("seven.png")
pic2 = Fl_PNG_Image("seven.png")
pic3 = Fl_PNG_Image("seven.png")


money = 10

def gamble(wid):
	global money
	L=[]
	money= money + 10
	for x in range(3):
		x = random.randrange(6)
		L.append(x)
	print(L)
	if L[0] == L[1] and L[0] == L[2]:
			fl_message(f'YOU WON $100!!!, You spent: ${money}')
	pic1 = Fl_PNG_Image(D[L[0]])
	pic2 = Fl_PNG_Image(D[L[1]])
	pic3 = Fl_PNG_Image(D[L[2]])
	
	pic1 = pic1.copy(slot1.w(),slot1.h())
	pic2 = pic2.copy(slot1.w(),slot1.h())
	pic3 = pic3.copy(slot1.w(),slot1.h())
	
	slot1.image(pic1)
	slot2.image(pic2)
	slot3.image(pic3)
	win.redraw()
	
	
	



ww=768
wh=356

win = Fl_Window(400,100,ww,wh)
win.begin()
but = Fl_Button(0, wh-100,ww,100,"P     U     L     L       $ 10")
but.label
slot1 = Fl_Box(0,0,256,256)
slot2 = Fl_Box(256,0,256,256)
slot3 = Fl_Box(512,0,256,256)
win.end()

pic1 = pic1.copy(slot1.w(),slot1.h())
pic2 = pic2.copy(slot1.w(),slot1.h())
pic3 = pic3.copy(slot1.w(),slot1.h())

slot1.image(pic1)
slot2.image(pic2)
slot3.image(pic3)
slot1.box(FL_BORDER_BOX)
slot2.box(FL_BORDER_BOX)
slot3.box(FL_BORDER_BOX)

but.callback(gamble)

win.show()
Fl.run()
