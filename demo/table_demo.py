import gtk
import goocanvas

DEMO_RECT_ITEM = 0
DEMO_TEXT_ITEM = 1
DEMO_WIDGET_ITEM = 2

def on_button_press (item, target, event):
    id = item.get_data ("id")
    if not id:
        id = "unknown"

    print ("%s received 'button-press' signal at %g, %g (root: %g, %g)") % (id , event.x, event.y, event.x_root, event.y_root)

    return True

def create_demo_item (table, demo_item_type, row, column, rows, columns, text):
    if demo_item_type == DEMO_RECT_ITEM:
        item = goocanvas.Rect (parent = table,
                               x = 0,
                               y = 0,
                               width = 38,
                               height = 19,
                               fill_color = "red")
    
    if demo_item_type == DEMO_TEXT_ITEM:
        item = goocanvas.Text (parent = table,
                               text = text, 
                               x = 0,
                               y = 0,
                               width = -1, 
                               anchor = gtk.ANCHOR_NW)
    
    if demo_item_type == DEMO_WIDGET_ITEM:
        widget = gtk.Button(label = text)
        item = goocanvas.Widget (parent = table, 
                                 widget = widget, 
                                 x = 0, 
                                 y = 0, 
                                 width = -1,
                                 height = -1)

    table.set_child_properties (item, 
                                row = row,
                                column = column,
                                rows = rows,
                                columns = columns,
                                x_expand = True,
                                x_fill = True,
                                y_expand = True,
                                y_fill = True)

    item.set_data ("id", text)
    item.connect ("button_press_event", on_button_press)

def create_table (parent, row, column, embedding_level, x, y, rotation, scale, demo_item_type):
    table = goocanvas.Table (parent = parent, 
                             row_spacing = 4.0,
                             column_spacing = 4.0)
  
    table.translate (x, y)
    table.rotate (rotation, 0, 0)
    table.scale (scale, scale)

    if row != -1:
        parent.set_child_properties (table, 
                                     row = row,
                                     column = column,
                                     x_expand = True,
                                     x_fill = True)
  
    if embedding_level:
        level = embedding_level - 1
        create_table (table, 0, 0, level, 50, 50, 0, 0.7, demo_item_type)
        create_table (table, 0, 1, level, 50, 50, 45, 1.0, demo_item_type)
        create_table (table, 0, 2, level, 50, 50, 90, 1.0, demo_item_type)
        create_table (table, 1, 0, level, 50, 50, 135, 1.0, demo_item_type)
        create_table (table, 1, 1, level, 50, 50, 180, 1.5, demo_item_type)
        create_table (table, 1, 2, level, 50, 50, 225, 1.0, demo_item_type)
        create_table (table, 2, 0, level, 50, 50, 270, 1.0, demo_item_type)
        create_table (table, 2, 1, level, 50, 50, 315, 1.0, demo_item_type)
        create_table (table, 2, 2, level, 50, 50, 360, 2.0, demo_item_type)
    else:
        create_demo_item (table, demo_item_type, 0, 0, 1, 1, "(0,0)")
        create_demo_item (table, demo_item_type, 0, 1, 1, 1, "(1,0)")
        create_demo_item (table, demo_item_type, 0, 2, 1, 1, "(2,0)")
        create_demo_item (table, demo_item_type, 1, 0, 1, 1, "(0,1)")
        create_demo_item (table, demo_item_type, 1, 1, 1, 1, "(1,1)")
        create_demo_item (table, demo_item_type, 1, 2, 1, 1, "(2,1)")
        create_demo_item (table, demo_item_type, 2, 0, 1, 1, "(0,2)")
        create_demo_item (table, demo_item_type, 2, 1, 1, 1, "(1,2)")
        create_demo_item (table, demo_item_type, 2, 2, 1, 1, "(2,2)")

    return table

def create_demo_table (root, x, y, width, height):
    table = goocanvas.Table (parent = root,
                             row_spacing = 4.0,
                             column_spacing = 4.0,
                             width = width,
                             height = height)
    
    table.translate (x, y)

    square = goocanvas.Rect (parent = table, 
                             x = 0.0, 
                             y = 0.0, width = 50.0, 
                             height = 50.0,
                             fill_color = "red")

    table.set_child_properties (square, 
                                row = 0,
                                column = 0,
                                x_shrink = True)
    
    square.set_data ("id", "Red square")
    square.connect ("button_press_event", on_button_press)
    
    circle = goocanvas.Ellipse (parent = table,
                                center_x = 0,
                                center_y = 0,
                                radius_x = 25,
                                radius_y = 25,
                                fill_color = "blue")

    table.set_child_properties (circle,
                                row = 0,
                                column = 1,
                                x_shrink = True)
    
    circle.set_data ("id", "Blue circle")
    circle.connect ("button_press_event", on_button_press)
  
    p = goocanvas.Points([(25, 0), (0, 50), (50, 50)])
    triangle = goocanvas.Polyline (parent = table, 
                                   close_path = True,
                                   points = p,
                                   fill_color = "yellow")

    table.set_child_properties (triangle,
                                row = 0,
                                column = 2,
                                x_shrink = True)
    
    triangle.set_data ("id", "Yellow triangle")
    triangle.connect ("button_press_event", on_button_press)

def create_width_for_height_table (root, x, y, width, height, rotation):

    text = "This is a long paragraph that will have to be split over a few \
           lines so we can see if its allocated height changes when its \
           allocated width is changed."

    table = goocanvas.Table (parent = root,
                             width = width,
                             height = height)

    table.translate (x, y)
    table.rotate (rotation, 0, 0)

    item = goocanvas.Rect (parent = table,
                           x = 0.0,
                           y = 0.0,
                           width = width - 2,
                           height = 10.0,
                           fill_color = "red")

    table.set_child_properties (item,
                                row = 0,
                                column = 0,
                                x_shrink = True)

    item = goocanvas.Text (parent = table,
                           text = text,
                           x = 0,
                           y = 0,
                           width = -1,
                           anchor = gtk.ANCHOR_NW)

    table.set_child_properties (item,
                                row = 1,
                                column = 0,
                                x_expand = True,
                                x_fill = True,
                                x_shrink = True,
                                y_expand = True,
                                y_fill = True)

    item.set_data ("id", "Text Item")
    item.connect ("button_press_event", on_button_press)

    item = goocanvas.Rect (parent = table,
                           x = 0.0,
                           y = 0.0,
                           width = width - 2,
                           height = 10.0,
                           fill_color = "red")
    
    table.set_child_properties (item,
                                row = 2,
                                column = 0,
                                x_shrink = True)

window = gtk.Window (gtk.WINDOW_TOPLEVEL)
window.set_default_size (640, 600)
window.connect ("delete_event", gtk.main_quit)
window.realize()

vbox = gtk.VBox (False, 4)
vbox.set_border_width (4)
window.add (vbox)

hbox = gtk.HBox (False, 4)
vbox.pack_start (hbox, False, False, 0)

scrolled_win = gtk.ScrolledWindow ()
scrolled_win.set_shadow_type (gtk.SHADOW_IN)
vbox.pack_start (scrolled_win, True, True, 0)

canvas = goocanvas.Canvas ()
canvas.flags () & gtk.CAN_FOCUS
canvas.set_size_request (600, 450)
canvas.set_bounds (0, 0, 1000, 2000)
scrolled_win.add (canvas)

root = canvas.get_root_item ()
  
create_demo_table (root, 400, 200, -1, -1)
create_demo_table (root, 400, 260, 100, -1)

create_table (root, -1, -1, 0, 10, 10, 0, 1.0, DEMO_TEXT_ITEM)
create_table (root, -1, -1, 0, 180, 10, 30, 1.0, DEMO_TEXT_ITEM)
create_table (root, -1, -1, 0, 350, 10, 60, 1.0, DEMO_TEXT_ITEM)
create_table (root, -1, -1, 0, 500, 10, 90, 1.0, DEMO_TEXT_ITEM)


table = create_table (root, -1, -1, 0, 30, 150, 0, 1.0, DEMO_TEXT_ITEM)
table.props.width = 300.0
table.props.height = 100.0

create_table (root, -1, -1, 1, 200, 200, 30, 0.8, DEMO_TEXT_ITEM)

table = create_table (root, -1, -1, 0, 10, 700, 0, 1.0, DEMO_WIDGET_ITEM)
table.props.width = 300.0
table.props.height = 200.0

create_width_for_height_table (root, 100, 1000, 200, -1, 0)
create_width_for_height_table (root, 100, 1200, 300, -1, 0)
create_width_for_height_table (root, 500, 1000, 200, -1, 30)
create_width_for_height_table (root, 500, 1200, 300, -1, 30)

window.show_all()

gtk.main ()
