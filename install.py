# installer for netatmo driver
# Copyright 2015 Matthew Wall
# Distributed under the terms of the GNU Public License (GPLv3)

from setup import ExtensionInstaller


def loader():
    return NetatmoInstaller()


class NetatmoInstaller(ExtensionInstaller):
    def __init__(self):
        super(NetatmoInstaller, self).__init__(
            version="0.17",
            name='netatmo',
            description='Driver for netatmo weather stations.',
            author="Matthew Wall",
            author_email="mwall@users.sourceforge.net",
            config={
                'netatmo': {
                    'client_id': 'INSERT_CLIENT_ID_HERE',
                    'client_secret': 'INSERT_CLIENT_SECRET_HERE',
                    'driver': 'user.netatmo',
                    'tokens_persistence_file': '/etc/weewx/tokens_persistence_file.json',
                }
            },
            files=[('bin/user', ['bin/user/netatmo.py'])]
        )
