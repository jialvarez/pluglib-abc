# - coding: utf-8 -

from pluglib.confstore import GConfStore
from pluglib.interfaces import IPlugin

class gConfPlugin(GConfStore):
    def __init__(self):
        super(gConfPlugin, self).__init__('/apps/popoter/plugins/test')
        self.save()
        print 'Hello World!'

class testPlugin(IPlugin):
    name = 'Test Plugin'
    description = 'A testing plugin for code tests' 
    version = '0.1pre'
    authors = ['J. Félix Ontañón <felixonta@gmail.com>', 'J. Ignacio Álvarez <neonigma@gmail.com>']
    website = 'http://fontanon.org'
    #icon = 'gtk-missing-image'

    defaults = {
        'hola':     1,
        'adios':    2,
        'estres':   'hola'
    }

    def __init__(self):
        gc_plug = gConfPlugin()



