#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 19:43:55 2021

@author: mahirkaya
"""



from tkinter import *

Tdirection='right'
initWay='right'
def initiate(n,master):
        global Tdirection,initWay
        import SnakeWithoutVisuals as SWV
        from visualizingBoard import visualizeBoard
        B1=SWV.Board(n)
        Snake=SWV.snake(coord=[(5,5),(5,4),(5,3)])
        a = B1.createApple(Snake.getSnakeCoords())
        B1.updateBoard(Snake.getSnakeCoords(),Snake.getSymb(),a)
        visualizeBoard(Snake,a, B1, master)
        Tdirection='right'
        initWay='right'
        return Snake,B1,a



def mainPlay(n):

    from visualizingBoard import visualizeBoard
    from visualizingBoard import drawBoxes
    import SnakeWithoutVisuals as SWV
    import time
    score=0
    global initWay,Tdirection

    #Drawing Board and Creating Elements
    master=Tk()
    master.title('Snake1')

    #Initiating game
    Snake,B1,a=initiate(n,master)

    def update1(event):
        opposites=[('left','right'),('right','left'),('up','down'),('down','up')]
        global Tdirection 
        global initWay  
        Tdirection='right'
        if (Tdirection,initWay) in opposites:
            Tdirection=initWay

    def update2(event):
        opposites=[('left','right'),('right','left'),('up','down'),('down','up')]
        global Tdirection 
        global initWay  
        Tdirection='left'
        if (Tdirection,initWay) in opposites:
            Tdirection=initWay

    def update3(event):
        opposites=[('left','right'),('right','left'),('up','down'),('down','up')]
        global Tdirection
        global initWay
        Tdirection='up'
        if (Tdirection,initWay) in opposites:
            Tdirection=initWay

    def update4(event):
        opposites=[('left','right'),('right','left'),('up','down'),('down','up')]
        global Tdirection   
        global initWay
        Tdirection='down'
        if (Tdirection,initWay) in opposites:
            Tdirection=initWay



    frame = Frame(master, width=100, height=100)
    master.bind('<Left>', update2)
    master.bind('<Right>', update1)
    master.bind('<Up>', update3)
    master.bind('<Down>', update4)

    while True:


        try:
            master.update_idletasks()
            master.update()
            Snake.move(initWay,a,Tdirection)
            initWay=Tdirection
            B1.updateBoard(Snake.getSnakeCoords(),Snake.getSymb(),a)

            if Snake.isAppleEaten(a)==True:
                a = B1.createApple(Snake.getSnakeCoords())
                score+=1

            drawBoxes(master,Snake,a)
            time.sleep(.01)
            
            if  Snake.didSnakeOverlap() or B1.OutBoard(Snake.getSnakeCoords()):
                Snake,B1,a=initiate(n)
                master.destroy()
                from IntroSnake import intro
                intro(score)

        except:
            master.destroy()
            from IntroSnake import intro
            intro(score)
        





