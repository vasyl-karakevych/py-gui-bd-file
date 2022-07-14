import tkinter as tk
from tkinter import *
from tkinter import messagebox
from users import User
from usersToFile import UsersToFile
from bd import DB

# draw GUI interface
class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.user = User('', '')
        self.geometry('400x270')
        self.title('My app')

        self.frameN1 = tk.Frame(self, relief=RAISED, borderwidth=1)
        self.frameN1.pack(anchor=N, fill=X, expand=True)
        self.frameN2 = tk.Frame(self)
        self.frameN2.pack(anchor=N, fill=X, expand=True)

        self.frame_l = tk.Frame(self.frameN1, relief=RAISED, borderwidth=1)
        self.frame_l.pack(anchor=N, side=LEFT, fill=X, expand=True, padx=5, pady=5)

        self.frame_r = tk.Frame(self.frameN2, relief=RAISED, borderwidth=1)
        self.frame_r.pack(anchor=N, padx=5, pady=5, side=RIGHT, fill=X, expand=True)

        self.frame1 = tk.Frame(self.frame_l, borderwidth=1)
        self.frame1.pack(padx=5, pady=10)

        self.frame2 = tk.Frame(self.frame_l, borderwidth=1)
        self.frame2.pack(padx=5, pady=5)

        self.l_name = tk.Label(self.frame1, text='      Name:')
        self.l_name.pack(side=LEFT)
        self.entry_name = tk.Entry(self.frame1, justify=RIGHT)
        self.entry_name.pack(side=LEFT)

        self.l_password = tk.Label(self.frame2, text='password:')
        self.l_password.pack(side=LEFT)
        self.entry_password = tk.Entry(self.frame2, show='*', justify=RIGHT)
        self.entry_password.pack(side=LEFT)

        self.btn_add = tk.Button(self.frame_r, text='Add', command=self.add)
        self.btn_add.pack(fill=X, expand=True, pady=5, padx=20)
        self.btn_remove = tk.Button(self.frame_r, text='Remove', command=self.remove)
        self.btn_remove.pack(fill=X, expand=True, pady=5, padx=20)
        self.btn_clear = tk.Button(self.frame_r, text='Clear', command=self.clear)
        self.btn_clear.pack(fill=X, expand=True, pady=5, padx=20, side=LEFT)
        self.btn_load = tk.Button(self.frame_r, text='Load', command=self.ShowUsers)
        self.btn_load.pack(fill=X, expand=True, pady=5, padx=20, side=LEFT)
        self.btn_exit = tk.Button(self.frame_r, text='Exit', command=self.exit)
        self.btn_exit.pack(pady=5, padx=20)

        self.scrollbar = tk.Scrollbar(self.frameN2)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox = tk.Listbox(self.frameN2, yscrollcommand=self.scrollbar.set)
        self.listbox.pack(fill=Y, expand=True, padx=5)
        self.scrollbar.config(command=self.listbox.yview)
        self.ShowUsers()
        self.mainloop()

    # add list from file to ListBox
    def ShowUsers(self):
        self.clear()
        file = UsersToFile('users.csv')
        users = file.openFile()
        for user in users:
            self.listbox.insert(END, user[0])

    def add(self):
        user = User(self.entry_name.get(), self.entry_password.get())
        if len(user.getName()) < 3:
            print('Enter the correct name!')
            messagebox.showinfo('Error', 'Enter the correct name!' )
            return False
        if len(user.getPassword()) < 6:
            print('Enter the password min 8 characters!')
            messagebox.showinfo('Error', 'Enter the password min 8 characters!')
            return False
        
        for i in range(self.listbox.size()):
            if user.getName() == self.listbox.get(i):
                return False

        self.listbox.insert(END, user.getName())

        # save to file
        file = UsersToFile('users.csv')
        file.addUser(user.getName(), user.getPassword())
        #
        # save to DB
        DB()
        DB.addToDB(user)
        #
        self.entry_name.delete(0, END)
        self.entry_password.delete(0, END)

    def remove(self):
        el = self.listbox.curselection()
        user = User(str(self.listbox.get(int(el[0]))), '')
        # remove in file
        file = UsersToFile('users.csv')
        file.openFile()
        file.removeUser(user.getName())
        #
        # Remove in DB
        DB()
        DB.removeToDB(user)
        #

        self.listbox.delete(el)

    def clear(self):
        self.listbox.delete(0,END)
    def exit(self):
       self.quit()
       self.destroy()

GUI()
