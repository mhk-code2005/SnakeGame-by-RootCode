
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 14:56:55 2021

@author: mahir
"""

from tkinter import *
#rules
def printRules():
    rules=Tk()
    x=10
    rules.title('TIC TAC TOE: Rules')
    rules['bg']='black'
    Label(rules, text='               Snake             ', font=('Helvetica',18), bg='black', fg='white').grid(row=0, column=0)
    Label(rules, text='    This game of snake was designed by Mahir Kaya, a coder at ROOT CODE', font=('Helvetica',18), bg='black', fg='white').grid(row=1, column=0)
    Label(rules, text='                           ', font=('Helvetica',18), bg='black', fg='white').grid(row=2, column=0)

    Label(rules, text='You will play the game using keyboard keys up, down, right and left', font=('Helvetica',18), bg='black', fg='white').grid(row=3, column=0)
    Label(rules, text='                           ', font=('Helvetica',18), bg='black', fg='white').grid(row=4, column=0)

    Label(rules, text='  First, you need to set the row and column numbers from left bottom', font=('Helvetica',18), bg='black', fg='white').grid(row=5, column=0)
    Label(rules, text='                           ', font=('Helvetica',16), bg='black', fg='white').grid(row=6, column=0)

    Label(rules, text='Recommended number of Rows and Columns: 15', font=('Helvetica',18), bg='black', fg='white').grid(row=7, column=0)
    Label(rules, text='                           ', font=('Helvetica',16), bg='black', fg='white').grid(row=8, column=0)

    Label(rules, text='Your job is to eat as many apples as you can', font=('Helvetica',18), bg='black', fg='white').grid(row=9, column=0)
    Label(rules, text='                           ', font=('Helvetica',16), bg='black', fg='white').grid(row=10, column=0)

    Label(rules, text='Then, when the game is over, your score which is', font=('Helvetica',18), bg='black', fg='white').grid(row=13, column=0)

    Label(rules, text='how many apples you ate, will be reported to you', font=('Helvetica',18), bg='black', fg='white').grid(row=15, column=0)
    Label(rules, text='                           ', font=('Helvetica',16), bg='black', fg='white').grid(row=16, column=0)

    Label(rules, text='If you want to go back to the main page, click the button "Back"', font=('Helvetica',18), bg='black', fg='white').grid(row=17, column=0)
    Label(rules, text='                           ', font=('Helvetica',16), bg='black', fg='white').grid(row=18, column=0)

    Label(rules, text='ENJOY', font=('Helvetica',18), bg='black', fg='white').grid(row=19, column=0)

    def a():
        rules.destroy()
        from IntroSnake import intro 
        intro(0)

    Button(rules, text='back', command=a, fg='black', bg='black').grid(row=20, column=0)

    mainloop()
