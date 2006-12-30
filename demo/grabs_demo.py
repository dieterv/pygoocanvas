import goocanvas
import gtk

def on_widget_expose (widget, event, item_id):
    print (("%s received 'expose' signal") % item_id)

    style = widget.props.style
    style.paint_box (widget.window,
                     gtk.STATE_NORMAL,
                     gtk.SHADOW_IN,
                     event.area,
                     widget,
                     None,
                     0,
                     0,
                     widget.allocation.width,
                     widget.allocation.height)

    return False

def on_widget_enter_notify (widget, event, item_id):
    print (("%s received 'enter-notify' signal") % item_id)
    return True

def on_widget_leave_notify (widget, event, item_id):
    print (("%s received 'leave-notify' signal") % item_id)
    return True

def on_widget_motion_notify (widget, event, item_id):
    print (("%s received 'motion-notify' signal (window: %s)") % (item_id, event.window))

    if event.is_hint:
        window = event.window
        window.get_pointer ()

    return True

def on_widget_button_press (widget, event, item_id):
    print (("%s received 'button-press' signal") % item_id)
    
    window = widget.window

    if "explicit" in item_id:
        mask = gtk.gdk.BUTTON_PRESS_MASK | gtk.gdk.BUTTON_RELEASE_MASK | gtk.gdk.POINTER_MOTION_MASK  | gtk.gdk.POINTER_MOTION_HINT_MASK | gtk.gdk.ENTER_NOTIFY_MASK | gtk.gdk.LEAVE_NOTIFY_MASK
        status = gtk.gdk.pointer_grab (window, False, mask, None, None, event.time)
        if status == gtk.gdk.GRAB_SUCCESS:
            print "grabbed pointer"
        else:
            print "pointer grab failed"

    return True

def on_widget_button_release (widget, event, item_id):
    print (("%s received 'button-release' signal") % item_id)
    if "explicit" in item_id:
        display = widget.get_display ()
        display.pointer_ungrab (event.time)
        print "released pointer grab"
    return True

def on_enter_notify (item, target, event):
    item_id = item.get_data ("id")

    print (("%s received 'enter-notify' signal") % item_id)
    return False

def on_leave_notify (item, target, event):
    item_id = item.get_data ("id")

    print (("%s received 'leave-notify' signal") % item_id)
    return False

def on_motion_notify (item, target, event):
    item_id = item.get_data ("id")

    print (("%s received 'motion-notify' signal") % item_id)
    return False

def on_button_press (item, target, event):
    
    item_id = item.get_data ("id")
    print (("%s received 'button-press' signal") % item_id)

    if "explicit" in item_id:
        mask = gtk.gdk.BUTTON_PRESS_MASK | gtk.gdk.BUTTON_RELEASE_MASK | gtk.gdk.POINTER_MOTION_MASK  | gtk.gdk.POINTER_MOTION_HINT_MASK | gtk.gdk.ENTER_NOTIFY_MASK | gtk.gdk.LEAVE_NOTIFY_MASK
        canvas = item.get_canvas ()
        status = canvas.pointer_grab (item, mask, None, event.time)
        if status == gtk.gdk.GRAB_SUCCESS:
            print "grabbed pointer"
        else:
            print "pointer grab failed"

    return False

def on_button_release (item, target, event):
    item_id = item.get_data ("id")

    print (("%s received 'button-release' signal") % item_id)

    if "explicit" in item_id:
        canvas = item.get_canvas ()
        canvas.pointer_ungrab (item, event.time)
        print ("released pointer grab")
    return False

def create_fixed (table, row, text, id):
    label = gtk.Label (text)
    table.attach (label, 0, 1, row, row + 1, 0, 0, 0, 0)

    fixed = gtk.Fixed ()
    fixed.set_has_window (True)
    fixed.set_events (gtk.gdk.EXPOSURE_MASK
                      | gtk.gdk.BUTTON_PRESS_MASK
                      | gtk.gdk.BUTTON_RELEASE_MASK
                      | gtk.gdk.POINTER_MOTION_MASK
                      | gtk.gdk.POINTER_MOTION_HINT_MASK
                      | gtk.gdk.KEY_PRESS_MASK
                      | gtk.gdk.KEY_RELEASE_MASK
                      | gtk.gdk.ENTER_NOTIFY_MASK
                      | gtk.gdk.LEAVE_NOTIFY_MASK
                      | gtk.gdk.FOCUS_CHANGE_MASK)
    fixed.set_size_request (200, 100)
    table.attach (fixed, 1, 2, row, row + 1, 0, 0, 0, 0)

    view_id = "%s-background" % id
    fixed.connect ("expose_event", on_widget_expose, view_id)
    fixed.connect ("enter_notify_event", on_widget_enter_notify, view_id)
    fixed.connect ("leave_notify_event", on_widget_leave_notify, view_id)
    fixed.connect ("motion_notify_event", on_widget_motion_notify, view_id)
    fixed.connect ("button_press_event", on_widget_button_press, view_id)
    fixed.connect ("button_release_event", on_widget_button_release, view_id)

    drawing_area = gtk.DrawingArea ()
    drawing_area.set_events (
             gtk.gdk.EXPOSURE_MASK
             | gtk.gdk.BUTTON_PRESS_MASK
             | gtk.gdk.BUTTON_RELEASE_MASK
             | gtk.gdk.POINTER_MOTION_MASK
             | gtk.gdk.POINTER_MOTION_HINT_MASK
             | gtk.gdk.KEY_PRESS_MASK
             | gtk.gdk.KEY_RELEASE_MASK
             | gtk.gdk.ENTER_NOTIFY_MASK
             | gtk.gdk.LEAVE_NOTIFY_MASK
             | gtk.gdk.FOCUS_CHANGE_MASK)
             
    drawing_area.set_size_request (60, 60)
    fixed.put (drawing_area, 20, 20)

    view_id = "%s-left" % id
    drawing_area.connect ("expose_event", on_widget_expose, view_id)
    drawing_area.connect ("enter_notify_event", on_widget_enter_notify, view_id)
    drawing_area.connect ("leave_notify_event", on_widget_leave_notify, view_id)
    drawing_area.connect ("motion_notify_event", on_widget_motion_notify, view_id)
    drawing_area.connect ("button_press_event", on_widget_button_press, view_id)
    drawing_area.connect ("button_release_event", on_widget_button_release, view_id)


    drawing_area = gtk.DrawingArea ()
    drawing_area.set_events (
             gtk.gdk.EXPOSURE_MASK
             | gtk.gdk.BUTTON_PRESS_MASK
             | gtk.gdk.BUTTON_RELEASE_MASK
             | gtk.gdk.POINTER_MOTION_MASK
             | gtk.gdk.POINTER_MOTION_HINT_MASK
             | gtk.gdk.KEY_PRESS_MASK
             | gtk.gdk.KEY_RELEASE_MASK
             | gtk.gdk.ENTER_NOTIFY_MASK
             | gtk.gdk.LEAVE_NOTIFY_MASK
             | gtk.gdk.FOCUS_CHANGE_MASK)
             
    drawing_area.set_size_request (60, 60)
    fixed.put (drawing_area, 120, 20)

    view_id = "%s-right" % id
    drawing_area.connect ("expose_event", on_widget_expose, view_id)
    drawing_area.connect ("enter_notify_event", on_widget_enter_notify, view_id)
    drawing_area.connect ("leave_notify_event", on_widget_leave_notify, view_id)
    drawing_area.connect ("motion_notify_event", on_widget_motion_notify, view_id)
    drawing_area.connect ("button_press_event", on_widget_button_press, view_id)
    drawing_area.connect ("button_release_event", on_widget_button_release, view_id)

def setup_item_signals (item):
  item.connect ("enter_notify_event", on_enter_notify)
  item.connect ("leave_notify_event", on_leave_notify)
  item.connect ("motion_notify_event", on_motion_notify)
  item.connect ("button_press_event", on_button_press)
  item.connect ("button_release_event", on_button_release)

def create_canvas (table, row, text, id):
    label = gtk.Label (text)
    table.attach (label, 0, 1, row, row + 1, 0, 0, 0, 0);

    canvas = goocanvas.Canvas ()

    canvas.set_size_request (200, 100)
    canvas.set_bounds (0, 0, 200, 100)
    table.attach (canvas, 1, 2, row, row + 1, 0, 0, 0, 0)

    root = canvas.get_root_item ()

    rect = goocanvas.Rect (parent = root,
                           x = 0,
                           y = 0,
                           width = 200,
                           height = 100,
                           fill_color = "yellow")
    view_id = "%s-yellow" % id
    rect.set_data ("id", view_id)
    setup_item_signals (rect)

    rect = goocanvas.Rect (parent = root,
                            x = 20,
                            y = 20,
                            width = 60,
                            height = 60,
                            fill_color = "blue")
    view_id = "%s-blue" % id
    rect.set_data ("id", view_id)
    setup_item_signals (rect)

    rect = goocanvas.Rect (parent = root,
                           x = 120,
                           y = 20,
                           width = 60,
                           height = 60,
                           fill_color = "red")
    view_id = "%s-red" % id
    rect.set_data ("id", view_id)
    setup_item_signals (rect)

def create_grabs_page ():
    table = gtk.Table (5, 2, False)
    table.set_border_width (12)
    table.set_row_spacings (12)
    table.set_col_spacings (12)

    label = gtk.Label ("Move the mouse over the widgets and canvas items on the right to see what events they receive.\nClick buttons to start explicit or implicit pointer grabs and see what events they receive now.\n(They should all receive the same events.)")
    table.attach (label, 0, 2, 0, 1, 0, 0, 0, 0)

    ''' Drawing area with explicit grabs. '''
    create_fixed (table, 1, "Widget with Explicit Grabs:", "widget-explicit")

    ''' Drawing area with implicit grabs. '''
    create_fixed (table, 2, "Widget with Implicit Grabs:", "widget-implicit")

    ''' Canvas with explicit grabs. '''
    create_canvas (table, 3, "Canvas with Explicit Grabs:", "canvas-explicit")

    ''' Canvas with implicit grabs. '''
    create_canvas (table, 4, "Canvas with Implicit Grabs:", "canvas-implicit")

    return table

def main ():
    win = gtk.Window()
    win.connect("destroy", gtk.main_quit)
    
    vbox = create_grabs_page ()
    
    win.add(vbox)
    win.show_all()
    
    gtk.main()

if __name__ == '__main__':
    main ()
