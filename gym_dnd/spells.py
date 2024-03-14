import numpy as np
from utils import enemy_saving_throw, AttackSave, CastingTime, Dice
"""
Each function in this file pertains to a spell a creature with the spellcasting ability can cast. 
"""

# Let's try to and organize spells like callable classess
class Spell:
    level: int = None
    casting_time: CastingTime = None
    range: int = None
    area: str =  None
    components: str = None
    concentration: bool = None
    duration: str = None
    attack_save: AttackSave = None

    def __call__(self) -> None:
        pass

class EnergyEbb(Spell):
    """
    When you cast this spell, and as an action on each of your turns until the spell ends, you can target one creature you can see within range.
    If the target isn't undead, it must succeed on a constitution saving through or take 4d8 necrotic damage and suffer one level of exhaustion
    If the targe is undead, you instead roll 4d8; the target gains half the total as temporary hit points

    When you cast this spell using a slot of 5th level or higher, the damage and temporary hit point dice increase by 1d8 for each slot level above 4th
    """
    def __init__(self, level=4):
        super().__init__()
        self.level = level
        self.casting_time = CastingTime.ACTION
        self.range = 60
        self.components = 'V,S'
        self.concentration = True
        self.duration = '1 minute'
        self.attack_save = AttackSave.CON
        self.damage_die = Dice.D8

    def average_damage(self) -> float:
        # Calculate average damage of 4d8
        average_per_die = (1 + self.damage_die) / 2
        num_dice = self.level
        average_total_damage = average_per_die * num_dice
        return average_total_damage

    def __call__(self, state: dict) -> tuple:
        # if the enemy makes the save, nothing happens
        if enemy_saving_throw(state):
            return 0, []
        else:
            # otherwise we give the enemy a point of exahustion and do 4d8
            state['ENEMY_EXHAUSTION'] += 1
            dice_roll = np.random.randint(1, self.damage_die + 1, size=np.max(4, self.level))
            return np.sum(dice_roll), dice_roll

class HoldMonster(Spell):
    """
    Choose a creature that you can see within range. The target must succeed on a Wisdom saving throw or be paralyzed for the duration.
    This spell has no effect on undead. At the end of each of its turns, the target can make another Wisdom saving throw. On a success, the spell ends on the target.
    """
    def __init__(self, level=5):
        super().__init__()
        self.level = level
        self.casting_time = CastingTime.ACTION
        self.range = 90
        self.components = 'V,S,M (a small, straight piece of iron)'
        self.concentration = True
        self.duration = '1 minute'
        self.attack_save = AttackSave.WIS

    def __call__(self, state: dict) -> tuple:
        if enemy_saving_throw(state):
            return 0, []
        else:
            return None, None  # Placeholder for spell effects

def _energy_ebb(state, exhaustion):
    # cause an enemy to make a save
    saving_throw = np.random.randint(20) + 1
    
    # if they make the result is less than my DC, they take another point of exhaustion
    if (saving_throw + state['ENEMY_SAVE_BONUS'] - exhaustion) < state['SPEL_SAVE_DC']:
        return 1
    else:
        return 0

def energy_ebb(state):
    results = []
    for trial in range(state.trials):
        # we are starting combat, the enemy has nothing done to them
        enemy_exhaustion = 0

        for round in range(state.rounds):
            # now we count all of our action based energy ebbs
            enemy_exhaustion += _energy_ebb(state, enemy_exhaustion)
            
            # # max exhaustion is 10, creature dies outright at that point
            if enemy_exhaustion == 10:
                break
        
        results.append(enemy_exhaustion)

    return results

def quickened_ebb(state):
    results = []
    for trial in range(state.trials):
        # we are starting combat, the enemy has nothing done to them
        enemy_exhaustion = 0

        # we get an "extra" energy ebb at the beginning of the first round (this is a bonus action technically)
        enemy_exhaustion += _energy_ebb(state, enemy_exhaustion)

        for round in range(state.rounds):
            # now we count all of our action based energy ebbs
            enemy_exhaustion += _energy_ebb(state, enemy_exhaustion)
            
            # # max exhaustion is 10, creature dies outright at that point
            if enemy_exhaustion == 10:
                break
        
        results.append(enemy_exhaustion)

    return results

def empowered_eruption(state):
    # empowered allows us to reroll up to 5 damage dice on a spell
    # arcane eruption is a spell that does full damage and triggers an effect on a failed save and half damage on a success
    results_1 = []
    results_2 = []
    results_3 = []
    for trial in range(state.trials):
        # let's start with rolling our damage, cause it determines our effect. We'll do a study on enemy saves in the next step
        initial = sorted(np.random.randint(6, size=6) + 1)
        init_sum = np.sum(initial)
        final = []
        
        # our goal is roll exactly one 1 or 2, and then reroll the rest for max damage
        initial_vals, initial_counts = np.unique(initial, return_counts=True)
        
        # if we have our desired number already, re-roll for optimal damage
        if initial_vals[0] == 1 or initial_vals[0] == 2:
            final.append(initial.pop(0)) # add our first value to final
            
            new_vals, new_counts = np.unique(initial, return_counts=True)
            for i, val in enumerate(new_vals):
                if val <= 3:
                    # if lte 3, reroll the dice
                    new_dice = np.random.randint(6, size=new_counts[i]) + 1
                    final.extend(new_dice)
                else:
                    final.extend([val] * new_counts[i])

            final_sum = np.sum(final)

            results_1.append(final_sum - init_sum)
        elif initial_vals[0] == 3:
            # we need to pick our lowest value (3s in this case, and reroll them)
            new_dice = np.random.randint(6, size=min(initial_counts[0], 5)) + 1
            final.extend(new_dice)

            # now add the highest values from before
            final.extend(initial[min(initial_counts[0], 5):])

            final_sum = np.sum(final)
            results_2.append(final_sum - init_sum)
        else:
            # everything is 4, 5 or 6, just reroll 1 of our lowest values
            new_dice = np.random.randint(6) + 1
            final.append(new_dice)
            final.extend(initial[1:])

            final_sum = np.sum(final)
            results_3.append(final_sum - init_sum)
    
    return results_1, results_2, results_3