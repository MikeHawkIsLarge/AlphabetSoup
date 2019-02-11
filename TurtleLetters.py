import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":#Goutham's 5
	    pass
    elif letter == "C":
	    pass
    elif letter == "D":
	    pass
    elif letter == "E":
	    pass
    elif letter == "F":
	    pass
    elif letter == "G":#Carter's 5
	    pass		
    elif letter == "H":
	    pass
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":#Gabe's5
	    pass
    elif letter == "M":
	    pass
    elif letter == "N":
	    pass
    elif letter == "O":
	    pass
    elif letter == "P":
	    pass		
    elif letter == "Q":#Nick's 5
	    pass
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.left(30)
        tur.fd(40)
        tur.left(120)
        tur.fd(40)
        tur.left(30)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)

    elif letter == "W":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.left(30)
        tur.fd(40)
        tur.left(130)
        tur.fd(15)
        tur.right(130)
        tur.fd(15)
        tur.left(130)
        tur.fd(40)
        tur.left(20)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)

    elif letter == "X":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.left(45)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.right(180)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.right(180)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.pu()
        tur.left(45)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)

    elif letter == "Y":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.left(90)
        tur.right(50)
        tur.fd(25)
        tur.right(40)
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(40)
        tur.fd(25)
        tur.pu()
        #fix
        tur.left(40)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)


    elif letter == "Z":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()     
        tur.left(90)
        tur.fd(30)
        tur.right(135)
        tur.forward(40)
        tur.left(135)
        tur.forward(30)
        #fix
        tur.pu()
        tur.left(90)
        tur.fd(40)
        tur.right(90)

    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        turtleLetter("box",tur)
	
2






window = turtle.Screen()
tur = turtle.Turtle()
tur.speed(1)
#turtleLetter("box",tur)
turtleLetter("A",tur)


window.exitonclick()
