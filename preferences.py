import config
from plugin_manager import plugmanager
import pluglib

class Preferences:

    def __init__(self, builder):
        self.pref_window = None

        if self.pref_window:
            return

        self.builder = builder
        self._cfg = config.Config()
        self.builder.add_from_file(self._cfg.path+'preferences.ui')
        self.pref_window = self.builder.get_object("preferences_window")
        self.close_button = self.builder.get_object("close_button")
        self.close_button.connect('clicked', self.onPluginCloseButton)

        # create and fill plugins tree
        self.plugins_tree = self.builder.get_object("plugins_tv")
        self.plugins_store = self.builder.get_object("plugins_store")
        self.plugabout_btn = self.builder.get_object("plugabout_btn")
        self.plugconf_btn = self.builder.get_object("plugconf_btn")
        self.plugabout_dialog = self.builder.get_object("plugabout_dialog")
       
        print "plugins detectados: " + str(plugmanager.get_plugins())

        print plugmanager.get_plugins()

        for plugin_id, plugin in plugmanager.get_plugins():
            self.plugins_store.append([plugmanager.is_plugin_enabled(plugin_id), 
                None, plugin.name, plugin_id])

        self.pref_window.show()

    def onPluginCloseButton(self, widget):
        self.pref_window.destroy()
        self.pref_window = None
