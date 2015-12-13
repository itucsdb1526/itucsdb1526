import psycopg2 as dbapi2

class Winrate:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_winratelist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT driver1_id, drivers.name, (FINISHDISTR.number_first+FINISHDISTR.number_second+FINISHDISTR.number_third), FINISHDISTR.number_first, (FINISHDISTR.number_first*100/(FINISHDISTR.number_first+FINISHDISTR.number_second+FINISHDISTR.number_third)) AS WINNRATE
                    FROM Winrates RIGHT JOIN drivers ON (driver1_id = drivers.id) 
                    LEFT JOIN FINISHDISTR ON (driver1_id = FINISHDISTR.DRIVER_ID) WHERE (FINISHDISTR.number_first != 0)
                    ORDER BY WINNRATE DESC
                    """
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