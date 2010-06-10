from flask import request, jsonify
from pgrouting import app

@app.route('/routing<format>')
def routing(format):
    return jsonify({
        'from': request.args.get('from'), 
        'to': request.args.get('to')
    })

