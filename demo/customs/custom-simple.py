### A custom item example

import sys
import gobject
import gtk
import goocanvas



class CustomRectItem(goocanvas.ItemSimple, goocanvas.Item):

    ## Note to read or modify the bounding box of ItemSimple use
    ## self.bounds_x1,x2,y1,y2

    def __init__(self, x, y, width, height, **kwargs):
        super(CustomRectItem, self).__init__(**kwargs)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def do_simple_create_path(self, cr):

        cr.rectangle(self.x, self.y, self.width, self.height)
        cr.move_to(self.x, self.y)
        cr.line_to(self.x + self.width, self.y + self.height)
        cr.move_to(self.x + self.width, self.y)
        cr.line_to(self.x, self.y + self.height)

    def do_button_press_event(self, target, event):
        print "button press!"

gobject.type_register(CustomRectItem)


def main(argv):
    window = gtk.Window()
    window.set_default_size(640, 600)
    window.show()
    window.connect("destroy", lambda w: gtk.main_quit())
    
    scrolled_win = gtk.ScrolledWindow()
    scrolled_win.set_shadow_type(gtk.SHADOW_IN)
    scrolled_win.show()
    window.add(scrolled_win)
    
    canvas = goocanvas.Canvas()
    canvas.set_size_request(600, 450)
    canvas.set_bounds(0, 0, 1000, 1000)

    root = canvas.get_root_item()

    CustomRectItem(x=100, y=100, width=400, height=400,
                   line_width=10, stroke_color="grey", parent=root)

    goocanvas.Text(text="Hello World",
                   x=300, y=300,
                   anchor=gtk.ANCHOR_CENTER,
                   font="Sans 24", parent=root).rotate(45, 300, 300)
    
    canvas.show()
    scrolled_win.add(canvas)
    

    gtk.main()



if __name__ == "__main__":
    main(sys.argv)
