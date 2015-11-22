import psycopg2 as dbapi2

class Track_info:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_trackinfolist(self,name):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT track_id, tracks.title, nations.title, lenght
                    FROM track_info RIGHT JOIN tracks ON (track_id = tracks.id) 
                    LEFT JOIN nations ON (nation_id=nations.id) WHERE (tracks.title LIKE '%%%s%%' OR nations.title LIKE '%%%s%%')  
                    ORDER BY tracks.id"""%(name,name)
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def delete_trackinfo(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM track_info WHERE track_id = '%s'" %(id)
            cursor.execute(query)
            connection.commit()
            return 
    def add_trackinfo(self, nname,coun,len):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            
            query="""INSERT INTO tracks (title) VALUES ('%s')""" %(nname)
            cursor.execute(query)

            query = "SELECT id FROM tracks WHERE title = '%s'" % (nname)
            cursor.execute(query)
            nid = cursor.fetchall()[0][0]

            query = "SELECT id FROM nations WHERE title = '%s'" % (coun)
            cursor.execute(query)
            cid = cursor.fetchall()[0][0]

            query = """INSERT INTO track_info VALUES ('%s','%s','%s')""" %(nid,cid,len)
            cursor.execute(query)

            connection.commit()
            return         

    def update_trackinfo(self, oname,nname,coun,len):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()

            query = "SELECT id FROM tracks WHERE title = '%s'" % (oname)
            cursor.execute(query)
            oid = cursor.fetchall()[0][0]


            query = "UPDATE tracks SET title='%s' WHERE title = '%s'" % (nname,oname)
            cursor.execute(query)

            query = "SELECT id FROM nations WHERE title = '%s'" % (coun)
            cursor.execute(query)
            cid = cursor.fetchall()[0][0]

            
            query = "UPDATE track_info SET nation_id='%s',lenght='%s' WHERE track_id = '%s'" %(cid,len,oid)
            cursor.execute(query)
            connection.commit()
            return