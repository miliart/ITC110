#draw a pine
#A program to draw an oject of choice using graphics.py
#by Gabriela Milillo

from graphics import *

def main():
    win = GraphWin("Draw a pine tree", 400, 400)
    '''This is a commment: coordicates set with the origin point in the lower left hand corner 0.0, 0.0
    upper right hand corner to 10.0, 10.0. it is a scaled coordinates system, at  scale of 10 instead of 100. I still have a 400 px window '''
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    #draw the third triangle
    p1 = Point(5,7)
    p2 = Point(1,3)
    p3 = Point(9,3)
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("green")
    triangle.draw(win)


    #draw the second triangle
    p1 = Point(5,8)
    p2 = Point(2,5)
    p3 = Point(8,5)
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("green")
    triangle.draw(win)

    #draw the first triangle
    p1 = Point(5,10)
    p2 = Point(3,7)
    p3 = Point(7,7)
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("green")
    triangle.draw(win)

    #draw rectangle
    p1 = Point(4,3)
    p2 = Point(6,1)
    rect = Rectangle(p1, p2)
    rect.setFill("brown")
    rect.draw(win)


    
    p1.draw(win)
    p2.draw(win)
    p3.draw(win)
  
    


   
main()



    
    

    

   

    

    
