import goocanvas
import gtk

N_COLS = 5
N_ROWS = 20
PADDING = 10

def create_canvas_scalability ():
    vbox = gtk.VBox (False, 4)
    vbox.set_border_width (4)

    table = gtk.Table (2, 2, False)
    table.set_row_spacings (4)
    table.set_col_spacings (4)
    
    vbox.pack_start (table, True, True, 0)
    
    frame = gtk.Frame ()
    frame.set_shadow_type (gtk.SHADOW_IN)
    
    table.attach (frame,
                  0, 1,
                  0, 1,
                  gtk.EXPAND | gtk.FILL | gtk.SHRINK,
                  gtk.EXPAND | gtk.FILL | gtk.SHRINK,
                  0, 0)
    
    ''' Create the canvas and board '''

    pixbuf = gtk.gdk.pixbuf_new_from_file("../images/toroid.png")
    width = pixbuf.get_width () + 3
    height = pixbuf.get_height () +1
    
    canvas = goocanvas.Canvas ()

    root = canvas.get_root_item ()

    canvas.set_size_request (600, 450)
    canvas.set_bounds (0, 0,
                       N_COLS * (width + PADDING),
                       N_ROWS * (height + PADDING))

    scrolled_win = gtk.ScrolledWindow ()

    frame.add (scrolled_win)

    scrolled_win.add (canvas)

    for i in range (N_COLS):
        for j in range (N_ROWS):
            item = goocanvas.Image (parent =root,
                                    pixbuf = pixbuf,
                                    x = i * (width + PADDING),
                                    y = j * (height + PADDING))
    return vbox

def main ():
    win = gtk.Window()
    win.connect("destroy", gtk.main_quit)
    
    vbox = create_canvas_scalability ()
    
    win.add(vbox)
    win.show_all()
    
    gtk.main()

if __name__ == "__main__":
    main ()





