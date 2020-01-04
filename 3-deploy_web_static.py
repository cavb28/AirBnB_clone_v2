#!/usr/bin/python3
"""
creates and distributes an archive to your web servers,
using the function deploy
"""

from datetime import datetime
from fabric.operations import local, put, run
from fabric.api import env
from os import path

env.hosts = ['35.243.220.111', '35.190.130.57']


def do_pack():
    """
    Tars every file in web_static into versions
    """
    local("mkdir -p versions")
    my_path = local("tar -zcvf versions/web_static_{}.tgz web_static".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))

    my_path_name = "versions/web_static_{}.tgz".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))

    if my_path.failed:
        return None
    return my_path_name


def do_deploy(archive_path):
    """
    deploy archive
    :param archive_path:
    :return:
    """
    if not path.exists(archive_path):
        return False

    try:
        my_name = archive_path[9:]
        my_name_short = archive_path[9:-4]
        put(archive_path, "/tmp/{}".format(my_name))
        run("mkdir -p /data/web_static/releases/{}/".format(my_name_short))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(my_name, my_name_short))
        run("mv /data/web_static/releases/{}/web_static/*\
                            /data/web_static/releases/{}/"
            .format(my_name_short, my_name_short))
        run("rm /tmp/{}".format(my_name))
        run("rm -fr /data/web_static/current")
        run("rm -fr /data/web_static/releases/{}/web_static"
            .format(my_name_short))
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(my_name_short))
        print("New version deployed!")
    except Exception:
        return False


def deploy():
    """
    Full deployment
    :return:
    """

    """Call the do_pack() function and store the path of the created archive"""
    my_pack = do_pack()
    """ Return False if no archive has been created"""
    if not my_pack:
        return False
    """ Return the return value of do_deploy"""
    return do_deploy(my_pack)
