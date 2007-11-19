import gobject
import gtk
import goocanvas
import rsvg
import cairo

class CustomSvgItem(goocanvas.ItemSimple):
    # setup our custom properties
    __gproperties__ = {
        'x': (float,                                # property type
              'X',                                  # property nick name
              'The x coordinate of a SVG image',    # property description
              0,                                    # property minimum value
              10e6,                                 # property maximum value
              0,                                    # property default value
              gobject.PARAM_READWRITE),             # property flags

        'y': (float,
              'Y',
              'The y coordinate of a SVG image',
              0,
              10e6,
              0,
              gobject.PARAM_READWRITE),

        'width': (float,
                  'Width',
                  'The width of the SVG Image',
                  0,
                  10e6,
                  0,
                  gobject.PARAM_READABLE),

        'height': (float,
                   'Height',
                   'The width of the SVG Image',
                   0,
                   10e6,
                   0,
                   gobject.PARAM_READABLE),
        }
    
    def __init__(self, x, y, handle, **kwargs):
        super(CustomSvgItem, self).__init__(**kwargs)
        
        self.x = x
        self.y = y
        
        self.width = handle.props.width
        self.height = handle.props.height
        
        self.handle = handle

    def do_set_property(self, pspec, value):
        if pspec.name == 'x':
            self.x = value
            
            # make sure we update the display
            self.changed(True)
        
        elif pspec.name == 'y':
            self.y = value
            
            # make sure we update the display
            self.changed(True)
        
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

        else:
            raise AttributeError, 'unknown property %s' % pspec.name
    
    def do_simple_paint(self, cr, bounds):
        matrix = cr.get_matrix()
        matrix.translate(self.x, self.y)
        cr.set_matrix(matrix)
        self.handle.render_cairo(cr)

    def do_simple_update(self, cr):
        self.bounds_x1 = float(self.x)
        self.bounds_y1 = float(self.y)
        self.bounds_x2 = float(self.x + self.width)
        self.bounds_y2 = float(self.y + self.height)

    def do_simple_is_item_at(self, x, y, cr, is_pointer_event):
        if ((x < self.x) or (x > self.x + self.width)) or ((y < self.y) or (y > self.y + self.height)):
            return False
        else:    
            return True

gobject.type_register(CustomSvgItem)

def on_press(item, target, event, root):
    item.props.y = 150
    
def on_r_press(item, target, event):
    item.props.x = 150

def main():
    window = gtk.Window()
    window.set_default_size(640, 600)
    window.show()
    window.connect("destroy", lambda w: gtk.main_quit())
    
    scrolled_win = gtk.ScrolledWindow()
    scrolled_win.set_shadow_type(gtk.SHADOW_IN)
    scrolled_win.show()
    
    window.add(scrolled_win)
    
    canvas = goocanvas.Canvas()
    canvas.set_size_request(600, 450)
    canvas.set_bounds(0, 0, 1000, 1000)

    root = canvas.get_root_item()
    
    handle = rsvg.Handle("../images/circle1.svg")

    svgitem = CustomSvgItem(x=100,
                            y=100,
                            handle=handle,
                            parent=root)
    svgitem.connect("button_press_event", on_press, root)
    
    r = goocanvas.Rect (parent=root,
                        x=10,
                        y=10,
                        width=20,
                        height=20)
    r.connect("button_press_event", on_r_press)
    r.props.fill_color = 'yellow'
    
    canvas.show()
    scrolled_win.add(canvas)

    gtk.main()

if __name__ == "__main__":
    main()
