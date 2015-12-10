import psycopg2 as dbapi2
from nation import Nation

class Nations:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_nationlist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Nations ORDER BY id ASC"
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

    def get_a_nation(self, id):
        if id is None:
            return None
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT nat.title AS Title, ninf.capital AS Capital, ninf.area_size AS Area, 
                    ninf.population AS Population, ninf.tld AS TLD
                    FROM 
                    nations_info ninf
                    JOIN (SELECT * FROM Nations WHERE id = '%s') nat ON ninf.nation_id = nat.id
                    """ % (id)
            cursor.execute(query)
            row = cursor.fetchone()
            if row is None:
                return None
            nat = Nation(row[0], row[1], row[2], row[3], row[4])
            return nat
            
    def get_trackfornation(self,nat_id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT tracks.id, tracks.title, nat.title, lenght
                    FROM track_info INNER JOIN tracks ON (track_id = tracks.id) 
                    INNER JOIN (SELECT * FROM nations WHERE id = '%s') AS nat
                    ON (nation_id=nat.id)
                    ORDER BY tracks.id"""%(nat_id)
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
