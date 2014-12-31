from wsgiref.simple_server import make_server
from spry.server import server


def run_server():
    """ Lets run a simple wsgi server on port 8000
    we route everything through our 'server' app """

    httpd = make_server('', 8000, server)
    httpd.serve_forever()
