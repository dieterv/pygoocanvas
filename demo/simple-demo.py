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
    
    canvas.connect("item_view_created", on_item_view_created)

    ## Create the canvas model
    canvas_model = create_canvas_model()
    canvas.set_model(canvas_model)

    gtk.main()


def create_canvas_model():
    canvas_model = goocanvas.CanvasModelSimple()

    root = canvas_model.get_root_item()

    ## Add a few simple items.
    item = gobject.new(goocanvas.Rect,
                       x=100, y=100, width=400, height=400,
                       line_width=10.0,
                       radius_x=20.0,
                       radius_y=10.0,
                       stroke_color="yellow",
                       fill_color="red")
    root.add_child(item)

    item = gobject.new(goocanvas.Text, text="Hello World",
                       x=300, y=300, width=-1,
                       anchor=gtk.ANCHOR_CENTER,
                       font="Sans 24")
    root.add_child(item)
    item.rotate(45, 300, 300)

    return canvas_model



## This is our handler for the "item-view-created" signal of the GooCanvasView.
##   We connect to the "button-press-event" signal of new rect views.
def on_item_view_created (view, item_view, item):
    if isinstance(item, goocanvas.Rect):
        item_view.connect("button_press_event", on_rect_button_press)


## This handles button presses in item views. We simply output a message to
##   the console.
def on_rect_button_press (view, target, event):
    print "rect item received button press event"
    return True


## This is our handler for the "delete-event" signal of the window, which
##   is emitted when the 'x' close button is clicked. We just exit here. */
def on_delete_event(window, event):
    raise SystemExit


if __name__ == "__main__":
    main(sys.argv)
