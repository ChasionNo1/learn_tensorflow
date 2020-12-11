"""
文件说明

"""
import gym

env = gym.make('CartPole-v0')
# 开始20局游戏
for i_episode in range(20):
    # 得到环境给的初始反馈
    ob = env.reset()
    # 一局游戏的操作步数
    for t in range(100):
        env.render()
        print(ob)
        action = env.action_space.sample()
        ob, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
