"""
文件说明

"""
import pyautogui as pag
import time

'''
设置一个监听时间，每t间隔移动一次鼠标
'''


class AutoOperation:
    def __init__(self, t):
        self.total_time = t

    def move(self):
        # 获取当前时间,毫秒值
        start_time = time.time()
        # 设置间隔5min移动一次
        # 可以设置sleep来完成，休眠5分钟，操作一次
        # flag = 0
        while 1:
            current_time = time.time()
            time.sleep(300)
            # # 获取当前屏幕的分辨率
            # screenWidth, screenHeight = pag.size()
            # print(screenHeight, screenWidth)
            # 获取当前鼠标的位置
            # currentMouseX, currentMouseY = pag.position()
            # print(currentMouseX, currentMouseY)
            # 鼠标左击一次
            # pag.click()
            # 鼠标移动,移动坐标为1000，500，绝对移动，时间为2s
            # 设置移动的话，这样会固定在一个位置上，可以设置一个随机数，或者设置两个位置来回跑
            # if flag % 2 == 0:
            #     pag.scroll(500)
            #     # pag.moveTo(1000, 500, 1)
            #
            # else:
            #     pag.scroll(-500)
            #     # pag.moveTo(900, 520, 1)
            # flag = flag + 1
            # 1054 161
            pag.moveTo(1054, 161, 1)
            pag.click()
            d_value = current_time - start_time
            end = self.total_time*60*60*1000
            if d_value > end:
                break


if __name__ == '__main__':
    auto = AutoOperation(5)
    auto.move()











