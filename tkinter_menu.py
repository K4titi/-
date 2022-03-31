import tkinter as tk
from tkinter import font as tkfont
from database import *


# def submit():
#     # print(fname.get(),lname.get(),mobile.get(),city.get(),email.get())
#     # print("to ekane")
#     create_user(fname)


class SampleApp(tk.Tk):

    #Αρχικοποίηση κλασης πατερα
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #Εισάγει την επικεφαλίδα με τη συγκερκιμένη μορφή
        self.title_font = tkfont.Font(family='Helvetica', size=15, slant="italic")

        #δημιουργει μία σελιδες με συγκερκιμένες διαστάσεις
        container = tk.Frame(self)
        container.pack(padx=100, pady=20)


        #Εισάγει στην σε ενα λεξικο τα ονοματα των κλασεων που εχουμε δημιουργήσει
        self.frames = {}
        for F in (Menu, Register_customer,Modification_customer, Modification_appointment):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            #Τοποθετει σωστα τις σελιδες ετσι ωστε να μην μπερδευονται η μια πανω απο τη αλλη
            frame.grid(row=0, column=0, sticky="nsew")


        #Αρχική εμφανιση της πρωτης σελιδας το μενου
        self.show_frame("Menu")

    #εμφανιση σελιδων σε χρηστη
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


#Δημιουργία κλάσης πρωτης σελίδας μενού
class Menu(tk.Frame):

    #Αρχικοποιηση κλασης μενου και δημιουργια κουμπιών για τη διαχειρηση της
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Μενού επιλογών", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        save_customer = tk.Button(self, text="Αποθήκευση πελάτη",
                            command=lambda: controller.show_frame("Register_customer"))
        modify_customer = tk.Button(self, text="Διαγραφή Πελάτη",
                            command=lambda: controller.show_frame("Modification_customer"))
        modify_appointment = tk.Button(self, text="Τροποποίηση Πελάτη",
                            command=lambda: controller.show_frame("Modification_customer"))
        search_view = tk.Button(self, text="Τροποποίηση Ραντεβού",
                                       command=lambda: controller.show_frame("Search_view"))
        save_customer.pack(fill="both")
        modify_customer.pack(fill="both")
        modify_appointment.pack(fill="both")
        search_view.pack(fill="both")


class Register_customer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text="Αποθήκευση Πελατών", font=controller.title_font).grid(row=0, column=1)


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

        begin = tk.Button(self, text="Αρχικό Μενού", command=lambda: controller.show_frame("Menu")).grid(row=10, column=1)
        save = tk.Button(self, text="Αποθήκευση", command=self.submit).grid(row=1, column=1)

    def submit(self):
        print(self.fname.get(),self.lname.get(),self.mobile.get(),self.city.get(),self.email.get())
        create_user(self.fname.get(),self.lname.get(),self.mobile.get(),self.city.get(),self.email.get())
        # create_appointment(self.date,self.start_time,self.end_time)

        self.fname.delete(0, "end")
        self.lname.delete(0, "end")
        self.mobile.delete(0,"end")
        self.city.delete(0, "end")
        self.email.delete(0,"end")
        self.date.delete(0,"end")
        self.start_time.delete(0,"end")
        self.end_time.delete(0,"end")




class Modification_customer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Τροποποίηση-Διαγραφή Πελατη", font=controller.title_font)
        label.grid(row=1, column=0)
        menu = tk.Button(self, text="Αρχικό Μενού", command=lambda: controller.show_frame("Menu"))
        menu.grid(row=2, column=0)
        modify = tk.Button(self, text="Τροποποίηση")
        modify.grid(row=3, column=0)
        customer = tk.Entry(self, width=30)
        customer.grid(row=3, column=1)
        modify = tk.Button(self, text="Διαγραφη")
        modify.grid(row=5, column=0)
        fname = tk.Entry(self, width=30)
        fname.grid(row=5, column=1)


class Modification_appointment(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Τροποποίηση-Διαγραφή Πελατη", font=controller.title_font)
        label.grid(row=1, column=0)
        menu = tk.Button(self, text="Αρχικό Μενού", command=lambda: controller.show_frame("Menu"))
        menu.grid(row=2, column=0)
        modify = tk.Button(self, text="Τροποποίηση")
        modify.grid(row=3, column=0)
        customer = tk.Entry(self, width=30)
        customer.grid(row=3, column=1)
        modify = tk.Button(self, text="Διαγραφη")
        modify.grid(row=5, column=0)

if __name__ == "__main__":
    app = SampleApp()
    app.title("Appointment Managment")
    app.mainloop()
