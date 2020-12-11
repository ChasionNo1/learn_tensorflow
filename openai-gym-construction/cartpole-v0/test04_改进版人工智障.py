"""
文件说明

"""
import gym
env = gym.make('CartPole-v0')
t_all = []
action_bef = 0
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        cp, cv, pa, pv = observation
        if abs(pa) <= 0.1:
            action = 1 - action_bef
        else:
            action = int(pa >= 0)
        observation, reward, done, info = env.step(action)
        action_bef = action
        if done:
            # print("Episode finished after {} timesteps".format(t+1))
            t_all.append(t)
            break
env.close()
print(sum(t_all)/len(t_all))