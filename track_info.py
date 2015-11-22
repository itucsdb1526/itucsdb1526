import psycopg2 as dbapi2

class Track_info:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_trackinfolist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT track_id, tracks.title, nations.title, lenght
                    FROM track_info LEFT JOIN tracks ON (track_id = tracks.id) 
                    LEFT JOIN nations ON (nation_id=nations.id) ORDER BY tracks.id"""
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