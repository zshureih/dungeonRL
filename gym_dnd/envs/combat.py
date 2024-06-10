import gym
from gym import spaces
import gym_dnd.spells as spells
from gym_dnd.character import CharacterSheet
from gym_dnd.creature import Monster
import json
import numpy as np
import cv2
import matplotlib.pyplot as plt

class DnDCombatEnv(gym.Env):
    def __init__(self, config_file='gym_dnd/envs/config.json', rounds=10, trials=100000):
        super(DnDCombatEnv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions
        self.action_space = spaces.Tuple(
            (
                spaces.Discrete(10),  # 10 types of actions for instance
            )
        )
        self.config_file = config_file
        self._init_game_state(self.config_file)

    def _create_characters(self, characters_data):
        characters = []
        print("Adding the following Player Characters")
        for i, data in enumerate(characters_data):
            new_character = CharacterSheet(data, i+1)
            print(new_character)
            characters.append(new_character)
        return characters

    def _create_creatures(self, creatures_data):
        creatures = []
        print("Adding the following Monsters")
        for i, data in enumerate(creatures_data):
            new_monster = Monster(data, i+1)
            print(new_monster)
            creatures.append(new_monster)
        return creatures

    def _place_characters(self, shape=(10, 10, 1)):
        self.state = np.zeros(shape, dtype=np.int8)
        for i, character in enumerate(self.player_characters):
            self.state[character.position[0]][
                character.position[1]
            ] = character.id
        for i, creature in enumerate(self.enemy_creatures):
            self.state[creature.position[0]][
                creature.position[1]
            ] = creature.id

    def _init_game_state(self, config_file='gym_dnd/envs/config.json'):
        # read the conifg file and set the game state
        with open(config_file, 'r') as f:
            config = json.load(f)

        self.player_characters = self._create_characters(config['player_characters'])
        self.enemy_creatures = self._create_creatures(config['enemy_creatures'])
        self.initiative_order = self._get_initiative_order()
        print(f"Initiative Order is {self.initiative_order}")

        # set the observation space as a 2D grid of the map
        # with each cell containing the id of the character or creature
        # or 0 if the cell is empty
        self.observation_space = spaces.Box(
            low=-255,
            high=255,
            shape=(config["map"]["rows"], config["map"]["cols"], 1),
            dtype=np.int8,
        )

        # TODO: implement hazards
        # self._place_hazards(config['hazards']) # place the hazards on the map

        # place the characters on the map
        self._place_characters(shape=(config["map"]["rows"], config["map"]["cols"], 1))

        self.current_actor = self.initiative_order[0][1] # get the first actor from the initiative order

    def _get_initiative_order(self):
        # roll initiative for all characters and sort them
        initiative_order = []
        for character in self.player_characters + self.enemy_creatures:
            initiative_order.append((character.name, character, character.roll_initiative()))

        initiative_order.sort(key=lambda x: x[2], reverse=True)
        return initiative_order

    def step(self, action):
        # Execute one time step within the environment
        action_type, action_param = action




        return observation, reward, done, info

    def reset(self, config_file=None):
        # Reset the state of the environment to an initial state
        if config_file != None:
            self.config_file = config_file
        self._init_game_state(self.config_file)

    def render(self):
        # Render the environment to the screen
        img = np.zeros(self.state.shape, dtype=np.uint8)
        for character in self.player_characters + self.enemy_creatures:
            print(character.id)
            if character.id > 0:
                img = cv2.rectangle(img, character.position, character.position, 100 + character.id, -1)
            else:
                img = cv2.rectangle(img, character.position, character.position, 255 + character.id, -1)

        # make a grid
        plt.xticks(ticks=np.arange(0.5, img.shape[1]+0.5, 1))
        plt.yticks(ticks=np.arange(0.5, img.shape[0]+0.5, 1))
        plt.grid()

        plt.imshow(img)
        plt.show()
