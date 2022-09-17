"""

"""

import os
import time
import math
import argparse

SCREEN_WIDTH = 10
SCREEN_HEIGHT = 10

FIRE = "🔥"

parser = argparse.ArgumentParser(description='Flickering fire simulation')
parser.add_argument('--showsteps', help="don't clear the terminal between steps")
parser.add_argument('--maxsteps', help="stop the simulation after a number of steps")
parser.add_argument('--stepdur', help="how long between steps")

args = parser.parse_args()

def clear():
    os.system('clear')

def loop(step_func, step_dur):
    step = 0
    while args.maxsteps != True or args.maxsteps > step:
        step_func(step)
        step += 1
        time.sleep(step_dur)
        if not args.showsteps:
            clear()

def fire(screen, step):
    cur_sin = abs(math.sin(step / math.pi))
    max_fire_height = math.ceil(cur_sin * SCREEN_HEIGHT)
    # print(cur_sin, max_fire_height)
    for i in range(0, max_fire_height):
        row = SCREEN_HEIGHT - i - 1
        screen[row] = [FIRE] * SCREEN_WIDTH

def step(step_count):
    screen = [["  "] * SCREEN_WIDTH] * SCREEN_HEIGHT
    fire(screen, step_count)
    print("⬜" * (SCREEN_WIDTH + 2))
    for row in screen:
        print("⬜" + "".join(row) + "⬜")
    print("⬜" * (SCREEN_WIDTH + 2))

loop(step, float(args.stepdur or 1))