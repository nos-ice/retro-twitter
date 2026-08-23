import pyxel
from frontend.text_field import TextField
from frontend.simple_text import SimpleText
from frontend.pointer import Pointer
from frontend.button import Button

width = 160
height = 120


class App:
    def __init__(self):
        pyxel.init(width, height, title="Pyxel App", fps=30)
        self.name_text = ""
        self.pw_text = ""        
        self.components = []
        self.name_focus = False
        self.pw_focus = False

        self.components.append(SimpleText(x=10, y=0, text="Name:"))
        self.name_field = TextField(x=10, y=10, width=140, height=10)
        self.components.append(self.name_field)
        self.components.append(SimpleText(x=10, y=20, text="PassWord:"))
        self.pw_field = TextField(x=10, y=30, width=140, height=10)
        self.components.append(self.pw_field)
        self.submit_buttton = Button(text="Login", x=10, y=50, width=30, height=10, on_click=self.submit)
        self.components.append(self.submit_buttton)

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
        return string

    def submit(self):
        print(f"Name: {self.name_text}, Password: {self.pw_text}")

    def update(self):
        for component in self.components:
            if hasattr(component, "update"):
                component.update()

        if self.name_field.mouse_over() and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.name_focus = True
            self.pw_focus = False
        if self.pw_field.mouse_over() and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.pw_focus = True
            self.name_focus = False

        self.name_field.text = self.name_text
        self.pw_field.text = self.pw_text
        if self.name_focus:
            self.name_text = self.string_input(self.name_text)
            self.name_field.text = self.name_text + "|"
        if self.pw_focus:
            self.pw_text = self.string_input(self.pw_text)
            self.pw_field.text = self.pw_text + "|"

    def draw(self):
        pyxel.cls(7)

        for component in self.components:
            component.draw()