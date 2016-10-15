# -*- coding: utf-8 -*-
import os

import cherrypy
from cherrypy._cpnative_server import CPHTTPServer
import click

from FirstCherryPy.app import create_app


@click.command()
@click.option('--env', help='CherryPy settings: production, staging, dev')
@click.option('--native', help='Use the native server, not the WSGI server',
              is_flag=True)
def run(env, native):
    """
    Start listening and serving applications on the address and port defining in
    the configuration.
    """
    create_app()

    conf = '/etc/FirstCherryPy.conf'
    if not os.path.isfile(conf):
        conf = os.path.normpath(os.path.join(os.path.dirname(__file__),
                                             '..', 'conf',
                                             'FirstCherryPy.conf'))
    cherrypy.config.update(conf)

    if env in ['production', 'staging']:
        cherrypy.config.update({'environment': env})

    if native:
        cherrypy.server = CPHTTPServer(cherrypy.server)
    cherrypy.engine.signals.subscribe()
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    run()