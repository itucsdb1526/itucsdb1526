import psycopg2 as dbapi2

class INIT:
    def __init__(self, cp):
        self.cp = cp
        return
    def nations(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """DROP TABLE IF EXISTS nations"""
            cursor.execute(query)
        
            query = """CREATE TABLE nations (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(40) UNIQUE NOT NULL
                )"""
            cursor.execute(query)

            cursor.execute("INSERT INTO nations (title) VALUES ('Turkiye')")
            cursor.execute("INSERT INTO nations (title) VALUES ('Germany')")
            cursor.execute("INSERT INTO nations (title) VALUES ('United Kingdom')")
            connection.commit()

    def All(self):
        self.nations()

