import pyxel

class SimpleText:
    def __init__(self, x: int = 0, y: int = 0, text: str = ""):
        self.x = x
        self.y = y
        self.text = text

    def update(self):
        pass

    def draw(self):
        pyxel.text(self.x + 2, self.y + 2, self.text, 0)