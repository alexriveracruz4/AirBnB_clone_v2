#!/usr/bin/python3
""" Fabfile to delete out-of-date archives. """
from fabric.api import local, env, run

env.hosts = ['34.73.0.81', '3.88.221.211']


def do_clean(number=0):
    """
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keep only the most recent archive.
    If number is 2, keep the most and second most recent archives,
    etc.
    """
    number = int(number)
    number = 2 if number < 1 else number + 1
    local("ls -d -1t versions/* | tail -n +{} | \
    xargs -d '\n' rm -f".format(number))

    run("ls -d -1tr /data/web_static/releases/* | tail -n +{} | \
    xargs -d '\n' rm -rf".format(number))
