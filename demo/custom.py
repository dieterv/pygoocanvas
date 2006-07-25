### A custom item example

import sys
import gobject
import gtk
import goocanvas

class CustomItem(gobject.GObject, goocanvas.Item, goocanvas.ItemView):

    __gproperties__ = {
        'x': (float, 'X position', 'X position',
              -10e6, 10e6, 0, gobject.PARAM_READWRITE|gobject.PARAM_CONSTRUCT),

        'y': (float, 'Y position', 'Y position',
              -10e6, 10e6, 0, gobject.PARAM_READWRITE|gobject.PARAM_CONSTRUCT),

        'width': (float, 'width', 'width',
              -10e6, 10e6, 0, gobject.PARAM_READWRITE|gobject.PARAM_CONSTRUCT),

        'height': (float, 'height', 'height',
              -10e6, 10e6, 0, gobject.PARAM_READWRITE|gobject.PARAM_CONSTRUCT),

        'title': (str, None, None, '', gobject.PARAM_READWRITE),
        'description': (str, None, None, '', gobject.PARAM_READWRITE),
        'can-focus': (bool, None, None, False, gobject.PARAM_READWRITE),
        'visibility-threshold': (float, None, None, 0, 10e6, 0, gobject.PARAM_READWRITE),
        'visibility': (goocanvas.ItemVisibility, None, None, goocanvas.ITEM_VISIBLE, gobject.PARAM_READWRITE),
        'pointer-events': (goocanvas.PointerEvents, None, None, goocanvas.EVENTS_NONE, gobject.PARAM_READWRITE),
        'transform': (goocanvas.TYPE_CAIRO_MATRIX, None, None, gobject.PARAM_READWRITE),
        }

    def do_create_view(self, canvas_view, parent_view):
        return self

    def __init__(self, **kwargs):
        gobject.GObject.__init__(self, **kwargs)
        self.bounds = goocanvas.Bounds()

    def do_set_property(self, pspec, value):
        if pspec.name == 'x':
            self.x = value
        elif pspec.name == 'y':
            self.y = value
        elif pspec.name == 'width':
            self.width = value
        elif pspec.name == 'height':
            self.height = value
        elif pspec.name == 'title':
            self.title = value
        elif pspec.name == 'can-focus':
            self.can_focus = value
        else:
            raise AttributeError, 'unknown property %s' % pspec.name
        
    def do_get_property(self, pspec):
        if pspec.name == 'x':
            return self.x
        elif pspec.name == 'y':
            return self.y
        elif pspec.name == 'width':
            return self.width
        elif pspec.name == 'height':
            return self.height
        elif pspec.name == 'title':
            return self.title
        elif pspec.name == 'can-focus':
            return self.can_focus
        else:
            raise AttributeError, 'unknown property %s' % pspec.name

    def do_update(self, entire_tree, cr):
        self.bounds.x1 = self.x
        self.bounds.y1 = self.y
        self.bounds.x2 = self.x + self.width
        self.bounds.y2 = self.y + self.height
        return self.bounds

    def do_get_bounds(self):
        return self.bounds

    def do_paint(self, cr, bounds, scale):
        cr.rectangle(self.x, self.y, self.width, self.height)
        cr.set_line_width(self.width/20)
        cr.stroke()
        return self.bounds

    def do_get_item_view_at(self, x, y, cr, is_pointer_event, parent_is_visible):
        return None

    def do_set_parent(self, parent):
        pass
    

def main(argv):
    window = gtk.Window()
    window.set_default_size(640, 600)
    window.show()
    window.connect("destroy", lambda w: gtk.main_quit())
    
    scrolled_win = gtk.ScrolledWindow()
    scrolled_win.set_shadow_type(gtk.SHADOW_IN)
    scrolled_win.show()
    window.add(scrolled_win)
    
    canvas = goocanvas.CanvasView()
    canvas.set_size_request(600, 450)
    canvas.set_bounds(0, 0, 1000, 1000)
    canvas.show()
    scrolled_win.add(canvas)
    
    ## Create the canvas model
    canvas_model = create_canvas_model()
    canvas.set_model(canvas_model)

    gtk.main()


def create_canvas_model():
    canvas_model = goocanvas.CanvasModelSimple()
    root = canvas_model.get_root_item()
    item = CustomItem(x=100, y=100, width=400, height=400)
    root.add_child(item)
    item = goocanvas.Text(text="Hello World",
                          x=300, y=300,
                          anchor=gtk.ANCHOR_CENTER,
                          font="Sans 24")
    root.add_child(item)
    item.rotate(45, 300, 300)

    return canvas_model


if __name__ == "__main__":
    main(sys.argv)
