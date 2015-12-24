Parts Implemented by Bilal Enes Fedar
=========================================

| Nations List
-------------------

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

| Nation Class default constructor
+++++++++++++++++++++++++++++++++++

| Gets cp parameter which will be app.config['dsn'] variable. This variable will be used as parameter in dbapi2.connect function. All implementations have a default constructor which wants dsn configuration as parameter like Nation class.

.. code-block:: python

	def __init__(self, cp):
	    self.cp = cp
	    return

| Print Nations
+++++++++++++++++

| Prints all nations ordered by id.

.. code-block:: python

	def get_nationlist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Nations ORDER BY id ASC"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

| Add Nation
++++++++++++++++++

| Adds new nation to nations table.

.. code-block:: python

	def add_nation(self, title):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO Nations (title) VALUES ('%s')" % (title)
            cursor.execute(query)
            connection.commit()
            return

| Delete Nation
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

| Update Nation
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


| Years List
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


| Print Years
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

| Add Year
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

| Delete Year
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

| Update Year
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
