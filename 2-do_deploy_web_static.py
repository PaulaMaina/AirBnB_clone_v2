#!/usr/bin/python3
"""This script distibutes an archive to the web servers"""


from fabric.api import env, run, put
from os.path import exists
env.hosts = ['54.234.7.217', '18.235.233.205']


def do_deploy(archive_path):
    """Distributes the archive to web-01 & web-02"""
    if exists(archive_path) is False:
        return False
    try:
        file = archive_path.split("/")[-1]
        no_ext = file.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file, path, no_ext))
        run('rm /tmp/{}'.format(file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
