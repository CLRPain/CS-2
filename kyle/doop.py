from curses import color_content


class Dog:

    alive = 0

    def __init__(self, color='white', breed='mutt'):
        print(' a dog is born')
        self.color=color
        self.breed=breed
        Dog.alive += 1
        
    def speak(self):
        print('ruf ruf')
        
    def __str__(self):
        return(f'this dog is a {self.color} {self.breed}')
    
    def __del__(self):
        print(f'the {self.color} {self.breed} dog died')
        Dog.alive -= 1
        
def birth():
    fido3 = Dog()
    print('fido3 in func', id(fido3))
    print('in funct birth', Dog.alive)
    

fido1=Dog()  #init is called when a dog is created
fido2=Dog('black', 'lab')
fido1.speak()
fido2.speak()
print(fido1)
print(fido2)

print('before birth func call',Dog.alive) # 2
birth()
#print fido3 #this line fails since fido3 no longer exists after func birth() (it was garbage collected)

print('after birth func call',Dog.alive)  # 2
input()

A=[]
for x in range(10):
    A.append(Dog())
print('after loop',Dog.alive)
