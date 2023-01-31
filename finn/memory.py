#!/usr/bin/python
from fltk import *
import random
import os
import io
from PIL import Image

class Marvel(Fl_Window):
	
	def __init__(self, w, h, name = ""):
		Fl_Window.__init__(self, w, h, name)
		
		self.buttons = []
		x = 0
		self.I=[]
		self.imgs = []
		
		def png_resiz_fltk(fname,w,h):
			'''resizes png file and returns Fl_PNG_Image object. Requires importing io and PIL Image '''
			img = Image.open(fname)
			#img = img.resize((w,h),Image.LANCZOS) #LANCZOS is highest quality filter
			img = img.resize((w,h),Image.BICUBIC) #BICUBIC is good quality filter
			#img = img.resize((w,h)) # default resample filter is bicubic (good quality) in later version of PIL
			temp = io.BytesIO()  # temp is an in memory file object byte stream
			img.save(temp,'PNG') # PIL Image.save img to png format file object temp
			siz = temp.tell()    # number of bytes in image (clever way to get size without reading again)
			#next line is Fl_PNG_Image ctor overloaded for in memory objects. It works in pyfltk!!!! :)
			return Fl_PNG_Image(None, temp.getvalue(), siz) #io.BytesIO .getvalue() converts contents to bytes
		
		
		fnames=os.listdir('marvel_pics')
		self.fnames=fnames+fnames
		random.shuffle(self.fnames)
		for fname in self.fnames:
			self.imgs.append(png_resiz_fltk(f'./marvel_pics/{fname}',150,150))
		
		self.begin()
		for r in range(4):
			for c in range(6):
				but=Fl_Button(c*150,r*150,150,150)
				but.color(FL_BACKGROUND2_COLOR)
				self.marvel=png_resiz_fltk('marvel.png',150,150)
				but.image(self.marvel)
				but.clear_visible_focus()
				but.callback(self.showimg)
				x+=1
				self.buttons.append(but)
		self.resizable(self)
		self.end()
	
	def showimg(self, w):
		i=self.buttons.index(w)
		if i in self.I: 
			#do nothing if same button. 
			return
	
		self.I.append(i)
		w.image(self.imgs[i]) #show image
		w.redraw()
		
		#check if same image
		if len(self.I)==2:
			if self.fnames[self.I[0]]==self.fnames[self.I[1]]:
				self.buttons[self.I[0]].deactivate()
				self.buttons[self.I[0]].image().inactive()
				self.buttons[self.I[1]].deactivate()
				self.buttons[self.I[1]].image().inactive()
				self.I.clear()
		elif len(self.I)==3:
			self.buttons[self.I[1]].image(self.marvel)
			self.buttons[self.I[1]].redraw()
			self.buttons[self.I[0]].image(self.marvel)
			self.buttons[self.I[0]].redraw()
			self.I.pop(1)
			self.I.pop(0)#order matters. Must remove in reverse order
    
		#check if win
		win=True
		for but in self.buttons:
			if but.active():
					win=False
					break
		if win:	
			fl_message('You Win!')

win = Marvel(900,600,'pyFLTK Memory')
win.show()

Fl.run()
