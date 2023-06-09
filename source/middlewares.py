from functools import wraps
from flask import request, session, abort, redirect, url_for
from source import app
from source.local_settings import DEBUG

    
    
@app.before_request
def before_request():
    if DEBUG:
        print(request.method, request.path)