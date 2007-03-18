import gtk
import goocanvas
import cairo
from time import clock

''' disclaimer ...sorry for all those globals... '''

N_GROUP_COLS = 25
N_GROUP_ROWS = 20
N_COLS = 10
N_ROWS = 10
ITEM_WIDTH = 400
PADDING = 10

ids = []
total_items = 0
left_offset = 0
top_offset = 0
total_width = 0
total_height = 0
start = 0
first_time = True

def on_motion_notify (item, target, event):
    id = item.get_data ("id")

    if id:
        print "%s item received 'motion-notify' signal" % id
    else:
        print "unknown"

    return False

def setup_canvas (canvas):
    global ids, total_items
    global left_offset, top_offset
    global total_height, total_width
    
    root = canvas.get_root_item ()
    root.props.font = "Sans 8"

    pixbuf = None
    item_width = ITEM_WIDTH
    item_height = 19
	
    cell_width = item_width + PADDING * 2
    cell_height = item_height + PADDING * 2

    group_width = N_COLS * cell_width
    group_height = N_ROWS * cell_height

    total_width = N_GROUP_COLS * group_width
    total_height = N_GROUP_ROWS * group_height

    # We use -ve offsets to test if -ve coords are handled correctly.
    left_offset = -total_width / 2
    top_offset = -total_height / 2

    style = goocanvas.Style ()
    color = gtk.gdk.color_parse ("mediumseagreen")
    pattern = cairo.SolidPattern (color.red / 65535.0,
                                  color.green / 65535.0,
                                  color.blue / 65535.0)
    style.set_style_property ("GooCanvasStyle:fill_pattern", pattern)

    style2 = goocanvas.Style ()
    color = gtk.gdk.color_parse ("steelblue")
    pattern = cairo.SolidPattern (color.red / 65535.0,
                                  color.green / 65535.0,
                                  color.blue / 65535.0)
    style2.set_style_property ("GooCanvasStyle:fill_pattern", pattern)
    
    id_item_num = 0
    
    for group_i in range (N_GROUP_COLS):
        for group_j in range (N_GROUP_ROWS):
            group_x = left_offset + (group_i * group_width)
            group_y = top_offset + (group_j * group_height)

            group = goocanvas.Group (parent = root)
            total_items += 1
            group.translate (group_x, group_y)

            for i in range (N_COLS):
                for j in range (N_ROWS):
                    item_x = (i * cell_width) + PADDING
                    item_y = (j * cell_height) + PADDING
                    rotation = i % 10 * 2
                    rotation_x = item_x + item_width / 2
                    rotation_y = item_y + item_height / 2

                    ids.append([(group_x + item_x), (group_y + item_y)])

                    item = goocanvas.Rect (parent = group,
                                           x = item_x,
                                           y = item_y,
                                           width = item_width,
                                           height = item_height)
                    if j % 2:
                        item.set_style (style)
                    else:
                        item.set_style (style2)
                    
                    item.rotate (rotation, rotation_x, rotation_y)
                    item.set_data ("id", ids[-1])

                    item.connect ("motion_notify_event", on_motion_notify)

                    item = goocanvas.Text (parent = group,
                                           text = ids[id_item_num],
                                           x = item_x + item_width / 2,
                                           y = item_y + item_height / 2,
                                           width = -1,
                                           anchor = gtk.ANCHOR_CENTER)

                    item.rotate (rotation, rotation_x, rotation_y)
                    
                    id_item_num += 1
                    total_items += 2

def on_expose_event (canvas, event):
    global start, first_time
    
    if first_time:
        print ("Update Canvas Time Used: %g" % (clock() - start))
        first_time = False
    
    return False

def create_canvas ():
    global start
    
    canvas = goocanvas.Canvas ()
    canvas.set_size_request (600, 450)

    start = clock()
    setup_canvas (canvas)
    print "Create Canvas Time Used: %g" % (clock() - start)

    start = clock()
    canvas.set_bounds (left_offset, top_offset, left_offset + total_width,
                       top_offset + total_height)
    canvas.show ()
    canvas.connect ("expose_event", on_expose_event)

    return canvas

window = gtk.Window (gtk.WINDOW_TOPLEVEL)
window.set_default_size (640, 600)
window.show ()
window.connect ("delete_event", gtk.main_quit)

scrolled_win = gtk.ScrolledWindow ()
scrolled_win.show ()
window.add (scrolled_win)

canvas = create_canvas ()
scrolled_win.add (canvas)

print "Total items: %d" % total_items

gtk.main ()
