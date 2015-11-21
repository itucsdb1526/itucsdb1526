import psycopg2 as dbapi2

class Raceinfos:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_raceinfolist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """ SELECT tr.title AS Track, yr.title AS Year,
                    dr1.name AS First, dr2.name AS Second, dr3.name AS Third,
                    nat.title AS Nation, fdr.name AS FastestDr, rc.fastest_time AS FastestLap FROM 
                    raceinfos rc
                    JOIN tracks tr ON tr.id = rc.track_id
                    JOIN years yr ON yr.id = rc.year_id
                    JOIN drivers dr1 ON dr1.id = rc.dr1_id
                    JOIN drivers dr2 ON dr2.id = rc.dr2_id
                    JOIN drivers dr3 ON dr3.id = rc.dr3_id
                    JOIN nations nat ON nat.id = rc.nation_id
                    JOIN drivers fdr ON fdr.id = rc.fastestdr_id
                    ORDER BY rc.track_id ASC, rc.year_id ASC;
                    """         
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def delete_raceinfo(self, n_raceinfo):
        raceinfo = n_raceinfo.split(":")
        print(raceinfo[0], raceinfo[1])
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM tracks WHERE title = '%s'" % (raceinfo[0])
            cursor.execute(query)
            track_id = cursor.fetchone()[0]

            query = "SELECT * FROM years WHERE title = '%s'" % (raceinfo[1])
            cursor.execute(query)
            year_id = cursor.fetchone()[0]
            
            query = "DELETE FROM raceinfos WHERE (track_id = '%s' AND year_id = '%s')" % (str(track_id), str(year_id))
            cursor.execute(query)
            connection.commit()
            return

    def add_raceinfo(self, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO raceinfos (title) VALUES ('%s')" % (title)
            cursor.execute(query)
            connection.commit()
            return
            
    def update_raceinfo(self, id, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE raceinfo SET title = '%s' WHERE id = '%s'" % (title, id)
            cursor.execute(query)
            connection.commit()
            return