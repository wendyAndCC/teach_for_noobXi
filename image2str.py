
'''
# 想要贪吃蛇 我们需要  蛇、 地图、 墙（也就是地图的边缘）
# 不讲类了 给你以最暴力的方式搞
# 地图我们比如搞个20*20
# 你就当他是蛇吧，复杂的你就搞不来了
# 下一步 动起来 监听键盘操作 用个库
# 我们用的python版本太新了 这个垃圾库不支持
# 我自己写 你开玩笑？  写到六月份去？ 不上班了？
# 傻子  监听操作很底层的，你要把我搞死去？
# 还自己写？ 你写的能有人家的好？
# 接下来 我们看下怎么用
# 我们只用他键盘的库
# 监测搞定
# 接下来就是移动
特么的这个库一定得搞多线程  我倒无所谓 就没法给你讲目前

智障，别人写的库 你不看api会用？ 你是人家肚子里的蛔虫？傻逼
'''

'''
你自己看下次
https://pypi.org/project/pynput/#description
'''


import os # 用来清屏
from pynput import keyboard # 用来监控键盘的
snake = ['S', 'S', 'S']
gameMap = []
snakePosition = [[2, 9], [2, 10], [2, 11]]
foodPosition = [5, 12]
food = 'F'

def refresh():
    # print('------------------------------------------')
    # 清空屏幕
    os.system("cls")
    for row in gameMap:
        
        for cell in row:
            print(cell, end=' ')
       
        print()

def addFood(food_Position):
    gameMap[food_Position[0]][food_Position[1]] = food

def addSnake(snake_Position, 吃了=False):
    # print("判断吃没吃")
    if(吃了):
        print("恰滴东西，变大一格")
    else:
        # print("没吃，初始化地图")
        initMap()
    count = 0
    for pos in snakePosition:
        try:
            gameMap[pos[0]][pos[1]] = snake[count]
        except:
            print("-----------------------------------")
            print("游戏结束，你的蛇死了")
            exit()
        count += 1

def snakeMove(num):
    count = 0
    if num == 0:
        # 上
        for i in range(len(snakePosition)):
            # 判断是不是蛇头
            if count == (len(snakePosition) - 1):
                
                snakePosition[2][0] = snakePosition[2][0] - 1
                # print("蛇头动")
                # print(snakePosition)
            else:
                # 大坑 对象引用
                snakePosition[i] = snakePosition[i+1].copy()
                # print("身子动")
                # print(snakePosition)
            count += 1
    

    elif num == 1:
        # 下
        for i in range(len(snakePosition)):
            if count == (len(snakePosition) - 1):
                
                snakePosition[count][0] = snakePosition[count][0] + 1
               
            else:
                # 大坑 对象引用
                snakePosition[i] = snakePosition[i+1].copy()
                
            count += 1

    elif num == 2:
        #     左
        for i in range(len(snakePosition)):
            if count == (len(snakePosition) - 1):
                
                snakePosition[count][1] = snakePosition[count][1] - 1
               
            else:
                # 大坑 对象引用
                snakePosition[i] = snakePosition[i+1].copy()
                
            count += 1
    elif num == 3:
    #     右
        for i in range(len(snakePosition)):
            if count == (len(snakePosition) - 1):
                
                snakePosition[count][1] = snakePosition[count][1] + 1
               
            else:
                # 大坑 对象引用
                snakePosition[i] = snakePosition[i+1].copy()
                
            count += 1

    # print("添加蛇进去")
    addSnake(snakePosition)


def initMap():
    global gameMap
    gameMap = []
    for i in range(10): 
        gameMap.append([]) 
        for j in range(20):
            gameMap[i].append('□')
         


def runGame():
    # ...or, in a non-blocking fashion:
    # 这必须找个线程来
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()
    # print("初始化地图")
    initMap()
    # print("初始化蛇")
    addSnake(snakePosition)
    # print("初始化蛇")
    addFood(foodPosition)
    # print("加到地图上去")
    refresh()
    while(True):
        pass


def on_press(key):
    try:
        if key.char == key.up:
            print("按了上键")
            snakeMove(0)
            refresh()
        elif key.char == key.down:
            print("按了下键")
            snakeMove(1)
            refresh()
        elif key.char == key.left:
            print("按了左键")
            snakeMove(2)
            refresh()
        elif key.char == key.right:
            print("按了右键")
            snakeMove(3)
            refresh()

    except AttributeError:
        if key == keyboard.Key.up:
            snakeMove(0)
            refresh()
        elif key == keyboard.Key.down:
            snakeMove(1)
            refresh()
        elif key == keyboard.Key.left:
            snakeMove(2)
            refresh()
        elif key == keyboard.Key.right:
            snakeMove(3)
            refresh()


# 监测到键盘松开
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False


if __name__ == '__main__':

    # 阻塞了 要搞个线程 来监听
    # 运行游戏
    runGame()
