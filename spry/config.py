from jinja2 import Environment, FileSystemLoader

STATIC_URL_PREFIX = '/static/'
STATIC_FILE_DIR = 'web/static/'
TEMPLATE_FILE_DIR = 'web/templates/'
CONTENT_FILE_DIR = 'web/content/'

MIME_TABLE = {'.ico': 'text/plain',
              '.txt': 'text/plain',
              '.png': 'image/png',
              '.jpg': 'image/jpeg',
              '.gif': 'image/gif',
              '.html': 'text/html',
              '.css': 'text/css',
              '.js': 'application/javascript',
              '.woff': 'application/octet-stream'}

# Setting up Jinja2 do not alter unless you know what you are doing
fileSystemLoader = FileSystemLoader(TEMPLATE_FILE_DIR)
TEMPLATE_ENVIRONMENT_LOADER = Environment(loader=fileSystemLoader,
                                          trim_blocks=True,
                                          lstrip_blocks=True)
