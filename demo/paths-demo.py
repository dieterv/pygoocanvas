import gtk
import goocanvas
import cairo

def create_canvas_model():
    canvas_model = goocanvas.CanvasModelSimple()
    root = canvas_model.get_root_item()
    
    path = goocanvas.Path(data="M 20 20 L 40 40")
    root.add_child(path)
    
    path = goocanvas.Path(data="M30 20 l20, 20")
    root.add_child(path)
    
    path = goocanvas.Path(data="M 60 20 H 80")
    root.add_child(path)
    
    path = goocanvas.Path(data="M60 40 h20")
    root.add_child(path)
    
    path = goocanvas.Path(data="M 100,20 V 40")
    root.add_child(path)
    
    path = goocanvas.Path(data="M 120 20 v 20")
    root.add_child(path)
    
    path = goocanvas.Path(data="M 140 20 h20 v20 h-20 z")
    root.add_child(path)
    
    path = goocanvas.Path(data="M 180 20 h20 v20 h-20 z m 5,5 h10 v10 h-10 z",
                          fill_color="red", fill_rule=cairo.FILL_RULE_EVEN_ODD)
    root.add_child(path)
    
    path = goocanvas.Path(data="M 220 20 L 260 20 L 240 40 z",
                          fill_color="red", stroke_color="blue", line_width=3.0)
    root.add_child(path)
    
    path = goocanvas.Path(data="M20,100 C20,50 100,50 100,100 S180,150 180,100")
    root.add_child(path)
    
    path = goocanvas.Path(data="M220,100 c0,-50 80,-50 80,0 s80,50 80,0")
    root.add_child(path)
    
    path = goocanvas.Path(data="M20,200 Q60,130 100,200 T180,200")
    root.add_child(path)
    
    path = goocanvas.Path(data="M220,200 q40,-70 80,0 t80,0")
    root.add_child(path)
    
    path = goocanvas.Path(data="M200,500 h-150 a150,150 0 1,0 150,-150 z",
                          fill_color="red", stroke_color="blue", line_width=5.0)
    root.add_child(path)
    
    path = goocanvas.Path(data="M175,475 v-150 a150,150 0 0,0 -150,150 z",
                          fill_color="yellow", stroke_color="blue",
                          line_width=5.0)
    root.add_child(path)
    
    path = goocanvas.Path(data="M400,600 l 50,-25 " 
                          "a25,25 -30 0,1 50,-25 l 50,-25 "
                          "a25,50 -30 0,1 50,-25 l 50,-25 "
                          "a25,75 -30 0,1 50,-25 l 50,-25 "
			              "a25,100 -30 0,1 50,-25 l 50,-25",
			              stroke_color="red", line_width=5.0)
    root.add_child(path)
    
    path = goocanvas.Path(data="M 525,75 a100,50 0 0,0 100,50", 
                          stroke_color="red", line_width=5.0)
    root.add_child(path)
    
    path = goocanvas.Path(data="M 725,75 a100,50 0 0,1 100,50",
                          stroke_color="red", line_width=5.0)
    root.add_child(path)
    
    path = goocanvas.Path(data="M 525,200 a100,50 0 1,0 100,50",
                          stroke_color="red", line_width=5.0)
    root.add_child(path)
    
    path = goocanvas.Path(data="M 725,200 a100,50 0 1,1 100,50",
                          stroke_color="red", line_width=5.0)
    root.add_child(path)

    return canvas_model
    
win = gtk.Window()
win.connect("destroy", gtk.main_quit)

vbox = gtk.VBox(False, 4)
vbox.set_border_width(4)

scrolled = gtk.ScrolledWindow()
scrolled.set_shadow_type(gtk.SHADOW_IN)

vbox.add(scrolled)

canvas = goocanvas.CanvasView()
canvas.set_size_request(600, 450)
canvas.set_bounds(0, 0, 1000, 1000)

scrolled.add(canvas)

canvas_model = create_canvas_model()

canvas.set_model(canvas_model)

win.add(vbox)
win.show_all()

gtk.main()
