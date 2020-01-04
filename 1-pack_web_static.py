#!/usr/bin/python3
"""Generates a .tgz archive from web_static folder."""
from datetime import datetime
from fabric.operations import local


def do_pack():
    """Function to generate version compressed files"""
    path = local("tar -cavf versions/web_static_{}.tgz web_static".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))

    if path.failed:
        return None
    return path
