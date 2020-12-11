"""
文件说明

"""
import gym
env = gym.make('CartPole-v0')
t_all = []
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        '''
        ob中四个参数的意思：
        cart position:          -4.8                    4.8    坐标
        cart velocity:          -Inf                    Inf    速度
        pole angle:             -0.418 rad (-24 deg)    0.418 rad (24 deg)  倾斜的角度
        pole angular velocity:  -Inf                    Inf    极角速度
        
        Actions:
        Type: Discrete(2)
        Num   Action
        0     Push cart to the left
        1     Push cart to the right
        '''
        cp, cv, pa, pv = observation
        action = int(pa >= 0)
        observation, reward, done, info = env.step(action)
        if done:
            # print("Episode finished after {} timesteps".format(t+1))
            t_all.append(t)
            break
env.close()
print(sum(t_all)/len(t_all))
