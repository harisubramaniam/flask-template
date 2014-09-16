from app import app 
from flask import Flask, request, jsonify, g
import time
import requests

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error':'Not found'}), 404

@app.errorhandler(500)
def error(exception):
    try:
        m_id = app.config.get("MONITOR_ID")
        if m_id and not app.debug:
            payload = {'app_id': m_id, 'error': exception}
            response = requests.post("http://dellpe605-06.azcentral.com/error", data=payload)
    except:
        print "Monitor errored out processing errors"

    return jsonify({'error':'Something went wrong'}), 500

# Stats
@app.before_request
def before_request():
  g.start = time.time()

@app.teardown_request
def teardown_request(exception=None):
    try:
        m_id = app.config.get("MONITOR_ID")
        if m_id and not app.debug and g.get("start"):
            total = time.time() - g.start
            payload = {'time': total, 'app_id': m_id, 'url': request.path}
            response = requests.post("http://dellpe605-06.azcentral.com/push", data=payload)
    except:
        print "Monitor errored out in teardown"