__author__ = 'hdemi'


import psycopg2 as dbapi2

class DriverInfo:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_driverinfo(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT DISTINCT DriverInfo.DRIVER_ID , nations.title, age, winning_number, Finishdistr.point
                    FROM DriverInfo left outer join nations on nations.id=nationid left outer join DRIVERS on DriverInfo.DRIVER_ID=DRIVERS.ID left outer join Finishdistr on Finishdistr.driver_id=DriverInfo.driver_id ORDER BY DRIVER_ID"""
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def delete_driver(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM DriverInfo WHERE DRIVER_ID = '%s'" % (id)
            cursor.execute(query)
            connection.commit()
            return

    def add_driver(self, id, nation_id, age ):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT COUNT(dr1_id) FROM RACEINFOS WHERE dr1_id = '%s'" % (id)
            cursor.execute(query)
            winning_number = cursor.fetchall()[0][0]
            query = "INSERT INTO DriverInfo VALUES ('%s','%s','%s','%s')" % (id,nation_id,age,winning_number)
            cursor.execute(query)
            connection.commit()
            return
    def search_byname(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()

            query = """SELECT DISTINCT DriverInfo.DRIVER_ID , nations.title, age, winning_number, Finishdistr.point
                    FROM DriverInfo left outer join nations on nations.id=nationid left outer join DRIVERS on DriverInfo.DRIVER_ID=DRIVERS.ID left outer join Finishdistr on Finishdistr.driver_id=DriverInfo.driver_id
                    WHERE (DriverInfo.driver_id = %s) ORDER BY DRIVER_ID
                    """ % (id)
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

