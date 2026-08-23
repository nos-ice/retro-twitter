import pyxel

class Button:
    def __init__(self, text: str, x: int = 0, y: int = 0, width: int = 100, height: int = 20, on_click: callable = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.on_click = on_click

    def update(self):
        if self.mouse_over() and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if self.on_click:
                self.on_click()

    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, 1)
        pyxel.text(self.x + 2, self.y + 2, self.text, 7)

    def mouse_over(self) -> bool:
        return self.x <= pyxel.mouse_x <= self.x + self.width and self.y <= pyxel.mouse_y <= self.y + self.height