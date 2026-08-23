import pyxel

class Pointer:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        # マウスカーソル
        x = pyxel.mouse_x
        y = pyxel.mouse_y

        # 矢印型カーソル
        pyxel.rect(x, y, 1, 1, 0)
