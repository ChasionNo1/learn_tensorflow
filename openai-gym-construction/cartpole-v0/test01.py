"""
文件说明
在强化学习中，agent需要多次尝试，积累经验，然后从经验中学到好的动作。
一次尝试我们称之为一条trajectory或一个episode。

图像引擎，一个仿真环境必不可少的两部分是物理引擎和图像引擎。物理引擎模拟环境中物体的运动规律；
图像引擎用来显示环境中的物体图像。便于直观显示当前环境物体的状态。方便调试代码。
"""
import gym
'''
gym.make():可以通过 make()函数来得到环境对象，每个环境都有一个ID，格式"Xxxx-vd"，
           d表示版本号
'''
env = gym.make('CartPole-v0')
# 该调用能返回智能体的初始观测，是np.array对象，环境初始化之后就可以使用了。
env.reset()
for _ in range(200):
    env.render()
    # take a random action
    # 从动作空间中随机选取一个动作
    # 每次调用env.step()只会让环境前进一步。所以env.step()往往放在循环结构里面，通过循环调用来完成整个回合。
    ob, r, done, info = env.step(env.action_space.sample())
'''
使用环境的核心是使用环境对象的step()方法，接收智能体的动作作为参数，并返回以下4个参数。
1. observation：np.array对象，表示观测，和env.reset()的返回值意义相同。
2. reward : float类型的值。
3. done:  bool类型的数值，本回合结束提示。Gym库里的实验环境大多是回合制的，这个返回值可以指示当前动作后游戏是否结束，如果结束，可以通过env.reset()开始下一回合。
4. info : dict类型的值，其他信息，包含以下调试信息。
env.reset()的参数取自动作空间。可以使用以下语句从动作空间中随机选取一个动作：
'''
env.close()

