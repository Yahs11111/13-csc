from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("RANK SCORE")

window.config(background="Pink")


label = Label(window,
              text="bro",
              font=('Arial',40,'bold'),
              fg='White',
              bg='Pink',)

label.pack()

count=0

def click():
    global count
    count+=1
    label.config(text=count)

button = Button(window,text='Click me!!')
button.config(command=click)
button.config(font=('Ink Free',50,'bold'))
button.config(bg='Pink')
button.config(fg='White')
button.config(activebackground='Pink')
button.config(activeforeground='White')
button.config(compound='bottom')
label = Label(window,text=count)
label.config(font=('Monospace',50))

label.pack()
button.pack()

entry = Entry()
window.mainloop()

