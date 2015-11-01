import datetime
import json
import os
import psycopg2 as dbapi2
import re

from flask import Flask
from flask import redirect
from flask import render_template
from flask.helpers import url_for
from flask import request

from nation import Nation

app = Flask(__name__)


def get_elephantsql_dsn(vcap_services):
    """Returns the data source name for ElephantSQL."""
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
             dbname='{}'""".format(user, password, host, port, dbname)
    return dsn

@app.route('/')
def home_page():
    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())

@app.route('/Nations', methods=['GET', 'POST'])
def nation_page():
    if request.method == 'GET':
        now = datetime.datetime.now()
        tr = Nation(id = 2, title = 'Turkiye')
        ct = Nation(3, 'Country')
        ct2 = Nation(7, 'Country2')
        nlist = [(1, tr), (2, ct), (3, ct2)]
        return render_template('nation.html', NationList = nlist, current_time = now.ctime())
    elif 'nations_to_delete' in request.form:
        keys = request.form.getlist('nations_to_delete') 
        #for key in keys:
            #app.store.delete_nation(int(key)) 
        return redirect(url_for('nation_page'))

@app.route('/initdb')
def init_db():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()

        query = """SELECT * FROM information_schema.tables WHERE table_name = 'tablo1'"""
        cursor.execute(query)

        if(cursor.rowcount == 1):
            query = """DROP TABLE IF EXISTS tablo1"""
            cursor.execute(query)
        else:
            query = """CREATE TABLE tablo1 (
                      ID SERIAL PRIMARY KEY,
                      NAME VARCHAR(40) UNIQUE NOT NULL
              )"""
            cursor.execute(query)

        connection.commit()
    return redirect(url_for('home_page'))



if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True

    VCAP_SERVICES = os.getenv('VCAP_SERVICES')
    if VCAP_SERVICES is not None:
        app.config['dsn'] = get_elephantsql_dsn(VCAP_SERVICES)
    else:
        app.config['dsn'] = """user='postgres' host='localhost' port=5432 dbname='mydb'"""
    app.run(host='0.0.0.0', port=port, debug=debug)

