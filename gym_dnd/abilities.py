class AbilityScores:
    def __init__(self):
        self.scores = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0,
        }
        self.modifiers = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0,
        }
    
    def __getitem__(self, key):
        return self.scores[key], self.modifiers[key]
    
    def __setitem__(self, key, value):
        self.scores[key] = value
        self.modifiers[key] = self._calculate_modifier(value)

    def _calculate_modifier(self, score):
        return (score - 10) // 2
    
    def __iter__(self):
        return iter(self.scores.keys())
