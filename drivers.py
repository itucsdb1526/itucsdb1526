__author__ = 'hdemi'


import psycopg2 as dbapi2

class Drivers:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_driverlist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Drivers ORDER BY ID"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def delete_driver(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM Drivers WHERE id = '%s'" % (id)
            cursor.execute(query)
            connection.commit()
            return

    def add_driver(self, name):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO Drivers (name) VALUES ('%s')" % (name)
            cursor.execute(query)
            connection.commit()
            return

    def update_driver(self, id, name):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE Drivers SET name = '%s' WHERE id = '%s'" % (name, id)
            cursor.execute(query)
            connection.commit()
            return
