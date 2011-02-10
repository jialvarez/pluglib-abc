# -*- coding: utf-8 -*-

# Copyright (C) 2010, J. Félix Ontañón <felixonta@gmail.com>

# This file is part of Pluglib.

# Pluglib is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Pluglib is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Pluglib.  If not, see <http://www.gnu.org/licenses/>.

import zope.interface
import interfaces

def register(cls):
    zope.interface.classImplements(cls, interfaces.IPlugin)
    return cls

def verify_conf_dialog(plugin_class):
    return interfaces.IConfigureDialog.implementedBy(plugin_class)
    
def verify_configurable(plugin_obj):
    return interfaces.IConfigureDialog.providedBy(plugin_obj)
