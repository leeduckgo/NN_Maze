#-*- coding:utf-8 -*-

mazeA=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]



#导入pygame库
import pygame
from pygame.locals import *


#from random import *
#from Network import *

pygame.init()
#初始化pygame,为使用硬件做准备
screen = pygame.display.set_mode((640, 480), 0, 32)
#创建了一个窗口
pygame.display.set_caption("NN_Maze")
#设置窗口标题
#填充屏幕
screen.fill((255, 255, 255))

#迷宫起始点
begin_pos=[240,220]

#设置物件颜色
#墙体：黑色
rc_wall =[0,0,0]
#通道：白色
rc_space=[255,255,255]
#目标位置为绿色
rc_apple=[0,255,0]
#机器人为红色
rc_hero=[255,0,0]

#方格大小
rs = [10,10]


#draw_screen
def screen_draw():
    global hero_pos
    rp = [begin_pos[0], begin_pos[1]]

    row_num=0
    rp[1]=begin_pos[1]
    for i in mazeA:
        rp[0] = begin_pos[0]
        col_num = 0
        for j in i:


            if j == 1:
                pygame.draw.rect(screen, rc_wall, Rect(rp, rs))
            elif j == 0:
                pygame.draw.rect(screen, rc_space, Rect(rp, rs))
            elif j == 2:
                pygame.draw.rect(screen, rc_apple, Rect(rp, rs))
            elif j == 3:
                pygame.draw.rect(screen,rc_hero,Rect(rp,rs))
                hero_pos=[row_num,col_num]
            rp[0] += 10
            col_num += 1
        rp[1] += 10
        row_num += 1

screen_draw()
pygame.display.update()


while True:
    for event in pygame.event.get():

        if event.type == QUIT:
            #接收到退出事件后退出程序
            exit()





