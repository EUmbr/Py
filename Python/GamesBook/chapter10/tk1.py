from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widget()
    def create_widget(self):
        self.bttn = Button(self, command = self.update_count)
        self.bttn["text"] = 'clicks: 0'
        #self.bttn["command"] = self.update_count
        self.bttn.grid()
    def update_count(self):
        self.bttn_clicks += 1
        self.bttn["text"] = 'Clicks: ' + str(self.bttn_clicks)


root = Tk()
root.title("Clicks counter")
root.geometry("400x500")
app = Application(root)
root.mainloop()