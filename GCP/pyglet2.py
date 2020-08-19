#!/usr/bin/env python3

# PURPOSE: inital forray into windowed applications / event-driven programming

import pyglet

window = pyglet.window.Window(width=400, height=300, caption='Test Window')

label1 = pyglet.text.Label('Hello World!', font_name='Times New Roman',
                          font_size=18, x=50, y=200)

label2 = pyglet.text.Label("Let's get this party started!", font_name='Helvetica',
                          font_size=18, x=100, y=160)

@window.event
def on_draw():
    window.clear()
    label1.draw()
    label2.draw()

pyglet.app.run()
