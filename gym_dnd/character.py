from .conditions import Conditions
from .abilities import AbilityScores
from .skills import CharacterSkills
from .classes import get_class_mapping
from src.utils import CharacterClass, CharacterRace

def map_class_data(class_data):
    class_mapping = get_class_mapping()
    return class_mapping[class_data['class']](class_data)

class CharacterSheet:
    def __init__(self, data):
        self.name = data['name']
        self.race = CharacterRace(data['race'])
        self.level = data['level']
        self.character_class = CharacterClass(data['class_data'])
        self.speed = data['speed']

        self.proficiency_bonus = data['proficiency_bonus']
        
        self.health = data['health']
        self.max_health = data['max_health']
        self.armor_class = data['armor_class']

        self.stats = AbilityScores()
        self.skills = CharacterSkills()
        self.conditions = Conditions()

        # Add more attributes and methods as needed
        self._set_stats(data['stats']) 
        self._set_skills(data['skills'])

        self.spellcaster = data['spellcaster'] # True or False
        if self.spellcaster:
            self.spellcasting_stat = self.class_type['spellcasting_stat']

    def _set_stats(self, stats):
        for stat_name, value in stats.items():
            self.set_stat(stat_name, value)
    
    def _set_skills(self, skills):
        for skill_name, value in skills.items():
            self.set_skill(skill_name, value)

    def set_stat(self, stat_name, value):
        if stat_name in self.stats:
            self.stats[stat_name] = value
        else:
            raise ValueError(f"Invalid stat name: {stat_name}")

    def set_skill(self, skill_name, value):
        if skill_name in self.skills:
            self.skills[skill_name] = value
        else:
            raise ValueError(f"Invalid skill name: {skill_name}")

    def get_stat(self, stat_name):
        return self.stats[stat_name]
    
    def get_skill(self, skill_name):
        return self.skills[skill_name]
    
    def get_actions(self):
        """
        Get the list of actions that the character can perform
        """
        # get class actions
        # get default actions
        return 