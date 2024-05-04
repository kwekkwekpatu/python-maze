from tkinter import Canvas
from . import point

class Line:
    def __init__(self, point_a, point_b) -> None:
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_color) -> None:
        x1, y1 = self.point_a.x, self.point_a.y
        x2, y2 = self.point_b.x, self.point_b.y

        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width= 2)