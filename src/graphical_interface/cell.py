from tkinter import Canvas
from . import window, line, point
from typing import Self

class Cell:
    def __init__(self,
                 win: window.Window = None, 
                 has_left_wall=True, 
                 has_right_wall=True, 
                 has_top_wall=True, 
                 has_bottom_wall=True) -> None:
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False
        
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def draw(self, x1:int, y1:int, x2:int, y2:int) -> None:
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        point_lt = point.Point(x=self._x1, y=self._y1)
        point_lb = point.Point(x=self._x1, y=self._y2)
        point_rt = point.Point(x=self._x2, y=self._y1)
        point_rb = point.Point(x=self._x2, y=self._y2)

        fill_color = "black"
        no_color = "white"
        left_line = line.Line(point_a=point_lt, point_b=point_lb)
        if self.has_left_wall:
            self._win.draw_line(line=left_line, fill_color=fill_color)
        else:
            self._win.draw_line(line=left_line, fill_color=no_color)

        right_line = line.Line(point_a=point_rt, point_b=point_rb)
        if self.has_right_wall:
            self._win.draw_line(line=right_line, fill_color=fill_color)
        else:
            self._win.draw_line(line=right_line, fill_color=no_color)

        top_line = line.Line(point_a=point_lt, point_b=point_rt)
        if self.has_top_wall:
            self._win.draw_line(line=top_line, fill_color=fill_color)
        else:
            self._win.draw_line(line=top_line, fill_color=no_color)
        
        bottom_line = line.Line(point_a=point_lb, point_b=point_rb)
        if self.has_bottom_wall:
            self._win.draw_line(line=bottom_line, fill_color=fill_color)
        else:
            self._win.draw_line(line=bottom_line, fill_color=no_color)

    def draw_move(self, to_cell: Self, undo=False) -> None:
        line_color = "red"
        if undo:
            line_color = "gray"
        center_line = line.Line(self.get_center(), to_cell.get_center())
        if self._win:
            self._win.draw_line(line=center_line, fill_color=line_color)
        
    def get_center(self) -> point.Point:
        x = (self._x1 + self._x2) / 2
        y = (self._y1 + self._y2) / 2
        return point.Point(x=x,y=y)
    