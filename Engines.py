import psycopg2 as dbapi2

class Engines:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_enginelist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Engines"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def delete_engine(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM Engines WHERE id = '%s'" % (id) 
            cursor.execute(query)
            connection.commit()
            return

    def add_engine(self, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO Engines (title) VALUES ('%s')" % (title)
            cursor.execute(query)
            connection.commit()
            return
            
    def update_engine(self, id, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE Engines SET title = '%s' WHERE id = '%s'" % (title, id)
            cursor.execute(query)
            connection.commit()
            return