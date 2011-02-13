import sys
import gtk
import config
import preferences as prefs
import pluglib
 
class TestGUI:

    def __init__(self):
        self.preferences = None

        self.builder = gtk.Builder()
        self._cfg = config.Config()
        self.builder.add_from_file(self._cfg.path+'testgui.ui')
        self.window = self.builder.get_object('window1')
        self.window.show_all()
        self.builder.connect_signals(self)
        
        from plugin_manager import plugmanager
        plugmanager.scan_plugins()

    def about(self, widget):
        """Display the about window."""
        authors = ["J. Ignacio Alvarez <jialvarez@emergya.es>"]
        url = "http://www.emergya.es"
        
        self.aboutDialog = gtk.AboutDialog()
        self.aboutDialog.set_authors(authors)
        self.aboutDialog.set_name('Pluglib ABC')
        self.aboutDialog.set_website(url)
        self.aboutDialog.set_title('Testing')
        self.aboutDialog.connect('response', self.aboutDialogOnResponse)
        self.aboutDialog.show()

    def aboutDialogOnResponse(self, dialog, responseID):
        """Signal handler for the About Dialog's "response" signal."""

        dialog.destroy()
        self.aboutDialog = None

    def showPreferences(self, widget):
        if self.preferences:
            return

        p = prefs.Preferences()

    def onPluginCloseButton(self, widget):
        self.preferences.destroy()
        self.preferences = None

    def onDestroy(self, widget):
        gtk.main_quit()

    def onExitButton(self, widget):
        gtk.main_quit()

if __name__ == '__main__':
    v = TestGUI()
    gtk.main()
    sys.exit(0)
