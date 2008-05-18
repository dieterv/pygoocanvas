import sys
import gobject
import gtk
import goocanvas
import cairo

def main(argv):
    window = gtk.Window()
    window.set_default_size(700, 350)
    window.show()
    window.connect("delete_event", on_delete_event)
    
    scrolled_win = gtk.ScrolledWindow()
    scrolled_win.set_shadow_type(gtk.SHADOW_IN)
    scrolled_win.show()
    window.add(scrolled_win)
    
    canvas = goocanvas.Canvas()
    canvas.set_size_request(700, 350)
    canvas.set_bounds(0, 0, 1000, 1000)
    canvas.show()
    scrolled_win.add(canvas)

    root = canvas.get_root_item()

    # Create a Linear Patter with cairo 
    linear = cairo.LinearGradient(50, 50, 300, 300)
    linear.add_color_stop_rgba(0.0,  1, 1, 1, 0)
    linear.add_color_stop_rgba(0.25,  0, 1, 0, 0.5)
    linear.add_color_stop_rgba(0.50,  1, 1, 1, 0)
    linear.add_color_stop_rgba(0.75,  0, 0, 1, 0.5)
    linear.add_color_stop_rgba(1.0,  1, 1, 1, 0)

   # Create a rect to be filled with the linear gradient
    item = goocanvas.Rect(x=50, y=50, width=250, height=250,
                          line_width=10.0,
                          radius_x=20.0,
                          radius_y=10.0,
                          fill_pattern=linear)
    root.add_child(item, 0)

    item.connect("button-press-event", on_rect_button_press)

    item = goocanvas.Text(parent=root,
                          text="Linear Gradient",
                          x=175, y=175,
                          anchor=gtk.ANCHOR_CENTER,
                          font="Sans 24")
    item.rotate(315, 175, 175)
    
    # Create a Radial Patter with cairo 
    radial = cairo.RadialGradient(450, 150, 15, 600, 250, 55)
    radial.add_color_stop_rgb(0,  1.0, 0.8, 0.8)
    radial.add_color_stop_rgb(0.50,  0.9, 0.5, 0.0)
    radial.add_color_stop_rgb(1,  0.9, 0.0, 0.0)


   # Create a rect to be filled with the radial gradient
    item = goocanvas.Rect(parent=root,
                          x=400, y=50, width=250, height=250,
                          line_width=10.0,
                          radius_x=20.0,
                          radius_y=10.0,
                          fill_pattern=radial)

    item.connect("button-press-event", on_rect_button_press)

    item = goocanvas.Text(parent=root,
                          text="Radial Gradient",
                          x=525, y=175,
                          anchor=gtk.ANCHOR_CENTER,
                          font="Sans 24")
    item.rotate(315, 525, 175)

    gtk.main()

## This handles button presses in item views. We simply output a message to
##   the console.
def on_rect_button_press (view, target, event):
    target.set_simple_transform(50, 50 , 1, 0)
    print "rect item received button press event"
    return True


## This is our handler for the "delete-event" signal of the window, which
##   is emitted when the 'x' close button is clicked. We just exit here. */
def on_delete_event(window, event):
    raise SystemExit

if __name__ == "__main__":
    main(sys.argv)
    
