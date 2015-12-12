import psycopg2 as dbapi2
from func import Func

class FastestDriver:
    def __init__(self, cp):
        self.cp = cp
        self.fn = Func(cp)
        return

    def get_fastestlist(self):
        with dbapi2.connect(self.cp) as connection:

            cursor = connection.cursor()
            query = """SELECT dr.name AS Driver, COUNT(rc.fastestdr_id) AS FastestCount FROM 
                    raceinfos rc JOIN drivers dr ON dr.id = rc.fastestdr_id GROUP BY dr.name
                    ORDER BY COUNT(rc.fastestdr_id) DESC
                    """
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows