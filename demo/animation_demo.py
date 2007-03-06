import goocanvas
import gtk

ellipse1 = None
ellipse2 = None
rect1 = None
rect2 = None
rect3 = None
rect4 = None

def start_animation_clicked (button):
    global ellipse1, ellipse2, rect1, rect2, rect3, rect4
    
    # Absolute.
    ellipse1.set_simple_transform (100, 100, 1, 0)
    ellipse1.animate (500, 100, 2, 720, True,
                      2000, 40, goocanvas.ANIMATE_BOUNCE)
    
    rect1.set_simple_transform (100, 200, 1, 0)
    rect1.animate (100, 200, 1, 350, True,
                   40 * 36, 40, goocanvas.ANIMATE_RESTART)

    rect3.set_simple_transform (200, 200, 1, 0)
    rect3.animate (200, 200, 3, 0, True,
                   400, 40, goocanvas.ANIMATE_BOUNCE)

    # Relative.
    ellipse2.set_simple_transform (100, 400, 1, 0)
    ellipse2.animate (400, 0, 2, 720, False,
                      2000, 40, goocanvas.ANIMATE_BOUNCE)

    rect2.set_simple_transform (100, 500, 1, 0)
    rect2.animate (0, 0, 1, 350, False,
                   40 * 36, 40, goocanvas.ANIMATE_RESTART)

    rect4.set_simple_transform (200, 500, 1, 0)
    rect4.animate (0, 0, 3, 0, False,
                   400, 40, goocanvas.ANIMATE_BOUNCE)


def stop_animation_clicked (button):
    global ellipse1, ellipse2, rect1, rect2, rect3, rect4
    
    ellipse1.stop_animation ()
    ellipse2.stop_animation ()
    rect1.stop_animation ()
    rect2.stop_animation ()
    rect3.stop_animation ()
    rect4.stop_animation ()

def setup_canvas (canvas):
    global ellipse1, ellipse2, rect1, rect2, rect3, rect4
    
    root = canvas.get_root_item ()

    # Absolute.
    ellipse1 = goocanvas.Ellipse (parent = root,
                                  center_x = 0,
                                  center_y = 0,
                                  radius_x = 25,
                                  radius_y = 15,
                                  fill_color = "blue")
    ellipse1.translate (100, 100)

    rect1 = goocanvas.Rect (parent = root,
                            x = -10,
                            y = -10,
                            width = 20,
                            height = 20,
                            fill_color = "blue")
    rect1.translate (100, 200)

    rect3 = goocanvas.Rect (parent = root,
                            x = -10,
                            y = -10,
                            width = 20,
                            height = 20,
                            fill_color = "blue")
    rect3.translate (200, 200)
    
    # Relative.
    ellipse2 = goocanvas.Ellipse (parent = root,
                                  center_x = 0,
                                  center_y = 0,
                                  radius_x = 25,
                                  radius_y = 15,
                                  fill_color = "red")
    ellipse2.translate (100, 400)

    rect2 = goocanvas.Rect (parent = root,
                            x = -10,
                            y = -10,
                            width = 20,
                            height = 20,
                            fill_color = "red")
    rect2.translate (100, 500)

    rect4 = goocanvas.Rect (parent = root,
                            x = -10,
                            y = -10,
                            width = 20,
                            height = 20,
                            fill_color = "red")
    rect4.translate (200, 500)

def create_animation_page ():
    vbox = gtk.VBox (False, 4)
    vbox.set_border_width (4)

    hbox = gtk.HBox (False, 4)
    vbox.pack_start (hbox, False, False, 0)

    w = gtk.Button ("Start Animation")
    hbox.pack_start (w, False, False, 0)
    w.connect ("clicked", start_animation_clicked, )
    
    w = gtk.Button ("Stop Animation")
    hbox.pack_start (w, False, False, 0)
    w.connect ("clicked", stop_animation_clicked, )

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
    v = create_animation_page ()
    
    w = gtk.Window()
    w.connect("destroy", gtk.main_quit)   
    w.add(v)
    w.show_all()
    
    gtk.main()

if __name__ == "__main__":
    main()
