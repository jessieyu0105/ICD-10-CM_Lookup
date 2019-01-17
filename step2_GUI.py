# coding : utf8
from tkinter import *
import re

class quertGUI:
    def __init__(self, root):
        self.root = root
        self.getData()
        self.initUI()

    def getData(self):
        self.de_dict = {}
        try:
            f = open('data/icd10cm.txt', 'r')
            for line in f:
                temp = line.strip("\n").split("\t")
                self.de_dict[temp[0]] = temp[1]
        except Exception:
            print("read file error ")
        finally:
             f.close()

    def initUI(self):
        self.root.geometry("600x400")
        root.maxsize(600,400)
        root.minsize(600,400)
        self.root.title("Query GUI")
        self.var = StringVar()
        self.entry_input = Entry(self.root, textvariable= self.var,width="40")
        self.entry_input.place(anchor='nw', x=40, y=20)
        self.query_btn = Button(self.root, text="Query", width="6", height="1", command=self.query_func).place(anchor='nw', x=400, y=20)
        self.clear_btn = Button(self.root, text="Clear", width="6", height="1", command=self.clear_func).place(anchor='nw', x=460, y=20)
        self.exit_btn = Button(root, text="Exit", width="6", height="1", command=self.exit_func).place(anchor='nw', x=520, y=20)
        self.res_text = Text(self.root,width = 80,height = 24)
        self.res_text.place(anchor='nw', x=20, y=60)

    def query_func(self):
        self.res_text.delete(0.0,END)
        user_input = self.var.get()
        item = 0
        is_key = False
        if re.match("[A-Z][0-9]{1,2}\.?[0-9]*",user_input):
            print("okok")
            is_key = True
        for key, value in self.de_dict.items():
            if is_key:
                if user_input in key :
                    self.res_text.insert(END,"{0}\t{1}\n".format(key, value))
                    item += 1
            else:
                if user_input in value:
                    self.res_text.insert(END, "{0}\t{1}\n".format(key, value))
                    item += 1
        if item == 0:
            self.res_text.insert(END,"{0} not in file".format(user_input))

    def clear_func(self):
        self.var.set("")
    def exit_func(self):
        exit()


if __name__ == "__main__":
    root = Tk()
    s = quertGUI(root)
    root.mainloop()