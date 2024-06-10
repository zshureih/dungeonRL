from enum import Enum
from src.utils import Dice, AttackSave, CharacterClass

# Mapping enum values to class names
def get_class_mapping():
    return {
        CharacterClass.BARBARIAN: Barbarian,
        CharacterClass.BARD: Bard,
        CharacterClass.CLERIC: Cleric,
        CharacterClass.DRUID: Druid,
        CharacterClass.FIGHTER: Fighter,
        CharacterClass.MONK: Monk,
        CharacterClass.PALADIN: Paladin,
        CharacterClass.RANGER: Ranger,
        CharacterClass.ROGUE: Rogue,
        CharacterClass.SORCERER: Sorcerer,
        CharacterClass.WARLOCK: Warlock,
        CharacterClass.WIZARD: Wizard,
    }

max_spell_level_by_level = {
    "full": {
        1: 1,
        2: 1,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 4,
        8: 4,
        9: 5,
        10: 5,
        11: 6,
        12: 6,
        13: 7,
        14: 7,
        15: 8,
        16: 8,
        17: 9,
        18: 9,
        19: 9,
        20: 9,
    },
    "half": {

    },
    "third": {
        
    },
    "none": None
}

# Class definitions
class Barbarian:
    def __init__(self, level):
        self.name = "Barbarian"
        self.hit_die = Dice.D12
        self.saving_throw_proficiencies = [AttackSave.STR, AttackSave.CON]
        
        self.rage_count_by_level = {
            1: 2,
            2: 2,
        }
        self.rage_count = 2
        self.rage_damage_bonus = 2

    def rage(self):
        if self.rage_count > 0:
            self.rage_count -= 1
            return True
        else:
            return False
        
class Bard:
    def __init__(self, class_data):
        self.name = "Bard"
        self.hit_die = Dice.D8
        self.saving_throw_proficiencies = [AttackSave.DEX, AttackSave.CHA]
        self.spellcasting_ability = "Charisma"
        
        self.max_spell_level_by_level = max_spell_level_by_level['full']
        self.max_spell_level = self.max_spell_level_by_level[class_data['level']]
        
        self.bardic_inspiration = class_data['spellcasting_ability_mod']
        self.bardic_inspiration_die = Dice.D6

    def bardic_inspire(self):
        if self.bardic_inspiration > 0:
            self.bardic_inspiration -= 1
            return True
        else:
            return False
        
    def cast_spell(self, spell):
        if spell.level <= self.max_spell_level:
            return spell(self.spellcasting_ability)
        else:
            return "You don't have a spell slot of that level."

class Cleric:
    def __init__(self, level):
        self.name = "Cleric"
        self.hit_die = Dice.D8
        self.saving_throw_proficiencies = [AttackSave.WIS, AttackSave.CHA]
        self.spellcasting_ability = "Wisdom"
        
        self.max_spell_level_by_level = max_spell_level_by_level['full']
        self.max_spell_level = self.max_spell_level_by_level[level]
    
    def cast_spell(self, spell):
        if spell.level <= self.max_spell_level:
            return spell(self.spellcasting_ability)
        else:
            return "You don't have a spell slot of that level."


class Druid:
    def __init__(self, level):
        self.name = "Druid"
        self.hit_die = Dice.D8
        self.saving_throw_proficiencies = [AttackSave.INT, AttackSave.WIS]
        self.spellcasting_ability = "Wisdom"
        
        self.max_spell_level_by_level = max_spell_level_by_level['full']
        self.max_spell_level = self.max_spell_level_by_level[level]

    def cast_spell(self, spell):
        if spell.level <= self.max_spell_level:
            return spell(self.spellcasting_ability)
        else:
            return "You don't have a spell slot of that level."

class Fighter: 
    def __init__(self, level):
        self.name = "Fighter"
        self.hit_die = Dice.D10
        self.saving_throw_proficiencies = [AttackSave.STR, AttackSave.CON]
        
        self.max_spell_level_by_level = max_spell_level_by_level['none']
        self.max_spell_level = 0

class Monk:
    def __init__(self, level):
        self.name = "Monk"
        self.hit_die = Dice.D8
        self.saving_throw_proficiencies = [AttackSave.STR, AttackSave.DEX]
        
        self.max_spell_level_by_level = max_spell_level_by_level['none']
        self.max_spell_level = 0
        self.ki_points = level

class Paladin:
    def __init__(self, level):
        self.name = "Paladin"
        self.hit_die = Dice.D10
        self.saving_throw_proficiencies = [AttackSave.WIS, AttackSave.CHA]
        
        self.max_spell_level_by_level = max_spell_level_by_level['half']
        self.max_spell_level = self.max_spell_level_by_level[level]

    def cast_spell(self, spell):
        if spell.level <= self.max_spell_level:
            return spell(self.spellcasting_ability)
        else:
            return "You don't have a spell slot of that level."

class Ranger:
    def __init__(self, level):
        self.name = "Ranger"
        self.hit_die = Dice.D10
        self.saving_throw_proficiencies = [AttackSave.STR, AttackSave.DEX]
        
        self.max_spell_level_by_level = max_spell_level_by_level['half']
        self.max_spell_level = self.max_spell_level_by_level[level]

    def cast_spell(self, spell):
        if spell.level <= self.max_spell_level:
            return spell(self.spellcasting_ability)
        else:
            return "You don't have a spell slot of that level."

class Rogue:
    def __init__(self, level):
        self.name = "Rogue"
        self.hit_die = Dice.D8
        self.saving_throw_proficiencies = [AttackSave.DEX, AttackSave.INT]
        
        self.max_spell_level_by_level = max_spell_level_by_level['none']
        self.max_spell_level = 0

class Sorcerer:
    def __init__(self, level):
        self.name = "Sorcerer"
        self.hit_die = Dice.D6
        self.saving_throw_proficiencies = [AttackSave.CON, AttackSave.CHA]
        self.spellcasting_ability = "Charisma"
        
        self.max_spell_level_by_level = max_spell_level_by_level['full']
        self.max_spell_level = self.max_spell_level_by_level[level]

    def cast_spell(self, spell):
        if spell.level <= self.max_spell_level:
            return spell(self.spellcasting_ability)
        else:
            return "You don't have a spell slot of that level."
    
class Warlock:
    def __init__(self, level):
        self.name = "Warlock"
        self.hit_die = Dice.D8
        self.saving_throw_proficiencies = [AttackSave.WIS, AttackSave.CHA]
        self.spellcasting_ability = "Charisma"
        
        self.max_spell_level_by_level = max_spell_level_by_level['full']
        self.max_spell_level = self.max_spell_level_by_level[level]
    
    def cast_spell(self, spell):
        if spell.level <= self.max_spell_level:
            return spell(self.spellcasting_ability)
        else:
            return "You don't have a spell slot of that level."
    
class Wizard:
    def __init__(self, level):
        self.name = "Wizard"
        self.hit_die = Dice.D6
        self.saving_throw_proficiencies = [AttackSave.INT, AttackSave.WIS]
        self.spellcasting_ability = "Intelligence"
        
        self.max_spell_level_by_level = max_spell_level_by_level['full']
        self.max_spell_level = self.max_spell_level_by_level[level]
    
    def cast_spell(self, spell):
        if spell.level <= self.max_spell_level:
            return spell(self.spellcasting_ability)
        else:
            return "You don't have a spell slot of that level."