import os

class Config:
    def __init__(self):
        self.home_path = os.path.expanduser('~')
        self.app_path = "trabajo/orca-git/pluglib-abc"
        self.ui_path = "ui/"
    
    def get_path(self):
        return os.path.join(self.home_path, self.app_path, self.ui_path)

    def set_path(self, f_home_path, f_app_path, f_ui_path):
        self.home_path = f_home_path
        self.app_path = f_app_path
        self.ui_path = f_ui_path

    path = property(fget = get_path, fset = set_path, doc = 'The path')
