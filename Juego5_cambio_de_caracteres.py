from random import *
from turtle import *
from freegames import path


contar = 1
lil_turtle = path('car.gif')
tiles = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E"]* 2
state = {'mark': None}
hide = [True] * 64

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    global contar
    
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        contar+=1 # Suma uno al tap


    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(lil_turtle)
    stamp()
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y+1)
        color('orange')
        write(tiles[mark], font=('Arial', 30, 'normal'), align="Center")
    
    
    up()
    goto(-180,230)
    write(contar, font=('Arial', 15, 'normal'), align="Center") 

    update()
    ontimer(draw, 100)












shuffle(tiles)
setup(420, 520, 370, 0)
addshape(lil_turtle)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
