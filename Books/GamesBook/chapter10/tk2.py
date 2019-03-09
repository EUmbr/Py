from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl1.grid(row=0, column=0, columnspan=2, sticky=W)

        self.lbl2 = Label(self, text="Password:")
        self.lbl2.grid(row=1, column=0, sticky=W)

        self.ent = Entry(self)
        self.ent.grid(row=1, column=1, sticky=W)

        self.submit_bttn = Button(self, text="Complete", command=self.reveal)
        self.submit_bttn.grid(row=2, column=0, sticky=W)

        self.secret_txt = Text(self, width=35, height=5, wrap=WORD)
        self.secret_txt.grid(row=3, column=0, columnspan=2, sticky=W)

    def reveal(self):
        contents = self.ent.get()
        if contents == 'secret':
            message = 'IT WORKS!!!'
        else:
            message = 'That is not the correct password'

        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)


root = Tk()
root.geometry('500x400')
app = Application(root)
root.mainloop()
