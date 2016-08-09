"""Hello World

This plug-in is a simple example of showing an entry in a context menu.
"""

###########################################################################
# No user customization below this line
###########################################################################

import GPS
from gps_utils import interactive


def __contextualMenuFilter(context):
    
    # Show the menu's context and context generator in GPS console
    GPS.Console().write(
        "Module "             + str(context.module_name) +
        " generated context " + str(context) + "\n")
    
    # Always show in context menu
    return True


def __contextualMenuLabel(context):
    
    # Name of the menu item
    return "Show Hello World!"


@interactive(
    name       ='Hello World!',
    contextual = __contextualMenuLabel,
    filter     = __contextualMenuFilter)
def on_activate():
    
    # Action when activated
    GPS.Console().write("Hello World!\n")
