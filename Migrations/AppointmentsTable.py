def appointments_table(conDatabase):
    appointment = conDatabase.cursor()
    appointment.execute("CREATE TABLE IF NOT EXISTS appointments("
                        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                        "time INTEGER NOT NULL,"
                        "day TEXT NOT NULL,"
                        "customer_id INTEGER,"
                        "FOREIGN KEY(customer_id) REFERENCES customers(id) ); ")
    conDatabase.commit()