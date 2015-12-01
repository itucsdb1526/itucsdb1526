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
from finishdistr import Finishdistr

from tires import Tires
from drivers import Drivers
from tracks import Tracks
from track_info import Track_info
from nations import Nations
from years import Years
from raceinfos import Raceinfos
from successfulnats import SuccessfulNats
from teams import Teams
from Engines import Engines
from champinfo import Champinfo
from init import INIT
from func import Func
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

@app.route('/Years/<year_title>', methods=['GET', 'POST'])
def a_year_page(year_title):
    now = datetime.datetime.now()
    fn = Func(app.config['dsn'])
    rc = Raceinfos(app.config['dsn'])
    year_id = fn.get_id("years", year_title)
    if year_id is None:
        return render_template('404.html', current_time = now.ctime())
    rclist = rc.get_raceinfolist(year_title = year_title)
    return render_template('a_year.html', YearTitle = year_title, RaceList = rclist, current_time = now.ctime())



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
        return render_template('raceinfos.html', RaceList = racinflist, current_time = now.ctime(), TrackList = tr_list, NationList = nat_list, YearList = yr_list, DriverList = dr_list)
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
        return render_template('raceinfos.html', RaceList = racinflist, current_time = now.ctime(), TrackList = tr_list, NationList = nat_list, YearList = yr_list, DriverList = dr_list)
    elif 'raceinfos_to_searchtrack' in request.form:
        now = datetime.datetime.now()
        racinflist = racs.search_raceinfolist('track', request.form)
        return render_template('raceinfos.html', RaceList = racinflist, current_time = now.ctime(), TrackList = tr_list, NationList = nat_list, YearList = yr_list, DriverList = dr_list)

@app.route('/SuccessfulNations', methods=['GET', 'POST'])
def sucnat_page():
    sn = SuccessfulNats(app.config['dsn'])
    now = datetime.datetime.now()
    if request.method == 'GET':
        return render_template('successfulnats.html', List = sn.get_sucnatlist(), current_time = now.ctime())

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
        clist = cinfos.search_champinfolist('')
        return render_template('champinfo.html', ChampinfoList = clist, current_time = now.ctime())
    return redirect(url_for('champinfo_page'))


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
