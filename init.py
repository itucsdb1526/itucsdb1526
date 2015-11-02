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

    def teams(self):
       with dbapi2.connect(self.cp) as connection:
           cursor = connection.cursor()
           query = "DROP TABLE IF EXISTS teams"
           cursor.execute(query)
       
           query = """CREATE TABLE teams (
                   id SERIAL PRIMARY KEY,
                   title VARCHAR(40) UNIQUE NOT NULL
               )"""
           cursor.execute(query)

           cursor.execute("INSERT INTO teams (title) VALUES ('Citroen')")
           cursor.execute("INSERT INTO teams (title) VALUES ('Volkswagen')")
           cursor.execute("INSERT INTO teams (title) VALUES ('Hyundai')")
           cursor.execute("INSERT INTO teams (title) VALUES ('F.W.R.T.')")
           cursor.execute("INSERT INTO teams (title) VALUES ('Subaru')")
           cursor.execute("INSERT INTO teams (title) VALUES ('Tofas')")
           connection.commit()

    def All(self):
        self.nations()
        self.tracks()
        self.teams()

