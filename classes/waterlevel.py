import random
import time
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def process_intruption():
    time.sleep(1)


class Tank:
    def __init__(self, capacity, rndusagemax):
        self.maxcap = capacity
        self.capacity = capacity
        self.rndusagemax = rndusagemax

    def generate_usage(self):
        return random.randrange(0, self.rndusagemax)

    def decrease_capacity(self):
        self.capacity -= random.randrange(0, self.rndusagemax)
        process_intruption()
        # Clearing the Screen
        os.system('cls')
        print("Decreasing.... Capacity of Tank is", ("%.1f" %((self.capacity / self.maxcap)*100)),"%")
        return self.capacity

    def increase_capacity(self):
    
        self.capacity += random.randrange(0, self.rndusagemax)
        if (self.capacity>self.maxcap):
            self.capacity=self.maxcap    
        process_intruption()
        # Clearing the Screen
        os.system('cls')
        print("Increasing.... Capacity of Tank is", ("%.1f" %((self.capacity / self.maxcap)*100)),"%")
        return self.capacity

    def get_capacity(self):
        return self.capacity
