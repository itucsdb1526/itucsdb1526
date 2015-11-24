import psycopg2 as dbapi2

class Func:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_nations(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT title FROM nations ORDER BY title"""
            cursor.execute(query)
            rows = cursor.fetchall()
            nrows=[]
            for row in rows:
                nrows.append(row[0])
            return nrows

    def get_tracks(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT title FROM tracks ORDER BY id"""
            cursor.execute(query)
            rows = cursor.fetchall()
            nrows=[]
            for row in rows:
                nrows.append(row[0])
            return nrows

    def get_drivers(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT name FROM drivers ORDER BY name"""
            cursor.execute(query)
            rows = cursor.fetchall()
            nrows=[]
            for row in rows:
                nrows.append(row[0])
            return nrows

    def get_years(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT title FROM years ORDER BY id"""
            cursor.execute(query)
            rows = cursor.fetchall()
            nrows=[]
            for row in rows:
                nrows.append(row[0])
            return nrows
