import psycopg2 as dbapi2

class Years:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_yearlist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Years ORDER BY id ASC"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def delete_year(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM Years WHERE id = '%s'" % (id) 
            cursor.execute(query)
            connection.commit()
            return

    def add_year(self, title):
        isTitleInt = False
        try:
            int(title)
            isTitleInt = True
        except:
            pass
        if(isTitleInt and int(title) >= 1952 and int(title) <= 2999):
            with dbapi2.connect(self.cp) as connection:
                cursor = connection.cursor()
                query = "INSERT INTO Years (title) VALUES ('%s')" % (title)
                cursor.execute(query)
                connection.commit()
                return
            
    def update_year(self, id, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE Years SET title = '%s' WHERE id = '%s'" % (title, id)
            cursor.execute(query)
            connection.commit()
            return