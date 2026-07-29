from room import *
class Maze:
    def __init__(self):
        self.maze = []
    def add_room(self):
        self.room = Room()
        self.maze.append(self.room)
    def get_maze(self):
        return self.maze
    
        