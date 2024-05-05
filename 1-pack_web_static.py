#!/usr/bin/python3
"""This script generates a .tgz files from the contents of web_static"""


from farbric.api import *
from datetime import datetime


def do_pack():
    """Makes an archive of the web_static folder"""
    date = datetime.now()
    archive = 'web_static_' + date.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))

    if create is not None:
        return archive
    else:
        return None
