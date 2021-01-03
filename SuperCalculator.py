import math
from tkinter import *

#CREATE THE BUTTON THAT CALCULATES THE DISTANCE
def Distance():
    x1 = x1_entry.get()
    y1 = y1_entry.get()
    x2 = x2_entry.get()
    y2 = y2_entry.get()

    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    #DISTANCE FORMULA
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    result.insert(END, dist)
    f'{round(dist, 2)}'

#CREATE THE BUTTON THAT CLEARS THE CONTENTS OF EACH ENTRY BOX FOR THE DISTANCE FORMULA
def clear_contents():
    x1_entry.delete(0, END)
    y1_entry.delete(0, END)
    x2_entry.delete(0, END)
    y2_entry.delete(0, END)
    result.delete(0.0, END)

#CREATE THE WINDOW
window = Tk()
window.title('Distance and Midpoint Formula Calculator')
window.configure(background='plum')
window.geometry('2000x2000')


#CREATE THE ENTRY BOX FOR THE X/Y VALUES
x1_entry = Entry(window, width=7, bg='white')
y1_entry = Entry(window, width=7, bg='white')
x2_entry = Entry(window, width=7, bg='white')
y2_entry = Entry(window, width=7, bg='white')

#GRID THE ENTRY BOXES FOR DIST FORMULA
x1_entry.grid(row=9, column=0, sticky='w', padx=40)#ROWS=1,2,3,4; COLUMNS=0
y1_entry.grid(row=10, column=0, sticky='w', padx=40)
x2_entry.grid(row=11, column=0, sticky='w', padx=40)
y2_entry.grid(row=12, column=0, sticky='w', padx=40)


#PHOTO OF DISTANCE FORMULA
photo = PhotoImage(file = 'dist_form_image.png')
Label(window, image=photo, bg='plum').grid(row=0, column=0, sticky='nw', padx=5, pady=5)

#CREATE CALCULATE BUTTON AND GRID IT FOR DISTANCE
calc_btn = Button(window, text='Calculate', width=8, command=Distance).grid(row=16, column=0, sticky='w', padx=5, pady=5)

#CREATE A CLEAR_CONTENTS BUTTON
clear_btn = Button(window, text='Clear', width=8, command=clear_contents).grid(row=17, column=0, sticky='w', padx=5, pady=5)

#CREATE A LABEL EXPLAINING HOW THE CALCULATOR WORKS FOR DIST FORMULA
how_it_works = Label(window, text='How it works: Enter numbers into the boxes below \n'
'and the calculator does the rest!', bg='plum', fg='white', font='courier 15 bold')
#GRID THE HOW IT WORKS LABEL FOR DIST FORMULA
how_it_works.grid(row=1, column=1, sticky='new', padx=5, pady=5)

#CREATE LABELS FOR X AND Y VALUES
x1_lbl = Label(window, text='X1', bg='plum', fg='white', font='courier 14 bold') #COLUMN 1 FOR ALL
x1_lbl.grid(row=9, column=0, sticky='W', padx=5, pady=5)

y1_lbl = Label(window, text='Y1', bg='plum', fg='white', font='courier 14 bold')
y1_lbl.grid(row=10, column=0, sticky='W', padx=5, pady=5)

x2_lbl = Label(window, text='X2', bg='plum', fg='white', font='courier 14 bold')
x2_lbl.grid(row=11, column=0, sticky='W', padx=5, pady=5)

y2_lbl = Label(window, text='Y2', bg='plum', fg='white', font='courier 14 bold')
y2_lbl.grid(row=12, column=0, sticky='W', padx=5, pady=5)

#CREATE A LABEL THAT SHOWS WHERE THE ANSWER WILL BE
answer_lbl = Label(window, text='ANSWER: ', bg='plum', fg='white', font='courier 15')
answer_lbl.grid(row=15, column=0, sticky='w', pady=5)

#CREATE A RESULT OUTPUT
result = Text(window, width=4, height=1, bg='plum', fg='white', font='courier 14 bold', wrap=WORD)
#GRID THE RESULT OUTPUT
result.grid(row=15, column=0, sticky='w', padx=75)

#////////////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

#CREATE THE BUTTON THAT CALCULATES THE MIDPOINT
def Midpoint(): 
    x1m = x1m_entry.get()
    y1m= y1m_entry.get()
    x2m = x2m_entry.get()
    y2m = y2m_entry.get()

    x1m = float(x1m)
    y1m = float(y1m)
    x2m = float(x2m)
    y2m = float(y2m)
    
    mid = (x1m + x2m)/2 , (y1m + y2m)/2
    result_m.insert(END, mid)
    f'{mid}'
    

#CREATE THE BUTTON THAT CLEARS THE CONTENTS OF EACH ENTRY BOX FOR THE MIDPOINT FORMULA
def clear_contents():
    x1m_entry.delete(0, END)
    y1m_entry.delete(0, END)
    x2m_entry.delete(0, END)
    y2m_entry.delete(0, END)
    result_m.delete(0.0, END)



#CREATE THE ENTRY BOX FOR THE X/Y VALUES
x1m_entry = Entry(window, width=7, bg='white')
y1m_entry = Entry(window, width=7, bg='white')
x2m_entry = Entry(window, width=7, bg='white')
y2m_entry = Entry(window, width=7, bg='white')

#GRID THE ENTRY BOXES
x1m_entry.grid(row=9, column=1, sticky='e', padx=40)#ROWS=1,2,3,4; COLUMNS=0
y1m_entry.grid(row=10, column=1, sticky='e', padx=40)
x2m_entry.grid(row=11, column=1, sticky='e', padx=40)
y2m_entry.grid(row=12, column=1, sticky='e', padx=40)


#PHOTO OF MIDPOINT FORMULA
photo_m = PhotoImage(file = 'midpoint.png')
Label(window, image=photo_m, bg='plum').grid(row=0, column=1, sticky='e', padx=70, pady=5)

#CREATE BUTTON AND GRID IT
calc_btn = Button(window, text='Calculate', width=8, command=Midpoint).grid(row=16, column=1, sticky='e', padx=5, pady=5)

#CREATE A CLEAR_CONTENTS BUTTON
clear_btn = Button(window, text='Clear', width=8, command=clear_contents).grid(row=17, column=1, sticky='e', padx=5, pady=5)


#CREATE LABELS FOR X AND Y VALUES
x1_lbl_m = Label(window, text='X1', bg='plum', fg='white', font='courier 14 bold') #COLUMN 1 FOR ALL
x1_lbl_m.grid(row=9, column=1, sticky='e', padx=5, pady=5)

y1_lbl_m = Label(window, text='Y1', bg='plum', fg='white', font='courier 14 bold')
y1_lbl_m.grid(row=10, column=1, sticky='e', padx=5, pady=5)

x2_lbl_m = Label(window, text='X2', bg='plum', fg='white', font='courier 14 bold')
x2_lbl_m.grid(row=11, column=1, sticky='e', padx=5, pady=5)

y2_lbl_m = Label(window, text='Y2', bg='plum', fg='white', font='courier 14 bold')
y2_lbl_m.grid(row=12, column=1, sticky='e', padx=5, pady=5)

#CREATE A LABEL THAT SHOWS WHERE THE ANSWER WILL BE
answer_lbl_m = Label(window, text='ANSWER: ', bg='plum', fg='white', font='courier 15')
answer_lbl_m.grid(row=15, column=1, sticky='e', padx=85, pady=9)

#CREATE A RESULT OUTPUT
result_m = Text(window, width=10, height=2, bg='plum', fg='white', font='courier 14 bold', wrap=WORD)
#GRID THE RESULT OUTPUT
result_m.grid(row=15, column=1, sticky='e', padx=5)


#MAINLOOP
window.mainloop()
