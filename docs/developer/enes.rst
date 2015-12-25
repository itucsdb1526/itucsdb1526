Parts Implemented by Bilal Enes Fedar
=====================================

Nations List
--------------

| Nations table is simple table that consists of nation id and nation title attributes. It's functions for operations are defined in nations.py file. There are codes below to create table or recover it if user clicks "initialize database" button.

.. code-block:: python

            query = "DROP TABLE IF EXISTS nations CASCADE"
            cursor.execute(query)
        
            query = """CREATE TABLE nations (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(40) UNIQUE NOT NULL
                )"""
            cursor.execute(query)

| Nations List has add, delete, and update operations. In server.py file, some funcions are called from nations.py file to perform these operations. Code in server.py file is shown below:

.. code-block:: python

	@app.route('/Nations', methods=['GET', 'POST'])
	def nation_page():
	    nats = Nations(app.config['dsn'])
	    if request.method == 'GET':
	        now = datetime.datetime.now()
	        nlist = nats.get_nationlist()
	        return render_template('nations.html', NationList = nlist, current_time = now.ctime())
	    elif 'nations_to_delete' in request.form:
	        ids = request.form.getlist('nations_to_delete') 
	        for id in ids:
	            nats.delete_nation(id)
	        return redirect(url_for('nation_page'))
	    elif 'nations_to_add' in request.form:
	        nats.add_nation(request.form['title'])
	        return redirect(url_for('nation_page'))
	    elif 'nations_to_update' in request.form:
	        nats.update_nation(request.form['id'], request.form['title'])
	        return redirect(url_for('nation_page'))

Nation Class default constructor
++++++++++++++++++++++++++++++++++

| Gets cp parameter which will be app.config['dsn'] variable. This variable will be used as parameter in dbapi2.connect function. All implementations have a default constructor which wants dsn configuration as parameter like Nation class.

.. code-block:: python

	def __init__(self, cp):
	    self.cp = cp
	    return

Print Nations
+++++++++++++++

| Prints all nations ordered by id.

.. code-block:: python

	def get_nationlist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Nations ORDER BY id ASC"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

Add Nation
++++++++++++

| Adds new nation to nations table.

.. code-block:: python

	def add_nation(self, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO Nations (title) VALUES ('%s')" % (title)
            cursor.execute(query)
            connection.commit()
            return

Delete Nation
+++++++++++++++++++++

| Deletes nation from nations table with given id. Deleting is performed with using checkboxes in page and there is a loop in server.py which calls this delete function for all selected checkboxes.

.. code-block:: python

	def delete_nation(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM Nations WHERE id = '%s'" % (id) 
            cursor.execute(query)
            connection.commit()
            return

Update Nation
+++++++++++++++++++++

| Updates title of nation with given id.

.. code-block:: python

	def update_nation(self, id, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE Nations SET title = '%s' WHERE id = '%s'" % (title, id)
            cursor.execute(query)
            connection.commit()
            return


Years List
-------------------

| Years table is basic table  consists of year id and year attributes. It's functions for operations are defined in years.py file. There are codes called from init.py file below to create table or recover it if user clicks "initialize database" button.

.. code-block:: python

            query = "DROP TABLE IF EXISTS years CASCADE"
            cursor.execute(query)
        
            query = """CREATE TABLE years (
                    id SERIAL PRIMARY KEY,
                    title NUMERIC(4) UNIQUE NOT NULL
                )"""
            cursor.execute(query)

| Years List has add, delete, and update operations. Functions of these operations are called from years.py file. Code in server.py file is shown below:

.. code-block:: python

	@app.route('/Years', methods=['GET', 'POST'])
	def year_page():
	    yrs = Years(app.config['dsn'])
	    if request.method == 'GET':
	        now = datetime.datetime.now()
	        yrlist = yrs.get_yearlist()
	        return render_template('years.html', YearList = yrlist, current_time = now.ctime())
	    elif 'years_to_delete' in request.form:
	        ids = request.form.getlist('years_to_delete') 
	        for id in ids:
	            yrs.delete_year(id)
	    elif 'years_to_add' in request.form:
	        yrs.add_year(request.form['title'])
	    elif 'years_to_update' in request.form:
	        yrs.update_year(request.form['id'], request.form['title'])
	    return redirect(url_for('year_page'))


Print Years
+++++++++++++++++

| Prints all years ordered by id.

.. code-block:: python

	def get_yearlist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Years ORDER BY id ASC"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

Add Year
++++++++++++++++++

| Adds new nation to nations table. User cannot add a year which is lower than 1952 or higher than 2999. Also there is a control checks whether user entered an integer or not.

.. code-block:: python

	def add_year(self, title):
        isTitleInt = False
        try:
            int(title)
            isTitleInt = True
        except:
            pass
        if(isTitleInt and int(title) >= 1952 and int(title) <= 2999):
            with dbapi2.connect(self.cp) as connection:
                cursor = connection.cursor()
                query = "INSERT INTO Years (title) VALUES ('%s')" % (title)
                cursor.execute(query)
                connection.commit()
                return

Delete Year
+++++++++++++++++++++

| Deletes year from years table with given id. Deleting is performed with using checkboxes in page and there is a loop in server.py which calls this delete function for all selected checkboxes.

.. code-block:: python

	def delete_year(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM Years WHERE id = '%s'" % (id) 
            cursor.execute(query)
            connection.commit()
            return

Update Year
+++++++++++++++++++++

| Updates value of record with given id.

.. code-block:: python

	def update_year(self, id, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE Years SET title = '%s' WHERE id = '%s'" % (title, id)
            cursor.execute(query)
            connection.commit()
            return


Local Races
-------------------

| Local Races page uses raceinfos table which has many references to other tables. raceinfos table consists of 8 attributes which are track_id, year_id, dr1_id, dr2_id, dr3_id, nation_id, fastestdr_id, and fastest_time.This table has add, delete, update, and search operations. It's functions for operations are defined in raceinfos.py file. Primary key is (track_id, year_id). There are codes below to create table.

.. code-block:: python

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

| There are add, delete, update, and search operations for Local Races. There are two options for search operation which are search track and search winner. In server.py file, some funcions are called from raceinfos.py file to perform these operations. In func.py, there is Func class which contains common functions like get_tracks, get_nations, etc. Functions in Func Class are beneficial for group members. Code in server.py file is shown below:

.. code-block:: python

	@app.route('/Raceinfos', methods=['GET', 'POST'])
	def raceinfo_page():
	    racs = Raceinfos(app.config['dsn'])
	    method = Func(app.config['dsn'])
	    tr_list = method.get_tracks()
	    nat_list = method.get_nations()
	    yr_list = method.get_years()
	    dr_list = method.get_drivers()
	    if request.method == 'GET':
	        now = datetime.datetime.now()
	        racinflist = racs.get_raceinfolist()
	        return render_template('raceinfos.html', RaceList = racinflist, 
            current_time = now.ctime(), TrackList = tr_list, NationList = nat_list, 
            YearList = yr_list, DriverList = dr_list)
	    elif 'raceinfos_to_delete' in request.form:
	        raceinfos = request.form.getlist('raceinfos_to_delete')
	        for raceinfo in raceinfos:
	            racs.delete_raceinfo(raceinfo)
	        return redirect(url_for('raceinfo_page'))
	    elif 'raceinfos_to_add' in request.form:
	        racs.add_raceinfo(request.form)
	        return redirect(url_for('raceinfo_page'))
	    elif 'raceinfos_to_update' in request.form:
	        racs.update_raceinfo(request.form)
	        return redirect(url_for('raceinfo_page'))
	    elif 'raceinfos_to_searchwinner' in request.form:
	        now = datetime.datetime.now()
	        racinflist = racs.search_raceinfolist('winner', request.form)
	        return render_template('raceinfos.html', RaceList = racinflist,
            current_time = now.ctime(), TrackList = tr_list, NationList = nat_list,
            YearList = yr_list, DriverList = dr_list)
	    elif 'raceinfos_to_searchtrack' in request.form:
	        now = datetime.datetime.now()
	        racinflist = racs.search_raceinfolist('track', request.form)
	        return render_template('raceinfos.html', RaceList = racinflist,
            current_time = now.ctime(), TrackList = tr_list, NationList = nat_list, 
            YearList = yr_list, DriverList = dr_list)


Print Local Races
+++++++++++++++++

| Prints all local races ordered by track and year attributes. nat_id parameter is used for specific nation page. year_title parameter is used for specific year page.

.. code-block:: python

	def get_raceinfolist(self, nat_id = None, year_title = None):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """ SELECT tr.title AS Track, yr.title AS Year,
                    dr1.name AS First, dr2.name AS Second, dr3.name AS Third,
                    nat.title AS Nation, fdr.name AS FastestDr, 
                    rc.fastest_time AS FastestLap FROM
                    """ 
                    
            if nat_id is None:
                query += "raceinfos rc"
            else:
                query += "(SELECT * FROM raceinfos WHERE nation_id = '%s') rc" %(str(nat_id))
            query +="""
                    JOIN tracks tr ON tr.id = rc.track_id
                    """
            if year_title is None:
                query += "JOIN years yr ON yr.id = rc.year_id"
            else:
                query += "JOIN (SELECT * FROM years WHERE title = '%s') yr ON 
                yr.id = rc.year_id" %(year_title)
            query +="""
                    JOIN drivers dr1 ON dr1.id = rc.dr1_id
                    JOIN drivers dr2 ON dr2.id = rc.dr2_id
                    JOIN drivers dr3 ON dr3.id = rc.dr3_id
                    JOIN nations nat ON nat.id = rc.nation_id
                    JOIN drivers fdr ON fdr.id = rc.fastestdr_id
                    ORDER BY rc.track_id ASC, rc.year_id ASC;
                    """        
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

Add Local Race
++++++++++++++++++

| Adds new local race to raceinfos table. There is a restriction: First, Second and Third drivers of a race must be different than each other. If not, add operation is skipped. 

.. code-block:: python

	def add_raceinfo(self, form):
        track_id = self.fn.get_id("tracks", form.get('Track'))
        year_id = self.fn.get_id("years", form.get('Year'))
        dr1_id = self.fn.get_id("drivers", form.get('First'))
        dr2_id = self.fn.get_id("drivers", form.get('Second'))
        dr3_id = self.fn.get_id("drivers", form.get('Third'))
        nation_id = self.fn.get_id("nations", form.get('Nation'))
        fastestdr_id = self.fn.get_id("drivers", form.get('FastestDr'))
        fastest_time = form['FastestLap']
        if (dr1_id == dr2_id) or (dr1_id == dr3_id) or (dr2_id == dr3_id):
            return
            
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO raceinfos  
            VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s' ,'%s')"""
            % (track_id, year_id, dr1_id, dr2_id, dr3_id, nation_id, fastestdr_id, fastest_time)
            cursor.execute(query)
            connection.commit()
            return

Delete Local Race
+++++++++++++++++++++

| Deletes a local race from raceinfos table with given track_id and year_id. Deleting is performed with using checkboxes in page and there is a loop in server.py which calls this delete function for all selected checkboxes. n_raceinfo parameter contains information like Turkey:2003. This information is parsed, ID's of track and year is found in this function. Finally, deleting operation is performed with track and year ids.

.. code-block:: python

	def delete_raceinfo(self, n_raceinfo):
        raceinfo = n_raceinfo.split(":")
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM tracks WHERE title = '%s'" % (raceinfo[0])
            cursor.execute(query)
            track_id = cursor.fetchone()[0]

            query = "SELECT * FROM years WHERE title = '%s'" % (raceinfo[1])
            cursor.execute(query)
            year_id = cursor.fetchone()[0]

            query = """DELETE FROM raceinfos WHERE (track_id = '%s' 
            AND year_id = '%s')""" % (str(track_id), str(year_id))
            cursor.execute(query)
            connection.commit()
            return

Update Local Race
+++++++++++++++++++++

| Updates all attributes of local races except track and year. Form contains names of attributes and this function finds id's of these values. get_id function is used from Func class to find ids. There is a restriction same like add operation: First, Second, Third drivers must be different than each other.

.. code-block:: python

	def update_raceinfo(self, form):
        track_id = self.get_id("tracks", form.get('Track'))
        year_id = self.get_id("years", form.get('Year'))
        dr1_id = self.get_id("drivers", form.get('First'))
        dr2_id = self.get_id("drivers", form.get('Second'))
        dr3_id = self.get_id("drivers", form.get('Third'))
        nation_id = self.get_id("nations", form.get('Nation'))
        fastestdr_id = self.get_id("drivers", form.get('FastestDr'))
        fastest_time = form['FastestLap']
        if (dr1_id == dr2_id) or (dr1_id == dr3_id) or (dr2_id == dr3_id):
            return

        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE raceinfos SET dr1_id = '{0}', dr2_id = '{1}', dr3_id = '{2}', 
            nation_id = '{3}', fastestdr_id = '{4}', fastest_time = '{5}' 
            WHERE track_id = '{6}' AND year_id = '{7}'".format(dr1_id, dr2_id, dr3_id, 
            nation_id, fastestdr_id, fastest_time, track_id, year_id)
            cursor.execute(query)
            connection.commit()
            return

Search Local Race
++++++++++++++++++++

| Search a local race in raceinfos table either by winner driver name or track title. Two search options is done in one function which is below:

.. code-block:: python

	def search_raceinfolist(self, searchtype, form):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()

            query = """SELECT tr.title AS Track, yr.title AS Year,
                    dr1.name AS First, dr2.name AS Second, dr3.name AS Third,
                    nat.title AS Nation, fdr.name AS FastestDr, rc.fastest_time AS FastestLap FROM 
                    raceinfos rc
                    JOIN tracks tr ON tr.id = rc.track_id
                    JOIN years yr ON yr.id = rc.year_id
                    JOIN drivers dr1 ON dr1.id = rc.dr1_id
                    JOIN drivers dr2 ON dr2.id = rc.dr2_id
                    JOIN drivers dr3 ON dr3.id = rc.dr3_id
                    JOIN nations nat ON nat.id = rc.nation_id
                    JOIN drivers fdr ON fdr.id = rc.fastestdr_id
                    ORDER BY rc.track_id ASC, rc.year_id ASC
                    """
            if searchtype == 'winner':
                query = "SELECT * FROM (" + query + ") AS Derived WHERE Derived.First ILIKE 
                '%%%s%%'" % (form['SearchWinner'])
            if searchtype == 'track':
                query = "SELECT * FROM (" + query + ") AS Derived WHERE Derived.Track ILIKE 
                '%%%s%%'" % (form['SearchTrack'])
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

Most Successful Nations
-------------------------------

| Most successful nations page uses raceinfos table and perform group by & count operations on it. This page is a result of query which hasnot any table in database. Most Audience Nation column of Local Races table is used to calculate most successful nations. Most Audience Nation attribute is that there is a local race which has audience from different nations, but there is one nation which has biggest percent of audiences in count for local race.

Print Most Successful Nations
+++++++++++++++++++++++++++++++++++

| Prints all rows of a result query.

.. code-block:: python

	def get_sucnatlist(self):
        with dbapi2.connect(self.cp) as connection:

            cursor = connection.cursor()
            query = """SELECT nat.title AS Nation, COUNT(nat.title) AS NationCount FROM 
                    raceinfos rc
                    JOIN tracks tr ON tr.id = rc.track_id
                    JOIN years yr ON yr.id = rc.year_id
                    JOIN drivers dr1 ON dr1.id = rc.dr1_id
                    JOIN drivers dr2 ON dr2.id = rc.dr2_id
                    JOIN drivers dr3 ON dr3.id = rc.dr3_id
                    JOIN nations nat ON nat.id = rc.nation_id
                    JOIN drivers fdr ON fdr.id = rc.fastestdr_id
                    GROUP BY nat.title
                    ORDER BY NationCount DESC
                    """

            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

Search Most Successful Nations
+++++++++++++++++++++++++++++++++++++

| Searches for specific nation in a result query.

.. code-block:: python

	def search_sucnatlist(self, form):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()

            query = """SELECT nat.title AS Nation, COUNT(nat.title) AS NationCount FROM 
                    raceinfos rc
                    JOIN tracks tr ON tr.id = rc.track_id
                    JOIN years yr ON yr.id = rc.year_id
                    JOIN drivers dr1 ON dr1.id = rc.dr1_id
                    JOIN drivers dr2 ON dr2.id = rc.dr2_id
                    JOIN drivers dr3 ON dr3.id = rc.dr3_id
                    JOIN nations nat ON nat.id = rc.nation_id
                    JOIN drivers fdr ON fdr.id = rc.fastestdr_id
                    GROUP BY nat.title
                    ORDER BY NationCount DESC
                    """

            query = "SELECT * FROM (" + query + ") AS Derived WHERE Derived.First ILIKE 
            '%%%s%%'" % (form['SearchNation'])
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

Extras
------------

Specific Nation Page
++++++++++++++++++++++

| When nation title is clicked, user will be directed to specific nation page which contains detailed information about that nation. If there is no nation, user will be directed to 404 page. In server.py, some functions are called both from func.py and nations.py to implement specific nation page.

.. code-block::python

	@app.route('/Nations/<nat_title>', methods=['GET', 'POST'])
	def a_nation_page(nat_title):
	    now = datetime.datetime.now()
	    fn = Func(app.config['dsn'])
	    nt = Nations(app.config['dsn'])
	    rc = Raceinfos(app.config['dsn'])

	    nat_id = fn.get_id("nations", nat_title) #will be null if unknown title entered
	    nat = nt.get_a_nation(nat_id)
	    if nat is None:
	        return render_template('404.html', current_time = now.ctime())
	    rclist = rc.get_raceinfolist(nat_id = nat_id)
	    trlist = nt.get_trackfornation(nat_id)
	    return render_template('a_nation.html', Nation = nat, RaceList = rclist, TrackInfoList = trlist, current_time = now.ctime())

| In nations.py, there are two functions are called from server.py:

.. code-block:: python

    def get_a_nation(self, id):
        if id is None:
            return None
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT nat.title AS Title, ninf.capital AS Capital, 
                    ninf.area_size AS Area, 
                    ninf.population AS Population, ninf.tld AS TLD
                    FROM 
                    nations_info ninf
                    JOIN (SELECT * FROM Nations WHERE id = '%s') nat 
                    ON ninf.nation_id = nat.id
                    """ % (id)
            cursor.execute(query)
            row = cursor.fetchone()
            if row is None:
                return None
            nat = Nation(row[0], row[1], row[2], row[3], row[4])
            return nat
            
    def get_trackfornation(self,nat_id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT tracks.id, tracks.title, nat.title, lenght
                    FROM track_info INNER JOIN tracks ON (track_id = tracks.id) 
                    INNER JOIN (SELECT * FROM nations WHERE id = '%s') AS nat
                    ON (nation_id=nat.id)
                    ORDER BY tracks.id"""%(nat_id)
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows


Specific Year Page
++++++++++++++++++++

| When a year is clicked on tables, user will be redirected to specific year page which contains information about only for that year. Implementation is done in server.py as shown below:

.. code-block:: python

	@app.route('/Years/<year_title>', methods=['GET', 'POST'])
	def a_year_page(year_title):
	    now = datetime.datetime.now()
	    fn = Func(app.config['dsn'])
	    rc = Raceinfos(app.config['dsn'])
	    year_id = fn.get_id("years", year_title)
	    if year_id is None:
	        return render_template('404.html', current_time = now.ctime())
	    rclist = rc.get_raceinfolist(year_title = year_title)
	    return render_template('a_year.html', YearTitle = year_title, RaceList = rclist, 
        current_time = now.ctime())

404 Page
+++++++++++

| If user tries to open page about unknown/invalid specific nation or year page, instead of internal server error page user will see 404 page. Implementation is done in server.py file.

| For Nations:

.. code-block:: python

	nat = nt.get_a_nation(nat_id)
	    if nat is None:
	        return render_template('404.html', current_time = now.ctime())

| For Years:

.. code-block:: python

    year_id = fn.get_id("years", year_title)
    if year_id is None:
        return render_template('404.html', current_time = now.ctime())

