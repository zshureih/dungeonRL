from enum import Enum

class Proficiency(Enum):
    NONE = 0.0
    HALF = 0.5
    FULL = 1.0
    EXPERT = 2.0

class CharacterSkills:
    def __init__(self):
        self.proficiencies = {
            'acrobatics': Proficiency.NONE,
            'animal_handling': Proficiency.NONE,
            'arcana': Proficiency.NONE,
            'athletics': Proficiency.NONE,
            'deception': Proficiency.NONE,
            'history': Proficiency.NONE,
            'insight': Proficiency.NONE,
            'intimidation': Proficiency.NONE,
            'investigation': Proficiency.NONE,
            'medicine': Proficiency.NONE,
            'nature': Proficiency.NONE,
            'perception': Proficiency.NONE,
            'performance': Proficiency.NONE,
            'persuasion': Proficiency.NONE,
            'religion': Proficiency.NONE,
            'sleight_of_hand': Proficiency.NONE,
            'stealth': Proficiency.NONE,
            'survival': Proficiency.NONE
        }

    def add_skill(self, skill_name, proficiency):
        self.skills[skill_name] = proficiency

    def remove_skill(self, skill_name):
        if skill_name in self.skills:
            del self.skills[skill_name]

    def get_skill_proficiency(self, skill_name):
        return self.skills.get(skill_name, Proficiency.NONE)

    def set_skill_proficiency(self, skill_name, proficiency):
        self.skills[skill_name] = proficiency