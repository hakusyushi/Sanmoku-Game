#-*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys
from wincheck import *
from tkinter import *

fieldSetList = [0,0,0,0,0,0,0,0,0]

def inputCheck(inputChar):
    if fieldSetList[inputChar] == 0:
        return 0
    else:
        return -1

def inputProc(inputChar,mb):
    fieldSetList[inputChar] = mb

def banmenCheck(basyo):
    if basyo[0] <= 50 and basyo[1] <= 50:
        return 0
    elif basyo[0] <= 105 and basyo[1] <= 50:
        return 1
    elif basyo[0] <= 160 and basyo[1] <= 50:
        return 2
    elif basyo[0] <= 50 and basyo[1] <= 105:
        return 3
    elif basyo[0] <= 105 and basyo[1] <= 105:
        return 4
    elif basyo[0] <= 160 and basyo[1] <= 105:
        return 5
    elif basyo[0] <= 50 and basyo[1] <= 160:
        return 6
    elif basyo[0] <= 105 and basyo[1] <= 160:
        return 7
    elif basyo[0] <= 160 and basyo[1] <= 160:
        return 8
    else:
        return -1

def banmenSet(num):
    if num == 0:
        return (2,2)
    elif num == 1:
        return (55,2)
    elif num == 2:
        return (107,2)
    elif num == 3:
        return (1,55)
    elif num == 4:
        return (55,55)
    elif num == 5:
        return (107,55)
    elif num == 6:
        return (1,107)
    elif num == 7:
        return (55,107)
    elif num == 8:
        return (107,107)
    else:
        return (160,160)

def main():
    global fieldSetList
    fieldSetList = [0,0,0,0,0,0,0,0,0]
    (x,y)=(160,160)
    mb=1
    cont_flg=True
    tk = Tk()

    pygame.init()
    screen=pygame.display.set_mode((x,y))
    pygame.display.set_caption("マルバツゲーム")
    bg = pygame.image.load("jpg/bg.jpg").convert_alpha() # 背景画像の指定
    rect_bg = bg.get_rect() # 画像のrect取得
    screen.blit(bg, rect_bg) # 背景画像の描画
    pygame.display.update()

    Basyo=(0,0)

    while(1):
 
        pressed=pygame.mouse.get_pressed()	
        if pressed[0] and cont_flg:			#もし左クリックされたら
            (x,y)=pygame.mouse.get_pos()	#座標を取得
            Basyo=(x,y)
            numberBanmen = banmenCheck(Basyo)   #座標がどの区画なのかを取得
            checkBanmen = inputCheck(numberBanmen)  #区画に配置可能かを確認

            if checkBanmen == 0:
                inputProc(numberBanmen,mb)  #盤面への反映
                Basyo = banmenSet(numberBanmen) #配置した区画の描画位置取得
                if mb == 1:
                    Img=pygame.image.load("jpg/maru.jpg").convert_alpha()
                    mb=-1
                else:
                    Img=pygame.image.load("jpg/batu.jpg").convert_alpha()
                    mb=1
                screen.blit(Img,Basyo)
                pygame.display.update()
            
            winCheck = winnerCheck(fieldSetList)
            if winCheck != -1:
                btn = Button(tk, text="sample")
                btn.pack()
                tk.mainloop()
                cont_flg = False

        for event in pygame.event.get():
            if event.type==QUIT:
                sys.exit()


if __name__ == "__main__":
    main()