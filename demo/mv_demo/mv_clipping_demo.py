import goocanvas
import gtk
import cairo

def on_button_press (item, target, event, id):
    print "%s received 'button-press' signal at %g, %g (root: %g, %g)" % \
           (id, event.x, event.y, event.x_root, event.y_root)
    return True

def setup_canvas (canvas):
    root = goocanvas.GroupModel ()
    canvas.set_root_item_model (root)

    #Plain items without clip path.
    model = goocanvas.EllipseModel (parent = root,
                                    center_x = 0,
                                    center_y = 0,
                                    radius_x = 50,
                                    radius_y = 30,
                                    fill_color = "blue")
    model.translate (100, 100)
    model.rotate (30, 0, 0)
    item = canvas.get_item (model)
    item.connect ("button_press_event",
                  on_button_press, "Blue ellipse (unclipped)")

    model = goocanvas.RectModel (parent = root,
                                 x = 200,
                                 y = 50,
                                 width = 100,
                                 height = 100,
                                 fill_color = "red",
                                 clip_fill_rule = cairo.FILL_RULE_EVEN_ODD)
    item = canvas.get_item (model)
    item.connect ("button_press_event",
                  on_button_press, "Red rectangle (unclipped)")

    model = goocanvas.RectModel (parent = root,
                                x = 380,
                                y = 50,
                                width = 100,
                                height = 100,
                                fill_color = "yellow")
    item = canvas.get_item (model)
    item.connect ("button_press_event",
                  on_button_press, "Yellow rectangle (unclipped)")

    # Clipped items.
    model = goocanvas.EllipseModel (parent = root,
                                    center_x = 0,
                                    center_y = 0,
                                    radius_x = 50,
                                    radius_y = 30,
                                    fill_color = "blue",
                                    clip_path = "M 0 0 h 100 v 100 h -100 Z")
    model.translate (100, 300)
    model.rotate (30, 0, 0)
    item = canvas.get_item (model)
    item.connect ("button_press_event", on_button_press, "Blue ellipse")

    model = goocanvas.RectModel (parent = root,
                                 x = 200,
                                 y = 250,
                                 width = 100,
                                 height = 100,
                                 fill_color = "red",
                                 clip_path = "M 250 300 h 100 v 100 h -100 Z",
                                 clip_fill_rule = cairo.FILL_RULE_EVEN_ODD)
    item = canvas.get_item (model)
    item.connect ("button_press_event", on_button_press, "Red rectangle")

    model = goocanvas.RectModel (parent = root,
                                 x = 380,
                                 y = 250,
                                 width = 100,
                                 height = 100,
                                 fill_color = "yellow",
                                 clip_path = "M480,230 l40,100 l-80 0 z")
    item = canvas.get_item (model)
    item.connect ("button_press_event", on_button_press, "Yellow rectangle")

    # Table with clipped items.
    table = goocanvas.TableModel (parent = root)
    table.translate (200, 400)
    table.rotate (30, 0, 0)

    model = goocanvas.EllipseModel (parent = table,
                                    center_x = 0,
                                    center_y = 0,
                                    radius_x = 50,
                                    radius_y = 30,
                                    fill_color = "blue",
                                    clip_path = "M 0 0 h 100 v 100 h -100 Z")
    model.translate (100, 300)
    model.rotate (30, 0, 0)
    item = canvas.get_item (model)
    item.connect ("button_press_event", on_button_press, "Blue ellipse")

    model = goocanvas.RectModel (parent = table,
                                 x = 200,
                                 y = 250,
                                 width = 100,
                                 height = 100,
                                 fill_color = "red",
                                 clip_path = "M 250 300 h 100 v 100 h -100 Z",
                                 clip_fill_rule = cairo.FILL_RULE_EVEN_ODD)
    item = canvas.get_item (model)
    item.connect ("button_press_event", on_button_press, "Red rectangle")
    table.set_child_properties (model, column = 1)

    model = goocanvas.RectModel (parent = table,
                                 x = 380,
                                 y = 250,
                                 width = 100,
                                 height = 100,
                                 fill_color = "yellow",
                                 clip_path = "M480,230 l40,100 l-80 0 z")
    item = canvas.get_item (model)
    item.connect ("button_press_event", on_button_press, "Yellow rectangle")
    table.set_child_properties (model, column = 2)

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

def create_window():
    v = create_clipping_page ()

    w = gtk.Window ()
    w.connect ("destroy", gtk.main_quit)
    w.add (v)
    w.show_all ()

    return w

def main ():
    window = create_window ()
    window = create_window ()

    gtk.main ()

if __name__ == "__main__":
    main ()
