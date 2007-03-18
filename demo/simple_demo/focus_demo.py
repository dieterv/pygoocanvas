import goocanvas
import gtk

def on_focus_in (item, target, event):
    id = item.get_data ("id")

    if id:
        print "%s received focus-in event" % id 
    else: 
        print "unknown"

    ''' Note that this is only for testing. Setting item properties to indicate
     focus isn't a good idea for real apps, as there may be multiple views. '''
    item.props.stroke_color = "black"

    return False

def on_focus_out (item, target, event):
    id = item.get_data ("id")
    if id:
        print "%s received focus-out event" % id
    else:
        print "unknown"

    ''' Note that this is only for testing. Setting item properties to indicate
     focus isn't a good idea for real apps, as there may be multiple views. '''
    item.props.stroke_pattern = None

    return False

def on_button_press (item, target, event):
    id = item.get_data ("id")

    if id:
        print "%s received button-press event" % id
    else:
        print "unknown"

    canvas = item.get_canvas ()
    canvas.grab_focus (item)

    return True

def on_key_press (item, target, event):
    id = item.get_data ("id")
    
    if id:
        print "%s received key-press event" % id
    else:
        print "unknown"

    return False

def create_focus_box (canvas, x, y, width, height, color):
    root = canvas.get_root_item ()
    item = goocanvas.Rect (parent = root,
                           x = x,
                           y = y,
                           width = width,
                           height = height,
                           stroke_pattern = None,
                           fill_color = color,
                           line_width = 5.0,
                           can_focus = True)
    item.set_data ("id", color)

    item.connect ("focus_in_event", on_focus_in)
    item.connect ("focus_out_event", on_focus_out)
    item.connect ("button_press_event", on_button_press)
    item.connect ("key_press_event",  on_key_press)

def setup_canvas (canvas):
    create_focus_box (canvas, 110, 80, 50, 30, "red")
    create_focus_box (canvas, 300, 160, 50, 30, "orange")
    create_focus_box (canvas, 500, 50, 50, 30, "yellow")
    create_focus_box (canvas, 70, 400, 50, 30, "blue")
    create_focus_box (canvas, 130, 200, 50, 30, "magenta")
    create_focus_box (canvas, 200, 160, 50, 30, "green")
    create_focus_box (canvas, 450, 450, 50, 30, "cyan")
    create_focus_box (canvas, 300, 350, 50, 30, "grey")
    create_focus_box (canvas, 900, 900, 50, 30, "gold")
    create_focus_box (canvas, 800, 150, 50, 30, "thistle")
    create_focus_box (canvas, 600, 800, 50, 30, "azure")
    create_focus_box (canvas, 700, 250, 50, 30, "moccasin")
    create_focus_box (canvas, 500, 100, 50, 30, "cornsilk")
    create_focus_box (canvas, 200, 750, 50, 30, "plum")
    create_focus_box (canvas, 400, 800, 50, 30, "orchid")

def create_focus_page ():
    vbox = gtk.VBox (False, 4)
    vbox.set_border_width (4)

    label = gtk.Label ("Use Tab, Shift+Tab or the arrow keys to move the keyboard focus between the canvas items.")
    vbox.pack_start (label, False, False, 0)

    scrolled_win = gtk.ScrolledWindow ()
    scrolled_win.set_shadow_type (gtk.SHADOW_IN)

    vbox.add (scrolled_win)

    canvas = goocanvas.Canvas ()
    canvas.set_flags (gtk.CAN_FOCUS)
    canvas.set_size_request (600, 450)
    canvas.set_bounds (0, 0, 1000, 1000)

    scrolled_win.add (canvas)

    setup_canvas (canvas)

    return vbox

def main ():
    vb = create_focus_page ()
    
    win = gtk.Window()
    win.connect("destroy", gtk.main_quit)
    win.add(vb)
    win.show_all()
    
    gtk.main()

if __name__ == "__main__":
    main ()







