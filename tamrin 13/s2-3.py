from graphics import *

win=GraphWin("test",300,300)

center=Point(150,150)
c=Circle(center,100)
c.draw(win)
c.setFill("gray")
t=Text(center,"Hi")         
t.draw(win) 
