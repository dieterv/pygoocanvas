import gtk
import goocanvas

def on_button_press(view, target, event):
    item = view.get_item()
    
    if event.button != 1:
        return False
    
    parent1 = item.get_data("parent1")
    parent2 = item.get_data("parent2")
    
    parent = item.get_parent()
    
    child_num = parent.find_child(item)
    
    parent.remove_child(child_num)
    
    if parent == parent1:
        parent2.add_child(item)
    else:
        parent1.add_child(item)

        return True

def on_item_view_created(view, item_view, item):
    if item.get_data("parent1"):
        item_view.connect("button-press-event", on_button_press)

win = gtk.Window()
win.connect("destroy", gtk.main_quit)

vb = gtk.VBox(False, 4)
vb.set_border_width(4)

label = gtk.Label("Reparent test:  click on the items to switch them between parents")

alignment = gtk.Alignment(0.5, 0.5, 0.0, 0.0)

frame = gtk.Frame()
frame.set_shadow_type(gtk.SHADOW_IN)

alignment.add(frame)

vb.pack_start(label, False, False, 0)
vb.pack_start(alignment, False, False, 0)

canvas = goocanvas.CanvasView()
canvas.connect("item-view-created", on_item_view_created)

canvas_model = goocanvas.CanvasModelSimple()

root = canvas_model.get_root_item()

canvas.set_size_request(400, 200)
canvas.set_bounds(0, 0, 300, 200)

frame.add(canvas)

parent1 = goocanvas.Group()

root.add_child(parent1)

rect = goocanvas.Rect(x=0, y=0, width=200, height=200, fill_color="tan")

parent1.add_child(rect)

parent2 = goocanvas.Group()
root.add_child(parent2)
parent2.translate(200, 0)

rect = goocanvas.Rect(x=0, y=0, width=200, height=200, fill_color="#204060")
parent2.add_child(rect)

ellipse = goocanvas.Ellipse(center_x=100, center_y=100, radius_x=90, radius_y=90,
                            stroke_color="black", fill_color="mediumseagreen",
                            line_width=3.0)

parent1.add_child(ellipse)

ellipse.set_data("parent1", parent1)
ellipse.set_data("parent2", parent2)

group = goocanvas.Group()
parent2.add_child(group)

group.translate(100, 100)

ellipse = goocanvas.Ellipse(center_x=0, center_y=0, radius_x=50, radius_y=50, 
                            stroke_color="black", fill_color="wheat", 
                            line_width=3.0)

group.add_child(ellipse)

ellipse = goocanvas.Ellipse(center_x=0, center_y=0, radius_x=25, radius_y=25, 
                            fill_color="steelblue")

group.add_child(ellipse)

group.set_data("parent1", parent1)
group.set_data("parent2", parent2)

canvas.set_model(canvas_model)

win.add(vb)
win.show_all()

gtk.main()
