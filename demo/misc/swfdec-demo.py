import sys
import gobject
import gtk
import goocanvas
try:
    import swfdec.ui
except ImportError:
    print "you need swfdec in order to run this demo"
    sys.exit(0)

## usage example:
##     python swfdec-demo.py file:///home/gianmt/Repos/pyswfdec/demo/mammyblue2.swf

drag_x = 0
drag_y = 0
dragging = False

def main(argv):
    window = gtk.Window()
    window.set_default_size(640, 600)
    window.show()
    window.connect("delete_event", on_delete_event)
    
    scrolled_win = gtk.ScrolledWindow()
    scrolled_win.set_shadow_type(gtk.SHADOW_IN)
    scrolled_win.show()
    window.add(scrolled_win)
    
    canvas = goocanvas.Canvas()
    canvas.set_size_request(600, 450)
    canvas.set_bounds(0, 0, 1000, 1000)
    canvas.show()
    scrolled_win.add(canvas)

    root = canvas.get_root_item()
    
    url = swfdec.URL(sys.argv[1])
    
    p = swfdec.ui.Player(None)
    p.set_url(url)
    
    wdg = swfdec.ui.Widget(player=p)
    
    p.set_playing (True)

    ## Add a few simple items.
    item = goocanvas.Widget(x=100, y=100,
                            height=-1,
                            width=-1,
                            widget=wdg)
    root.add_child(item, 0)

    wdg.connect("motion-notify-event", on_motion_notify, item)
    wdg.connect("button-press-event", on_button_press)
    wdg.connect("button-release-event", on_button_release)

    gtk.main()

def on_button_press(widget, event):
    global dragging
    global drag_x
    global drag_y
    if event.button == 1:
        drag_x = event.x
        drag_y = event.y

        fleur = gtk.gdk.Cursor (gtk.gdk.FLEUR)
        gtk.gdk.pointer_grab (widget.window,
                              True,
                              gtk.gdk.POINTER_MOTION_MASK | gtk.gdk.BUTTON_RELEASE_MASK,
                              None,
                              fleur,
                              event.time)
        dragging = True
    return True

def on_motion_notify (widget, event, item):
    global dragging
    global drag_x
    global drag_y
    if (dragging == True) and (event.state & gtk.gdk.BUTTON1_MASK):
        new_x = event.x
        new_y = event.y
        item.translate (new_x - drag_x, new_y - drag_y)
    return True

def on_button_release (widget, event):
    global dragging
    global drag_x
    global drag_y
    gtk.gdk.pointer_ungrab (event.time)
    dragging = False
    return True

## This is our handler for the "delete-event" signal of the window, which
##   is emitted when the 'x' close button is clicked. We just exit here. */
def on_delete_event(window, event):
    raise SystemExit


if __name__ == "__main__":
    main(sys.argv)
    
