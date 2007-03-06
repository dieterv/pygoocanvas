import goocanvas
import gtk

def on_motion_notify (item, target, event):
    id = item.get_data ("id")
    
    if id:
        print "%s item received 'motion-notify' signal" % id
    else:
        print "Unknown item received 'motion-notify' signal"

    return False

def setup_canvas (canvas, units, units_name):
    data = [
    [100, 100, 200, 20, 10, 200, 310, 24],
    [100, 100, 200, 20, 10, 200, 310, 24],
    [1, 1, 3, 0.5, 0.16, 3, 4, 0.3],
    [30, 30, 100, 10, 5, 80, 60, 10]
    ]

    d = data[units]

    root = canvas.get_root_item ()

    item = goocanvas.Rect (parent = root,
                           x = d[0],
                           y = d[1],
                           width = d[2],
                           height = d[3])
    
    item.connect ("motion_notify_event", on_motion_notify)

    buffer = "This box is %gx%g %s" % (d[2], d[3], units_name)
    font_desc = "Sans %gpx" % d[4]
    
    item = goocanvas.Text (parent = root,
                           text = buffer,
                           x = d[0] + d[2] / 2,
                           y = d[1] + d[3] / 2,
                           width = -1,
                           anchor = gtk.ANCHOR_CENTER,
                           font = font_desc)

    buffer = "This font is %g %s high" % (d[7], units_name)
    font_desc = "Sans %gpx" % d[7]
    
    item = goocanvas.Text (parent = root,
                           text = buffer,
                           x = d[5],
                           y = d[6],
                           width = -1,
                           anchor = gtk.ANCHOR_CENTER,
                           font = font_desc)
    
def zoom_changed (adj, canvas):
    canvas.set_scale (adj.value)

def create_canvas (units, units_name):
    vbox = gtk.VBox (False, 4)
    vbox.set_border_width (4)

    hbox = gtk.HBox (False, 4)
    vbox.pack_start (hbox, False, False, 0)

    canvas = goocanvas.Canvas ()

    w = gtk.Label ("Zoom:")
    hbox.pack_start (w, False, False, 0)

    adj = gtk.Adjustment (1.00, 0.05, 100.00, 0.05, 0.50, 0.50)
    w = gtk.SpinButton (adj, 0.0, 2)
    adj.connect ("value_changed", zoom_changed, canvas)
    w.set_size_request (50, -1)
    hbox.pack_start (w, False, False, 0)

    scrolled_win = gtk.ScrolledWindow ()
    vbox.pack_start (scrolled_win, True, True, 0)

    # Create the canvas.
    canvas.set_size_request (600, 450)
    setup_canvas (canvas, units, units_name)

    canvas.set_bounds (0, 0, 1000, 1000)
    canvas.props.units = units
    canvas.props.anchor = gtk.ANCHOR_CENTER

    scrolled_win.add (canvas)

    return vbox

def main ():
    window = gtk.Window (gtk.WINDOW_TOPLEVEL)
    window.set_default_size (640, 600)

    window.connect ("delete_event", gtk.main_quit)

    notebook = gtk.Notebook ()

    window.add (notebook)

    notebook.append_page (create_canvas (gtk.UNIT_PIXEL, "pixels"), gtk.Label ("Pixels"))
    notebook.append_page (create_canvas (gtk.UNIT_POINTS, "points"), gtk.Label ("Points"))
    notebook.append_page (create_canvas (gtk.UNIT_INCH, "inch"), gtk.Label ("Inch"))
    notebook.append_page (create_canvas (gtk.UNIT_MM, "millimiters"), gtk.Label ("Millimiters"))
    
    window.show_all()
    gtk.main ()
    
if __name__ == "__main__":
    main()
