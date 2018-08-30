class Text:
    def __init__(self, canvas):
        self.canvas = canvas
        self.exist = False

    def set(self, x, y, text, color, font_size):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.size = font_size

    def draw(self):
        self.canvas.create_text(self.x, self.y, text=self.text, fill=self.color, font=('System', self.size))
