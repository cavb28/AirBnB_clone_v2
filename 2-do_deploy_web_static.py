#!/usr/bin/python3
"""
Distributes an archive to the web servers,
using the function do_deploy
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

    if my_path.failed:
        return None
    return path


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

        """ Upload the archive to the /tmp/ directory of the web server"""
        put(archive_path, "/tmp/{}".format(my_name))

        """Uncompress the archive to the folder /data/web_static/releases/<archive
        filename without extension> on the web server"""
        run("mkdir -p /data/web_static/releases/{}/".format(my_name_short))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(my_name, my_name_short))
        run("mv /data/web_static/releases/{}/web_static/*\
                            /data/web_static/releases/{}/"
            .format(my_name_short, my_name_short))

        """Delete the archive from the web server"""
        run("rm /tmp/{}".format(my_name))

        """Delete the symbolic link /data/web_static/current
        from the web server"""
        run("rm -fr /data/web_static/current")

        """Create a new the symbolic link /data/web_static/current on the web server,
        linked to the new version of your code
        (/data/web_static/releases/<archive filename without extension>)
        """
        run("rm -fr /data/web_static/releases/{}/web_static"
            .format(my_name_short))
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(my_name_short))

        print("New version deployed!")

    except Exception:
        return False
