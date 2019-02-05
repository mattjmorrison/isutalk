import json
from cgi import FieldStorage
from wsgiref.simple_server import make_server

def simple_app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain; charset=utf-8'), ('Access-Control-Allow-Origin', '*')])
    return [json.dumps({'message': "Hello from the server!"}).encode('utf-8')]


with make_server('', 8000, simple_app) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
