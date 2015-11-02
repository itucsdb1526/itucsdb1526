import psycopg2 as dbapi2

class Teams:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_teamlist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Teams"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def delete_team(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM Teams WHERE id = '%s'" % (id) 
            cursor.execute(query)
            connection.commit()
            return

    def add_team(self, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO Teams (title) VALUES ('%s')" % (title)
            cursor.execute(query)
            connection.commit()
            return
            
    def update_team(self, id, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE Teams SET title = '%s' WHERE id = '%s'" % (title, id)
            cursor.execute(query)
            connection.commit()
            return