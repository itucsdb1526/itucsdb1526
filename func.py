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

    def get_id(self, tablename, value):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM {0} WHERE ".format(tablename)
            if tablename == 'drivers':
                query += "name = '{0}'".format(value)
            else:
                query += "title = '{0}'".format(value)
            cursor.execute(query)
            row = cursor.fetchone()
            if row is None:
                return None
            ret_id = row[0]
            return ret_id

    def get_title(self, tablename, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM {0} WHERE id = '{1}'".format(tablename, id)
            cursor.execute(query)
            row = cursor.fetchone()
            if row is None:
                return None
            ret_title = row[1]
            return ret_title
