from flask import request
from pgrouting import app
from pgrouting.utils import jsonify

@app.route('/routing')
@jsonify
def routing():
    return {
        'from': request.args.get('from'), 
        'to': request.args.get('to')
    }

