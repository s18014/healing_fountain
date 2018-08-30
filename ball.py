class Ball:
    def __init__(self, canvas):
        self.canvas_h = canvas.winfo_reqheight()
        self.canvas_w = canvas.winfo_reqwidth()
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.size = 0
        self.onGround = False
        self.onWall = False
        self.onRoof = False
        self.exist = False

    def set(self, x, y, size, color):
        self.exist = True
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, canvas):
        canvas.create_oval(self.x - self.size, self.y - self.size, self.x + self.size, self.y + self.size, fill=self.color, outline="")

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def returnToWindow(self):
        if self.y - self.size < 0:
            self.y = self.size
        if self.y + self.size > self.canvas_h:
            self.y = self.canvas_h - self.size
        if self.x - self.size < 0:
            self.x = self.size
        if self.x + self.size > self.canvas_w:
            self.x = self.canvas_w - self.size

    def outOfwindow(self):
        if self.y - self.size > self.canvas_h:
            self.exist = False
        if self.x + self.size < 0:
            self.exist = False
        if self.x - self.size > self.canvas_w:
            self.exist = False
