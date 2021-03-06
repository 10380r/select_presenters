import tkinter
from tkinter import font
import random


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.next_presenter = tkinter.Button(self)
        self.next_presenter['text'] = 'next'
        self.next_presenter['command'] = self.display_username
        self.next_presenter.pack(side='bottom')

        self.font2 = font.Font(family='Times', size=100)

        self.are_you_ready = tkinter.Label(root,
                text='Are you ready?',
                fg='black',
                font=self.font2)
        self.are_you_ready.pack(side='top')
        
        self.students = ['Mr.foo',
                     'Mr.bar',
                     'Mr.buz',
                     'Mr.hoge',]

        self.label = tkinter.Label()
        self.are_you_ready.pack(side='top')


    def display_username(self):
        try:
             self.are_you_ready.destroy()
             self.label.destroy()
             self.i = random.randint(0, len(self.students)-1)

             self.font1 = font.Font(family='Times', size=40)
             self.font2 = font.Font(family='Times', size=120, weight='bold')

             self.label = tkinter.Label(root,
                     text='Next Presenter is',
                     fg='black',
                     font=self.font1)
             self.label.pack(side='top')
             
             self.are_you_ready = tkinter.Label(root,
                     text=self.students.pop(self.i),
                     fg='black',
                     font=self.font2)
             self.are_you_ready.pack(side='top')
        except ValueError:
            self.label = tkinter.Label(root,
                     text='以上になります。\nお疲れ様でした！',
                     fg='black',
                     font=self.font1)
            self.label.pack(side='top')


if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry('1000x900')
    root.title('Presenter')
    app = Application(master=root)
    app.mainloop()
