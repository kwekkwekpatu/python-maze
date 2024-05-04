from . import cell, window
import time
import random

class Maze:
    def __init__(self,
                 x1: float,
                 y1: float,
                 num_rows: int,
                 num_cols: int,
                 cell_size_x: float,
                 cell_size_y: float,
                 win: window.Window = None,
                 seed: any = None,
                 ) -> None:
        self._cells = []
        self._x1 = x1
        self._y1 = y1

        self._num_rows = num_rows
        self._num_cols = num_cols

        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._random = 0
        if seed:
            self.random = random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

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

    def _break_walls_r(self, i: int, j:int) -> None:
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            new_list = self._get_adjacent_to_visit(i,j)
            if len(new_list) == 0:
                self._draw_cell(i,j)
                return
            # choose a random direction
            direction_index = random.randrange(len(new_list))
            random_direction = new_list[direction_index]
            # break the wall
            next_x = random_direction[0]
            next_y = random_direction[1]
            next_cell = self._cells[next_x][next_y]
            if next_x < i:
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif next_x > i:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            elif next_y < j:
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif next_y > j:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            # move to direction
            self._break_walls_r(next_x,next_y)

    def _get_adjacent_to_visit(self, i:int, j:int) -> list:
        to_visit = []
        # left
        if i > 0 and not self._cells[i - 1][j].visited:
            to_visit.append((i-1,j))
        # right
        if i < self._num_cols-1 and not self._cells[i + 1][j].visited:
            to_visit.append((i+1,j))
        # up
        if j > 0 and not self._cells[i][j - 1].visited:
            to_visit.append((i,j-1))
        # down
        if j < self._num_rows-1 and not self._cells[i][j + 1].visited:
            to_visit.append([i,j+1])
        return to_visit
    
    def _reset_cells_visited(self) -> None:
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def _get_adjacent_without_walls(self, i:int, j:int) -> list:
        to_visit = []
        current_cell = self._cells[i][j]
        # left
        if i > 0 and not self._cells[i - 1][j].visited and not current_cell.has_left_wall:
            to_visit.append((i-1,j))
        # right
        if i < self._num_cols-1 and not self._cells[i + 1][j].visited and not current_cell.has_right_wall:
            to_visit.append((i+1,j))
        # up
        if j > 0 and not self._cells[i][j - 1].visited and not current_cell.has_top_wall:
            to_visit.append((i,j-1))
        # down
        if j < self._num_rows-1 and not self._cells[i][j + 1].visited and not current_cell.has_bottom_wall:
            to_visit.append([i,j+1])
        return to_visit

    def solve(self) -> bool:
        return self._solve_r()
        
    def _solve_r(self, i:int = 0, j:int = 0) -> bool:
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        to_visit = self._get_adjacent_without_walls(i, j)
        for target in to_visit:
            next_cell = self._cells[target[0]][target[1]]
            current_cell.draw_move(to_cell=next_cell)
            is_right_way = self._solve_r(target[0], target[1])
            if is_right_way:
                return True
            current_cell.draw_move(to_cell=next_cell, undo=True)
        return False

