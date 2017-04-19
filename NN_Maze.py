#-*- coding:utf-8 -*-
import pygame
#导入pygame库
from pygame.locals import *
#导入一些常用的函数和常量
from random import *

import time,sys
from Tkinter import *

from Network import *

#初始化神经网络
the_network=Network()

pygame.init()
#初始化pygame,为使用硬件做准备
screen = pygame.display.set_mode((640, 480), 0, 32)
#创建了一个窗口
pygame.display.set_caption("NN_Maze")
#设置窗口标题

#设置物件颜色
rc_wall =[0,0,0]
rc_space=[255,255,255]
rc_apple=[0,255,0]
rc_hero=[255,0,0]

#起始点
begin_pos=[240,220]

#方格大小
rs = [10,10]

mazeA=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [3,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
hero_pos=[1,0]

#clock=pygame.time.Clock()
#time_passed=clock.tick(30)

screen.fill((255, 255, 255))

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
        rp[1] += 15
        row_num += 1

screen_draw()

def cac_pos(matrix_pos,begin_pos):
    x_pos=begin_pos[0]+matrix_pos[1]*10
    y_pos=begin_pos[1]+matrix_pos[0]*15
    return [x_pos,y_pos]

#上下左右！
def left():
    mazeA[hero_pos[0]][hero_pos[1]], \
    mazeA[hero_pos[0]][hero_pos[1] - 1] = mazeA[hero_pos[0]][hero_pos[1] - 1], \
                                          mazeA[hero_pos[0]][hero_pos[1]]

    return mazeA[hero_pos[0]][hero_pos[1]]
def right():

    mazeA[hero_pos[0]][hero_pos[1]], \
    mazeA[hero_pos[0]][hero_pos[1] + 1] = mazeA[hero_pos[0]][hero_pos[1] + 1], \
                                          mazeA[hero_pos[0]][hero_pos[1]]

    #print mazeA[hero_pos[0]][hero_pos[1] + 1]
    return mazeA[hero_pos[0]][hero_pos[1]]

def up():
    mazeA[hero_pos[0]][hero_pos[1]], \
    mazeA[hero_pos[0]-1][hero_pos[1]] = mazeA[hero_pos[0]-1][hero_pos[1]], \
                                          mazeA[hero_pos[0]][hero_pos[1]]
    return mazeA[hero_pos[0]][hero_pos[1]]
def down():
    mazeA[hero_pos[0]][hero_pos[1]], \
    mazeA[hero_pos[0]+1][hero_pos[1]] = mazeA[hero_pos[0]+1][hero_pos[1]], \
                                          mazeA[hero_pos[0]][hero_pos[1]]
    return mazeA[hero_pos[0]][hero_pos[1]]

#sensorA：通过check判断物件
def check_wall():
    if mazeA[hero_pos[0]][hero_pos[1] + 1]==0:
        return 1
    else:
        return 0

#sensorB：执行移动，并返回移动结果
def move(result):
    #这里是eval的用法
    #eval(str)()
    if result==1:
        move_to=right()
        print mazeA
        return move_to

#碰撞判断
def check_crash(move_to):
    if move_to==1:
        return "crash"
    else:

        screen_draw()
        pygame.time.delay(500)




begin=False
while True:
    if begin==True:

        #此处利用神经网络进行判断
        move_to=move(the_network.run(check_wall()))
        result=check_crash(move_to)
        if result=="crash":
            print "crash!"
            break


    for event in pygame.event.get():
        if event.type == KEYDOWN:
            begin=True


        if event.type == QUIT:
            #接收到退出事件后退出程序
            exit()
    pygame.display.update()
