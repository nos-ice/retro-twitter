import pyxel
from frontend.text_field import TextField
from frontend.simple_text import SimpleText
from frontend.pointer import Pointer

width = 160
height = 120


class App:
    def __init__(self):
        pyxel.init(width, height, title="Pyxel App", fps=30)
        self.name_text = ""
        self.pw_text = ""        
        self.components = []

        self.components.append(SimpleText(x=10, y=0, text="Name:"))
        self.name_field = TextField(x=10, y=10, width=140, height=10)
        self.components.append(self.name_field)
        self.components.append(SimpleText(x=10, y=20, text="PassWord:"))
        self.pw_field = TextField(x=10, y=30, width=140, height=10)
        self.components.append(self.pw_field)
        self.components.append(Pointer())

        pyxel.run(self.update, self.draw)

    def string_input(self, string: str) -> str:
        for i in range(26):
            if pyxel.btnp(pyxel.KEY_A + i):
                string += chr(ord("a") + i)

            if pyxel.btnp(pyxel.KEY_SPACE):
                string += " "

            if pyxel.btnp(pyxel.KEY_BACKSPACE):
                string = string[:-1]

            if pyxel.btnp(pyxel.KEY_RETURN):
                print(string)
        return string

    def update(self):
        self.name_text = self.string_input(self.name_text)
        self.name_field.text = self.name_text
        self.pw_text = self.string_input(self.pw_text)
        self.pw_field.text = self.pw_text

    def draw(self):
        pyxel.cls(7)

        for component in self.components:
            component.draw()
