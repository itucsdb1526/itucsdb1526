import psycopg2 as dbapi2

class INIT:
    def __init__(self, cp):
        self.cp = cp
        return
    def nations(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DROP TABLE IF EXISTS nations CASCADE"
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
            for year in range(1952,2017):
                if(year != 2016):
                    query += "('%s'), " % str(year)
                else:
                    query += "('%s');" % str(year)

            cursor.execute(query)
            connection.commit()

    def tracks(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DROP TABLE IF EXISTS tracks CASCADE"
            cursor.execute(query)
        
            query = """CREATE TABLE tracks (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(40) UNIQUE NOT NULL
                )"""
            cursor.execute(query)

            query = """INSERT INTO tracks (title) VALUES 
            		   ('Rally Jamaica'),
                       ('Intercity Istanbul Park'),
                       ('Cochrane Winter Rally'),
                       ('Rally Tasmania'),
                       ('Rally Argentina'),
                       ('Schneebergland Rallye'),
                       ('Bushy Park Circuit'),
                       ('Rally Van Haspengouw'),
                       ('Rally Hebros'),
                       ('Pražský Rallysprint');
                    """
            cursor.execute(query)
            connection.commit()

    def tracks_info(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DROP TABLE IF EXISTS track_info"
            cursor.execute(query)
        
            query = """CREATE TABLE track_info (
                    track_id INTEGER REFERENCES tracks(id) ON DELETE CASCADE ON UPDATE CASCADE,
                    nation_id INTEGER REFERENCES nations(id) ON DELETE CASCADE ON UPDATE CASCADE,
                    lenght NUMERIC
                )"""
            cursor.execute(query)

            query = """INSERT INTO track_info VALUES 
            			(1,1,4532.51),
            			(2,5,4211.98),
            			(3,4,4981.1),
            			(4,2,4104.98),
            			(5,3,4696.51),
            			(6,4,3457.98),
            			(7,4,4771.51),
            			(8,1,3987.98),
            			(9,2,4532.51),
            			(10,5,4211.98)
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

            query = """INSERT INTO tires (title) VALUES ('Goodyear'),
                       ('Pirelli'),
                       ('BFGoodrich'),
                       ('Michelin'),
                       ('Yokohama'),
                       ('Toyo');
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
           cursor.execute("INSERT INTO teams (title) VALUES ('Mercedes')")
           cursor.execute("INSERT INTO teams (title) VALUES ('Ferrari')")
           cursor.execute("INSERT INTO teams (title) VALUES ('Mclaren')")
           cursor.execute("INSERT INTO teams (title) VALUES ('Anadol')")
           connection.commit()
           
           
    def engines(self):
       with dbapi2.connect(self.cp) as connection:
           cursor = connection.cursor()
           query = "DROP TABLE IF EXISTS engines"
           cursor.execute(query)
       
           query = """CREATE TABLE engines (
                   id SERIAL PRIMARY KEY,
                   title VARCHAR(40) UNIQUE NOT NULL
               )"""
           cursor.execute(query)

           cursor.execute("INSERT INTO engines (title) VALUES ('Motor1')")
           cursor.execute("INSERT INTO engines (title) VALUES ('Motor2')")
           cursor.execute("INSERT INTO engines (title) VALUES ('Motor3')")
           cursor.execute("INSERT INTO engines (title) VALUES ('Motor4')")
           cursor.execute("INSERT INTO engines (title) VALUES ('Motor5')")
           cursor.execute("INSERT INTO engines (title) VALUES ('Motor6')")
           cursor.execute("INSERT INTO engines (title) VALUES ('Motor7')")
           cursor.execute("INSERT INTO engines (title) VALUES ('Motor8')")
           cursor.execute("INSERT INTO engines (title) VALUES ('Motor9')")
           cursor.execute("INSERT INTO engines (title) VALUES ('Motor10')")
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

            query = """INSERT INTO Drivers (name) VALUES ('Erik Aaby'),
                       ('Robert Woodside'),
                       ('Miguel Vazquez'),
                       ('Wilhelm Stengg');
                    """
            cursor.execute(query)
            connection.commit()



    def All(self):
        self.years()
        self.tracks_info()
        self.nations()
        self.tracks()
        self.teams()
        self.engines()
        self.drivers()
        self.tires()

