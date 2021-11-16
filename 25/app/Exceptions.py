from flask import abort
from app import app
from flask import jsonify, make_response
import json


class Exception_404 (Exception):
    def __init__(self, text_error):
        self.text = text_error
        print (f'Exception_404:{self.text}')
        abort(404, description=f'Exception_404:{self.text}')

class Exception_500 (Exception):
    def __init__(self, text_error):
        self.text = text_error
        print(f'Exception_500:{self.text}')
        abort(500, description=f'Exception_500:{self.text}')

class Exception_400 (Exception):
    def __init__(self, text_error):
        self.text = text_error
        print(f'Exception_400:Bad Request:{self.text}')
        abort(400, description=f'Exception_400:Bad Request {self.text}')