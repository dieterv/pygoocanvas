import gtk
import goocanvas
import cairo

LEFT = 50.0
RIGHT = 350.0
MIDDLE = 150.0
DEFAULT_WIDTH = 2
DEFAULT_SHAPE_A = 4
DEFAULT_SHAPE_B = 5
DEFAULT_SHAPE_C = 4

def set_dimension (canvas, arrow_name, text_name, x1, y1, x2, y2, tx, ty, dim):
    points = goocanvas.Points([(x1, y1), (x2, y2)])
    
    item = canvas.get_data(arrow_name)
    item.props.points = points
    
    item = canvas.get_data(text_name)
    item.props.text = str(dim)
    item.props.x = tx
    item.props.y = ty

def move_drag_box(item, x, y):
    item.props.x = x - 5.0
    item.props.y = y - 5.0
    
def set_arrow_shape(canvas):
    width = canvas.get_data("width")
    shape_a = canvas.get_data("shape_a")
    shape_b = canvas.get_data("shape_b")
    shape_c = canvas.get_data("shape_c")
    
    item = canvas.get_data("big_arrow")
    item.props.line_width = 10.0 * width
    item.props.arrow_tip_length = shape_a
    item.props.arrow_length = shape_b
    item.props.arrow_width = shape_c
    
    x1 = RIGHT - 10 * shape_a * width
    y1 = MIDDLE - 10 * width / 2
    x2 = RIGHT - 10 * shape_b * width
    y2 = MIDDLE - 10 * (shape_c * width / 2.0)
    x3 = RIGHT
    y3 = MIDDLE
    x4 = x2
    y4 = MIDDLE + 10 * (shape_c * width / 2.0)
    x5 = x1
    y5 = MIDDLE + 10 * width / 2
    
    points = goocanvas.Points([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)])
    
    item = canvas.get_data("outline")
    item.props.points = points
    
    move_drag_box(canvas.get_data("width_drag_box"), LEFT, MIDDLE - 10 * width / 2.0)
    move_drag_box (canvas.get_data("shape_a_drag_box"), RIGHT - 10 * shape_a * width, MIDDLE)
    move_drag_box (canvas.get_data("shape_b_c_drag_box"), RIGHT - 10 * shape_b * width,
                    MIDDLE - 10 * (shape_c * width / 2.0))

    set_dimension(canvas, "width_arrow", "width_text",
               LEFT - 10,
               MIDDLE - 10 * width / 2.0,
               LEFT - 10,
               MIDDLE + 10 * width / 2.0,
               LEFT - 15,
               MIDDLE,
               width)

    set_dimension (canvas, "shape_a_arrow", "shape_a_text",
               RIGHT - 10 * shape_a * width,
               MIDDLE + 10 * (shape_c * width / 2.0) + 10,
               RIGHT,
               MIDDLE + 10 * (shape_c * width / 2.0) + 10,
               RIGHT - 10 * shape_a * width / 2.0,
               MIDDLE + 10 * (shape_c * width / 2.0) + 15,
               shape_a)

    set_dimension (canvas, "shape_b_arrow", "shape_b_text",
               RIGHT - 10 * shape_b * width,
               MIDDLE + 10 * (shape_c * width / 2.0) + 35,
               RIGHT,
               MIDDLE + 10 * (shape_c * width / 2.0) + 35,
               RIGHT - 10 * shape_b * width / 2.0,
               MIDDLE + 10 * (shape_c * width / 2.0) + 40,
               shape_b)

    set_dimension (canvas, "shape_c_arrow", "shape_c_text",
               RIGHT + 10,
               MIDDLE - 10 * shape_c * width / 2.0,
               RIGHT + 10,
               MIDDLE + 10 * shape_c * width / 2.0,
               RIGHT + 15,
               MIDDLE,
               shape_c)

    item = canvas.get_data("width_info")
    item.props.text = "line-width: " + str(width)

    item = canvas.get_data("shape_a_info")
    item.props.text = "arrow-tip-length: " + str(shape_a) + " (* line-width)"

    item = canvas.get_data("shape_b_info")
    item.props.text = "arrow-length: " + str(shape_b) + " (* line-width)"
    
    item = canvas.get_data("shape_c_info")
    item.props.text = "arrow-width: " + str(shape_c) + " (* line-width)"
    
    item = canvas.get_data("sample_1")
    item.props.line_width = width
    item.props.arrow_tip_length = shape_a
    item.props.arrow_length = shape_b
    item.props.arrow_width = shape_c

    item = canvas.get_data("sample_2")
    item.props.line_width = width
    item.props.arrow_tip_length = shape_a
    item.props.arrow_length = shape_b
    item.props.arrow_width = shape_c

    item = canvas.get_data("sample_3")
    item.props.line_width = width
    item.props.arrow_tip_length = shape_a
    item.props.arrow_length = shape_b
    item.props.arrow_width = shape_c
    
def create_drag_box(canvas, root, box_name):
    item = goocanvas.Rect(parent = root, 
                         x=0, y=0, width=10, height=10,
                         fill_color="black",
                         stroke_color="black",
                         line_width=1.0)
    canvas.set_data(box_name, item)

    item.connect("enter_notify_event", on_enter_notify)
    item.connect("leave_notify_event", on_leave_notify)
    item.connect("button_press_event", on_button_press)
    item.connect("button_release_event", on_button_release)
    item.connect("motion_notify_event", on_motion)

def create_dimension(canvas, root, arrow_name, text_name, anchor):
    p3 = goocanvas.Polyline(parent = root,
                            fill_color="black", 
                            start_arrow=True, 
                            end_arrow=True)

    canvas.set_data(arrow_name, p3)

    text = goocanvas.Text(parent = root,
                          x=0, y=0, width=-1, anchor=anchor,
                    fill_color="black",
                    font="Sans 12")
    canvas.set_data(text_name, text)

def create_info(canvas, root, info_name, x, y):
    t = goocanvas.Text(parent = root, 
                       x=x, y=y, width=-1, 
                       anchor=gtk.ANCHOR_NW,
                       fill_color="black",
                       font="Sans 14")
    canvas.set_data(info_name, t)

def create_sample_arrow(canvas, root, sample_name, x1, x2, y1, y2):
    p4 = goocanvas.polyline_new_line(root, x1, x2, y1, y2,
                        start_arrow=True,
                        end_arrow=True)
    canvas.set_data(sample_name, p4)

def on_enter_notify(item, target, event):
    item.props.fill_color = "red"
    return True

def on_leave_notify(item, target, event):
    item.props.fill_color = "black"
    return True

def on_button_press(item, target, event):
    fleur = gtk.gdk.Cursor(gtk.gdk.FLEUR)
    canvas = item.get_canvas ()
    canvas.pointer_grab(item, 
                        gtk.gdk.POINTER_MOTION_MASK | gtk.gdk.BUTTON_RELEASE_MASK,
                        fleur, event.time)
    return True

def on_button_release(item, target, event):
    canvas = item.get_canvas ()
    canvas.pointer_ungrab(item, event.time)
    return True

def on_motion(item, target, event):
    canvas = item.get_canvas ()
    change = False
    if not event.state == gtk.gdk.BUTTON1_MASK:
        return False

    if item == canvas.get_data("width_drag_box"):
        y = event.y
        width = (MIDDLE - y) / 5
        if width < 0:
            return False
        canvas.set_data("width", width)
        set_arrow_shape (canvas)
    elif item == canvas.get_data("shape_a_drag_box"):
        x = event.x
        width = canvas.get_data("width")
        shape_a = (RIGHT - x) / 10 / width
        if shape_a < 0 or shape_a > 30:
            return False
        canvas.set_data("shape_a", shape_a)
        set_arrow_shape (canvas)
    elif item == canvas.get_data("shape_b_c_drag_box"):
        x = event.x
        width = canvas.get_data("width")
        shape_b = (RIGHT - x) / 10 / width
        if shape_b >= 0 and shape_b <= 30:
            canvas.set_data("shape_b", shape_b)
            change = True
        y = event.y
        shape_c = (MIDDLE - y) * 2 / 10 / width
        if shape_c >= 0:
            canvas.set_data("shape_c", shape_c)
            change = True
    if change:
        set_arrow_shape (canvas)
    return True

def create_canvas_arrowhead ():
    v = gtk.VBox(False, 4)
    v.set_border_width(4)
    
    l = gtk.Label("This demo allows you to edit arrowhead shapes.  Drag the little boxes\n"
            "to change the shape of the line and its arrowhead.  You can see the\n"
            "arrows at their normal scale on the right hand side of the window.")
    
    a = gtk.Alignment(0.5, 0.5, 0.0, 0.0)
    
    v.pack_start(l, False, False, 0)
    v.pack_start(a, True, True, 0)
    
    f = gtk.Frame()
    f.set_shadow_type(gtk.SHADOW_IN)
    
    a.add(f)
    
    canvas = goocanvas.Canvas()
    canvas.set_size_request(500, 350)
    canvas.set_bounds(0, 0, 500, 350)
    
    f.add(canvas)
    
    root = canvas.get_root_item()
    
    canvas.set_data("width", DEFAULT_WIDTH)
    canvas.set_data("shape_a", DEFAULT_SHAPE_A)
    canvas.set_data("shape_b", DEFAULT_SHAPE_B)
    canvas.set_data("shape_c", DEFAULT_SHAPE_C)
    
    p1 = goocanvas.polyline_new_line(root, LEFT, MIDDLE, RIGHT, MIDDLE, 
                    stroke_color="mediumseagreen",
                    end_arrow=True)
    
    canvas.set_data("big_arrow", p1)
    
    p2 = goocanvas.Polyline(parent = root,
                            close_path=True, 
                            stroke_color="black",
                            line_width=2.0,
                            line_cap=cairo.LINE_CAP_ROUND,
                            line_join=cairo.LINE_JOIN_ROUND)
    canvas.set_data("outline", p2)
    
    create_drag_box (canvas, root, "width_drag_box")
    create_drag_box (canvas, root, "shape_a_drag_box")
    create_drag_box (canvas, root, "shape_b_c_drag_box")
    
    create_dimension (canvas, root, "width_arrow", "width_text", gtk.ANCHOR_E)
    create_dimension (canvas, root, "shape_a_arrow", "shape_a_text", gtk.ANCHOR_N)
    create_dimension (canvas, root, "shape_b_arrow", "shape_b_text", gtk.ANCHOR_N)
    create_dimension (canvas, root, "shape_c_arrow", "shape_c_text", gtk.ANCHOR_W)
    
    create_info (canvas, root, "width_info", LEFT, 260)
    create_info (canvas, root, "shape_a_info", LEFT, 280)
    create_info (canvas, root, "shape_b_info", LEFT, 300)
    create_info (canvas, root, "shape_c_info", LEFT, 320)
    
    p_div = goocanvas.polyline_new_line(root, RIGHT + 50, 0, RIGHT + 50, 1000,
                                        fill_color="black", line_width=2.0)
    
    create_sample_arrow (canvas, root, "sample_1",
                     RIGHT + 100, 30, RIGHT + 100, MIDDLE - 30)
    
    create_sample_arrow (canvas, root, "sample_2",
                     RIGHT + 70, MIDDLE, RIGHT + 130, MIDDLE)
    
    create_sample_arrow (canvas, root, "sample_3",
                     RIGHT + 70, MIDDLE + 30, RIGHT + 130, MIDDLE + 120)
    
    set_arrow_shape(canvas)

    return v

def main ():
    v = create_canvas_arrowhead ()
    
    w = gtk.Window()
    w.connect("destroy", gtk.main_quit)   
    w.add(v)
    w.show_all()
    
    gtk.main()

if __name__ == "__main__":
    main()
