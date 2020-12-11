from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt


# MNIST_data指的是存放数据的文件夹路径，one_hot=True 为采用one_hot的编码方式编码标签
mnist = input_data.read_data_sets('../MNIST_data', one_hot=True)
# 加载数据,加载到这里应该是图片了
train_X = mnist.train.images
validation_X = mnist.validation.images
test_X = mnist.test.images
# 加载标签
label_Y = mnist.train.labels
validation_Y = mnist.validation.labels
test_Y = mnist.test.labels

# 查看训练集第一个样本的内容和标签
# (784,)
print(train_X[0], test_Y[0])
print(test_X[0].shape)


# 可视化样本
# fig是整个显示的页面，ax是一个个小容器
fig, ax = plt.subplots(nrows=4, ncols=5, sharex='all', sharey='all')
# 将4x5的排列平铺成20个，方便for循环

ax = ax.flatten()
for i in range(20):
    # resize图像的大小
    img = train_X[i].reshape(28, 28)
    # 每个容器放一个图
    ax[i].imshow(img, cmap='Greys')
ax[0].set_xticks([])
ax[0].set_yticks([])
plt.tight_layout()
plt.show()
