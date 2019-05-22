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
    if quiz_type == 0:
        for i in shapes:
            if i['text'] == text:
                toa_do = i['rect']
    else:
        for i in shapes:
            if i['color'] == color:
                toa_do = i['rect']
    if toa_do[0] <= x <= toa_do[0] + toa_do[2] and toa_do[1] <= y <= toa_do[1] + toa_do[3]:
        return True
    else:
        return False
