__author__ = 'hdemi'


import psycopg2 as dbapi2

class Finishdistr:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_finishdistr(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT DISTINCT DRIVER_ID , NAME, number_first, number_second, number_third
                    FROM FINISHDISTR, RACEINFOS,DRIVERS WHERE DRIVER_ID=DRIVERS.ID ORDER BY DRIVER_ID"""
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def delete_driver(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM FINISHDISTR WHERE DRIVER_ID = '%s'" % (id)
            cursor.execute(query)
            connection.commit()
            return

    def add_driver(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT COUNT(dr1_id) FROM RACEINFOS WHERE dr1_id = '%s'" % (id)
            cursor.execute(query)
            numberof1 = cursor.fetchall()[0][0]
            query = "SELECT COUNT(dr2_id) FROM RACEINFOS WHERE dr2_id = '%s'" % (id)
            cursor.execute(query)
            numberof2 = cursor.fetchall()[0][0]
            query = "SELECT COUNT(dr3_id) FROM RACEINFOS WHERE dr3_id = '%s'" % (id)
            cursor.execute(query)
            numberof3 = cursor.fetchall()[0][0]

            query = "INSERT INTO FINISHDISTR VALUES ('%s','%s','%s','%s')" % (id,numberof1,numberof2,numberof3)
            cursor.execute(query)
            connection.commit()
            return
    def search_byname(self, name):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()

            query = """SELECT DISTINCT DRIVER_ID , NAME, number_first, number_second, number_third
                    FROM FINISHDISTR, RACEINFOS,DRIVERS
                    WHERE (DRIVER_ID=DRIVERS.ID  AND NAME ILIKE '%%%s%%') ORDER BY DRIVER_ID
                    """ % (name)
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

