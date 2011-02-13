import config
import gtk
from plugin_manager import plugmanager
import pluglib

class Preferences:

    def __init__(self):
        self.pref_window = None

        if self.pref_window:
            return

        self.builder = gtk.Builder()
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
            print "el plugin es: " + str(type(plugin))
            if plugin.name != None:
                self.plugins_store.append([plugmanager.is_plugin_enabled(plugin_id), None, plugin.name, plugin_id])
        
        self.builder.connect_signals(self)
        self.pref_window.show_all()

    def onPluginCloseButton(self, widget):
        self.pref_window.destroy()
        self.pref_window = None

    def on_preferences_window_destroy(self, window):
        self.window = None

    def on_close_button_clicked(self, button):
        self.close_window()

    def on_close(self, widget, event):
        self.close_window()

    def on_preferences_window_key_press(self, widget, event):
        # ctrl+w means close window
        if (event.keyval == gtk.keysyms.w \
            and event.state & gtk.gdk.CONTROL_MASK):
            self.close_window()

        # escape can mean several things
        if event.keyval == gtk.keysyms.Escape:
            #check, maybe we are editing stuff
            if self.activityCell.get_property("editable"):
                self.activityCell.set_property("editable", False)
                return
            if self.categoryCell.get_property("editable"):
                self.categoryCell.set_property("editable", False)
                return

            self.close_window()

    def on_plugabout_btn_clicked(self, button):
        selection = self.plugins_tree.get_selection()
        model, selected = selection.get_selected()

        if selected:
            plugin = plugmanager.get_plugin_class(model[selected][3])
            if plugin:
                self.plugabout_dialog.set_name(plugin.name)
                self.plugabout_dialog.set_version(plugin.version)
                self.plugabout_dialog.set_authors(plugin.authors)
                self.plugabout_dialog.set_website(plugin.website)
                self.plugabout_dialog.set_comments(plugin.description)

                response = self.plugabout_dialog.run()
                if response in (gtk.RESPONSE_DELETE_EVENT, gtk.RESPONSE_CANCEL):
                    self.plugabout_dialog.hide()

    def on_plugins_tv_cursor_changed(self, treeview):
        selection = self.plugins_tree.get_selection()
        model, selected = selection.get_selected()

        if selected:
            plugin = plugmanager.get_plugin_class(model[selected][3])
            self.plugconf_btn.set_sensitive(pluglib.verify_conf_dialog(plugin))

    def on_plugconf_btn_clicked(self, button):
        selection = self.plugins_tree.get_selection()
        model, selected = selection.get_selected()

        if selected:
            plugin = plugmanager.get_plugin_class(model[selected][3])
            if pluglib.verify_conf_dialog(plugin):
                plugin.configure_dialog(self.parent)

    def on_active_cell_toggled(self, checkbox, path):
        active = not checkbox.get_active()
        plugin_name = self.plugins_store[path][3]

        if active:
            plugmanager.enable_plugin(plugin_name)
        else:
            plugmanager.disable_plugin(plugin_name)

        self.plugins_store[path][0] = active

