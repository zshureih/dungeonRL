class Monster:
    def __init__(self, name, hit_points, armor_class, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.name = name
        self.hit_points = hit_points
        self.armor_class = armor_class
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

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
        return f"Monster: {self.name}, HP: {self.hit_points}, AC: {self.armor_class}"