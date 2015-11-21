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

from tires import Tires
from drivers import Drivers
from tracks import Tracks
from nations import Nations
from years import Years
from raceinfos import Raceinfos
from teams import Teams
from Engines import Engines
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

@app.route('/Raceinfos', methods=['GET', 'POST'])
def raceinfo_page():
    racs = Raceinfos(app.config['dsn'])
    if request.method == 'GET':
        now = datetime.datetime.now()
        racinflist = racs.get_raceinfolist()
        return render_template('raceinfos.html', RaceList = racinflist, current_time = now.ctime())
    elif 'raceinfos_to_delete' in request.form:
        raceinfos = request.form.getlist('raceinfos_to_delete')
        for raceinfo in raceinfos:
            racs.delete_raceinfo(raceinfo)
        return redirect(url_for('raceinfo_page'))

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



@app.route('/initdb')
def init_db():
    initialize = INIT(app.config['dsn'])
    initialize.All()
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
