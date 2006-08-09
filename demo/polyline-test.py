## Polyline demo by Brendan Howell (mute@howell-ersatz.com)

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
    
    canvas = goocanvas.CanvasView()
    canvas.set_size_request(600, 450)
    canvas.set_bounds(0, 0, 1000, 1000)
    canvas.show()
    scrolled_win.add(canvas)
    
    canvas.connect("button_press_event", on_arrow_button_press)

    ## Create the canvas model
    canvas_model = create_canvas_model()
    canvas.set_model(canvas_model)

    gtk.main()


def create_canvas_model():
    canvas_model = goocanvas.CanvasModelSimple()

    root = canvas_model.get_root_item()

    ## Add a few simple items.
    global item
    item = goocanvas.polyline_new_line(root, 300, 200, 200, 200)
    item.props.end_arrow = True
    item.props.line_width = 10

    return canvas_model



## This is our handler for the "item-view-created" signal of the GooCanvasView.
##   We connect to the "button-press-event" signal of new rect views.
def on_item_view_created (view, item_view, item):
    if isinstance(item, goocanvas.Polyline):
        item_view.connect("button_press_event", on_arrow_button_press)


## This handles button presses in item views. We simply output a message to
##   the console.
def on_arrow_button_press (view, event):
    global item
    print "received button press event"
    points = goocanvas.Points([(300, 200), (event.x, event.y)])
    item.props.points = points
    return True


## This is our handler for the "delete-event" signal of the window, which
##   is emitted when the 'x' close button is clicked. We just exit here. */
def on_delete_event(window, event):
    raise SystemExit


if __name__ == "__main__":
    main(sys.argv)
