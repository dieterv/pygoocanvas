import goocanvas
import gtk

def on_motion_notify (item, target, event):
    if target:
        item_id = target.get_data ("id")

    if item_id:
        print (("%s item received 'motion-notify' signal") % item_id)

    return False

def setup_item_signals (item):
    item.connect ("motion_notify_event", on_motion_notify)

def create_events_area (canvas, area_num, pointer_events, label):
    row = area_num / 3
    col = area_num % 3
    
    x = col * 200
    y = row * 150
    
    root = canvas.get_root_item ()

    dash = goocanvas.LineDash ([2.0, 5.0, 5.0])

    ''' Create invisible item. '''
    rect = goocanvas.Rect (parent = root,
                           x = x + 45,
                           y = y + 35,
                           width = 30,
                           height = 30,
                           fill_color = "red",
                           visibility = goocanvas.ITEM_INVISIBLE,
                           line_width = 5.0,
                           pointer_events = pointer_events)
    view_id = "%s invisible" % label
    rect.set_data ("id", view_id)
    setup_item_signals (rect)

    ''' Display a thin rect around it to indicate it is there. '''

    rect = goocanvas.Rect (parent = root,
                           x = x + 42.5, 
                           y = y + 32.5,
                           width =  36,
                           height = 36,
                           line_dash = dash,
                           line_width = 1.0,
                           stroke_color = "gray")

    ''' Create unpainted item. '''
    rect = goocanvas.Rect (parent = root,
                           x = x + 85,
                           y = y + 35,
                           width = 30,
                           height = 30,
                           line_width = 5.0,
                           pointer_events = pointer_events)
  
    view_id = "%s unpainted" % label
    rect.set_data ("id", view_id)
    setup_item_signals (rect)

    ''' Display a thin rect around it to indicate it is there. '''
    
    rect = goocanvas.Rect (parent = root,
                           x = x + 82.5,
                           y = y + 32.5,
                           width = 36,
                           height = 36,
                           line_dash = dash,
                           line_width = 1.0,
                           stroke_color = "gray")

    ''' Create stroked item. '''
    rect = goocanvas.Rect (parent = root,
                           x = x + 125,
                           y = y + 35,
                           width = 30,
                           height = 30,
                           line_width = 5.0,
                           pointer_events = pointer_events)
    view_id = "%s stroked" % label
    rect.set_data ("id", view_id)
    setup_item_signals (rect)

    ''' Create filled item. '''
    rect = goocanvas.Rect (parent = root,
                           x = x + 60,
                           y = y + 75,
                           width = 30,
                           height = 30,
                           fill_color = "red",
                           line_width = 5.0,
                           pointer_events = pointer_events)
    view_id = "%s filled" % label
    rect.set_data ("id", view_id)
    setup_item_signals (rect)

    ''' Create stroked & filled item. '''
    rect = goocanvas.Rect (parent = root,
                           x = x + 100,
                           y = y + 75,
                           width = 30,
                           height = 30,
                           fill_color = "red",
                           line_width = 5.0,
                           pointer_events = pointer_events)
    view_id = "%s stroked & filled" % label
    rect.set_data ("id", view_id)
    setup_item_signals (rect)

    goocanvas.Text (parent = root,
                    text = label,
                    x = x + 100,
                    y = y + 130,
                    width = -1,
                    anchor = gtk.ANCHOR_CENTER,
                    font = "Sans 12",
                    fill_color = "blue")
  
def create_events_page ():
    vbox = gtk.VBox (False, 4)
    vbox.set_border_width (4)

    ''' Instructions '''

    label = gtk.Label ("Move the mouse over the items to check they receive the right motion events.\nThe first 2 items in each group are 1) invisible and 2) visible but unpainted.")
    vbox.pack_start (label, False, False, 0)

    ''' Frame and canvas '''

    alignment = gtk.Alignment (0.5, 0.5, 0.0, 0.0)
    vbox.pack_start (alignment, False, False, 0)

    frame = gtk.Frame ()
    frame.set_shadow_type (gtk.SHADOW_IN)
    alignment.add (frame)

    canvas = goocanvas.Canvas ()

    canvas.set_size_request (600, 450)
    canvas.set_bounds (0, 0, 600, 450)
    frame.add (canvas)

    create_events_area (canvas, 0, goocanvas.EVENTS_NONE, "none");
    create_events_area (canvas, 1, goocanvas.EVENTS_VISIBLE_PAINTED, "visible-painted");
    create_events_area (canvas, 2, goocanvas.EVENTS_VISIBLE_FILL, "visible-fill");
    create_events_area (canvas, 3, goocanvas.EVENTS_VISIBLE_STROKE, "visible-stroke");
    create_events_area (canvas, 4, goocanvas.EVENTS_VISIBLE, "visible");
    create_events_area (canvas, 5, goocanvas.EVENTS_PAINTED, "painted");
    create_events_area (canvas, 6, goocanvas.EVENTS_FILL, "fill");
    create_events_area (canvas, 7, goocanvas.EVENTS_STROKE, "stroke");
    create_events_area (canvas, 8, goocanvas.EVENTS_ALL, "all");

    return vbox

def main ():
    vb = create_events_page ()
    
    win = gtk.Window()
    win.connect("destroy", gtk.main_quit)
    win.add(vb)
    win.show_all()
    
    gtk.main()

if __name__ == "__main__":
    main ()

