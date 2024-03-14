import gym
from gym import spaces
import gym_dnd.spells as spells

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
        ...

    def render(self, mode="human"):
        # Render the environment to the screen
        ...
