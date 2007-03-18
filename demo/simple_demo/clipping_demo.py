import goocanvas
import gtk
import cairo

def on_button_press (item, target, event, id):
    print "%s received 'button-press' signal at %f, %f (root: %f, %f)" % \
           (id, event.x, event.y, event.x_root, event.y_root)
    return True

def setup_canvas (canvas):
    root = canvas.get_root_item ()

    #Plain items without clip path.
    item = goocanvas.Ellipse (parent = root,
                              center_x = 0,
                              center_y = 0,
                              radius_x = 50,
                              radius_y = 30,
                              fill_color = "blue")
    item.translate (100, 100)
    item.rotate (30, 0, 0)
    item.connect ("button_press_event",
                  on_button_press, "Blue ellipse (unclipped)")

    item = goocanvas.Rect (parent = root,
                           x = 200,
                           y = 50,
                           width = 100,
                           height = 100,
                           fill_color = "red",
                           clip_fill_rule = cairo.FILL_RULE_EVEN_ODD)
    item.connect ("button_press_event",
                  on_button_press, "Red rectangle (unclipped)")

    item = goocanvas.Rect (parent = root,
                           x = 380,
                           y = 50,
                           width = 100,
                           height = 100,
                           fill_color = "yellow")
    item.connect ("button_press_event",
                  on_button_press, "Yellow rectangle (unclipped)")

    # Clipped items.
    item = goocanvas.Ellipse (parent = root,
                              center_x = 0,
                              center_y = 0,
                              radius_x = 50,
                              radius_y = 30,
                              fill_color = "blue",
                              clip_path = "M 0 0 h 100 v 100 h -100 Z")
    item.translate (100, 300)
    item.rotate (30, 0, 0)
    item.connect ("button_press_event", on_button_press, "Blue ellipse")

    item = goocanvas.Rect (parent = root,
                           x = 200,
                           y = 250,
                           width = 100,
                           height = 100,
                           fill_color = "red",
                           clip_path = "M 250 300 h 100 v 100 h -100 Z",
                           clip_fill_rule = cairo.FILL_RULE_EVEN_ODD)
    item.connect ("button_press_event", on_button_press, "Red rectangle")

    item = goocanvas.Rect (parent = root,
                           x = 380,
                           y = 250,
                           width = 100,
                           height = 100,
                           fill_color = "yellow",
                           clip_path = "M480,230 l40,100 l-80 0 z")
    item.connect ("button_press_event", on_button_press, "Yellow rectangle")

    # Table with clipped items.
    table = goocanvas.Table (parent = root)
    table.translate (200, 400)
    table.rotate (30, 0, 0)

    item = goocanvas.Ellipse (parent = table,
                              center_x = 0,
                              center_y = 0,
                              radius_x = 50,
                              radius_y = 30,
                              fill_color = "blue",
                              clip_path = "M 0 0 h 100 v 100 h -100 Z")
    item.translate (100, 300)
    item.rotate (30, 0, 0)
    item.connect ("button_press_event", on_button_press, "Blue ellipse")

    item = goocanvas.Rect (parent = table,
                           x = 200,
                           y = 250,
                           width = 100,
                           height = 100,
                           fill_color = "red",
                           clip_path = "M 250 300 h 100 v 100 h -100 Z",
                           clip_fill_rule = cairo.FILL_RULE_EVEN_ODD)
    item.connect ("button_press_event", on_button_press, "Red rectangle")
    table.set_child_properties (item, column = 1)

    item = goocanvas.Rect (parent = table,
                           x = 380,
                           y = 250,
                           width = 100,
                           height = 100,
                           fill_color = "yellow",
                           clip_path = "M480,230 l40,100 l-80 0 z")
    item.connect ("button_press_event", on_button_press, "Yellow rectangle")
    table.set_child_properties (item, column = 2)

def create_clipping_page ():
    vbox = gtk.VBox (False, 4)
    vbox.set_border_width (4)

    scrolled_win = gtk.ScrolledWindow ()
    scrolled_win.set_shadow_type (gtk.SHADOW_IN)

    vbox.add (scrolled_win)

    canvas = goocanvas.Canvas ()
    canvas.set_size_request (600, 450)
    canvas.set_bounds (0, 0, 1000, 1000)

    scrolled_win.add (canvas)
    setup_canvas (canvas)

    return vbox

def main ():
    vb = create_clipping_page ()

    win = gtk.Window()
    win.connect("destroy", gtk.main_quit)
    win.add(vb)
    win.show_all()

    gtk.main()

if __name__ == "__main__":
    main ()
