import psycopg2 as dbapi2
from func import Func

class SuccessfulNats:
    def __init__(self, cp):
        self.cp = cp
        self.fn = Func(cp)
        return

    def get_sucnatlist(self):
        with dbapi2.connect(self.cp) as connection:

            cursor = connection.cursor()
            query = """SELECT nat.title AS Nation, COUNT(nat.title) AS NationCount FROM 
                    raceinfos rc
                    JOIN tracks tr ON tr.id = rc.track_id
                    JOIN years yr ON yr.id = rc.year_id
                    JOIN drivers dr1 ON dr1.id = rc.dr1_id
                    JOIN drivers dr2 ON dr2.id = rc.dr2_id
                    JOIN drivers dr3 ON dr3.id = rc.dr3_id
                    JOIN nations nat ON nat.id = rc.nation_id
                    JOIN drivers fdr ON fdr.id = rc.fastestdr_id
                    GROUP BY nat.title
                    ORDER BY NationCount DESC
                    """

            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def search_sucnatlist(self, form):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()

            query = """SELECT nat.title AS Nation, COUNT(nat.title) AS NationCount FROM 
                    raceinfos rc
                    JOIN tracks tr ON tr.id = rc.track_id
                    JOIN years yr ON yr.id = rc.year_id
                    JOIN drivers dr1 ON dr1.id = rc.dr1_id
                    JOIN drivers dr2 ON dr2.id = rc.dr2_id
                    JOIN drivers dr3 ON dr3.id = rc.dr3_id
                    JOIN nations nat ON nat.id = rc.nation_id
                    JOIN drivers fdr ON fdr.id = rc.fastestdr_id
                    GROUP BY nat.title
                    ORDER BY NationCount DESC
                    """

            query = "SELECT * FROM (" + query + ") AS Derived WHERE Derived.First ILIKE '%%%s%%'" % (form['SearchNation'])
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
