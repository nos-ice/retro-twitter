import pyxel

class TextField:
    def __init__(self, x: int = 0, y: int = 0, width: int = 100, height: int = 20):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = ""

    def update(self):
        # A〜Z
        for i in range(26):
            if pyxel.btnp(pyxel.KEY_A + i):
                self.text += chr(ord("a") + i)

        # スペース
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.text += " "

        # バックスペース
        if pyxel.btnp(pyxel.KEY_BACKSPACE):
            self.text = self.text[:-1]

    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, 1)
        pyxel.text(self.x + 2, self.y + 2, self.text, 7)