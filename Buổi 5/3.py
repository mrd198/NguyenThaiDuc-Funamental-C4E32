from turtle import *
def draw_square(length,colors):
    speed(-1)
    color(colors)
    for i in range(4):
        forward(length)
        right(90)
draw_square(200,'red')
mainloop()