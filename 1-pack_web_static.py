#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static folder
of the AirBnB Clone repo, using the function do_pack.
"""
from datetime import datetime
from fabric.operations import local


def do_pack():
    """
    Tars every file in web_static into versions
    """
    """Create local directory versions"""
    local("mkdir -p versions")
    """execute te tar command locally tar -zcvf
    use datetime for the file name
    """
    my_path = local("tar -zcvf versions/web_static_{}.tgz web_static".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))

    if my_path.failed:
        return None
    return my_path
