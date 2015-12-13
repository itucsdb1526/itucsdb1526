__author__ = 'hdemi'


import psycopg2 as dbapi2

class Sponsors:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_sponsorlist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Sponsors ORDER BY ID"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def delete_sponsor(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM Sponsors WHERE id = '%s'" % (id)
            cursor.execute(query)
            connection.commit()
            return

    def add_sponsor(self, name):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO Sponsors (name) VALUES ('%s')" % (name)
            cursor.execute(query)
            connection.commit()
            return

    def update_sponsor(self, id, name):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE Sponsors SET name = '%s' WHERE id = '%s'" % (name, id)
            cursor.execute(query)
            connection.commit()
            return
