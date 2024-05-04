from tkinter import Canvas
from . import window, line, point

class Cell:
    def __init__(self, x1, x2, y1, y2, win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True) -> None:
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def draw(self) -> None:
        point_lt = point.Point(x=self._x1, y=self._y1)
        point_lb = point.Point(x=self._x1, y=self._y2)
        point_rt = point.Point(x=self._x2, y=self._y1)
        point_rb = point.Point(x=self._x2, y=self._y2)

        fill_color = "black"
        if self.has_left_wall:
            left_line = line.Line(point_a=point_lt, point_b=point_lb)
            self._win.draw_line(line=left_line, fill_color=fill_color)
        if self.has_right_wall:
            right_line = line.Line(point_a=point_rt, point_b=point_rb)
            self._win.draw_line(line=right_line, fill_color=fill_color)
        if self.has_top_wall:
            top_line = line.Line(point_a=point_lt, point_b=point_rt)
            self._win.draw_line(line=top_line, fill_color=fill_color)
        if self.has_bottom_wall:
            bottom_line = line.Line(point_a=point_lb, point_b=point_rb)
            self._win.draw_line(line=bottom_line, fill_color=fill_color)

    def draw_move(self, to_cell, undo=False) -> None:
        line_color = "red"
        if undo:
            line_color = "gray"
        center_line = line.Line(self.get_center(), to_cell.get_center())
        self._win.draw_line(line=center_line, fill_color=line_color)
        
    def get_center(self) -> point.Point:
        x = (self._x1 + self._x2) / 2
        y = (self._y1 + self._y2) / 2
        return point.Point(x=x,y=y)