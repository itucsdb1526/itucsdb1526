import psycopg2 as dbapi2

class Champinfo:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_champinfolist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT year_id, years.title, drivers.name, teams.title
                    FROM Champinfos LEFT JOIN years ON (year_id = years.id) 
                    LEFT JOIN drivers ON (driver_id=drivers.id) 
                    LEFT JOIN teams ON (team_id = teams.id) 
                    ORDER BY years.id"""
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

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
            
    def get_teams(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT title FROM teams ORDER BY title"""
            cursor.execute(query)
            rows = cursor.fetchall()
            nrows=[]
            for row in rows:
                nrows.append(row[0])
            return nrows
    
    def delete_champinfo(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM Champinfos WHERE year_id = '%s'" % (id) 
            cursor.execute(query)
            connection.commit()
            return

    def add_champinfo(self, nyear, ndriv, nteam):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            
            query="""INSERT INTO years (title) VALUES ('%s')""" %(nyear)
            cursor.execute(query)            
            
            
            query = "SELECT id FROM years WHERE title = '%s'" % (nyear)
            cursor.execute(query)
            nid = cursor.fetchall()[0][0]

            query = "SELECT id FROM drivers WHERE name = '%s'" % (ndriv)
            cursor.execute(query)
            cid = cursor.fetchall()[0][0]

            query = "SELECT id FROM teams WHERE title = '%s'" % (nteam)
            cursor.execute(query)
            tid = cursor.fetchall()[0][0]
            
            query = """INSERT INTO Champinfos VALUES ('%s','%s','%s')""" %(nid,cid,tid)
            cursor.execute(query)

            connection.commit()
            return
            
    def update_champinfo(self, oyear, nyear, ndriv, nteam):
        with dbapi2.connect(self.cp) as connection:           
            cursor = connection.cursor()

            query = "SELECT id FROM years WHERE title = '%s'" % (oyear)
            cursor.execute(query)
            oid = cursor.fetchall()[0][0]

            
            query = "SELECT id FROM years WHERE title = '%s'" % (nyear)
            cursor.execute(query)
            nid = cursor.fetchall()[0][0]

            query = "SELECT id FROM drivers WHERE name = '%s'" % (ndriv)
            cursor.execute(query)
            cid = cursor.fetchall()[0][0]

            query = "SELECT id FROM teams WHERE title = '%s'" % (nteam)
            cursor.execute(query)
            tid = cursor.fetchall()[0][0]
            
            query = "UPDATE Champinfos SET year_id = '%s', driver_id='%s',team_id='%s' WHERE year_id = '%s'" %(nid,cid,tid,oid)
            cursor.execute(query)
            connection.commit()            
            
            return
            
    def search_champinfolist(self, name):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()

            query = """SELECT year_id, years.title, drivers.name ,teams.title
                    FROM Champinfos LEFT JOIN years ON (year_id = years.id) 
                    LEFT JOIN drivers ON (driver_id=drivers.id) 
                    LEFT JOIN teams ON (team_id = teams.id) WHERE (drivers.name ILIKE '%%%s%%' OR teams.title ILIKE '%%%s%%' )
                    ORDER BY year_id"""%(name,name)
                 
            
            
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows