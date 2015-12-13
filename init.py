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

            cursor.execute("""INSERT INTO nations (title) VALUES 
              ('Turkey'), 
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
              ('Bulgaria'),
              ('Finland'),
              ('Qatar'),
              ('Uruguay'),
              ('Spain'),
              ('Japan'),
              ('Italy'),
              ('Hungary'),
              ('France');
            """)
            connection.commit()

    def nations_info(self):
      with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DROP TABLE IF EXISTS nations_info CASCADE"
            cursor.execute(query)
        
            query = """CREATE TABLE nations_info (
                    nation_id INTEGER NOT NULL REFERENCES nations
                        ON DELETE RESTRICT
                        ON UPDATE CASCADE,
                    capital VARCHAR(40) NOT NULL,
                    area_size NUMERIC(10),
                    population NUMERIC(10),
                    tld VARCHAR(10),
                    UNIQUE (nation_id)
                )"""
            cursor.execute(query)
            query = """INSERT INTO nations_info VALUES 
              (1, 'Ankara', 783562, 77695904, '.tr'), 
              (2, 'Berlin', 357168, 81083600, '.de/.eu'),
              (3, 'London', 242495, 64511000, '.uk'),
              (4, 'Prague', 78866, 10541466, '.cz'),
              (5, 'Buenos Aires', 2780400, 43417000, '.ar'),
              (6, 'Brussels', 30528, 11239755, '.be'),
              (7, 'Kingston', 10991, 2950210, '.jm'),
              (8, 'Canberra', 7692024, 23972100, '.au'),
              (9, 'Ottawa', 9984670, 35851774, '.ca'),
              (10, 'Vienna', 83879, 8623073, '.at'),
              (11, 'Baku', 86600, 9624900, '.az'),
              (12, 'Sofia', 110994, 7364570, '.bg'),
              (13, 'Helsinki', 338424, 5489097, '.fi'),
              (14, 'Doha', 11586, 2155446, '.qa'),
              (15, 'Montevideo', 176215, 3324460, '.uy'),
              (16, 'Madrid', 505990, 46439864, '.es'),
              (17, 'Tokyo', 377944, 126919659, '.jp'),
              (18, 'Rome', 301338, 60795612, '.it'),
              (19, 'Budapest', 93030, 9877365, '.hu'),
              (20, 'Bridgetown', 439, 277821, '.bb');
            """
            cursor.execute(query)
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
            for year in range(1983,2017):
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
                       (8, 25, 3, 2, 16, 2, 11, '01:57:20.898'),
                       (10, 15, 15, 2, 17, 6, 15, '00:23:22.295'),
                       (7, 20, 5, 4, 1, 2, 16, '01:23:29.355'),
                       (3, 8, 14, 17, 8, 2, 3, '00:33:15.807'),
                       (1, 26, 8, 1, 3, 3, 13, '00:23:45.909'),
                       (5, 6, 2, 15, 16, 2, 10, '00:05:35.589'),
                       (7, 29, 1, 7, 11, 7, 14, '00:40:33.801'),
                       (5, 23, 7, 5, 10, 8, 11, '00:24:21.433'),
                       (7, 32, 16, 4, 3, 4, 4, '00:33:44.879'),
                       (1, 4, 7, 8, 13, 1, 11, '00:22:40.521'),
                       (2, 21, 13, 6, 4, 1, 13, '01:18:17.154'),
                       (2, 31, 1, 13, 11, 7, 7, '00:23:18.952'),
                       (1, 19, 16, 15, 4, 8, 14, '01:28:36.176'),
                       (2, 3, 15, 16, 17, 3, 11, '00:39:22.602'),
                       (5, 22, 14, 9, 13, 10, 5, '01:13:29.945'),
                       (4, 5, 15, 7, 14, 5, 16, '00:10:06.771'),
                       (3, 11, 12, 4, 9, 1, 8, '01:50:50.710'),
                       (1, 2, 2, 15, 5, 4, 17, '00:44:52.993'),
                       (10, 30, 5, 14, 16, 8, 1, '00:52:32.816'),
                       (4, 18, 1, 13, 2, 9, 14, '00:18:10.115'),
                       (9, 34, 2, 9, 11, 8, 12, '00:09:48.891'),
                       (1, 24, 14, 2, 16, 4, 14, '01:04:51.943'),
                       (4, 16, 14, 7, 12, 2, 15, '00:00:36.127'),
                       (3, 28, 14, 6, 2, 6, 2, '00:19:20.637'),
                       (8, 7, 12, 3, 15, 6, 6, '00:10:30.067'),
                       (6, 33, 15, 5, 3, 2, 15, '00:25:38.893'),
                       (6, 13, 6, 8, 2, 9, 14, '00:09:43.522'),
                       (5, 14, 13, 2, 16, 9, 5, '01:46:59.067'),
                       (7, 17, 9, 8, 17, 3, 15, '01:01:51.173'),
                       (6, 9, 14, 3, 7, 10, 1, '00:26:28.582'),
                       (6, 10, 16, 10, 13, 3, 12, '01:35:24.538'),
                       (4, 27, 1, 4, 15, 9, 12, '01:56:35.711'),
                       (10, 12, 10, 13, 8, 10, 13, '01:37:24.991');
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
            		       ('Bosphorus Rally'),
                       ('Intercity Istanbul Park'),
                       ('Auf nach Melsungen'),
                       ('Cambrian Rally'),
                       ('Jim Clark Rally'),
                       ('Barum Czech Rally Zlín'),
                       ('Rally Krkonoše'),
                       ('Rally Argentina'),
                       ('Circuit des Ardennes'),
                       ('Rally Jamaica'),
                       ('Rally Australia'),
                       ('Cochrane Winter Rally'),
                       ('Judenburg-Pölstal Rallye'),
                       ('Rally Barbados'),
                       ('Rally Hebros'),
                       ('Arctic Lapland Rally'),
                       ('Neste Oil Rally Finland'),
                       ('Qatar International Rally'),
                       ('Rally del Atlántico'),
                       ('Rally Islas Canarias'),
                       ('Rally Hokkaido'),
                       ('Rally 1000 Miglia'),
                       ('Rally Alpi Orientali'),
                       ('Allianz Rallye'),
                       ('Rallye Antibes Côte d’Azur');
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
            			(2,1,4211.98),
            			(3,2,4981.1),
            			(4,3,4104.98),
            			(5,3,4696.51),
            			(6,4,3457.98),
            			(7,4,4771.51),
            			(8,5,3987.98),
            			(9,6,4532.51),
            			(10,7,4211.98),
                  (11,8,6234.1),
                  (12,9,8754.8),
                  (13,10,4498.6),
                  (14,11,3741.6),
                  (15,12,6628.0),
                  (16,13,5387.4),
                  (17,13,2981.4),
                  (18,14,3641.52),
                  (19,15,7534.45),
                  (20,16,6842.4),
                  (21,17,4918.7),
                  (22,18,6479.85),
                  (23,18,4718.62),
                  (24,19,7485.69),
                  (25,20,4483.7);
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
            			(9,2,1),
                             (10,2,1),
                             (11,1,1),
            			(12,5,5),
            			(13,4,2),
            			(14,2,5),
            			(15,3,6),
            			(16,4,3),
            			(17,4,4),
            			(18,1,2),
            			(19,2,1),
                             (20,2,1),
                             (21,1,1),
            			(22,5,5),
            			(23,4,2),
            			(24,2,5),
            			(25,3,6),
            			(26,4,3),
            			(27,4,4),
            			(28,1,2),
            			(29,2,1),
                             (30,2,1),
                             (31,1,1),
            			(32,5,5),
            			(33,4,2),
            			(34,2,5)
                               
                   """
           cursor.execute(query)
           connection.commit()


    def winrates(self):
       with dbapi2.connect(self.cp) as connection:
           cursor = connection.cursor()
           query = "DROP TABLE IF EXISTS winrates"
           cursor.execute(query)
       
           query = """CREATE TABLE winrates (
                    driver1_id INTEGER REFERENCES drivers(id) ON DELETE CASCADE ON UPDATE CASCADE

                )"""
               
            
           cursor.execute(query)

           query = """INSERT INTO winrates VALUES 
            			(1),
            			(2),
            			(3),
            			(4),
            			(5),
                             (6),
                             (7),
                             (8),
                             (9),
                             (10),
                             (11),
                             (12),
                             (13),
                             (14),
                             (15),
                             (16),
                             (17)
                             
                             
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
                       ('Marius Aasen'),
                       ('Kevin Abbring'),
                       ('Daniel Adamo'),
                       ('Andrea Aghini'),
                       ('Subhan Aksa'),
                       ('Nasser Al-Attiyah'),
                       ('Khalid Al-Qassimi'),
                       ('Francisco Alcuaz'),
                       ('Robert Woodside2'),
                       ('Miguel Vazquez2'),
                       ('Wilhelm Stengg2'),
                       ('Marius Aasen2'),
                       ('Juan Carlos Alonso');
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
                    number_third INTEGER,
                    point INTEGER
                )"""
            cursor.execute(query)
            query = """INSERT INTO Finishdistr VALUES
            			(1,2,2,2,116),
            			(2,1,2,1,76),
            			(3,1,4,1,112),
            			(4,2,5,2,170),
            			(5,4,1,3,163)
                    """
            cursor.execute(query)

            connection.commit()
            
    def sponsors(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DROP TABLE IF EXISTS Sponsors CASCADE"
            cursor.execute(query)

            query = """CREATE TABLE Sponsors(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(40) UNIQUE NOT NULL
                )"""
            cursor.execute(query)

            query = """INSERT INTO Sponsors (name) VALUES ('Erik Aaby'),
                       ('Ferrari'),
                       ('Force India'),
                       ('Lotus'),
                       ('Marussia'),
                       ('McLaren'),
                       ('Mercedes'),
                       ('Red Bull'),
                       ('Sauber'),
                       ('Toro Rosso	'),
                       ('Williams');
                    """
            cursor.execute(query)
            connection.commit()
    
    def driverinfo(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DROP TABLE IF EXISTS DriverInfo CASCADE"
            cursor.execute(query)
            query = """CREATE TABLE DriverInfo (
                    driver_id INTEGER NOT NULL REFERENCES drivers(id)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE,
                    nationid INTEGER REFERENCES nations(id),
                    age INTEGER,
                    winning_number INTEGER
                )"""
            cursor.execute(query)
            query = """INSERT INTO DriverInfo VALUES
            			(1,1,21,2),
            			(2,2,25,1),
            			(3,3,40,1),
            			(4,4,34,2),
            			(5,5,27,4);
                    """
            cursor.execute(query)
            connection.commit()

    def All(self):
        self.years()
        self.nations()
        self.nations_info()
        self.tracks()
        self.teams()
        self.engines()
        self.drivers()
        self.tires()
        self.tracks_info()
        self.raceinfos()
        self.champinfos()
        self.finishdistr()
        self.winrates()
        self.sponsors()
        self.driverinfo()

