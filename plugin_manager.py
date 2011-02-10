import os
import gobject

import pluglib
from pluglib.manager import ModulePluginManager
from pluglib.confstore import GConfStore

PLUGINS_DIR = ['baseplugins']
GCONF_DIR = '/apps/popoter/applet/plugins'

class TestPluginManager(ModulePluginManager, GConfStore, gobject.GObject):

    __gsignals__ = {
        'plugin_enabled': (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE,
                (gobject.TYPE_PYOBJECT,)),
        'plugin_disabled': (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE,
                (gobject.TYPE_PYOBJECT,)),
    }

    defaults = {
        'active_plugins': [],
    }
 
    def __init__(self):
        ModulePluginManager.__init__(self, PLUGINS_DIR)
        GConfStore.__init__(self, GCONF_DIR)
        gobject.GObject.__init__(self)
        self.load()
 
    def restore(self):
        for plugin_name in self.options['active_plugins']:
            if plugin_name in self.plugins.keys():
                self.enable_plugin(plugin_name, emit=False)

    def cleanup(self):
        for plugin_object in [plugin['object'] for plugin in self.plugins.values() \
                if pluglib.verify_configurable(plugin['object'])]:
            plugin_object.save()

    def enable_plugin(self, plugin_name, emit=True):
        super(TestPluginManager, self).enable_plugin(plugin_name)

        if not plugin_name in self.options['active_plugins']:
            self.options['active_plugins'].append(plugin_name)
        self.save()

        if emit:
            self.emit('plugin_enabled', plugin_name)

    def disable_plugin(self, plugin_name, emit=True):
        super(TestPluginManager, self).disable_plugin(plugin_name)

        if plugin_name in self.options['active_plugins']:
            self.options['active_plugins'].remove(plugin_name)
        self.save()

        if emit:
            self.emit('plugin_disabled', plugin_name)

    def get_plugin_class(self, plugin_name):
        if self.plugins.has_key(plugin_name):
            return self.plugins[plugin_name]['class']
        else:
            raise PluginManagerError, 'No plugin named %s' % plugin_name

plugmanager = TestPluginManager()
