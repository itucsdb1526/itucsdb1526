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
            query = "DROP TABLE IF EXISTS years CASCADE"
            cursor.execute(query)
        
            query = """CREATE TABLE years (
                    id SERIAL PRIMARY KEY,
                    title NUMERIC(4) UNIQUE NOT NULL
                )"""
            cursor.execute(query)

            query = "INSERT INTO years (title) VALUES "
            for year in range(1952,2017):
                if(year != 2016):
                    query += "(%s), " % str(year)
                else:
                    query += "(%s);" % str(year)

            cursor.execute(query)
            connection.commit()
    def raceinfos(self):
      with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DROP TABLE IF EXISTS raceinfos CASCADE"
            cursor.execute(query)

            query = """CREATE TABLE raceinfos (
                    track_id  INTEGER NOT NULL REFERENCES tracks(id)
                        ON DELETE RESTRICT
                        ON UPDATE CASCADE,
                    year_id INTEGER NOT NULL REFERENCES years
                        ON DELETE RESTRICT
                        ON UPDATE CASCADE,
                    dr1_id INTEGER NOT NULL REFERENCES drivers(id)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE,
                    dr2_id INTEGER REFERENCES drivers(id)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE,
                    dr3_id INTEGER REFERENCES drivers(id)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE,
                    nation_id INTEGER NOT NULL REFERENCES nations
                        ON DELETE RESTRICT
                        ON UPDATE CASCADE,
                    fastestdr_id INTEGER NOT NULL REFERENCES drivers(id)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE,
                    fastest_time TIME NOT NULL,
                    PRIMARY KEY(track_id, year_id)
              )"""
            cursor.execute(query)

            query = """INSERT INTO raceinfos (track_id, year_id, dr1_id, dr2_id, dr3_id, nation_id, fastestdr_id, fastest_time) VALUES
                       (7, 4, 8, 13, 11, 1, 14, '01:59:18.138'),
                       (4, 25, 11, 12, 4, 10, 15, '00:25:43.380'),
                       (3, 9, 5, 2, 14, 6, 9, '01:10:41.345'),
                       (1, 15, 5, 8, 10, 6, 5, '00:44:06.450'),
                       (7, 6, 14, 6, 3, 6, 3, '01:11:22.939'),
                       (7, 3, 9, 3, 11, 3, 11, '00:36:28.411'),
                       (10, 20, 3, 1, 14, 9, 4, '00:51:48.723'),
                       (6, 8, 10, 4, 2, 7, 6, '00:02:23.158'),
                       (2, 4, 6, 2, 15, 8, 9, '01:00:24.161'),
                       (4, 3, 1, 7, 8, 7, 11, '00:02:25.269'),
                       (3, 25, 4, 15, 1, 9, 10, '00:15:28.715'),
                       (6, 31, 5, 7, 4, 8, 12, '01:54:48.687'),
                       (9, 33, 11, 3, 5, 7, 12, '01:00:35.536'),
                       (10, 21, 9, 12, 10, 2, 5, '00:16:58.054'),
                       (10, 23, 1, 9, 10, 6, 14, '00:20:22.846'),
                       (4, 27, 15, 9, 1, 5, 2, '00:51:31.819'),
                       (8, 16, 10, 1, 13, 8, 4, '01:06:21.649'),
                       (2, 16, 6, 9, 5, 6, 6, '00:53:53.537'),
                       (2, 1, 12, 5, 9, 10, 12, '00:18:42.776'),
                       (7, 19, 12, 3, 7, 2, 13, '01:49:19.475'),
                       (7, 25, 4, 3, 15, 8, 3, '00:45:48.371'),
                       (6, 28, 9, 4, 11, 4, 10, '00:09:01.374'),
                       (9, 20, 2, 4, 7, 1, 15, '00:40:30.076'),
                       (8, 11, 7, 4, 8, 1, 8, '00:09:47.795'),
                       (7, 30, 12, 15, 6, 6, 4, '01:47:59.441'),
                       (2, 33, 10, 4, 7, 8, 7, '01:06:00.447'),
                       (6, 35, 13, 11, 5, 6, 14, '01:26:02.732'),
                       (8, 34, 10, 6, 8, 4, 9, '00:24:52.801'),
                       (2, 19, 5, 11, 10, 10, 14, '00:01:12.586'),
                       (7, 1, 15, 9, 13, 10, 15, '00:06:25.989');
            """
            cursor.execute(query);

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
            query = "DROP TABLE IF EXISTS tires CASCADE"
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
           query = "DROP TABLE IF EXISTS teams CASCADE"
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

    def champinfos(self):
       with dbapi2.connect(self.cp) as connection:
           cursor = connection.cursor()
           query = "DROP TABLE IF EXISTS champinfos"
           cursor.execute(query)
       
           query = """CREATE TABLE champinfos (
                    year_id INTEGER REFERENCES years(id) ON DELETE CASCADE ON UPDATE CASCADE,
                    driver_id INTEGER REFERENCES drivers(id) ON DELETE CASCADE ON UPDATE CASCADE,
                    team_id INTEGER REFERENCES teams(id) ON DELETE CASCADE ON UPDATE CASCADE
                )"""
               
            
           cursor.execute(query)

           query = """INSERT INTO champinfos VALUES 
            			(1,1,1),
            			(2,5,5),
            			(3,4,2),
            			(4,2,5),
            			(5,3,6),
            			(6,4,3),
            			(7,4,4),
            			(8,1,2),
            			(9,2,1)
                   """
           cursor.execute(query)
           connection.commit()






    def drivers(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DROP TABLE IF EXISTS Drivers CASCADE"
            cursor.execute(query)

            query = """CREATE TABLE Drivers (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(40) UNIQUE NOT NULL
                )"""
            cursor.execute(query)

            query = """INSERT INTO Drivers (name) VALUES ('Erik Aaby'),
                       ('Robert Woodside'),
                       ('Miguel Vazquez'),
                       ('Wilhelm Stengg'),
                       ('Wilhelm Stengg1'),
                       ('Wilhelm Stengg2'),
                       ('Wilhelm Stengg3'),
                       ('Wilhelm Stengg4'),
                       ('Wilhelm Stengg5'),
                       ('Wilhelm Stengg6'),
                       ('Wilhelm Stengg7'),
                       ('Wilhelm Stengg8'),
                       ('Wilhelm Stengg9'),
                       ('Wilhelm Stengg10'),
                       ('Wilhelm Stengg11'),
                       ('Wilhelm Stengg12'),
                       ('Wilhelm Stengg13');
                    """
            cursor.execute(query)
            connection.commit()

def finishdistr(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DROP TABLE IF EXISTS Finishdistr CASCADE"
            cursor.execute(query)

            query = """CREATE TABLE Finishdistr (
                    driver_id INTEGER NOT NULL REFERENCES drivers(id)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE,
                    number_first INTEGER,
                    number_second INTEGER,
                    number_third INTEGER
                )"""
            cursor.execute(query)
            query = """INSERT INTO Finishdistr VALUES
            			(1,2,2,2),
            			(2,1,2,1),
            			(3,1,4,1),
            			(4,2,5,2),
            			(5,4,1,3)
                    """
            cursor.execute(query)

            connection.commit()

    def All(self):
        self.years()
        self.nations()
        self.tracks()
        self.teams()
        self.engines()
        self.drivers()
        self.tires()
        self.raceinfos()
        self.tracks_info()
        self.champinfos()

