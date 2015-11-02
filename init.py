import psycopg2 as dbapi2

class INIT:
    def __init__(self, cp):
        self.cp = cp
        return
    def nations(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DROP TABLE IF EXISTS nations"
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

    def tracks(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DROP TABLE IF EXISTS tracks"
            cursor.execute(query)
        
            query = """CREATE TABLE tracks (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(40) UNIQUE NOT NULL
                )"""
            cursor.execute(query)

            query = """INSERT INTO tracks (title) VALUES ('Rally Jamaica');
                       INSERT INTO tracks (title) VALUES ('Intercity Istanbul Park');
                       INSERT INTO tracks (title) VALUES ('Cochrane Winter Rally');
                       INSERT INTO tracks (title) VALUES ('Rally Tasmania');
                       INSERT INTO tracks (title) VALUES ('Rally Argentina');
                       INSERT INTO tracks (title) VALUES ('Schneebergland Rallye');
                       INSERT INTO tracks (title) VALUES ('Bushy Park Circuit');
                       INSERT INTO tracks (title) VALUES ('Rally Van Haspengouw');
                       INSERT INTO tracks (title) VALUES ('Rally Hebros');
                       INSERT INTO tracks (title) VALUES ('Pražský Rallysprint');
                    """
            cursor.execute(query)
            connection.commit()

    def tires(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DROP TABLE IF EXISTS tires"
            cursor.execute(query)
        
            query = """CREATE TABLE tires (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(40) UNIQUE NOT NULL
                )"""
            cursor.execute(query)

            query = """INSERT INTO tires (title) VALUES ('Goodyear');
                       INSERT INTO tires (title) VALUES ('Pirelli');
                       INSERT INTO tires (title) VALUES ('BFGoodrich');
                       INSERT INTO tires (title) VALUES ('Michelin');
                       INSERT INTO tires (title) VALUES ('Yokohama');
                       INSERT INTO tires (title) VALUES ('Toyo');
                    """
            cursor.execute(query)
            connection.commit()

    def All(self):
        self.nations()
        self.tracks()
        self.tires()
