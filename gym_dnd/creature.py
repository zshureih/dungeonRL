from .conditions import Conditions
from .abilities import AbilityScores
from .skills import CharacterSkills
from .classes import get_class_mapping

import random

def map_class_data(class_data):
    class_mapping = get_class_mapping()
    return class_mapping[class_data["class"]](class_data)


class Creature:
    def __init__(self, data):
        self.name = data["name"]
        self.size = data["size"]
        self.speed = data["speed"]
        self.position = data["position"]
        self.race = data["race"]

        self.current_health = data["current_health"]
        self.max_health = data["max_health"]
        self.armor_class = data["armor_class"]

        self.stats = AbilityScores()
        self.skills = CharacterSkills()
        self.conditions = Conditions()

        # Add more attributes and methods as needed
        self._set_stats(data["stats"])
        self._set_skills(data["skills"])

    def _set_stats(self, stats):
        for stat_name, value in stats.items():
            self.set_stat(stat_name, value)

    def _set_skills(self, skills):
        for skill_name, value in skills.items():
            self.skills.set_skill_proficiency(skill_name, value)

    def set_stat(self, stat_name, value):
        if stat_name in self.stats:
            self.stats[stat_name] = value
        else:
            raise ValueError(f"Invalid stat name: {stat_name}")

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
        return []

    def attack(self):
        # Implement the logic for the monster's attack here
        pass

    def take_damage(self, damage):
        # Implement the logic for the monster taking damage here
        pass

    def is_alive(self):
        # Implement the logic to check if the monster is alive here
        pass

    def __str__(self):
        return f"Creature: {self.name}, HP: {self.current_health}, AC: {self.armor_class}"

    def roll_initiative(self):
        initiative = random.randint(1, 20) + self.stats["dexterity"][1]
        print(f"{self.name} rolled {initiative} for initiative")
        return initiative

class Monster(Creature):
    def __init__(self, data, i):
        super().__init__(data)
        self.id = -1 * i

    def __str__(self):
        return super().__str__()
