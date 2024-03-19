import gym
from gym import spaces
import gym_dnd.spells as spells
from gym_dnd.character import Character
import json

print(len(spells))

class DnDCombatEnv(gym.Env):
    def __init__(self, ):
        super(DnDCombatEnv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions
        self.action_space = spaces.Tuple(
            (
                spaces.Discrete(10),  # 10 types of actions
                spaces.Discrete(len(spells)),  # Number of spells
            )
        )
        self.observation_space = spaces.Box(low=0, high=100, shape=(1,))

        self._init_game_state(config_file='config.json')

    def _create_characters(self, characters_data):
        characters = []
        for data in characters_data:
            characters.append(Character(data))
        return characters
    
    def _init_game_state(self, config_file):
        # read the conifg file and set the game state
        with open(config_file, 'r') as f:
            config = json.load(f)

        self.player_characters = self._create_chracters(config['player_characters'])
        self.enemy_creatures = config['enemy_creatures']
        self.initiative_order = self._get_initiative_order()
        self.current_actor = self.initiative_order[0][0] # get the first actor from the initiative order

    def _get_initiative_order(self):
        # roll initiative for all characters and sort them
        initiative_order = []
        for character in self.player_characters + self.enemy_creatures:
            initiative_order.append((character, character.roll_initiative()))

        initiative_order.sort(key=lambda x: x[1], reverse=True)
        return initiative_order

    def step(self, action):
        action_type, action_param = action

        if action_type == 0:  # Attack
            # Perform an attack
            ...
        elif action_type == 1:  # Cast a spell
            # Cast the selected spell
            self.spells[action_param].cast()
            ...
        # Handle other action types...
        # ...

        # Compute your observation, reward, done and info
        observation = ...
        reward = ...
        done = ...
        info = ...

        return observation, reward, done, info

    def reset(self):
        # Reset the state of the environment to an initial state
        self._init_game_state()

    def render(self, mode="human"):
        # Render the environment to the screen
        ...
