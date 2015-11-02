import psycopg2 as dbapi2

class Tracks:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_tracklist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Tracks"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def delete_track(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM Tracks WHERE id = '%s'" % (id) 
            cursor.execute(query)
            connection.commit()
            return

    def add_track(self, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO Tracks (title) VALUES ('%s')" % (title)
            cursor.execute(query)
            connection.commit()
            return
            
    def update_track(self, id, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE Tracks SET title = '%s' WHERE id = '%s'" % (title, id)
            cursor.execute(query)
            connection.commit()
            return