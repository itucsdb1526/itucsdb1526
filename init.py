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

            cursor.execute("""INSERT INTO nations (title) VALUES ('Turkiye'), 
              ('Germany'),
              ('United Kingdom'),
              ('Czech Republic'),
              ('Argentina'),
              ('Belgium'),
              ('Jamaica'),
              ('Australia'),
              ('Canada'),
              ('Austria'),
              ('Barbados'),
              ('Bulgaria');
            """)
            connection.commit()

    def years(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DROP TABLE IF EXISTS years"
            cursor.execute(query)
        
            query = """CREATE TABLE years (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(40) UNIQUE NOT NULL
                )"""
            cursor.execute(query)

            query = "INSERT INTO years (title) VALUES "
            for year in range(1952,2016):
                if(year != 2016):
                    query += "('%s')," % str(year)
                else:
                    query += "('%s');" % str(year)

            cursor.execute(query)
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





    def drivers(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DROP TABLE IF EXISTS Drivers"
            cursor.execute(query)

            query = """CREATE TABLE Drivers (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(40) UNIQUE NOT NULL
                )"""
            cursor.execute(query)

            query = """INSERT INTO Drivers (name) VALUES ('Erik Aaby');
                       INSERT INTO Drivers (name) VALUES ('Robert Woodside');
                       INSERT INTO Drivers (name) VALUES ('Miguel Vazquez');
                       INSERT INTO Drivers (name) VALUES ('Wilhelm Stengg');
                    """
            cursor.execute(query)
            connection.commit()



    def All(self):
        self.nations()
        self.years()
        self.tracks()
        self.teams()
        self.drivers()
        self.tires()

