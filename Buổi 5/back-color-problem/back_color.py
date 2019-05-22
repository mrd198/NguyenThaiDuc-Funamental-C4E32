from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    list_text = []
    list_color = []
    for shape in shapes:
        list_text.append(shape["text"])
        list_color.append(shape["color"])
    text = choice(list_text)
    color = choice(list_color)
    return [
                'RED',
                '#4CAF50',
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    choose_color = 0
    choose_text = 0
    for choose_shape in shapes:
        if is_inside([x,y],choose_shape["rect"]):
            choose_color = choose_shape["color"]
            choose_text = choose_shape["text"]
    if quiz_type == 0:
        if choose_text == text:
            return True
        else: return False
    elif quiz_type == 1:
        if choose_color == color:
            return True
        else: return False
