import tkinter as tk


class ModifyAppointment(tk.Frame):
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
