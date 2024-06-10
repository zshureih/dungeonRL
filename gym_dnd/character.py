from .creature import Creature
from .classes import get_class_mapping
from src.utils import CharacterClass, CharacterRace

# Function to map class data to the corresponding class object
def map_class_data(class_data):
    class_mapping = get_class_mapping()
    return class_mapping[class_data["class"]](class_data)

# Class to represent a character sheet
class CharacterSheet(Creature):
    # Initialize a character sheet with data and id
    def __init__(self, data, id):
        super().__init__(data)
        self.id = id
        self.level = data["level"]
        self.character_class = CharacterClass(data["class_data"])
        self.proficiency_bonus = data["proficiency_bonus"]
        self.race = CharacterRace(data["race"])

        # Check if the character is a spellcaster
        self.spellcaster = data["spellcaster"]  # True or False
        if self.spellcaster:
            self.spellcasting_stat = self.class_type["spellcasting_stat"]

    # String representation of the character sheet
    def __str__(self):
        return super().__str__().replace("Creature", "Character")
