Parts Implemented by Mustafa Gökçeoğlu
======================================

Note ;
++++++++++
    
| cursor() Allows Python code to execute PostgreSQL command in a database session.
| execute() Prepare and execute a database operation
| commit() Commit any pending transaction to the database.
| fetchall() Fetch all (remaining) rows of a query result, returning them as a list of tuples.




Teams List
----------------

| Teams table has got a id and title. Id is serial key and title which is unique in table. Title is team name in table.

.. code-block:: python

        query = """CREATE TABLE teams (
                   id SERIAL PRIMARY KEY,
                   title VARCHAR(40) UNIQUE NOT NULL
               )"""
           cursor.execute(query)

| There are get, delete, add and update operations in server.py shown at below. These operations functions are written in teams.py file.

.. code-block:: python
	
    @app.route('/Teams', methods=['GET', 'POST'])
    def team_page():
        tems = Teams(app.config['dsn'])
        if request.method == 'GET':
            now = datetime.datetime.now()
            temlist = tems.get_teamlist()
            return render_template('teams.html', TeamList = temlist, current_time = now.ctime())
        elif 'teams_to_delete' in request.form:
            ids = request.form.getlist('teams_to_delete') 
            for id in ids:
                tems.delete_team(id)
            return redirect(url_for('team_page'))
        elif 'teams_to_add' in request.form:
            tems.add_team(request.form['title'])
            return redirect(url_for('team_page'))
        elif 'teams_to_update' in request.form:
            tems.update_team(request.form['id'], request.form['title'])
            return redirect(url_for('team_page'))



Teams listing
++++++++++++++++++

| Select all team in team table and show the all teams.

.. code-block:: python
	
    def get_teamlist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Teams"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows


Teams adding
+++++++++++++++++++

| This code is adding operation according to team name. Team id is calculated automatically.
.. code-block:: python
	
    def add_team(self, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO Teams (title) VALUES ('%s')" % (title)
            cursor.execute(query)
            connection.commit()
            return


Team deleting
+++++++++++++++++++

| Team deleting operation work on team id. When we want to delete any team, this code is deleting from team table according to id.
.. code-block:: python
	
    def delete_team(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM Teams WHERE id = '%s'" % (id) 
            cursor.execute(query)
            connection.commit()
            return


Team updating
+++++++++++++++++++

| Team updating code works according to id, and code update the team name.
.. code-block:: python
	
    def update_team(self, id, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE Teams SET title = '%s' WHERE id = '%s'" % (title, id)
            cursor.execute(query)
            connection.commit()
            return

Engines List
----------------

| Engines table has got a id and title. Id is serial key and title which is unique in table. Tittle is engine name in table.

.. code-block:: python

        query = """CREATE TABLE engines (
                   id SERIAL PRIMARY KEY,
                   title VARCHAR(40) UNIQUE NOT NULL
               )"""
           cursor.execute(query)

| There are get, delete, add and update operations in server.py shown at below. These operations functions are written in Engines.py file.

.. code-block:: python
    
    @app.route('/Engines', methods=['GET', 'POST'])
    def engine_page():
        engs = Engines(app.config['dsn'])
        if request.method == 'GET':
            now = datetime.datetime.now()
            englist = engs.get_enginelist()
            return render_template('Engines.html', EngineList = englist, current_time = now.ctime())
        elif 'engines_to_delete' in request.form:
            ids = request.form.getlist('engines_to_delete') 
            for id in ids:
                engs.delete_engine(id)
            return redirect(url_for('engine_page'))
        elif 'engines_to_add' in request.form:
            engs.add_engine(request.form['title'])
            return redirect(url_for('engine_page'))
        elif 'engines_to_update' in request.form:
            engs.update_engine(request.form['id'], request.form['title'])
            return redirect(url_for('engine_page'))



Engines listing
++++++++++++++++++

| Select all engine in engine table and show the all engines.

.. code-block:: python
    
    def get_enginelist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Engines"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows


Engines adding
+++++++++++++++++++

| This code is adding operation according to engine name. Engine id is calculated automatically.
.. code-block:: python
    
    def add_engine(self, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO Engines (title) VALUES ('%s')" % (title)
            cursor.execute(query)
            connection.commit()
            return


Engine deleting
+++++++++++++++++++

| Engine deleting operation work on engine id. When we want to delete any engine, this code is deleting from engine table according to id.
.. code-block:: python
    
    def delete_engine(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM Engines WHERE id = '%s'" % (id) 
            cursor.execute(query)
            connection.commit()
            return


Engine updating
+++++++++++++++++++

| Engine updating code works according to id, and code update the engine name.
.. code-block:: python
    
    def update_engine(self, id, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE Engines SET title = '%s' WHERE id = '%s'" % (title, id)
            cursor.execute(query)
            connection.commit()
            return


Champions of Years List
-----------------------------

| This table contains three attributes year id driver id and team id. Year id referenced from years table for years, driver id referenced from drivers table for driver name and team id referenced from teams table for team name. These references have cascade operation for delete and update.


.. code-block:: python

    query = """CREATE TABLE champinfos (
                    year_id INTEGER REFERENCES years(id) ON DELETE CASCADE ON UPDATE CASCADE,
                    driver_id INTEGER REFERENCES drivers(id) ON DELETE CASCADE ON UPDATE CASCADE,
                    team_id INTEGER REFERENCES teams(id) ON DELETE CASCADE ON UPDATE CASCADE
                )"""
               
            
           cursor.execute(query)


| There are get, delete, add, update and search operations in server.py shown at below. These operations functions are written in champinfo.py file.

.. code-block:: python

    @app.route('/Champinfo', methods=['GET', 'POST'])
    def champinfo_page():
        cinfos = Champinfo(app.config['dsn'])
        if request.method == 'GET':
            now = datetime.datetime.now()
            clist = cinfos.get_champinfolist()
            drivers=cinfos.get_drivers()
            teams=cinfos.get_teams()
            return render_template('champinfo.html', ChampinfoList = clist, drivers=drivers,teams=teams, current_time = now.ctime())
        elif 'champinfos_to_delete' in request.form:
            ids = request.form.getlist('champinfos_to_delete') 
            for id in ids:
                cinfos.delete_champinfo(id)
            return redirect(url_for('champinfo_page'))
        elif 'champinfos_to_add' in request.form:
            nyear=request.form['nyear']
            ndriv=request.form['ndriv']
            nteam=request.form['nteam']
            cinfos.add_champinfo(nyear,ndriv,nteam)
        elif 'champinfos_to_update' in request.form:
            oyear=request.form['oyear']
            nyear=request.form['nyear']
            ndriv=request.form['ndriv']
            nteam=request.form['nteam']
            cinfos.update_champinfo(oyear,nyear,ndriv,nteam)
        elif 'champinfos_to_search' in request.form:
            now = datetime.datetime.now()
            clist = cinfos.search_champinfolist(request.form['name'])
            return render_template('champinfo.html', ChampinfoList = clist, current_time = now.ctime())
        return redirect(url_for('champinfo_page'))


Champions of Years listing
+++++++++++++++++++++++++++++


| get_drivers function returns driver names. In server.py these drivers names stored in drivers tuple. Select all drivers in driver table and show the all drivers name according to ordered driver name list.

.. code-block:: python

    def get_drivers(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT name FROM drivers ORDER BY name"""
            cursor.execute(query)
            rows = cursor.fetchall()
            nrows=[]
            for row in rows:
                nrows.append(row[0])
            return nrows


| get_teams function returns team names. In server.py these teams names stored in teams tuple. Select all teams in team table and show the all teams name according to ordered team name list.

.. code-block:: python

    def get_teams(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT title FROM teams ORDER BY title"""
            cursor.execute(query)
            rows = cursor.fetchall()
            nrows=[]
            for row in rows:
                nrows.append(row[0])
            return nrows

| get_champinfolist function returns year id, years tittle,  drivers name and teams tittle. Select champions in driver table, which is providing conditions in terms of year and teams and show the all champions name, championship year and their team name.

.. code-block:: python

    def get_champinfolist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT year_id, years.title, drivers.name, teams.title
                    FROM Champinfos LEFT JOIN years ON (year_id = years.id) 
                    LEFT JOIN drivers ON (driver_id=drivers.id) 
                    LEFT JOIN teams ON (team_id = teams.id) 
                    ORDER BY years.id"""
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows


Champions of Years adding
+++++++++++++++++++++++++++++

| Add the new year for championship year. We cannot add same year since year is unique. When the champions year adding  we select the champion names and their team according to driver id and team id.

.. code-block:: python

    def add_champinfo(self, nyear, ndriv, nteam):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            
            query="""INSERT INTO years (title) VALUES ('%s')""" %(nyear)
            cursor.execute(query)            
            
            
            query = "SELECT id FROM years WHERE title = '%s'" % (nyear)
            cursor.execute(query)
            nid = cursor.fetchall()[0][0]

            query = "SELECT id FROM drivers WHERE name = '%s'" % (ndriv)
            cursor.execute(query)
            cid = cursor.fetchall()[0][0]

            query = "SELECT id FROM teams WHERE title = '%s'" % (nteam)
            cursor.execute(query)
            tid = cursor.fetchall()[0][0]
            
            query = """INSERT INTO Champinfos VALUES ('%s','%s','%s')""" %(nid,cid,tid)
            cursor.execute(query)

            connection.commit()
            return



Champions of Years deleting
+++++++++++++++++++++++++++++++

| Champions deleting operation work on champions of year id. When we want to delete any champion, this code is deleting from champions of years table according to id. 

.. code-block:: python

    def delete_champinfo(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM Champinfos WHERE year_id = '%s'" % (id) 
            cursor.execute(query)
            connection.commit()
            return 


Champions of Years updating
+++++++++++++++++++++++++++++++

|  This code updating the year, championship year and champions team. Firstly we find a old year which is updated. After that we can update year, champions name and champions team. We can also only updated champions year if we select new year and old year is same and champions name doesn't change. Finally, updates the champions of years information with using the new informations.

.. code-block:: python

    def update_champinfo(self, oyear, nyear, ndriv, nteam):
        with dbapi2.connect(self.cp) as connection:           
            cursor = connection.cursor()

            query = "SELECT id FROM years WHERE title = '%s'" % (oyear)
            cursor.execute(query)
            oid = cursor.fetchall()[0][0]

            
            query = "SELECT id FROM years WHERE title = '%s'" % (nyear)
            cursor.execute(query)
            nid = cursor.fetchall()[0][0]

            query = "SELECT id FROM drivers WHERE name = '%s'" % (ndriv)
            cursor.execute(query)
            cid = cursor.fetchall()[0][0]

            query = "SELECT id FROM teams WHERE title = '%s'" % (nteam)
            cursor.execute(query)
            tid = cursor.fetchall()[0][0]
            
            query = "UPDATE Champinfos SET year_id = '%s', driver_id='%s',team_id='%s' WHERE year_id = '%s'" %(nid,cid,tid,oid)
            cursor.execute(query)
            connection.commit()            
            
            return

Champions of Years searching
+++++++++++++++++++++++++++++++

| Search operation is work on driver name and team name. We don't need write all team name or driver name.  This code finds the team name in team table or driver name in driver table.

.. code-block:: python

    def search_champinfolist(self, name):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()

            query = """SELECT year_id, years.title, drivers.name ,teams.title
                    FROM Champinfos LEFT JOIN years ON (year_id = years.id) 
                    LEFT JOIN drivers ON (driver_id=drivers.id) 
                    LEFT JOIN teams ON (team_id = teams.id) WHERE (drivers.name ILIKE '%%%s%%' OR teams.title ILIKE '%%%s%%' )
                    ORDER BY year_id"""%(name,name)
                 
            
            
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows




Winning Rate List
-----------------------------

| This table contains only one attributes driver1 id for driver name. Driver1 id referenced from drivers table for driver name. These references have cascede operation for delete and update.


.. code-block:: python

     query = """CREATE TABLE winrates (
                    driver1_id INTEGER REFERENCES drivers(id) ON DELETE CASCADE ON UPDATE CASCADE

                )"""


| There is only get operation in server.py shown at below. The get operation function is written in winrate.py file.

.. code-block:: python

    @app.route('/Winrate', methods=['GET', 'POST'])
    def winrate_page():
        winfos = Winrate(app.config['dsn'])
        
        if request.method == 'GET':
            now = datetime.datetime.now()
            wlist = winfos.get_winratelist()
            return render_template('winrate.html', WinrateList = wlist, current_time = now.ctime())
        return redirect(url_for('winrate_page'))



| get_winratelist function takes drivers name, Number of Attanded Races and Number of First Place from finishdistribution table and calculated the winning rate according to finish distribution. After that list is ordering according to winning rate.


.. code-block:: python

    def get_winratelist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT driver1_id, drivers.name, (FINISHDISTR.number_first+FINISHDISTR.number_second+FINISHDISTR.number_third), FINISHDISTR.number_first, (FINISHDISTR.number_first*100/(FINISHDISTR.number_first+FINISHDISTR.number_second+FINISHDISTR.number_third)) AS WINNRATE
                    FROM Winrates RIGHT JOIN drivers ON (driver1_id = drivers.id) 
                    LEFT JOIN FINISHDISTR ON (driver1_id = FINISHDISTR.DRIVER_ID) WHERE (FINISHDISTR.number_first != 0)
                    ORDER BY WINNRATE DESC
                    """
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows


| We need to driver name for winning rate calculate, therefore we use get_drivers function returns driver names. In server.py these drivers names stored in drivers tuple. Select all drivers in driver table and show the all drivers name according to ordered driver name list.

.. code-block:: python

    def get_drivers(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT name FROM drivers ORDER BY name"""
            cursor.execute(query)
            rows = cursor.fetchall()
            nrows=[]
            for row in rows:
                nrows.append(row[0])
            return nrows




