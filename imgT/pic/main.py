'''
Author: CC-TSR
Date: 2021-01-09 23:59:10
LastEditTime: 2021-01-11 22:13:55
LastEditors: xiejiancheng1999@qq.com
Description: 
FilePath: \img2char\main.py
可以输入预定的版权声明、个性签名、空行等
'''
#-*- coding: UTF-8 -*-    
from PIL import Image  
# 你看 他在这里引用的PIL 库 里的 ImageDraw  函数
# 接下来带你去看看这个函数， 大佬直接写好的
# 你不用管 会用就行 就和PRINT 之类一样 你不用管他咋实现的
# 你会调 晓得咋传参就行 不用抄
# 这么查
from PIL import ImageDraw  
from PIL import ImageFont
import matplotlib.pyplot as plt
import numpy as np
import time

def happyNewYear(srd_img_file_path, dst_img_file_path = None, scale = 2, sample_step = 3):
    # 获取当前系统时间 并转换为整数
    # 从1970年到当前时间的秒数
    start_time = int(time.time())
    # 读取图片信息
    old_img = Image.open(srd_img_file_path)
    # pix里面保存了照片里的每一个像素值
    pix = old_img.load()

        
    # 获取到需要转换的照片的宽度和高度
    width = old_img.size[0]
    height = old_img.size[1]
    imgDic = {}
    # for i in range(width):
    #     imgDic[i] = []
    #     for j in range(height):
    #         imgDic[i].append(pix[i, j])
    
    # 把宽高输出到控制台
    print ("width:%d, height:%d" % (width, height))

    # 创建新图片
    # scale = 2, sample_step = 3
    # 第一个参数对照片进行缩放， 第二个参数指定数组的类型 uint8 无符号整形 
    # （就理解成整数）
    # 
    # ndarray 函数  创建数组， 第一个参数决定数组的大小
    # 第二个参数决定数组里的数字的类型 
    # 数字的类型有以下几种 先统一理解成整数 整形：（int） 又分长整形（short） 有符号， 无符号
    #  浮点型 下分 双精度 单精度 ，不管 先理解成小数
    # 所以就当是小数 和整数
    # uint8 8位无符号整形  你就当是整数
    # 初始化时 数组里所有的数字都是0
    canvas = np.ndarray((height*scale, width*scale, 3), np.uint8)
    
    # 这一句给数组里的数字赋值了 ，现在每一个都是255
    # 目前数组是这样的
    '''
         [
             [255, 255, 255],
             [255, 255, 255],
             [255, 255, 255],
             ...等等等等 一共有照片的长度乘以高度乘以缩放的比率 scale 他这里给了2
         ]    
         照片的每个像素值在0-255之间 决定了像素的颜色
         255好像是黑色 0是白色
    '''
    canvas[:, :, :] = 255
    # 这里通过这个数组创建了一副图像
    # 很明显目前这个图像肯定是全白的
    # 因为每一个像素值都是255 在RGB模式下每个像素的颜色
    # 由三个值决定（R(红色),G(绿色),B(蓝色)）
    # （255， 255 ， 255） 白色
    new_image = Image.fromarray(canvas)
    new_image.show()
    # 这里应该是拿到画笔对象， 接下来通过Draw来进行绘制
    # 这函数没必要记 这也不是他写的，是调用的人家写好的函数
    # 你看他这里调了 IMAGEDRAW 里的 Draw 函数
    draw = ImageDraw.Draw(new_image)

    #创建绘制对象
    font = ImageFont.truetype("consola.ttf", 10, encoding="unic")
    char_table = list('shabi')
    # font = ImageFont.truetype('simsun.ttc', 10)
    # char_table = list(u'新年快乐')
    # 咋不用写？

    #开始绘制
    # 搞个值为0新的变量， 目前我们看他取了个名字叫 pix_count   pixel （像素）
    # count (数量) 我们猜他用来记录xin
    pix_count = 0
    # char_table 内容的长度
    table_len = len(char_table)
    for y in range(height):
        for x in range(width):
            if x % sample_step == 0 and y % sample_step == 0:
                
                draw.text((x*scale, y*scale),   # 画在哪
                        char_table[pix_count % table_len],  # 画啥
                        pix[x, y],  # 啥颜色
                        font)  # 啥字体
                pix_count += 1
    new_image.show()
    # 保存
    if dst_img_file_path is not None:
        new_image.save(dst_img_file_path)

    print("used time : %d second, pix_count : %d" % ((int(time.time()) - start_time), pix_count))
    print(pix_count)
    

if __name__ == '__main__':   
    # 下面我们改一下 你看他这里以及把照片定死了
    # 我们可以运行的时候自己输
    
    # imgName = input("请输入照片路径") 
    imgName = 'dog.jpg' 
    resultName = imgName +'result.jpg'
    happyNewYear(imgName, resultName)
