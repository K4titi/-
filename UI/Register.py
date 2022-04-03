import tkinter as tk
from Models.UserModel import *


class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text="Νέα Εγγραφή", font=controller.title_font).grid(row=0, column=1)

        self.fname = tk.Entry(self, width=30)
        self.fname.grid(row=2, column=1)
        self.lname = tk.Entry(self, width=30)
        self.lname.grid(row=3, column=1)
        self.mobile = tk.Entry(self, width=30)
        self.mobile.grid(row=4, column=1)
        self.city = tk.Entry(self, width=30)
        self.city.grid(row=5, column=1)
        self.email = tk.Entry(self, width=30)
        self.email.grid(row=6, column=1)
        self.date = tk.Entry(self, width=30)
        self.date.grid(row=7, column=1)
        self.start_time = tk.Entry(self, width=30)
        self.start_time.grid(row=8, column=1)
        self.end_time = tk.Entry(self, width=30)
        self.end_time.grid(row=9, column=1)

        self.fname_label = tk.Label(self, text="Όνομα").grid(row=2, column=0)
        self.lastName_label = tk.Label(self, text="Επώνυμο").grid(row=3, column=0)
        self.mobile_label = tk.Label(self, text="Κινητό").grid(row=4, column=0)
        self.city_label = tk.Label(self, text="Πόλη").grid(row=5, column=0)
        self.email_label = tk.Label(self, text="e-mail").grid(row=6, column=0)
        self.date_label = tk.Label(self, text="Ημερομηνία").grid(row=7, column=0)
        self.start_time_label = tk.Label(self, text="Ώρα έναρξης").grid(row=8, column=0)
        self.end_time_label = tk.Label(self, text="Ώρα λήξης").grid(row=9, column=0)

        tk.Button(self, text="Αρχικό Μενού", command=lambda: controller.show_frame("Menu")).grid(row=10,
                                                                                                         column=1)
        tk.Button(self, text="Αποθήκευση", command=self.submit).grid(row=1, column=1)

    def submit(self):
        print(self.fname.get(), self.lname.get(), self.mobile.get(), self.city.get(), self.email.get())
        create_user(self.fname.get(), self.lname.get(), self.mobile.get(), self.city.get(), self.email.get())
        # create_appointment(self.date,self.start_time,self.end_time)

        self.fname.delete(0, "end")
        self.lname.delete(0, "end")
        self.mobile.delete(0, "end")
        self.city.delete(0, "end")
        self.email.delete(0, "end")
        self.date.delete(0, "end")
        self.start_time.delete(0, "end")
        self.end_time.delete(0, "end")
