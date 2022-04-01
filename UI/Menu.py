import tkinter as tk


class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Μενού επιλογών", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        save_customer = tk.Button(self, text="Αποθήκευση πελάτη",
                                  command=lambda: controller.show_frame("Register"))
        modify_customer = tk.Button(self, text="Διαγραφή Πελάτη",
                                    command=lambda: controller.show_frame("ModifyCustomer"))
        modify_appointment = tk.Button(self, text="Τροποποίηση Πελάτη",
                                       command=lambda: controller.show_frame("ModifyCustomer"))
        search_view = tk.Button(self, text="Τροποποίηση Ραντεβού",
                                command=lambda: controller.show_frame("ModifyAppointment"))
        save_customer.pack(fill="both")
        modify_customer.pack(fill="both")
        modify_appointment.pack(fill="both")
        search_view.pack(fill="both")
