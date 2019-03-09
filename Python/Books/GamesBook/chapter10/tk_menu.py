from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text="Welcome to our restoraunt!"
              ).grid(row=0, column=0, columnspan=2, sticky=W)
        Label(self,
              text="Please, choose"
              ).grid(row=1, column=0, sticky=W)
        Label(self,
              text="Drinks:"
              ).grid(row=2, column=0, sticky=W)

        self.drink = StringVar()
        self.drink.set(None)
        drinks = ['Water(1$)', 'Juice(2$)', 'Coffee(1.5$)']
        column = 0
        for dr in drinks:
            Radiobutton(self,
                        text=dr,
                        variable=self.drink,
                        value=dr
                        ).grid(row=3, column=column, sticky=W)
            column += 1

        Label(self,
              text="Food:"
              ).grid(row=4, column=0, sticky=W)
        self.food = StringVar()
        self.food.set(None)
        Radiobutton(self,
                    text='Pizza(7$)',
                    variable=self.food,
                    value='Pizza'
                    ).grid(row=5, column=0, sticky=W)

        Radiobutton(self,
                    text='Burger(3$)',
                    variable=self.food,
                    value='Burger'
                    ).grid(row=5, column=1, sticky=W)

        self.ingridients_b = ['Cheese(0.5$)', 'Tomatos(0.5$)', 'Sauce(0.5$)', 'Salat(0.5$)']
        self.cheese = BooleanVar()
        self.tom = BooleanVar()
        self.sauce = BooleanVar()
        self.salat = BooleanVar()
        self.a_b = [self.cheese, self.tom, self.sauce, self.salat]

        Checkbutton(self,
                    text=self.ingridients_b[0],
                    variable=self.a_b[0]
                    ).grid(row=6, column=1, sticky=W)

        Checkbutton(self,
                    text=self.ingridients_b[1],
                    variable=self.a_b[1]
                    ).grid(row=7, column=1, sticky=W)

        Checkbutton(self,
                    text=self.ingridients_b[2],
                    variable=self.a_b[2]
                    ).grid(row=8, column=1, sticky=W)

        Checkbutton(self,
                    text=self.ingridients_b[3],
                    variable=self.a_b[3]
                    ).grid(row=9, column=1, sticky=W)

        self.ingridients = ['Mashrooms(0.5$)', 'Tomatos(0.5$)', 'Sauce(0.5$)', 'Olives(0.5$)']
        self.mash = BooleanVar()
        self.tom = BooleanVar()
        self.sauce = BooleanVar()
        self.olive = BooleanVar()
        self.a = [self.mash, self.tom, self.sauce, self.olive]

        Checkbutton(self,
                    text=self.ingridients[0],
                    variable=self.a[0]
                    ).grid(row=6, column=0, sticky=W)

        Checkbutton(self,
                    text=self.ingridients[1],
                    variable=self.a[1]
                    ).grid(row=7, column=0, sticky=W)

        Checkbutton(self,
                    text=self.ingridients[2],
                    variable=self.a[2]
                    ).grid(row=8, column=0, sticky=W)

        Checkbutton(self,
                    text=self.ingridients[3],
                    variable=self.a[3]
                    ).grid(row=9, column=0, sticky=W)

        self.bttn = Button(self,
                           text="Sum Up",
                           command=self.update_text)
        self.bttn.grid(row=10, column=0)

        self.result_text = Text(self, width=50, height=8, wrap=WORD)
        self.result_text.grid(row=11, column=0, columnspan=2, sticky = W)

    def update_text(self):
        text = 'Your order:\n'
        final_in = []
        total = 0
        drink = self.drink.get()
        if drink:
            text += drink + '\n'
        else:
            text += 'Nothing\n'
        if drink == 'Water(1$)':
            total += 1
        elif drink == 'Juice(2$)':
            total += 2
        elif drink == 'Coffee(1.5$)':
            total += 1.5
        food = self.food.get()
        if food == 'Burger':
            text += 'Burger(3$)'
            total += 3
            for i in range(4):
                if self.a_b[i].get():
                    final_in.append(self.ingridients_b[i])
            if final_in:
                text += ' with ' + ', '.join(final_in) + '\n\n'
                total += 0.5 * len(final_in)
            else:
                text += '\n\n'
        elif food == 'Pizza':
            text += 'Pizza(7$)'
            total += 7
            for i in range(4):
                if self.a[i].get():
                    final_in.append(self.ingridients[i])
            if final_in:
                text += ' with ' + ', '.join(final_in) + '\n\n'
                total += 0.5 * len(final_in)
            else:
                text += '\n\n'
        else:
            text += 'Nothing\n\n'

        text += 'Total: ' + str(total) + '$\n' + 'Thank you for visiting us'

        self.result_text.delete(0.0, END)
        self.result_text.insert(0.0, text)


root = Tk()
root.geometry('500x400')
root.title('menu')
app = Application(root)
root.mainloop()
