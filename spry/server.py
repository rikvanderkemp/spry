from wsgiref.simple_server import make_server

import os
import re

import spry.structure
import spry.template
from spry.config import *


def run_server():
    """ Lets run a simple wsgi server on port 8000
    we route everything through our 'server' app """

    httpd = make_server('', 8000, server)
    httpd.serve_forever()


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
            """
                The root of our website will contain a very simple
                file listing containing links to both static
                and dynamic (=yaml fueled) files
            """
            file_listing = []

            spry.structure.get_static_html_files(
                file_listing, TEMPLATE_FILE_DIR)

            if os.path.isdir(CONTENT_FILE_DIR):
                file_listing.extend(
                    spry.structure.get_files_from_path(CONTENT_FILE_DIR))

            return [('<a href="%s">%s</a><br>' %
                    (filename, filename)).encode('UTF-8')
                    for filename in file_listing]
        else:
            template_data = False

            """
                if a path with a .html extension is given
                try and retrieve the matching yml file
            """
            if re.search('.*\.html', path):
                template_data = spry.template.get_yaml_data(path)
                if template_data:
                    path = spry.template.determine_template_by_path(path)

            # Serve regular existing html templates
            template = TEMPLATE_ENVIRONMENT_LOADER.get_template(path)
            render = template.render(data=template_data)

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
