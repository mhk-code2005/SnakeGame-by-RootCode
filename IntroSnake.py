#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 11:10:48 2021

@author: mahir
"""

import tkinter
from tkinter import *

def intro(score):
    main=Tk()

    main.title('Snake Game')
    main.configure(bg='black')
    def snakePlay():
        n=int(a.get())
        print(n)
        main.destroy()
        from MainPageSnake import mainPlay
        mainPlay(n)
        
    def rul():
        main.destroy()
        from Rules import printRules
        printRules()

    try:
        image2=PhotoImage(file="a.png")
        label=Label(main, image=image2, text='a').grid(row=1, columnspan=10)
    except:
        label=Label(main, text='Error Loading Image',width=40, height=20).grid(row=1, columnspan=10)
    
    Button(main, text='Start', width=30, height=5, command=snakePlay).grid(row=2, column=1)
    Button(main, text='rules', command=rul, width=10, height=5).grid(row=2, column=2)
    
    Label(main, text='Your Score:  '+str(score), width=10, height=2).grid(row=2, column=4)
    
    Label(main, text='Rows And Columns    :     ', bg='black', fg='white').grid(row=4, column=2, columnspan=4)
    a=Entry(main, width=5, bg='black', fg='white')
    a.insert(END,25)
    a.grid(row=4,column=4, columnspan=2)
    def quit():
        main.destroy()
        exit()
    Button(main, text="Quit",fg='black', bg='black',command=quit).grid(row=4, column=1)
    mainloop()
    
    



