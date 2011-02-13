# - coding: utf-8 -

from pluglib.confstore import GConfStore
from pluglib.interfaces import IPlugin

class testPlugin(GConfStore, IPlugin):
    name = 'Test Plugin'
    description = 'A testing plugin for code tests' 
    version = '0.1pre'
    authors = ['J. Félix Ontañón <felixonta@gmail.com>']
    website = 'http://fontanon.org'
    #icon = 'gtk-missing-image'

    defaults = {
        'hola':     1,
        'adios':    2,
        'estres':   'hola'
    }

    def __init__(self):
        super(testPlugin, self).__init__('/apps/hamster-applet/plugins/test')
        print 'Hello World!'
