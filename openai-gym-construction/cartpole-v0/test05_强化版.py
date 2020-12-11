"""
文件说明
ob中有四个参数，要利用每一个参数来控制是向左还是向右
可以将最优权重求均值来作为模型的参数
"""
import numpy as np
import gym
import json


def get_action(weights, ob):
    # 根据权值对当前的状态做出决策
    # 对ob中的四个参数进行加权求和，weights[4]是偏置b
    wxb = np.dot(weights[:4], ob) + weights[4]
    # 如果加权和大于0执行1动作，否则执行0动作
    return int(wxb >= 0)


def get_sum_reward_by_weights(env, weighs):
    # 测试不同权值的控制模型有效控制的持续时间（也就是奖励）
    ob = env.reset()
    # 记录总的奖励和
    sum_reward = 0
    for t in range(200):
        # 获取当前权值下的决策动作
        action = get_action(weighs, ob)
        # 获取执行动作后的环境参数
        ob, r, done, info = env.step(action)
        sum_reward += r
        if done:
            break
    return sum_reward


def get_weights_by_random_guess():
    # 随机初始化五个参数
    return np.random.rand(5)


def get_weights_by_hill_climbing(best_weights):
    # 通过爬山算法选取权值（在当前最好权值上加入随机数）
    return best_weights + np.random.normal(0, 0.1, 5)


def get_best_result(algo='random_guess'):
    # 如果将得到的best_weights保存起来，用于下次的调用？
    env = gym.make('CartPole-v0')
    np.random.seed(10)
    best_reward = 0
    best_weights = np.random.rand(5)
    a = []
    for i in range(100):
        cur_weights = None
        env.render()
        if algo == 'hill_climbing':
            cur_weights = get_weights_by_hill_climbing(best_weights)
        else:
            # 若为随机猜测算法，则选取随机权值
            cur_weights = get_weights_by_random_guess()
        # 获取当前权值的模型控制奖励和
        if algo == 'load_model':
            with open('best_weights.txt', 'rb') as f:
                line = f.readline()
                a = json.loads(line)
                # print(dicta)
            cur_weights = np.array(a)
        cur_sum_reward = get_sum_reward_by_weights(env, cur_weights)
        # 更新当前最优权值
        # print('cur:', cur_sum_reward, cur_weights)
        # print('best:', best_reward, best_weights)
        if cur_sum_reward > best_reward:
            best_weights = cur_weights
            best_reward = cur_sum_reward
        if best_reward >= 200:
            break
    print('当前是第%d回合' % (i+1))
    env.close()
    if algo != 'load_model':
        for k in range(best_weights.size):
            a.append(best_weights[k])
        with open('best_weights.txt', 'w+') as f:
            f.write(str(a))

    return best_reward, best_weights


# print(get_best_result('hill_climbing'))
# 有有时候加载的模型不一定第一次就是最优结果
print(get_best_result('load_model'))

