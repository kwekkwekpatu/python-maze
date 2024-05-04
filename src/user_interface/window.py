from tkinter import Tk, BOTH, Canvas
from . import line

class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title("Maze runner")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, height=height, width=width)
        self.__canvas.pack()
        self.__running = False

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self) -> None:
        self.__running = False

    def draw_line(self, line, fill_color) -> None:
        line.draw(self.__canvas, fill_color)
