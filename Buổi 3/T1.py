from turtle import *
colors = ["red","blue","brown","yellow","grey"]

shape("turtle")
speed(-1)

for i in range(3,3+len(colors),1):
    color(colors[i-3])
    for j in range(i):
        forward(100)
        left(360/i)
        
mainloop()