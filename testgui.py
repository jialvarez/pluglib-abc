import sys
import gtk
import config
 
class TestGUI:
    def __init__(self):
        self.builder = gtk.Builder()
        _cfg = config.Config()
        self.builder.add_from_file(_cfg.path+'testgui.ui')
        self.window = self.builder.get_object('window1')
        self.window.show_all()
        self.builder.connect_signals(self)

if __name__ == '__main__':
    v = TestGUI()
    gtk.main()
    exit(1)
