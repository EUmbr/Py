from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text="Choose your favorite movie types"
              ).grid(row=0, column=0, sticky=W)

        Label(self,
              text="There are right here!"
              ).grid(row=1, column=0, sticky=W)

        self.drama = BooleanVar()
        Checkbutton(self,
                    text="Drama",
                    variable=self.drama,
                    command=self.update_text
                    ).grid(row=2, column=0, sticky=W)

        self.comedy = BooleanVar()
        Checkbutton(self,
                    text="Comedy",
                    variable=self.comedy,
                    command=self.update_text
                    ).grid(row=3, column=0, sticky=W)

        self.romance = BooleanVar()
        Checkbutton(self,
                    text="Romance",
                    variable=self.romance,
                    command=self.update_text
                    ).grid(row=4, column=0, sticky=W)

        self.result_txt = Text(self, width=35, height=5, wrap=WORD)
        self.result_txt.grid(row=5, column=0, columnspan=2, sticky=W)

    def update_text(self):
        likes = ''
        if self.drama.get():
            likes += 'You like drama\n'
        if self.comedy.get():
            likes += 'You like comedy\n'
        if self.romance.get():
            likes += 'You like romance\n'
        self.result_txt.delete(0.0, END)
        self.result_txt.insert(0.0, likes)


root = Tk()
root.geometry('290x210')
root.title('Films')
app = Application(root)
root.mainloop()
