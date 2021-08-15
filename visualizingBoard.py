#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 12:59:17 2021

@author: mahirkaya
"""

#tiles,dictionary, n*n, ex: {(0,0):'black'} 
#snake, ex: [(0,0),(0,1)]
import tkinter
from tkinter import *

def createBoard(snake,n):
    #n:number of rows and columns
    #snake: list of coordinates that will be colored green in the board
    
    wid=0
    het=0
    board={}
    Coord=snake.getSnakeCoords()
    for i in range(n**2):
        
        if (wid,het) in Coord:
            board.update({(wid,het):'green'})
        else:
            board.update({(wid,het):'black'})
    
        if wid==n-1:
            wid=0
            het+=1
        else:
            wid+=1
    return board
    

def visualizeBoard(Snake, a, B1,master):

    board=B1.getBoard()
    snakeCord=Snake.getSnakeCoords()
    for i in range(B1.n):
        for b in range(B1.n):   
            if (i,b) in snakeCord:  
                #borderwidth=1, relief="groove"
                q=Label(master, fg='white', bg="green",  width=2, height=1)
            elif (i,b)==a:
                q=Label(master, fg='white', bg="red",  width=2, height=1)
            else:
                q=Label(master, fg='black', bg="black",  width=2, height=1)
            q.grid(row=i,column=b)
    
def drawBoxes(master,snake,a):
    widgets=master.winfo_children()
    coord=snake.getSnakeCoords()
    for widget in widgets:
        if type(widget)==tkinter.Label:
            coordinate=(widget.grid_info()['row'], widget.grid_info()['column'])
            if coordinate in coord:
                widget['background']='green'
            elif coordinate==a:
                widget['background']='red'
            else:
                widget['background']='black'



