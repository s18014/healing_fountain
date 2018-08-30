from time import time


class Input:
    def __init__(self, root):
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.space = False
        self.last_press_time = 0
        root.bind_all('<KeyPress>', self.keyPress)
        root.bind_all('<KeyRelease>', self.keyUp)

    def keyPress(self, e):
        self.last_press_time = time()
        key = e.keysym
        if key == 'Up':
            self.up = True
        if key == 'Down':
            self.down = True
        if key == 'Right':
            self.right = True
        if key == 'Left':
            self.left = True
        if key == 'space':
            self.space = True

    def keyUp(self, e):
        self.last_press_time = time()
        key = e.keysym
        if key == 'Up':
            self.up = False
        if key == 'Down':
            self.down = False
        if key == 'Right':
            self.right = False
        if key == 'Left':
            self.left = False
        if key == 'space':
            self.space = False
