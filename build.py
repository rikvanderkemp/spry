import spry.structure
import spry.config
import os.path
import urllib.request
import subprocess
import sys
import re

BUILD_FOLDER = './build'


def clean():
    """
        Cleanup build directory
    """
    print("Removing possible build directory....")
    subprocess.call(["rm", "-Rf", BUILD_FOLDER])


def ping():
    try:
        urllib.request.urlopen('http://localhost:8000')
    except:
        print("Did you start SPRY?")
        sys.exit()


def generate_file_list():
    file_list = []

    spry.structure.get_static_html_files(
        file_list, spry.config.TEMPLATE_FILE_DIR)

    if os.path.isdir(spry.config.CONTENT_FILE_DIR):
        file_list.extend(
            spry.structure.get_files_from_path(spry.config.CONTENT_FILE_DIR))

    return file_list


def read_write_response():
    file_list = generate_file_list()

    for url in file_list:
        try:
            full_url = 'http://localhost:8000/%s' % url
            print("Processing %s" % full_url)
            response = urllib.request.urlopen(full_url)

            html = response.read().decode('utf-8')
        except:
            print("Weirdness has happened trying to process %s" % full_url)
            sys.exit()

        target_path = '%s/%s' % (BUILD_FOLDER, url)

        print("Saving HTML output to %s" % target_path)

        target_file = open(target_path, 'w')
        target_file.write(str(html))
        target_file.close()
        response.close()


def generate_folder_structure():
    """ Create build folder """
    subprocess.call(["mkdir", BUILD_FOLDER])

    file_list = generate_file_list()

    for url in file_list:
        """
            We are being quite ignorant and only building
            one level deep structures, this is the way spry
            behaves and so we not need recursiveness
        """
        path_chunks = re.split('\/', url)
        if len(path_chunks) > 1:
            """
                We are only concerned about non-root level elements
            """
            subprocess.call(["mkdir", "%s/%s" % (BUILD_FOLDER, path_chunks[0])])


def collect_static():
    subprocess.call(["cp", "-Rf", "../web/static", BUILD_FOLDER])


print(
    """
  _|_|_|  _|_|_|    _|_|_|    _|      _|
_|        _|    _|  _|    _|    _|  _|
  _|_|    _|_|_|    _|_|_|        _|
      _|  _|        _|    _|      _|
_|_|_|    _|        _|    _|      _|
"""
)

clean()
ping()
generate_folder_structure()
read_write_response()
collect_static()
