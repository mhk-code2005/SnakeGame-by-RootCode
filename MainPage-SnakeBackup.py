#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 19:43:55 2021

@author: mahirkaya
"""
import tkinter
from tkinter import *
from visualizingBoard import visualizeBoard
from visualizingBoard import drawBoxes
import SnakeWithoutVisuals as SWV
from quitTable import EndOfGame as EOG

score=0
n=15
Tdirection='right'
initWay='right'

#Drawing Board and Creating Elements
master=Tk()
master.title('Snake1')


#Initiating game
def initiate(n):
    B1=SWV.Board(n)
    Snake=SWV.snake()
    a = B1.createApple(Snake.getSnakeCoords())
    B1.updateBoard(Snake.getSnakeCoords(),Snake.getSymb(),a)
    visualizeBoard(Snake,a, B1, master)
    return Snake,B1,a
Snake,B1,a=initiate(n)

#key and button functions
def update1(event):
    global Tdirection,a,initWay,B1,w,n, score,Snake
    Tdirection='right'
    Snake.move(initWay,a,Tdirection)
    initWay=Tdirection
    B1.updateBoard(Snake.getSnakeCoords(),Snake.getSymb(),a)
    if Snake.isAppleEaten(a)==True:
        a = B1.createApple(Snake.getSnakeCoords())
        score+=1
    if B1.OutBoard(Snake.getSnakeCoords()) or Snake.didSnakeOverlap():
        master.destroy()
        EOG(score)
        print('Game Over')
        Snake,B1,a=initiate(n)
    drawBoxes(master,Snake,a)


def update2(event):
    global Tdirection,a,initWay,B1,w,n,Snake
    global score
    Tdirection='left'
    Snake.move(initWay,a,Tdirection)
    initWay=Tdirection
    B1.updateBoard(Snake.getSnakeCoords(),Snake.getSymb(),a)
    if Snake.isAppleEaten(a)==True:
        a = B1.createApple(Snake.getSnakeCoords())
        score+=1
    if B1.OutBoard(Snake.getSnakeCoords()) or Snake.didSnakeOverlap():
        master.destroy()
        EOG(score)
        print('Game Over')
        Snake,B1,a=initiate(n)

    drawBoxes(master,Snake,a)


def update3(event):
    global Tdirection,a,initWay,B1,w,n,Snake
    global score
    Tdirection='up'
    Snake.move(initWay,a,Tdirection)
    initWay=Tdirection
    B1.updateBoard(Snake.getSnakeCoords(),Snake.getSymb(),a)
    if Snake.isAppleEaten(a)==True:
        a = B1.createApple(Snake.getSnakeCoords())
        score+=1
    if B1.OutBoard(Snake.getSnakeCoords()) or Snake.didSnakeOverlap():
        master.destroy()
        EOG(score)
        print('Game Over')   
        Snake,B1,a=initiate(n)
 
    drawBoxes(master,Snake,a)


def update4(event):
    global Tdirection,a,initWay,B1,w,n,Snake
    global score
    Tdirection='down'
    Snake.move(initWay,a,Tdirection)
    initWay=Tdirection
    B1.updateBoard(Snake.getSnakeCoords(),Snake.getSymb(),a)
    if Snake.isAppleEaten(a)==True:
        a = B1.createApple(Snake.getSnakeCoords())
        score+=1
    if B1.OutBoard(Snake.getSnakeCoords()) or Snake.didSnakeOverlap():
        master.destroy()
        EOG(score)
        print('Game Over')
        Snake,B1,a=initiate(n)
    drawBoxes(master,Snake,a)



frame = Frame(master, width=100, height=100)
master.bind('<Left>', update2)
master.bind('<Right>', update1)
master.bind('<Up>', update3)
master.bind('<Down>', update4)


mainloop()


