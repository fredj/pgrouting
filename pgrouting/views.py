from flask import request
from pgrouting import app

@app.route('/routing')
def routing():
    start = request.args.get('from')
    end = request.args.get('to')
    return "%s -> %s"%(start, end)
