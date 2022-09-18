"""

"""

import os
import time
import math
import argparse
import random
import screen
import player

SCREEN_WIDTH = 10
SCREEN_HEIGHT = 10

CELL_CHANCE = 0.5

FIRE = "🔥"

class Range:
    def __init__(self, min, max):
        self.min = min
        self.max = max
    
    def is_in_range(self, val):
        return self.min <= val <= self.max

ADD_RANGE = Range(3,3)
SURVIVE_RANGE = Range(2,3)
TOLERANCE = 2

play_screen = screen.Screen(SCREEN_WIDTH, SCREEN_HEIGHT, "  ")

parser = argparse.ArgumentParser(description='Flickering fire simulation')
parser.add_argument('--showsteps', help="don't clear the terminal between steps")
parser.add_argument('--maxsteps', help="stop the simulation after a number of steps")
parser.add_argument('--stepdur', default=1, type=float, help="how long between steps")

args = parser.parse_args()


"""
The active board is the 'current' sim.
When we step the simulation, we create the new state on the inactive board
then switch the inactive board to be the active one.
"""
class CellSim:
    def __init__(self, width, height, add_range, survive_range, cell_chance, tolerance):
        self._sim_boards = [[[False] * width for i in range(height)] for k in range(2)]
        self._sim_board_x_range = Range(0, width - 1)
        self._sim_board_y_range = Range(0, height - 1)
        self._active_board_idx = 0
        self._add_range = add_range
        self._survive_range = survive_range
        self._tolerance = tolerance

        for y in range(height):
            for x in range(width):
                if random.random() < cell_chance:
                    self._active_board[y][x] = True

    def _get_num_neighbors(self, x, y):
        num_neighbors = 0
        for i in range(-1,2):
            for k in range(-1,2):
                if i == 0 and k == 0:
                    continue
                if self._sim_board_x_range.is_in_range(x + i) and self._sim_board_y_range.is_in_range(y+k):
                    if self._active_board[y + k][x + i]:
                        num_neighbors += 1
        return num_neighbors

    def _is_alive(self, x, y):
        return self._active_board[y][x]

    def step_sim(self):
        for y in range(len(self._active_board)):
            for x in range(len(self._active_board[0])):
                tolerance = y / len(self._active_board) * self._tolerance
                survive_range = Range(self._survive_range.min - tolerance, self._survive_range.max + tolerance)
                add_range = Range(self._add_range.min - tolerance, self._add_range.max + tolerance)
                self._inactive_board[y][x] = False
                neighbors = self._get_num_neighbors(x, y)
                if self._is_alive(x, y):
                    if survive_range.is_in_range(neighbors):
                        self._inactive_board[y][x] = True
                else:
                    if add_range.is_in_range(neighbors):
                        self._inactive_board[y][x] = True

        self._active_board_idx = (1 + self._active_board_idx) % 2

    @property
    def _active_board(self):
        return self._sim_boards[self._active_board_idx] 

    @property
    def _inactive_board(self):
        return self._sim_boards[(1 + self._active_board_idx) % 2]

    def get_state(self):
        return self._active_board

cell_sim = CellSim(SCREEN_WIDTH, SCREEN_HEIGHT, ADD_RANGE, SURVIVE_RANGE, CELL_CHANCE, TOLERANCE)

def step(step_count):
    play_screen.clear()
    state = cell_sim.get_state()
    for y in range(len(state)):
        for x in range(len(state[0])):
            if state[y][x]:
                play_screen.set_point(x, y, FIRE)
    play_screen.print()
    cell_sim.step_sim()

looper = player.Player(step, args.stepdur, args.maxsteps, args.showsteps)


looper.loop()