# - coding: utf-8 -

import hamster.pluglib
from hamster.pluglib.confstore import GConfStore

@hamster.pluglib.register
class testPlugin(GConfStore):
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