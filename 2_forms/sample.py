from cgi import FieldStorage
from wsgiref.simple_server import make_server

def simple_app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain; charset=utf-8')])
    post = FieldStorage(fp=environ['wsgi.input'], environ=environ.copy(), keep_blank_values=True)
    return [
        b"You Entered",
        b'\nFirst: ', post['first'].value.encode(),
        b'\nSecond: ', post['second'].value.encode(),
        b'\nThird: ', post['third'].value.encode(),
        b'\nFourth: ', post['fourth'].value.encode(),
    ]


with make_server('', 8000, simple_app) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
