class Conditions():
    def __init__(self):
        self.conditions = {
            "blinded": {
                "description": "A blinded creature can't see and automatically fails any ability check that requires sight. Attack rolls against the creature have advantage, and the creature's attack rolls have disadvantage.",
                "duration": "Varies",
                "affected": False,
            },
            "charmed": {
                "description": "A charmed creature can't attack the charmer or target the charmer with harmful abilities or magical effects. The charmer has advantage on any ability check to interact socially with the creature.",
                "duration": "Varies",
                "affected": False,
            },
            "deafened": {
                "description": "A deafened creature can't hear and automatically fails any ability check that requires hearing.",
                "duration": "Varies",
                "affected": False,
            },
            "frightened": {
                "description": "A frightened creature has disadvantage on ability checks and attack rolls while the source of its fear is within line of sight. The creature can't willingly move closer to the source of its fear.",
                "duration": "Varies",
                "affected": False,
            },
            "grappled": {
                "description": "A grappled creature's speed becomes 0, and it can't benefit from any bonus to its speed. The condition ends if the grappler is incapacitated (see the condition). The condition also ends if an effect removes the grappled creature from the reach of the grappler or grappling effect, such as when a creature is hurled away by the thunderwave spell.",
                "duration": "Varies",
                "affected": False,
            },
            "incapacitated": {
                "description": "An incapacitated creature can't take actions or reactions.",
                "duration": "Varies",
                "affected": False,
            },
            "invisible": {
                "description": "An invisible creature is impossible to see without the aid of magic or a special sense. For the purpose of hiding, the creature is heavily obscured. The creature's location can be detected by any noise it makes or any tracks it leaves.",
                "duration": "Varies",
                "affected": False,
            },
            "paralyzed": {
                "description": "A paralyzed creature is incapacitated (see the condition) and can't move or speak.",
                "duration": "Varies",
                "affected": False,
            },
            "petrified": {
                "description": "A petrified creature is transformed, along with any nonmagical object it is wearing or carrying, into a solid inanimate substance (usually stone). Its weight increases by a factor of ten, and it ceases aging. The creature is incapacitated (see the condition), can't move or speak, and is unaware of its surroundings.",
                "duration": "Varies",
                "affected": False,
            },
            "poisoned": {
                "description": "A poisoned creature has disadvantage on attack rolls and ability checks.",
                "duration": "Varies",
                "affected": False,
            },
            "prone": {
                "description": "A prone creature's only movement option is to crawl, unless it stands up and thereby ends the condition. The creature has disadvantage on attack rolls. An attack roll against the creature has advantage if the attacker is within 5 feet of the creature. Otherwise, the attack roll has disadvantage.",
                "duration": "Varies",
                "affected": False,
            },
            "restrained": {
                "description": "A restrained creature's speed becomes 0, and it can't benefit from any bonus to its speed. Attack rolls against the creature have advantage, and the creature's attack rolls have disadvantage. The creature has disadvantage on Dexterity saving throws.",
                "duration": "Varies",
                "affected": False,
            },
            "stunned": {
                "description": "A stunned creature is incapacitated (see the condition), can't move, and can speak only falteringly. The creature automatically fails Strength and Dexterity saving throws. Attack rolls against the creature have advantage.",
                "duration": "Varies",
                "affected": False,
            },
            "unconscious": {
                "description": "An unconscious creature is incapacitated (see the condition), can't move or speak, and is unaware of its surroundings. The creature drops whatever it's holding and falls prone.",
                "duration": "Varies",
                "affected": False,
            },
            "exhaustion": {
                "description": "Modifier to attack rolls, ability checks, saving throws, and spell save DC. The creature loses a level of exhaustion after a long rest.",
                "duration": "Varies",
                "count": 0,
            }
        }

    def __getitem__(self, condition):
        return self.conditions[condition]
    
    def __setitem__(self, condition, value):
        self.conditions[condition] = value 

    def __contains__(self, condition):
        return condition in self.conditions
    
    def __iter__(self):
        return iter(self.conditions)
    
    def __len__(self):
        return len(self.conditions)
    
    def affected(self):
        return [condition for condition in self.conditions if condition['affected']]
    
    def __str__(self) -> str:
        # return a pretty formatted string of the conditions the character is affected by
        return str(self.affected())