import psycopg2 as dbapi2
from func import Func

class Raceinfos:
    def __init__(self, cp):
        self.cp = cp
        self.fn = Func(cp)
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

    def add_raceinfo(self, form):
        track_id = self.fn.get_id("tracks", form.get('Track'))
        year_id = self.fn.get_id("years", form.get('Year'))
        dr1_id = self.fn.get_id("drivers", form.get('First'))
        dr2_id = self.fn.get_id("drivers", form.get('Second'))
        dr3_id = self.fn.get_id("drivers", form.get('Third'))
        nation_id = self.fn.get_id("nations", form.get('Nation'))
        fastestdr_id = self.fn.get_id("drivers", form.get('FastestDr'))
        fastest_time = form['FastestLap']
        if (dr1_id == dr2_id) or (dr1_id == dr3_id) or (dr2_id == dr3_id):
            return
            
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO raceinfos  VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s' ,'%s')" % (track_id, year_id, dr1_id, dr2_id, dr3_id, nation_id, fastestdr_id, fastest_time)
            cursor.execute(query)
            connection.commit()
            return
            
    def update_raceinfo(self, form):
        track_id = self.get_id("tracks", form.get('Track'))
        year_id = self.get_id("years", form.get('Year'))
        dr1_id = self.get_id("drivers", form.get('First'))
        dr2_id = self.get_id("drivers", form.get('Second'))
        dr3_id = self.get_id("drivers", form.get('Third'))
        nation_id = self.get_id("nations", form.get('Nation'))
        fastestdr_id = self.get_id("drivers", form.get('FastestDr'))
        fastest_time = form['FastestLap']
        if (dr1_id == dr2_id) or (dr1_id == dr3_id) or (dr2_id == dr3_id):
            return

        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE raceinfos SET dr1_id = '{0}', dr2_id = '{1}', dr3_id = '{2}', nation_id = '{3}', fastestdr_id = '{4}', fastest_time = '{5}' WHERE track_id = '{6}' AND year_id = '{7}'".format(dr1_id, dr2_id, dr3_id, nation_id, fastestdr_id, fastest_time, track_id, year_id)
            cursor.execute(query)
            connection.commit()
            return
    def search_raceinfolist(self, searchtype, form):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()

            query = """SELECT tr.title AS Track, yr.title AS Year,
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
                    ORDER BY rc.track_id ASC, rc.year_id ASC
                    """
            if searchtype == 'winner':
                query = "SELECT * FROM (" + query + ") AS Derived WHERE Derived.First ILIKE '%%%s%%'" % (form['SearchWinner'])
            if searchtype == 'track':
                query = "SELECT * FROM (" + query + ") AS Derived WHERE Derived.Track ILIKE '%%%s%%'" % (form['SearchTrack'])
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
