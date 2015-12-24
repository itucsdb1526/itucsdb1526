Parts Implemented by Alper Akyıldız
======================================

Tracks List
----------------

| This table contains two attributes tracks and their id's. Id is primary key and serial. Title is string that length to 40 character. There are add, delete and update functions of this table.

.. code-block:: python

        query = """CREATE TABLE tracks (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(40) UNIQUE NOT NULL
                )"""
                cursor.execute(query)

| Get, delete add and update operations are called in server.py shown at below. These operations functions are written in tracks.py file.

.. code-block:: python
	
    @app.route('/Tracks', methods=['GET', 'POST'])
    def track_page():
        tras = Tracks(app.config['dsn'])
        if request.method == 'GET':
            now = datetime.datetime.now()
            tlist = tras.get_tracklist()
            return render_template('tracks.html', TrackList = tlist, current_time = now.ctime())
        elif 'tracks_to_delete' in request.form:
            ids = request.form.getlist('tracks_to_delete') 
            for id in ids:
                tras.delete_track(id)
                return redirect(url_for('track_page'))
        elif 'tracks_to_add' in request.form:
            tras.add_track(request.form['title'])
            return redirect(url_for('track_page'))
        elif 'tracks_to_update' in request.form:
            tras.update_track(request.form['id'], request.form['title'])
            return redirect(url_for('track_page'))

Track listing
++++++++++++++++++

| Prints all of tracks.

.. code-block:: python
	
    def get_tracklist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT * FROM tracks"""
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows


Track adding
+++++++++++++++++++

| Add track according to title. Id increment automatically.
.. code-block:: python
	
    def add_track(self, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO Tracks (title) VALUES ('%s')" % (title)
            cursor.execute(query)
            connection.commit()
            return

Track deleting
+++++++++++++++++++

| Delete track according to id.
.. code-block:: python
	
    def delete_track(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM Tracks WHERE id = '%s'" % (id) 
            cursor.execute(query)
            connection.commit()
            return

Track updating
+++++++++++++++++++

| Select track according to id and rename it.
.. code-block:: python
	
    def update_track(self, id, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE Tracks SET title = '%s' WHERE id = '%s'" % (title, id)
            cursor.execute(query)
            connection.commit()
            return

Tires List
----------------

| This table contains two attributes: tire names and their id's. Id is primary key and serial. Title is string that length to 40 character. There are add, delete and update functions of  table.

.. code-block:: python

    query = """CREATE TABLE tires (
                id SERIAL PRIMARY KEY,
                title VARCHAR(40) UNIQUE NOT NULL)
            """
    cursor.execute(query)
               

| Get, delete add and update operations are called in server.py shown at below. These operations functions are written in tires.py file.

.. code-block:: python

    @app.route('/Tires', methods=['GET', 'POST'])
    def tire_page():
        tirs = Tires(app.config['dsn'])
        if request.method == 'GET':
            now = datetime.datetime.now()
            tilist = tirs.get_tirelist()    
            return render_template('tires.html', TireList = tilist, current_time = now.ctime())
        elif 'tires_to_delete' in request.form:
            ids = request.form.getlist('tires_to_delete') 
            for id in ids:
                tirs.delete_tire(id)
            return redirect(url_for('tire_page'))
        elif 'tires_to_add' in request.form:
            tirs.add_tire(request.form['title'])
            return redirect(url_for('tire_page'))
        elif 'tires_to_update' in request.form:
            tirs.update_tire(request.form['id'], request.form['title'])
            return redirect(url_for('tire_page'))


Tire listing
++++++++++++++++++

| Prints all of tires.

.. code-block:: python

    def get_tirelist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Tires"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows


Tire adding
+++++++++++++++++++

| Add track according to title. Id increment automatically.

.. code-block:: python

    def add_tire(self, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO Tires (title) VALUES ('%s')" % (title)
            cursor.execute(query)
            connection.commit()
            return


Tire deleting
+++++++++++++++++++

| Delete tire according to id.

.. code-block:: python

    def delete_tire(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM Tires WHERE id = '%s'" % (id) 
            cursor.execute(query)
            connection.commit()
            return


Track Information List
-----------------------------

| This table contains three attributes track id nation id and length of pists. Track id referenced from tracks table and nation id referenced from nations table.
Both of them cascade on update and delete. Length is numeric, contain length of pist.

.. code-block:: python

    query = """CREATE TABLE track_info (
                    track_id INTEGER REFERENCES tracks(id) ON DELETE CASCADE ON UPDATE CASCADE,
                    nation_id INTEGER REFERENCES nations(id) ON DELETE CASCADE ON UPDATE CASCADE,
                    lenght NUMERIC)
            """
            cursor.execute(query)


| Get, delete, add, search and update operations are called in server.py shown at below. These operations functions are written in track_info.py file.

.. code-block:: python

    @app.route('/Track_info', methods=['GET', 'POST'])
    def track_info_page():
        trainfos = Track_info(app.config['dsn'])
        if request.method == 'GET':
            now = datetime.datetime.now()
            tlist = trainfos.get_trackinfolist('')
            nations=trainfos.get_nations()
            tracks=trainfos.get_tracks()
            return render_template('track_info.html', TrackInfoList = tlist,nations=nations,tracks=tracks, current_time = now.ctime())
        elif 'trackinfo_to_delete' in request.form:
            ids = request.form.getlist('trackinfo_to_delete') 
            for id in ids:
                print(id)
                trainfos.delete_trackinfo(id)
        elif 'trackinfo_to_update' in request.form:
            oname=request.form['oname']
            nname=request.form['nname']
            coun=request.form['coun']
            len=request.form['len']
            trainfos.update_trackinfo(oname,nname,coun,len)
        elif 'trackinfo_to_add' in request.form:
            nname=request.form['nname']
            coun=request.form['coun']
            len=request.form['len']
            trainfos.add_trackinfo(nname,coun,len)
        elif 'trackinfo_to_search' in request.form:
            now = datetime.datetime.now()
            tlist = trainfos.get_trackinfolist(request.form['name'])
            return render_template('track_info.html', TrackInfoList = tlist, current_time = now.ctime())   
        return redirect(url_for('track_info_page'))

Track information listing
+++++++++++++++++++++++++++++

| Prints all of tracks informations.

| get_nations function returns nation names. In server.py these nation names stored in nation tuple.

.. code-block:: python

    def get_nations(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT title FROM nations ORDER BY title"""
            cursor.execute(query)
            rows = cursor.fetchall()
            nrows=[]
            for row in rows:
                nrows.append(row[0])
            return nrows


| get_tracks function returns track names. In server.py these tracks names stored in tracks tuple.

.. code-block:: python

    def get_tracks(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT title FROM tracks ORDER BY id"""
            cursor.execute(query)
            rows = cursor.fetchall()
            nrows=[]
            for row in rows:
                nrows.append(row[0])
            return nrows

| get_trackinfolist function returns tracks id track titles nations of ttracks and length of them.

.. code-block:: python

    def get_trackinfolist(self,name):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT tracks.id, tracks.title, nations.title, lenght
                    FROM track_info LEFT JOIN tracks ON (track_id = tracks.id) 
                    LEFT JOIN nations ON (nation_id=nations.id) WHERE (tracks.title ILIKE '%%%s%%' OR nations.title ILIKE '%%%s%%')  
                    ORDER BY tracks.id"""%(name,name)
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows


Track information adding
+++++++++++++++++++++++++++++

| add_trackinfo function crates new track on tracks table and take its id, find country id using given country name and insert new track information on track_info table using id's with length. 

.. code-block:: python

    def add_trackinfo(self, nname,coun,len):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            
            query="""INSERT INTO tracks (title) VALUES ('%s')""" %(nname)
            cursor.execute(query)

            query = "SELECT id FROM tracks WHERE title = '%s'" % (nname)
            cursor.execute(query)
            nid = cursor.fetchall()[0][0]

            query = "SELECT id FROM nations WHERE title = '%s'" % (coun)
            cursor.execute(query)
            cid = cursor.fetchall()[0][0]

            query = """INSERT INTO track_info VALUES ('%s','%s','%s')""" %(nid,cid,len)
            cursor.execute(query)

            connection.commit()
            return



Track information deleting
+++++++++++++++++++++++++++++++

| delete_tire function removes track information using track id on track_info table. 

.. code-block:: python

    def delete_trackinfo(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM track_info WHERE track_id = '%s'" %(id)
            cursor.execute(query)
            connection.commit()
            return 


Track information updating
+++++++++++++++++++++++++++++++

|  update_trackinfo function takes old name of track, new name of track, new country and new length. It finds track id with old name, updates that tracks name. After that updates former track information with the new one.

.. code-block:: python

    def update_trackinfo(self, oname,nname,coun,len):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()

            query = "SELECT id FROM tracks WHERE title = '%s'" % (oname)
            cursor.execute(query)
            oid = cursor.fetchall()[0][0]

            query = "UPDATE tracks SET title='%s' WHERE title = '%s'" % (nname,oname)
            cursor.execute(query)

            query = "SELECT id FROM nations WHERE title = '%s'" % (coun)
            cursor.execute(query)
            cid = cursor.fetchall()[0][0]

            query = "UPDATE track_info SET nation_id='%s',lenght='%s' WHERE track_id = '%s'" %(cid,len,oid)
            cursor.execute(query)
            connection.commit()
            return

Track information searching
+++++++++++++++++++++++++++++++

| Search operation seek on track names and country names. There isn't additional search function. To search something get_trackinfolist function is used.

.. code-block:: python

    def get_trackinfolist(self,name):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT tracks.id, tracks.title, nations.title, lenght
                    FROM track_info LEFT JOIN tracks ON (track_id = tracks.id) 
                    LEFT JOIN nations ON (nation_id=nations.id) WHERE (tracks.title ILIKE '%%%s%%' OR nations.title ILIKE '%%%s%%')  
                    ORDER BY tracks.id"""%(name,name)
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

| As mentioned at listing track information part, this function takes name of country or track that wanted to search and return information lines that related with this names.
It is not necessary to write all of the name. Also this function is case insensitive.


Fastest Driver List
-----------------------------

| There isnt a table for this page. There is get_fastestlist function on fastestdrivers.py .

.. code-block:: python

    @app.route('/FastestDrivers', methods=['GET', 'POST'])
    def fastest_page():
        fd = FastestDriver(app.config['dsn'])
        now = datetime.datetime.now()
        if request.method == 'GET':
            return render_template('fastdriver.html', List = fd.get_fastestlist(), current_time = now.ctime())

| get_fastestlist function takes fastest drivers id and name, then group them according to name and order in descending.


.. code-block:: python

    def get_fastestlist(self):
        with dbapi2.connect(self.cp) as connection:

            cursor = connection.cursor()
            query = """SELECT dr.name AS Driver, COUNT(rc.fastestdr_id) AS FastestCount FROM 
                    raceinfos rc JOIN drivers dr ON dr.id = rc.fastestdr_id GROUP BY dr.name
                    ORDER BY COUNT(rc.fastestdr_id) DESC
                    """
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

