import os
from spry.config import *


def server(environ, start_response):
    # only serve the file if it is within STATIC_FILE_DIR and
    # if it exists
    if environ['PATH_INFO'].startswith(STATIC_URL_PREFIX):
        return static(environ, start_response)
    else:
        status = '200 OK'
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response(status, headers)

        path = environ['PATH_INFO']
        path = os.path.normpath(path)

        if path == '/':
            f = []
            for (dirpath, dirnames, filenames) in os.walk(TEMPLATE_FILE_DIR):
                f.extend(filenames)

            return [('<a href="%s">%s</a><br>' %
                    (filename, filename)).encode('UTF-8') for filename in f]
        else:
            template = TEMPLATE_ENVIRONMENT_LOADER.get_template(path)
            render = template.render()

            return [render.encode('UTF-8')]


def static(environ, start_response):
    """Serve static files from the directory named
    in STATIC_FILE_DIR"""

    path = environ['PATH_INFO']
    # we want to remove '/static' from the start
    path = path.replace(STATIC_URL_PREFIX, STATIC_FILE_DIR)

    path = os.path.normpath(path)

    if path.startswith(STATIC_FILE_DIR) and os.path.exists(path):
        h = open(path, 'rb')
        content = h.read()
        h.close()

        headers = [('content-type', content_type(path))]
        start_response('200 OK', headers)
        return [content]
    else:
        start_response('404 NOT FOUND')
        return []


def content_type(path):
    """Return a guess at the mime type for this path
    based on the file extension"""

    name, ext = os.path.splitext(path)

    if ext in MIME_TABLE:
        return MIME_TABLE[ext]
    else:
        return "application/octet-stream"
