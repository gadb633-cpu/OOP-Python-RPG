from player import User
from config import config
from maze import *

class Main:

    def __init__(self):
        self.player=User(config)
        self.maze=Maze(self.player)

    def print_starting_massage(self):
        print("\n=== Wellcome to Battle Maze game! ===\n")

    def visit_rooms(self):
        for i in range(3):
            if self.player.is_alive():
                enter_room=input(f"Do you want to go into room {i+1}? (yes/no) ")
                if enter_room == "yes":
                    print(f"\nYou are now in room {i+1}")
                    self.maze.rooms_in_maze[i].create_battle()
                    self.maze.visited_rooms+=1
                else:
                    break
                 
    def print_game_summary(self):
        print(f"\nGame over! {self.player.name} visited in {self.maze.visited_rooms} rooms")

    def run_game(self):
        self.print_starting_massage()
        self.maze.create_rooms()
        self.visit_rooms()
        self.print_game_summary()

game=Main()
game.run_game()

