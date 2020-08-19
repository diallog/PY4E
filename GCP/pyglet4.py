#!/usr/bin/env python3

# PURPOSE: inital forray into windowed applications / event-driven programming

import pyglet

window = pyglet.window.Window(width=400, height=300, caption='Test Window')

label = pyglet.text.Label('Nothing pressed yet.', font_name='Times New Roman',
                          font_size=18, x=50, y=200)

@window.event
def on_key_press(symbol, modifier):
    global label
    label = pyglet.text.Label('You pressed the '+key_pressed+' key.',
                              font_name='Times New Roman',
                              font_size=18, x=50, y=200)

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()
