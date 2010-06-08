from functools import wraps
import json
from flask import Response

def jsonify(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return Response(json.dumps(f(*args, **kwargs)), 
                        mimetype='application/json')
    return decorated_function


