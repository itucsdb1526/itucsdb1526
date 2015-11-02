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
from nations import Nations
from init import INIT
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

@app.route('/initdb')
def init_db():
    initialize = INIT(app.config['dsn'])
    initialize.All()
    return redirect(url_for('nation_page'))

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
    
