"""Add Header

This plug-in can be used to quickly add a header to a subprogram, task or package.
"""

###############################################################################
# No user customization below this line
###############################################################################

import GPS
from gps_utils import interactive


def __contextualMenuFilter(context):

    # Check if the context is generated by the source editor
    if not (context.module_name == 'Source_Editor'):
        return False

    # Get current view and cursor
    ev = GPS.EditorBuffer.get().current_view()
    c  = ev.cursor()

    # Return true if the file is writable and
    # the name of the "active" subprogram is non-empty
    if not ev.is_read_only()                  and \
       c.subprogram_name()                    and \
      (c.block_type()      == 'CAT_PACKAGE'   or  \
       c.block_type()      == 'CAT_PROCEDURE' or  \
       c.block_type()      == 'CAT_FUNCTION'  or  \
       c.block_type()      == 'CAT_TASK'      ):
        return True
    else:
        return False


def __contextualMenuLabel(context):

    # Get current view and cursor
    ev = GPS.EditorBuffer.get().current_view()
    c  = ev.cursor()

    # Name of the menu item
    return 'Add header to <b>{}</b>'.format(c.subprogram_name())


def insert_header(eb, c):

    # Obtain the current view
    ev = eb.current_view()

    # Jump the start of the block
    el = c.block_start()

    ev.goto(el)
    ev.center(el)

    # Name of the subprogram at the current location
    name = c.subprogram_name()

    # Create a mark at the current location
    em1 = ev.cursor().create_mark()

    # Write header
    eb.insert('-' * (3 + len(name) + 3) + '\n')
    eb.insert('-- ' + name + ' --\n');
    eb.insert('-' * (3 + len(name) + 3) + '\n')
    eb.insert('\n')

    # Create a mark at the current location
    em2 = ev.cursor().create_mark()

    # Indent
    eb.indent(
      em1.location().beginning_of_line(),
      em2.location().end_of_line())

    # Remove marks
    em1.delete()
    em2.delete()


@interactive(
    name       = 'Add header',
    category   = 'Editor',
    contextual = __contextualMenuLabel,
    filter     = __contextualMenuFilter)
def on_activate():

    # Get current buffer
    eb = GPS.EditorBuffer.get()

    # Get current view
    ev = eb.current_view()

    # Create a mark at the current location
    em = ev.cursor().create_mark()

    # Add header
    insert_header(eb, em.location())

    # Always remove mark
    em.delete()
