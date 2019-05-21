from turtle import *
def draw_square(length,colors):
    speed(-1)
    color(colors)
    for i in range(4):
        forward(length)
        right(90)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
draw_square(200,'red')
mainloop()