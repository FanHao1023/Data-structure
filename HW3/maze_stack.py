# Author: 林凡皓
# Date: 2024/4/14
# Purpose: Implement a maze solver that employs DFS, which is similar to maze.py.
#          However, maze_stach.py utilizes a stack-based approach instead of a
#          recursion approach.


import sys
sys.path.append("../pythonds3/")
from pythonds3.basic import Stack
import turtle
import os

START = "S"
OBSTACLE = "+"
TRIED = "."
DEAD_END = "-"
PART_OF_PATH = "O"

class Maze:
    def __init__(self, maze_filename, use_gui=True):
        with open(maze_filename, "r") as maze_file:
            self.maze_list = [
                [ch for ch in line.rstrip("\n")]
                for line in maze_file.readlines()
            ]
        self.rows_in_maze = len(self.maze_list)
        self.columns_in_maze = len(self.maze_list[0])
        for row_idx, row in enumerate(self.maze_list):
            if START in row:
                self.start_row = row_idx
                self.start_col = row.index(START)
                break

        self.x_translate = -self.columns_in_maze / 2
        self.y_translate = self.rows_in_maze / 2
        self.current_speed = 6  # Default speed
        self.use_gui = use_gui

        if self.use_gui:
            # Create the turtle and set its shape
            self.t = turtle.Turtle()
            #self.t.shape("turtle")
            self.wn = turtle.Screen()
            self.wn.register_shape("snor.gif")
            self.t.shape("snor.gif")
            self.wn.setworldcoordinates(
                -(self.columns_in_maze - 1) / 2 - 0.5,
                -(self.rows_in_maze - 1) / 2 - 0.5,
                (self.columns_in_maze - 1) / 2 + 0.5,
                (self.rows_in_maze - 1) / 2 + 0.5,
            )

    def draw_maze(self):
        if self.use_gui:  # Check if GUI should be used
            self.t.speed(10)
            self.wn.tracer(0)
            for y in range(self.rows_in_maze):
                for x in range(self.columns_in_maze):
                    if self.maze_list[y][x] == OBSTACLE:
                        self.draw_centered_box(
                            x + self.x_translate, -y + self.y_translate, "orange"
                        )
            self.t.color("black")
            self.t.fillcolor("blue")
            self.wn.update()
            self.wn.tracer(1)

    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x - 0.5, y - 0.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def update_position(self, row, col, val=None):
        if self.use_gui:  # Check if GUI should be used before updating the turtle position
            if val:
                self.maze_list[row][col] = val
            self.move_turtle(col, row)

            if val == PART_OF_PATH:
                color = "green"
            elif val == OBSTACLE:
                color = "red"
            elif val == TRIED:
                color = "black"
            elif val == DEAD_END:
                color = "red"
            else:
                color = None

            if color:
                self.drop_bread_crumb(color)
        else:
            # For non-GUI mode, simply update the maze structure without visual feedback
            if val:
                self.maze_list[row][col] = val

    def move_turtle(self, x, y):
        if self.use_gui:  # Check if GUI should be used
            self.t.up()
            self.t.setheading(self.t.towards(x + self.x_translate, -y + self.y_translate))
            self.t.goto(x + self.x_translate, -y + self.y_translate)

    def drop_bread_crumb(self, color):
        self.t.dot(10, color)

    def is_exit(self, row, col):
        return (
            row == 0
            or row == self.rows_in_maze - 1
            or col == 0
            or col == self.columns_in_maze - 1
        )

    def __getitem__(self, idx):
        return self.maze_list[idx]
    
    def set_speed(self, speed):
        self.current_speed = speed
        self.t.speed(speed)

    def start_interactive_control(self):
        self.wn.listen()
        self.wn.onkey(lambda: self.set_speed(10), "f")
        self.wn.onkey(lambda: self.set_speed(3), "n")
        self.wn.onkey(lambda: self.set_speed(1), "s")

def close_window(maze):
    maze.wn.bye()  # This method closes the turtle graphics window


##### Do not modify the code above

def search_from_stack(maze, start_row, start_column):
    # 使用stack來模擬遞迴的函數調用
    stack = Stack()
    stack.push((start_row, start_column))  
    path = []  

    while not stack.is_empty(): 
        row, column = stack.peek()

        # sucessfully find exit
        if maze.is_exit(row, column):
            maze.update_position(row, column, PART_OF_PATH)
            stack_reg = Stack()
            for i in range(stack.size()):
                p = stack.pop()
                stack_reg.push(p)
            for j in range(stack_reg.size()):
                p = stack_reg.pop()
                path.append(p)
            return True, path
        
        maze.update_position(row, column, TRIED)  # Mark the position as tried
        # path.append((row, column))
        
        # Up
        if maze[row-1][column] not in [TRIED, DEAD_END, OBSTACLE]:
            stack.push((row-1, column))
            # path.append((row-1, column))

        # Down
        elif maze[row+1][column] not in [TRIED, DEAD_END, OBSTACLE]:
            stack.push((row+1, column))
            # path.append((row+1, column))

        # Left    
        elif maze[row][column-1] not in [TRIED, DEAD_END, OBSTACLE]:
            stack.push((row, column-1))
            # path.append((row, column-1))

        # Right    
        elif maze[row][column+1] not in [TRIED, DEAD_END, OBSTACLE]:
            stack.push((row, column+1))
            # path.append((row, column+1))

        # Dead end    
        else:
            stack.pop()
            # path.pop()

    return False, []
     
##### Do not modify the code below


def main(maze_filename, correct_path_filename=None, use_gui=True):
    my_maze = Maze(maze_filename, use_gui=use_gui)

    if use_gui:
        my_maze.draw_maze()
        my_maze.update_position(my_maze.start_row, my_maze.start_col)
        my_maze.start_interactive_control()

    # Search for the path using the existing algorithm
    success, path = search_from_stack(my_maze, my_maze.start_row, my_maze.start_col)
    print("Search path:", path)

    if correct_path_filename:
        with open(correct_path_filename, "r") as path_file:
            correct_path = [(int(row), int(col)) for row, col in (line.split() for line in path_file)]
        print("Correct path:", correct_path)
        if path == correct_path:
            print("The search path matches the correct path!")
        else:
            print("The search path does not match the correct path.")

    if use_gui:
        my_maze.wn.listen()  # Listen for events
        my_maze.wn.onkey(lambda: close_window(my_maze), "q")  # Press 'q' to close the window
        my_maze.wn.mainloop()  # Start the main loop, waiting for events

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py maze.txt [correct_path.txt] [--nogui]")
    else:
        maze_filename = sys.argv[1]
        correct_path_filename = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] != "--nogui" else None
        use_gui = "--nogui" not in sys.argv
        main(maze_filename, correct_path_filename, use_gui)
        
     