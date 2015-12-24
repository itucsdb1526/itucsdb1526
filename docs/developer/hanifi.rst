Parts Implemented by Hanifi Demirel
================================





.. Note::     
            | **cursor()** allows python code to execute PostgreSQL command in database session. 
            | **execute()** allows to execute database operation( query or command) 
            | **commit()** commits pending transaction to the database. 
            | **fetchall()** fetches all rows of query result and return them as list of tuples. 



|
|
|
*Drivers Class*
-----------------------
| Table for Drivers:


.. code-block:: python

        query = """CREATE TABLE Drivers (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(40) UNIQUE NOT NULL
                )"""
                cursor.execute(query)


| This code is from the server.py file. It handles the adding,deleting and updating requests from web page.

.. code:: python

    @app.route('/Drivers', methods=['GET', 'POST'])
    def driver_page():
    drivers = Drivers(app.config['dsn'])
    if request.method == 'GET':
        now = datetime.datetime.now()
        driver_list = drivers.get_driverlist()
        return render_template('drivers.html', DriverList = driver_list, current_time = now.ctime())
    elif 'drivers_to_delete' in request.form:
        ids = request.form.getlist('drivers_to_delete')
        for id in ids:
            drivers.delete_driver(id)
        return redirect(url_for('driver_page'))
    elif 'drivers_to_add' in request.form:
        drivers.add_driver(request.form['name'])
        return redirect(url_for('driver_page'))
    elif 'drivers_to_update' in request.form:
        drivers.update_driver(request.form['id'], request.form['name'])
        return redirect(url_for('driver_page'))
|
|
|
|


.. code:: python

	class Drivers:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_driverlist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Drivers ORDER BY ID"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows


| First function of the driver class is get_driverlist. It brings all rows in the 'Drivers'
|

.. code-block:: python

    def delete_driver(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM Drivers WHERE id = '%s'" % (id)
            cursor.execute(query)
            connection.commit()
            return

| Function deletes the row with the same id functions gets as parameter in the 'Drivers' table.

|
|

.. code-block:: python

    def add_driver(self, name):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO Drivers (name) VALUES ('%s')" % (name)
            cursor.execute(query)
            connection.commit()
            return

| Function add a new row to 'Drivers' table with the 'name'  indicated in parameter of function

|
|

.. code-block:: python

    def update_driver(self, id, name):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE Drivers SET name = '%s' WHERE id = '%s'" % (name, id)
            cursor.execute(query)
            connection.commit()
            return

| 

*Sponsors Class*
-----------------------
| Table for Sponsors:


.. code-block:: python

        query = """CREATE TABLE Sponsors (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(40) UNIQUE NOT NULL
                )"""
                cursor.execute(query)


| This code is from the server.py file. It handles the adding,deleting and updating requests from web page.

.. code:: python

    @app.route('/Sponsors', methods=['GET', 'POST'])
    def sponsors_page():
    sponsors = Sponsors(app.config['dsn'])
    if request.method == 'GET':
        now = datetime.datetime.now()
        sponsors_list = sponsors.get_sponsorlist()
        return render_template('sponsors.html', SponsorsList = sponsors_list, current_time = now.ctime())
    elif 'sponsors_to_delete' in request.form:
        ids = request.form.getlist('sponsors_to_delete')
        for id in ids:
            sponsors.delete_sponsor(id)
        return redirect(url_for('sponsors_page'))
    elif 'sponsors_to_add' in request.form:
        sponsors.add_sponsor(request.form['name'])
        return redirect(url_for('sponsors_page'))
    elif 'sponsors_to_update' in request.form:
        sponsors.update_sponsor(request.form['id'], request.form['name'])
        return redirect(url_for('sponsors_page'))

|
|
|
|

.. code-block:: python

	class Sponsors:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_sponsorlist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Sponsors ORDER BY ID"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

| Sponsor class. This function brings all the rows in the 'Sponsors' table.

|

.. code-block:: python

	def delete_sponsor(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM Sponsors WHERE id = '%s'" % (id)
            cursor.execute(query)
            connection.commit()
            return


| This function deletes the row whose id is same with parameter 'id'.

|
|

.. code-block:: python

    def add_sponsor(self, name):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO Sponsors (name) VALUES ('%s')" % (name)
            cursor.execute(query)
            connection.commit()
            return

| This function add a new row to 'Sponsors' table whose name attribute is taken from 'name' parameter.

|
|

.. code-block:: python

    def update_sponsor(self, id, name):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE Sponsors SET name = '%s' WHERE id = '%s'" % (name, id)
            cursor.execute(query)
            connection.commit()
            return


| This function updates the name attribute in the row whose id attribute is same with 'id' parameter.

|
|


*Finish Distributions Class*
-----------------------
| Table for Finish Distributions:


.. code-block:: python

        query = """CREATE TABLE Finishdistr (
                    driver_id INTEGER NOT NULL REFERENCES drivers(id)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE,
                    number_first INTEGER,
                    number_second INTEGER,
                    number_third INTEGER,
                    point INTEGER)"""
                


| This code is from the server.py file. It handles the adding,deleting and searching requests from web page.

.. code:: python

    @app.route('/Finishdistr', methods=['GET', 'POST'])
    def fd_page():
    fd = Finishdistr(app.config['dsn'])
    if request.method == 'GET':
        now = datetime.datetime.now()
        fd_list = fd.get_finishdistr()
        return render_template('finishdistr.html', Fd_list = fd_list, current_time = now.ctime())
    elif 'drivers_to_delete' in request.form:
        ids = request.form.getlist('drivers_to_delete')
        for driver_id in ids:
            fd.delete_driver(driver_id)
    elif 'drivers_to_add' in request.form:
        fd.add_driver(request.form['driver_id'])
    elif 'drivers_to_search' in request.form:
        now = datetime.datetime.now()
        search_result = fd.search_byname(request.form['name'])
        return render_template('finishdistr.html', Fd_list = search_result, current_time = now.ctime())
    return redirect(url_for('fd_page'))

|
|
|
|
.. code-block:: python

	class Finishdistr:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_finishdistr(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT DISTINCT DRIVER_ID , NAME, number_first, number_second, number_third
                    FROM FINISHDISTR, RACEINFOS,DRIVERS WHERE DRIVER_ID=DRIVERS.ID ORDER BY DRIVER_ID"""
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

| This class is about finish distributions of drivers.This function brings all driver in the 'Drivers' table with degrees.

|

.. code-block:: python

    def delete_driver(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM FINISHDISTR WHERE DRIVER_ID = '%s'" % (id)
            cursor.execute(query)
            connection.commit()
            return


| | This function deletes the row whose id is same with 'id' parameter.
 

|
|

.. code-block:: python

    def add_driver(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT COUNT(dr1_id) FROM RACEINFOS WHERE dr1_id = '%s'" % (id)
            cursor.execute(query)
            numberof1 = cursor.fetchall()[0][0]
            query = "SELECT COUNT(dr2_id) FROM RACEINFOS WHERE dr2_id = '%s'" % (id)
            cursor.execute(query)
            numberof2 = cursor.fetchall()[0][0]
            query = "SELECT COUNT(dr3_id) FROM RACEINFOS WHERE dr3_id = '%s'" % (id)
            cursor.execute(query)
            numberof3 = cursor.fetchall()[0][0]
            point= 25*numberof1 + 18*numberof2 + 15*numberof3
            query = "INSERT INTO FINISHDISTR VALUES ('%s','%s','%s','%s','%s')" % (id,numberof1,numberof2,numberof3,point)
            cursor.execute(query)
            connection.commit()
            return
| This function add new drivers to 'FinishDistr' table. It calculates how many times the driver came first
| second and third by looking at 'RaceInfos' table.

|
|

.. code-block:: python

    def search_byname(self, name):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()

            query = """SELECT DISTINCT DRIVER_ID , NAME, number_first, number_second, number_third
                    FROM FINISHDISTR, RACEINFOS,DRIVERS
                    WHERE (DRIVER_ID=DRIVERS.ID  AND NAME ILIKE '%%%s%%') ORDER BY DRIVER_ID
                    """ % (name)
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows



| This function search for the name stated in the parameter in the Finish Distrubitions page.



|
|

*Driver Informations Class*
-----------------------
 Table for Driver Informations:


.. code-block:: python

        query = """CREATE TABLE DriverInfo (
                    driver_id INTEGER NOT NULL REFERENCES drivers(id)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE,
                    nationid INTEGER REFERENCES nations(id),
                    age INTEGER,
                    winning_number INTEGER
                )"""
                


| This code is from the server.py file. It handles the adding,deleting and searching requests from web page.

.. code:: python

    @app.route('/DriverInfo', methods=['GET', 'POST'])
    def drinfo_page():
    dr = DriverInfo(app.config['dsn'])
    if request.method == 'GET':
        now = datetime.datetime.now()
        dr_list=dr.get_driverinfo()
        return render_template('driverinfo.html', dr_list = dr_list, current_time = now.ctime())
    elif 'drivers_to_delete' in request.form:
        ids = request.form.getlist('drivers_to_delete')
        for driver_id in ids:
            dr.delete_driver(driver_id)
    elif 'drivers_to_add' in request.form:
        dr.add_driver(request.form['driver_id'],request.form['nation_id'],request.form['age'])
    elif 'drivers_to_search' in request.form:
        now = datetime.datetime.now()
        search_result = dr.search_byname(request.form['id'])
        return render_template('driverinfo.html', dr_list = search_result, current_time = now.ctime())
    return redirect(url_for('drinfo_page'))

|
|
|
|
.. code-block:: python

    class DriverInfo:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_driverinfo(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT DISTINCT DriverInfo.DRIVER_ID , nations.title, age, winning_number, Finishdistr.point
                    FROM DriverInfo left outer join nations on nations.id=nationid left outer join DRIVERS on DriverInfo.DRIVER_ID=DRIVERS.ID left outer join Finishdistr on Finishdistr.driver_id=DriverInfo.driver_id ORDER BY DRIVER_ID"""
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

| Driver Informations class. This function list all driver with detailed informations. It take point attribute from 'FinishDistr' table.
|

.. code-block:: python

    def delete_driver(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM FINISHDISTR WHERE DRIVER_ID = '%s'" % (id)
            cursor.execute(query)
            connection.commit()
            return


| This function deletes the row whose id is same with 'id' parameter.
 

|
|

.. code-block:: python

    def add_driver(self, id, nation_id, age ):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT COUNT(dr1_id) FROM RACEINFOS WHERE dr1_id = '%s'" % (id)
            cursor.execute(query)
            winning_number = cursor.fetchall()[0][0]
            query = "INSERT INTO DriverInfo VALUES ('%s','%s','%s','%s')" % (id,nation_id,age,winning_number)
            cursor.execute(query)
            connection.commit()
            return
| This function add new driver to 'DriverInfo' table. It calculates winning number as number of times the drivers came first and
| it take it from the 'RaceInfos' table.
 
|
|

.. code-block:: python

    def search_byname(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()

            query = """SELECT DISTINCT DriverInfo.DRIVER_ID , nations.title, age, winning_number, Finishdistr.point
                    FROM DriverInfo left outer join nations on nations.id=nationid left outer join DRIVERS on DriverInfo.DRIVER_ID=DRIVERS.ID left outer join Finishdistr on Finishdistr.driver_id=DriverInfo.driver_id
                    WHERE (DriverInfo.driver_id = %s) ORDER BY DRIVER_ID
                    """ % (id)
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows





| This function search for the id stated in the parameter in the Driver Informations page.




|
|
