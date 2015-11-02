import psycopg2 as dbapi2

class Tires:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_tirelist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Tires"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def delete_tire(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM Tires WHERE id = '%s'" % (id) 
            cursor.execute(query)
            connection.commit()
            return

    def add_tire(self, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO Tires (title) VALUES ('%s')" % (title)
            cursor.execute(query)
            connection.commit()
            return
            
    def update_tire(self, id, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE Tires SET title = '%s' WHERE id = '%s'" % (title, id)
            cursor.execute(query)
            connection.commit()
            return