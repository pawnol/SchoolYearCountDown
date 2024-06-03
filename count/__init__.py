import os

from flask import Flask, render_template
from count.scrape_calendar import get_events

east_troy_calendar_url = 'http://www.easttroy.k12.wi.us/pro/events_ical_subscribe.cfm?detailid=659489&categoryids=19&categoryids2=all&facultyflag=0'

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index_page():
        return render_template('index.html')
    
    @app.route('/jsonfile')
    def json_file():
        return get_events(east_troy_calendar_url)

    return app