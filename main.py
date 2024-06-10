import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

import argparse

from gym_dnd.envs import combat

# random seeding
np.random.seed(42069)

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-r", "--rounds", type=int, default=10, help="number of rounds we do analysis over (JD's Turns)")
    parser.add_argument("-T", "--trials", type=int, default=100000, help="how many random trials (total combats) we test this over")

    args = parser.parse_args()
    
    return args

if __name__ == "__main__":
    args = parse_args()
    np.random.seed(int(time.time()))

    env = combat.DnDCombatEnv(config_file='gym_dnd/envs/config.json', rounds=args.rounds, trials=args.trials)
    env.reset()
    env.render()