import psycopg2 as dbapi2

class Track_info:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_tracklist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT tracks.title, nations.title, lenght 
                    FROM track_info,tracks, nations 
                    WHERE ((track_id = tracks.id) AND (nation_id=nations.id))
                    """
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
