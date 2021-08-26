#!/usr/bin/python3
"""
Python fabric that manages archives for web servers
"""
import os.path
from fabric.api import local, put, run, env
from datetime import datetime as dt

env.hosts = ["34.73.0.81", "3.88.221.211"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

now = dt.now()


def do_pack():
    """Packs web_static files into .tgz file"""

    file_name = 'versions/web_static_{}.tgz'\
                .format(now.strftime("%Y%m%d%H%M%S"))

    if not os.path.isdir("versions"):
        if local("mkdir -p versions").failed:
            return None

    command = local("tar -cvzf {} web_static".format(file_name))
    if command.succeeded:
        return file_name
    return None


def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """
    Packs and deploys a webstatic site from an archive
    Returns: Value of do_deploy, False if no archive created
    """
    archive = do_pack()
    if archive is None:
        return False
    return(do_deploy(archive))
