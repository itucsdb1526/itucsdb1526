import psycopg2 as dbapi2

class Nations:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_nationlist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Nations"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def delete_nation(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM Nations WHERE id = '%s'" % (id) 
            cursor.execute(query)
            connection.commit()
            return

    def add_nation(self, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO Nations (title) VALUES ('%s')" % (title)
            cursor.execute(query)
            connection.commit()
            return
            
    def update_nation(self, id, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE Nations SET title = '%s' WHERE id = '%s'" % (title, id)
            cursor.execute(query)
            connection.commit()
            return