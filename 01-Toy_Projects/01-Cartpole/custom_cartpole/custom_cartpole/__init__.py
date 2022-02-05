from gym.envs.registration import register

register(id='CustomCartPole-v0',
    entry_point='custom_cartpole.envs:CustomCartPoleEnv',
    max_episode_steps=200,
    reward_threshold=195.0,
)

