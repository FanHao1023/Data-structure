# Author: 林凡皓
# Date: 2024/5/22
# Purpose: Read and understand build_graph(), search_from_graph_dfs.
#          Implement maze searching algorithm using bfs and dijkstra.


import sys
sys.path.append("../../../../pythonds3/")
from pythonds3.basic import Stack, Queue
from pythonds3.graphs import Graph, Vertex
from pythonds3.trees.priority_queue import PriorityQueue
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


def build_graph(maze):
    graph = Graph()
    rows = len(maze)
    cols = len(maze[0])
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] != OBSTACLE:
                node_id = f"{r}-{c}"
                if node_id not in graph._vertices:
                    graph.set_vertex(node_id)
                # Check adjacent cells and add edges if they're not obstacles
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Directions: Up, Down, Left, Right
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != OBSTACLE:
                        neighbor_id = f"{nr}-{nc}"
                        if neighbor_id in graph._vertices:
                            # Add an edge in both directions
                            graph.add_edge(node_id, neighbor_id)
                            graph.add_edge(neighbor_id, node_id)
    return graph


def search_from_graph_dfs(maze, graph, start_row, start_col):
    start_id = f"{start_row}-{start_col}"
    start_vertex = graph.get_vertex(start_id)
    if not start_vertex:
        return False, []

    stack = Stack()  
    path = []  # Initialize an empty list to keep track of the path
    graph._time = 0  # Reset time counter for discovery and closing times

    # Start DFS with the initial vertex
    stack.push(start_vertex)
    start_vertex.color = "gray"
    start_vertex.discovery_time = graph._time
    maze.update_position(start_row, start_col, TRIED)  # Mark the initial position
    graph._time += 1

    while not stack.is_empty():
        vertex = stack.peek()  # Peek at the top vertex using the Stack class
        all_neighbors_visited = True
        row, col = map(int, vertex.key.split('-'))

        if vertex.color == "white":
            vertex.color = "gray"
            vertex.discovery_time = graph._time
            graph._time += 1
            maze.update_position(row, col, TRIED)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < maze.rows_in_maze and 0 <= nc < maze.columns_in_maze:
                neighbor_id = f"{nr}-{nc}"
                neighbor = graph.get_vertex(neighbor_id)
                if neighbor and neighbor.color == "white":
                    stack.push(neighbor)
                    neighbor.previous = vertex  # Set the previous vertex
                    all_neighbors_visited = False
                    break  # Stop and explore this new neighbor first

        if all_neighbors_visited:
            if vertex.color == "gray":  # Ensure it is processed only once
                vertex.color = "black"
                vertex.closing_time = graph._time
                graph._time += 1
                stack.pop()  # Fully processed, pop from stack

                if maze.is_exit(row, col):
                    maze.update_position(row, col, PART_OF_PATH)
                    path.append((row, col))
                    trace_vertex = vertex
                    while trace_vertex.previous:
                        trace_vertex = trace_vertex.previous
                        r, c = map(int, trace_vertex.key.split('-'))
                        maze.update_position(r, c, PART_OF_PATH)
                        path.append((r, c))
                    path.reverse()
                    return True, path

    return False, []


##### Do not modify the code above
def search_from_graph_bfs(maze, graph, start_row, start_col):
    # Your code here
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    start_id = f"{start_row}-{start_col}"
    start_vertex = graph.get_vertex(start_id)
    if not start_vertex:
        return False, []

    queue = Queue()  
    path = []  # Initialize an empty list to keep track of the path
    graph._time = 0  # Reset time counter for discovery and closing times

    # Start DFS with the initial vertex
    queue.enqueue(start_vertex)
    start_vertex.color = "gray"
    start_vertex.discovery_time = graph._time
    maze.update_position(start_row, start_col, TRIED)  # Mark the initial position
    graph._time += 1

    while not queue.is_empty():
        vertex = queue.dequeue()  # get the front vertex in queue
        # all_neighbors_visited = True
        row, col = map(int, vertex.key.split('-'))

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < maze.rows_in_maze and 0 <= nc < maze.columns_in_maze:
               neighbor_id = f"{nr}-{nc}"
               neighbor = graph.get_vertex(neighbor_id)
               if neighbor and neighbor.color == "white":
                    queue.enqueue(neighbor)
                    neighbor.color = "gray"
                    neighbor.discovery_time = graph._time
                    graph._time += 1
                    neighbor.previous = vertex  
                    maze.update_position(nr, nc, TRIED)

                    # check if exit
                    if maze.is_exit(nr, nc):
                        maze.update_position(nr, nc, PART_OF_PATH)
                        path.append((nr, nc))
                        trace_vertex = neighbor
                        # back trace to get path
                        while trace_vertex.previous:
                            trace_vertex = trace_vertex.previous
                            r, c = map(int, trace_vertex.key.split('-'))
                            maze.update_position(r, c, PART_OF_PATH)
                            path.append((r, c))
                        path.reverse()
                        return True, path
        vertex.color = 'black'
        vertex.closing_time = graph._time
        graph._time += 1

    return False, []



def search_from_graph_dijkstra(maze, graph, start_row, start_col):
    # Your code here
    start_id = f"{start_row}-{start_col}"
    start_vertex = graph.get_vertex(start_id)
    
    if not start_vertex:
        return False, []

    priority_queue = PriorityQueue()
    start_vertex.distance = 0  # initialize distance
    priority_queue.insert((start_vertex.distance, start_vertex))  # put start vertex and distance into priority queue
    visited = set()  # a set to record visited vertex

    path = []

    while not priority_queue.is_empty():
        current_distance, current_vertex = priority_queue.delete()
        print(f"current distance : {current_distance}")
        row, col = map(int, current_vertex.key.split('-'))
        visited.add(current_vertex)

        # check if exit
        if maze.is_exit(row, col):
            maze.update_position(row, col, PART_OF_PATH)
            path.append((row, col))
            trace_vertex = current_vertex
            # back trace to get path
            while trace_vertex.previous:
                trace_vertex = trace_vertex.previous
                r, c = map(int, trace_vertex.key.split('-'))
                maze.update_position(r, c, PART_OF_PATH)
                path.append((r, c))
            path.reverse()
            return True, path

        
        for next_v in current_vertex.get_neighbors():
            if next_v in visited:
                continue
            # distance = current_distance + current_vertex.get_neighbor(next_v)
            distance = current_distance + 1  # all edge has the same weight
            print(f"new distance : {distance}")
            # check if need to update distance
            if distance < next_v.distance:
                next_v.distance = distance
                next_v.previous = current_vertex
                if next_v in priority_queue:
                    priority_queue.change_priority(next_v, distance)  # update distance
                else:
                    priority_queue.insert((distance, next_v))  # create new vertex and distance

    return False, []


##### Do not modify the code below
def main(maze_filename, use_gui=True, algorithm='dfs', correct_path_filename=None):
    
    my_maze = Maze(maze_filename, use_gui=use_gui)
    graph = build_graph(my_maze.maze_list)
    # Reinitialize the maze for visualization and algorithm execution
    if use_gui:
        my_maze.draw_maze()
        my_maze.update_position(my_maze.start_row, my_maze.start_col)
        my_maze.start_interactive_control()

    # Execute the selected search algorithm
    if algorithm == 'dfs':
        success, path = search_from_graph_dfs(my_maze, graph, my_maze.start_row, my_maze.start_col)
    elif algorithm == 'bfs':
        success, path = search_from_graph_bfs(my_maze, graph, my_maze.start_row, my_maze.start_col)
    else:  # Dijkstra
        success, path = search_from_graph_dijkstra(my_maze, graph, my_maze.start_row, my_maze.start_col)

    header = f"{'Key':^8}|{'Color':^8}|{'Distance':^8}|{'Discover':^4}|{'Closing':^4}|{'Previous':^8}"
    print(header)
    # Print vertex states post-DFS
    for key in graph.get_vertices():
        vertex = graph.get_vertex(key)
        print(vertex)

    # Output the path from the selected algorithm
    print(f"Selected algorithm ({algorithm}) path:", path)
    if success:
        print(f"Path to exit found by {algorithm}. Total path length: {len(path)-1}")
    else:
        print(f"No path found by {algorithm}.")

    # Compare paths based on the algorithm used
    if correct_path_filename:
        with open(correct_path_filename, "r") as path_file:
            correct_path = [(int(row), int(col)) for row, col in (line.split() for line in path_file)]
        print("Correct path from file:", correct_path)
        if path == correct_path:
            print("The search path matches the correct path!")
        else:
            print("The search path does not match the correct path.")

    # Setup GUI interactions if applicable
    if use_gui:
        my_maze.wn.listen()  # Listen for events
        my_maze.wn.onkey(lambda: close_window(my_maze), "q")  # Press 'q' to close the window
        my_maze.wn.mainloop()  # Start the main loop, waiting for events

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py maze.txt [algorithm] [correct_path.txt] [--nogui]")
    else:
        maze_filename = sys.argv[1]
        algorithm = 'dfs'  # Default algorithm
        correct_path_filename = None
        use_gui = True

        # Process additional command line arguments
        for arg in sys.argv[2:]:
            if arg == "--nogui":
                use_gui = False
            elif arg in ['dfs', 'bfs', 'dijkstra']:
                algorithm = arg
            else:
                correct_path_filename = arg

        main(maze_filename, use_gui, algorithm, correct_path_filename)

        
     
