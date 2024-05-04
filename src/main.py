from user_interface import window, point, line, cell

def main():
    win = window.Window(800, 600)
    point_a = point.Point()
    point_b = point.Point(400, 300)
    line_a = line.Line(point_a, point_b)
    line_color = "red"
    win.draw_line(line=line_a, fill_color=line_color)

    cell_1 = cell.Cell(x1=0, x2=200, y1=0, y2=100, win=win)
    cell_1.draw()

    cell_2 = cell.Cell(x1=200, x2=400, y1=0, y2=100, win=win, has_right_wall=False, has_left_wall=False)
    cell_2.draw()
    cell_1.draw_move(cell_2)
    cell_3 = cell.Cell(x1=400, x2=600, y1=300, y2=400, win=win)
    cell_3.draw()
    cell_2.draw_move(cell_3, undo=True)
    win.wait_for_close()


if __name__ == "__main__":
    main()