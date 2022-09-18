"""

"""

import os
import time

class Player:
    def __init__(self, step_func, step_dur, max_steps, show_steps):
        self.step_func = step_func
        self.step_dur = step_dur
        self.max_steps = max_steps
        self.show_steps = show_steps
        self.step = 0

    def clear(self):
        os.system('clear')

    def loop(self):
        while self.max_steps != True or self.max_steps > self.step:
            self.step_func(self.step)
            self.step += 1
            time.sleep(self.step_dur)
            if not self.show_steps:
                self.clear()