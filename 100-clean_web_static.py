#!/usr/bin/python3
"""Deletes out-of-date archives"""


from fabric.api import *
import os
env.hosts = []


def do_clean(number=0):
    """Deletes out of date archives"""
    if int(number) == 0:
        number = 1
    else:
        int(number)

    archives = sorted(os.listdir("versions"))
    for i in range(number):
        archives.pop()
    with lcd("versions"):
        for a in archives:
            local("rm ./{}".format(a))
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        for i in range(number):
            archives.pop()
            for a in archives:
                run("rm -rf ./{}".format(a))
