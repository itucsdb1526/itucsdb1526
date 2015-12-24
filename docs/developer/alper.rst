Parts Implemented by Alper Akyıldız
======================================

| Tracks List
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

| Track listing
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


| Track adding
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

| Track deleting
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

| Track updating
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

| Tires List
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


| Tire listing
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


| Tire adding
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


| Tire deleting
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


| Track Information List
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

