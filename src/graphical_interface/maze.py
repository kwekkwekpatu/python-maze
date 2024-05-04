from . import cell, window
import time

class Maze:
    def __init__(self,
                 x1: float,
                 y1: float,
                 num_rows: int,
                 num_cols: int,
                 cell_size_x: float,
                 cell_size_y: float,
                 win: window.Window = None,
                 ) -> None:
        self._cells = []
        self._x1 = x1
        self._y1 = y1

        self._num_rows = num_rows
        self._num_cols = num_cols

        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self) -> None:
        for column in range(self._num_cols):
            temp_list = []
            for row in range(self._num_rows):          
                temp_list.append(cell.Cell(self._win))
            self._cells.append(temp_list)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int) -> None:
        if self._win is None:
            return
        temp_x1 = self._x1 + i * self._cell_size_x
        temp_x2 = self._x1 + (i + 1) * self._cell_size_x
        temp_y1 = self._y1 + j * self._cell_size_y
        temp_y2 = self._y1 + (j + 1) * self._cell_size_y

        self._cells[i][j].draw(x1=temp_x1, x2=temp_x2, 
                                           y1=temp_y1, y2=temp_y2)
        self._animate()
    
    def _animate(self) -> None:
        if self._win:
            self._win.redraw()
            time.sleep(0.05)

    def _break_entrance_and_exit(self) -> None:
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)