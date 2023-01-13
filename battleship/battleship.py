from fltk import *
class BattleshipSelf(Fl_Window):
    BL = []
    def __init__(self, x, y, width, height):
        Fl_Window.__init__(self, width, height)
        self.begin()
        XB =[]
        YB = []
        for col in range(10):
            for row in range(10):
                BattleshipSelf.BL.append(Fl_Button(col*30+30,row*30+30, 30,30))
                BattleshipSelf.BL[-1].callback(self.but_cb)
                
        for x in range(11):
            XB.append(Fl_Box(x*30,0, 30,30))
            
        for y in range(10):
            YB.append(Fl_Box(0,30+y*30, 30,30))
        self.end()
        
        for xbut in range(1, 11):
            XB[xbut].label(chr(64+xbut))
            XB[xbut].deactivate()
        XB[0].deactivate()
            
        for ybut in range(10):
            YB[ybut].label(str(ybut+1))
            YB[ybut].deactivate()
            
        self.resizable(self)

    def but_cb(self, wid):
        pass
    
class BattleshipOther(BattleshipSelf):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)    

    def but_cb(self, wid):
        x = BattleshipOther.BL.index(wid)
        BattleshipSelf.BL[x].value(1)
        print(BattleshipOther.BL[x], 'aaaaaaaaaaaa')
        print(BattleshipSelf.BL[x])
        
if __name__ == "__main__":
    gameSelf = BattleshipSelf(0, 0, 330, 330)
    gameOther = BattleshipOther(330, 330, 330, 330)
    gameSelf.show()
    gameOther.show()
    Fl.run()