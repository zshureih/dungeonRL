import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

import argparse

from jd_spells import *

#GLOBAL ASSUMPTIONS
state = {
    "player": {
        "name": "JD Caulfield",
        "hp": 50,
        "max_hp": 50,
        "ac": 18,
        "atk_bonus": 5,
        "spell_save_dc": 16,
        "spell_slots": {
            "1st_level": 3,
            "2nd_level": 2,
            "3rd_level": 1
        }
    },
    "enemy": {
        "name": "Enemy",
        "hp": 60,
        "max_hp": 60,
        "ac": 15,
        "save_bonus": 3
    },
    "round": 1,
    "status": "ongoing"
}



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

    # let's get the histogram of quickened energy ebb
    qe_unique, qe_counts = np.unique(quickened_ebb(args), return_counts=True)
    plt.bar(qe_unique, qe_counts/args.trials, label=f"Probability of Exhaustion Count After {args.rounds} Rounds of Combat")
    plt.title(f"Probability of Exhaustion Count After {args.rounds} Rounds of Combat")
    plt.show()

    # let's do a study of empowered Arcane Eruption
    r1, r2, r3 = empowered_eruption(args)
    r1_unique, r1_counts = np.unique(r1, return_counts=True)
    r2_unique, r2_counts = np.unique(r2, return_counts=True)
    r3_unique, r3_counts = np.unique(r3, return_counts=True)
    plt.bar(r1_unique, r1_counts/args.trials, label=f"r1, avg_change={np.mean(r1)}")
    plt.bar(r2_unique, r2_counts/args.trials, label=f"r2, avg_change={np.mean(r2)}")
    plt.bar(r3_unique, r3_counts/args.trials, label=f"r3, avg_change={np.mean(r3)}")
    plt.title(f"Probability of Damage Increase on Empowered Arcane Eruption")
    plt.legend()
    plt.show()