"""

"""

import os
import time
import math
import argparse
import random

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
    middle_point = math.floor(SCREEN_WIDTH / 2 + random.randrange(-1,1))
    cur_sin = abs(math.sin(step / math.pi))
    max_fire_height = math.ceil(cur_sin * SCREEN_HEIGHT)
    # print(cur_sin, max_fire_height)
    for i in range(SCREEN_HEIGHT):
        screen_i = SCREEN_HEIGHT - i - 1
        if i <= max_fire_height:
            for k in range(middle_point):
                if max_fire_height / middle_point * k > i:
                    screen[screen_i][k] = FIRE

            for k in range(middle_point, SCREEN_WIDTH):
                if -max_fire_height / (SCREEN_WIDTH - middle_point) * (k - middle_point) + max_fire_height > i:
                    screen[screen_i][k] = FIRE

def step(step_count):
    screen = [["  "] * SCREEN_WIDTH for i in range(SCREEN_HEIGHT)]
    fire(screen, step_count)
    print("⬜" * (SCREEN_WIDTH + 2))
    for row in screen:
        print("⬜" + "".join(row) + "⬜")
    print("⬜" * (SCREEN_WIDTH + 2))

loop(step, float(args.stepdur or 1))