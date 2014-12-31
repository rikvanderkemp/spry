import os
import re
from spry.config import *


def get_files_from_path(path, max_depth=1, level=0):
    if level <= max_depth:
        f = []

        for (item) in os.listdir(path):
            if (os.path.isfile(os.path.join(path, item))):
                if level <= 0:
                    """
                        Root items should not include any folder
                        structure whatsoever, so append just the
                        file name.
                    """
                    file_name = item
                else:
                    """
                        Anything else deeper then the root will need
                        to contain the folder structure they are in.
                        We will assume this happens when files are
                        accessed or read from the CONTENT_FILE_DIR we
                        will need to strip this reference of the base
                        path so we will end up with just the regular path.
                    """
                    file_name = (
                        '%s/%s' % (path.replace(CONTENT_FILE_DIR, ''), item)
                    ).lstrip('/')

                """
                    Simply replace yml extension files with
                    .html so it is more web friendly :-)
                """
                if re.search('.*\.yml', file_name):
                    file_name = ('%s.html' % file_name[:-4])

                f.append(file_name)

            elif (os.path.isdir(os.path.join(path, item))):
                level += 1
                f.extend(
                    get_files_from_path(
                        os.path.join(path, item), max_depth, level
                    )
                )

        return f
    else:
        return False


def get_files_from_static_content_root(file_listing):
    """
        Go through all 'static' files in our TEMPLATE_FILE_DIR
        and add these to our files list. We will only be scanning
        through our root directory and won't descend
        into any subdirectories.
    """
    for (item) in os.listdir(TEMPLATE_FILE_DIR):
        if (os.path.isfile(os.path.join(TEMPLATE_FILE_DIR, item))):
            """
                Exclude files beginning with a _ (underscore)
                these files will be used to populate from yaml files
            """
            if re.search('^(?!\_)', item):
                file_listing.append(item)


def get_files_from_yaml_directories(file_listing):
    """
        Collect all file names from CONTENT_FILE_DIR
        which will contain yaml files, replace their
        extension with html for front-end consistency
    """

    file_listing.extend(get_files_from_path(CONTENT_FILE_DIR))
    # file_listing.append(('%s.html' % item[:-4]))
