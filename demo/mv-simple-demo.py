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
    canvas.set_size_request(600, 450)
    canvas.set_bounds(0, 0, 1000, 1000)
    canvas.show()
    scrolled_win.add(canvas)

    root = goocanvas.GroupModel()
    

    ## Add a few simple items.
    rect_model = goocanvas.RectModel(x=100, y=100, width=400, height=400,
                                     line_width=10.0,
                                     radius_x=20.0,
                                     radius_y=10.0,
                                     stroke_color="yellow",
                                     fill_color="red")
    root.add_child(rect_model, 0)


    text_model = goocanvas.TextModel(text="Hello World",
                                     x=300, y=300,
                                     anchor=gtk.ANCHOR_CENTER, 
                                     font="Sans 24")
    root.add_child(text_model, 1)
    text_model.rotate(45, 300, 300)

    canvas.set_root_item_model(root)

    rect_item = canvas.get_item(rect_model)
    rect_item.connect("button-press-event", on_rect_button_press)

    gtk.main()

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
    
