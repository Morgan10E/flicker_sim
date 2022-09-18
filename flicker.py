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

FIRE = "🔥"

parser = argparse.ArgumentParser(description='Flickering fire simulation')
parser.add_argument('--showsteps', help="don't clear the terminal between steps")
parser.add_argument('--maxsteps', help="stop the simulation after a number of steps")
parser.add_argument('--stepdur', default=1, type=float, help="how long between steps")

args = parser.parse_args()

play_screen = screen.Screen(SCREEN_WIDTH, SCREEN_HEIGHT, "  ")

def fire(play_screen, step):
    middle_point = math.floor(SCREEN_WIDTH / 2 + random.randrange(-1,1))
    cur_sin = abs(math.sin(step / math.pi))
    max_fire_height = math.ceil(cur_sin * SCREEN_HEIGHT)
    # print(cur_sin, max_fire_height)
    for i in range(SCREEN_HEIGHT):
        screen_i = SCREEN_HEIGHT - i - 1
        if i <= max_fire_height:
            for k in range(middle_point):
                if max_fire_height / middle_point * k > i:
                    play_screen.set_point(k, screen_i, FIRE)

            for k in range(middle_point, SCREEN_WIDTH):
                if -max_fire_height / (SCREEN_WIDTH - middle_point) * (k - middle_point) + max_fire_height > i:
                    play_screen.set_point(k, screen_i, FIRE)

def step(step_count):
    play_screen.clear()
    fire(play_screen, step_count)
    play_screen.print()

print(args)
looper = player.Player(step, args.stepdur, args.maxsteps, args.showsteps)

looper.loop()