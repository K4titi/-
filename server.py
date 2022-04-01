import tkinter as tk
from tkinter import font as tkfont
import UI.Register as Register
import UI.Menu as Menu
import UI.ModifyCustomer as ModifyCustomer
import UI.ModifyAppointment as ModifyAppointment
from Migrations.TableCreation import sql_table
from database import conDatabase

# def submit():
#     # print(fname.get(),lname.get(),mobile.get(),city.get(),email.get())
#     # print("to ekane")
#     create_user(fname)


class server(tk.Tk):

    # Αρχικοποίηση κλασης πατερα
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        sql_table(conDatabase)

        # Εισάγει την επικεφαλίδα με τη συγκερκιμένη μορφή
        self.title_font = tkfont.Font(family='Helvetica', size=15, slant="italic")

        # δημιουργει μία σελιδες με συγκερκιμένες διαστάσεις
        container = tk.Frame(self)
        container.pack(padx=100, pady=20)

        # Declare forms
        self.frames = {
            "Register": Register.Register(parent=container, controller=self),
            "Menu": Menu.Menu(parent=container, controller=self),
            "ModifyCustomer": ModifyCustomer.ModifyCustomer(parent=container, controller=self),
            "ModifyAppointment": ModifyAppointment.ModifyAppointment(parent=container, controller=self)
        }

        # Layout
        self.frames["Menu"].grid(row=0, column=0, sticky="nsew")
        self.frames["Register"].grid(row=0, column=0, sticky="nsew")
        self.frames["ModifyCustomer"].grid(row=0, column=0, sticky="nsew")
        self.frames["ModifyAppointment"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("Menu")

    # εμφανιση σελιδων σε χρηστη
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = server()
    app.title("Appointment Managment")
    app.mainloop()
