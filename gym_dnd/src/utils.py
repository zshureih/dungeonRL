import numpy as np
from enum import Enum

def enemy_saving_throw(args):
    saving_throw = np.random.randint(20) + 1
    
    # if the result less than my DC, they fail their saving throw
    if (saving_throw + args['ENEMY_SAVE_BONUS'] - args['ENEMY_EXHAUSTION']) < (args['SPELL_SAVE_DC'] - args['PLAYER_EXHAUSTION']):
        return 0
    else:
        return 1


class CharacterClass(Enum):
    BARBARIAN = "Barbarian"
    BARD = "Bard"
    CLERIC = "Cleric"
    DRUID = "Druid"
    FIGHTER = "Fighter"
    MONK = "Monk"
    PALADIN = "Paladin"
    RANGER = "Ranger"
    ROGUE = "Rogue"
    SORCERER = "Sorcerer"
    WARLOCK = "Warlock"
    WIZARD = "Wizard"

class CharacterRace(Enum):
    DWARF = "Dwarf"
    ELF = "Elf"
    HALFLING = "Halfling"
    HUMAN = "Human"
    DRAGONBORN = "Dragonborn"
    GNOME = "Gnome"
    HALF_ELF = "Half-Elf"
    HALF_ORC = "Half-Orc"
    TIEFLING = "Tiefling"

class ActionEconomy(Enum):
    ACTION = "Action"
    BONUS_ACTION = "Bonus Action"
    REACTION = "Reaction"
    FREE_ACTION = "Free Action"
    INTERACTION = "Interaction"
    MOVE = "Move"

class Dice(Enum):
    D4 = 4
    D6 = 6
    D8 = 8
    D10 = 10
    D12 = 12
    D20 = 20
    D100 = 100

class CastingTime(Enum):
    ACTION = "1 action"
    BONUS_ACTION = "1 bonus action"
    REACTION = "1 reaction"
    MINUTE = "1 minute"
    HOUR = "1 hour"
    RITUAL = "Ritual"

class AttackSave(Enum):
    MELEE = "Melee Attack"
    RANGED = "Ranged Attack"
    SPELL = "Spell Attack"
    DEX = "Dexterity Saving Throw"
    CON = "Constitution Saving Throw"
    STR = "Strength Saving Throw"
    INT = "Intelligence Saving Throw"
    WIS = "Wisdom Saving Throw"
    CHA = "Charisma Saving Throw"
