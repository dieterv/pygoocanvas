import sys
import gobject
import gtk
import goocanvas

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
    #canvas.set_size_request(600, 450)
    #canvas.set_bounds(0, 0, 0, 0)
    canvas.show()
    scrolled_win.add(canvas)

    root = canvas.get_root_item ()

    ## Add a few simple items.
    item = goocanvas.Path(parent = root,
                          line_width=10.0,
                          line_dash=goocanvas.LineDash([5.0, 10.0, 20.0, 10.0, 5.0]),
                          data="M 100 100 L 400 400 L 100 300 Z", fill_color="red")

    gtk.main()

## This is our handler for the "delete-event" signal of the window, which
##   is emitted when the 'x' close button is clicked. We just exit here. */
def on_delete_event(window, event):
    raise SystemExit


if __name__ == "__main__":
    main(sys.argv)
