import psycopg2 as dbapi2

class Func:
    def __init__(self, cp):
        self.cp = cp
        return


    def get_trackid(self, track_title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT id FROM tracks WHERE title='%s'"%(track_title)
            cursor.execute(query)
            return cursor.fetchall()[0][0]

    def get_trackinfo(self, t_id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """ SELECT tr.title AS Track, yr.title AS Year,
                    dr1.name AS First, dr2.name AS Second, dr3.name AS Third,
                    fdr.name AS FastestDr, rc.fastest_time AS FastestLap FROM
                    """     
            query += "(SELECT * FROM raceinfos WHERE track_id = '%s') rc" %(t_id)
            query +="""
                    JOIN tracks tr ON tr.id = rc.track_id
                    """
            query += "JOIN years yr ON yr.id = rc.year_id"
            query +="""
                    JOIN drivers dr1 ON dr1.id = rc.dr1_id
                    JOIN drivers dr2 ON dr2.id = rc.dr2_id
                    JOIN drivers dr3 ON dr3.id = rc.dr3_id
                    JOIN drivers fdr ON fdr.id = rc.fastestdr_id
                    ORDER BY Year 
                    """        
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def get_countryname(self,id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query="""SELECT title FROM nations WHERE id='%s'"""%(id)
            cursor.execute(query)
            return cursor.fetchall()[0][0]

    def get_country(self,rally_name):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query="""SELECT nation_id FROM tracks LEFT JOIN track_info ON (tracks.id=track_info.track_id) 
            WHERE (tracks.title='%s')"""%(rally_name)
            cursor.execute(query)
            return cursor.fetchall()[0][0]

    def get_firstrace(self,rally_name):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query="(SELECT MIN(year_id) FROM raceinfos WHERE (track_id=(SELECT id FROM tracks WHERE title ='%s')))"%(rally_name)
            cursor.execute(query)
            if(cursor.fetchall()[0][0]!=None):
                query="""SELECT title FROM years WHERE (id=(SELECT MIN(year_id) FROM raceinfos WHERE (track_id=(SELECT id FROM tracks WHERE title ='%s'))))"""%(rally_name)
                cursor.execute(query)
                return cursor.fetchall()[0][0]
            else:
                return "unknown"

            

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
