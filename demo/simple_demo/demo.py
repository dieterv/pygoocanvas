import goocanvas
import gtk, cairo, pango
import array, math
import fifteen_demo, arrowhead_demo, features_demo
import paths_demo, scalability_demo, grabs_demo
import events_demo, focus_demo, clipping_demo
import animation_demo

class MyCanvas(object):
    def __init__(self):
        self.last_state = 0
        self.dragging = False
        self.VERTICES  = 10
        self.RADIUS = 60
        self.SCALE = 7
        self.drag_x = 0
        self.drag_y = 0

        window = gtk.Window (gtk.WINDOW_TOPLEVEL)
        window.set_default_size (640, 600)
        window.connect("destroy", gtk.main_quit)

        notebook = gtk.Notebook()
        window.add(notebook)

        notebook.append_page(self.create_canvas_primitives (), gtk.Label("Primitives"))
        notebook.append_page(arrowhead_demo.create_canvas_arrowhead (), gtk.Label("Arrowhead"))
        notebook.append_page(fifteen_demo.create_canvas_fifteen (), gtk.Label("Fifteen"))
        notebook.append_page(features_demo.create_canvas_features (), gtk.Label("Features"))
        notebook.append_page(scalability_demo.create_canvas_scalability (), gtk.Label("Scalability"))
        notebook.append_page(grabs_demo.create_grabs_page (), gtk.Label("Grabs"))
        notebook.append_page(events_demo.create_events_page (), gtk.Label("Events"))
        notebook.append_page(paths_demo.create_paths_page (), gtk.Label("Paths"))
        notebook.append_page(focus_demo.create_focus_page (), gtk.Label("Focus"))
        notebook.append_page(animation_demo.create_animation_page (), gtk.Label("Animation"))
        notebook.append_page(clipping_demo.create_clipping_page (), gtk.Label("Clipping"))
        window.show_all()

    def main(self):
        gtk.main()

    def zoom_changed (self, adj, canvas):
        canvas.set_scale (adj.get_value())

    def center_toggled (button, data):
        pass
    
    def anchor_toggled (self, button, canvas):
        anchor = button.get_data("anchor")
        canvas.props.anchor = anchor
        
    def scroll_to_50_50_clicked (self, button, canvas):
        canvas.scroll_to (50, 50)
    
    def scroll_to_250_250_clicked (self, button, canvas):
        canvas.scroll_to (250, 250)
    
    def scroll_to_500_500_clicked (self, button, canvas):
        canvas.scroll_to (500, 500)
        
    def animate_ellipse_clicked (self, button, canvas):
        self.ellipse2.animate (100, 100, 1, 90, True, 1000, 40,
                               goocanvas.ANIMATE_BOUNCE)
    
    def stop_animation_clicked (self, button, canvas):
        self.ellipse2.stop_animation()
    
    def move_ellipse_clicked (self, button, canvas):
        if self.last_state == 0:
            self.ellipse2.props.center_x = 300
            self.ellipse2.props.center_y = 70
            self.ellipse2.props.radius_x = 45
            self.ellipse2.props.radius_y = 30
            self.ellipse2.props.fill_color = "red"
            self.ellipse2.props.stroke_color = "midnightblue"
            self.ellipse2.props.line_width = 4
            self.ellipse2.props.title = "A red ellipse"
            self.last_state = 1
        elif self.last_state == 1:
            self.ellipse2.props.center_x = 390
            self.ellipse2.props.center_y = 150
            self.ellipse2.props.radius_x = 45
            self.ellipse2.props.radius_y = 40
            self.ellipse2.props.fill_color = "brown"
            self.ellipse2.props.stroke_color = "midnightblue"
            self.ellipse2.props.line_width = 4
            self.ellipse2.props.title = "A brown ellipse"
            self.last_state = 2
        elif self.last_state == 2:
            self.ellipse2.props.center_x = 335
            self.ellipse2.props.center_y = 70
            self.ellipse2.props.radius_x = 45
            self.ellipse2.props.radius_y = 30
            self.ellipse2.props.fill_color = "purple"
            self.ellipse2.props.stroke_color = "midnightblue"
            self.ellipse2.props.line_width = 4
            self.ellipse2.props.title = "A purple ellipse"
            self.last_state = 0
    
    def setup_item_signals (self, item):
        item.connect ("motion_notify_event", self.on_motion_notify)
        item.connect ("button_press_event", self.on_button_press)
        item.connect ("button_release_event", self.on_button_release)

    def on_motion_notify (self, item, target, event):
        if (self.dragging == True) and (event.state & gtk.gdk.BUTTON1_MASK):
            new_x = event.x
            new_y = event.y
            item.translate (new_x - self.drag_x, new_y - self.drag_y)
        return True
    
    def on_button_press (self, item, target, event):
        if event.button == 1:
            if event.state & gtk.gdk.SHIFT_MASK:
                parent = item.get_parent()
                child_num = parent.find_child (item)
                parent.remove_child (child_num)
            else:
                self.drag_x = event.x
                self.drag_y = event.y

                fleur = gtk.gdk.Cursor (gtk.gdk.FLEUR)
                canvas = item.get_canvas ()
                canvas.pointer_grab (item,
                                     gtk.gdk.POINTER_MOTION_MASK | gtk.gdk.BUTTON_RELEASE_MASK,
                                     fleur,
                                     event.time)
                self.dragging = True
        elif event.button == 2:
            item.lower(None)
        elif event.button == 3:
            item.raise_(None)
        return True

    def on_button_release (self, item, target, event):
        canvas = item.get_canvas ()
        canvas.pointer_ungrab (item, event.time)
        self.dragging = False
    
    def on_background_button_press (self, item, target, event):
        print "background received 'button-press' signal"
        return True

    def create_canvas_primitives (self):
        bg_color = gtk.gdk.Color (50000, 50000, 65535, 0)
        
        vbox = gtk.VBox (False, 4)
        vbox.set_border_width (4)
        
        w = gtk.Label ("Drag an item with button 1.  Click button 2 on an item to lower it, or button 3 to raise it.")
        
        hbox = gtk.HBox (False, 4)
        
        vbox.pack_start (w, False, False, 0)
        vbox.pack_start (hbox, False, False, 0)
        
        ''' Create the canvas'''   
        
        canvas = goocanvas.Canvas()
        canvas.modify_base (gtk.STATE_NORMAL, bg_color)
        canvas.set_bounds (0, 0, 604, 454)
        
        ''' Zoom '''
        
        w = gtk.Label ("Zoom:")
        
        hbox.pack_start (w, False, False, 0)
        
        adj = gtk.Adjustment (1.00, 0.05, 100.00, 0.05, 0.50, 0.50)
        adj.connect("value_changed", self.zoom_changed, canvas)
        
        w = gtk.SpinButton (adj, 0.0, 2)
        w.set_size_request (50, -1)
        
        hbox.pack_start (w, False, False, 0)
        
        ''' Center '''
        
        w = gtk.CheckButton("Center scroll region")
        
        hbox.pack_start (w, False, False, 0)
        
        w.connect ("toggled", self.center_toggled, canvas)
    
        ''' Move Ellipse '''
    
        w = gtk.Button ("Move Ellipse")
        hbox.pack_start (w, False, False, 0)
        w.connect ("clicked", self.move_ellipse_clicked, canvas)
    
        ''' Animate Ellipse '''
    
        w = gtk.Button ("Animate Ellipse")
        hbox.pack_start (w, False, False, 0)
        w.connect ("clicked", self.animate_ellipse_clicked, canvas)
        
        ''' Stop Animation '''
    
        w = gtk.Button ("Stop Animation")
        hbox.pack_start (w, False, False, 0)
        w.connect ("clicked", self.stop_animation_clicked, canvas)
        
    
        if cairo.HAS_PDF_SURFACE:
            '''Create PDF '''
    
            w = gtk.Button ("Write PDF")
            hbox.pack_start (w, False, False, 0)
            w.connect ("clicked", self.write_pdf_clicked, canvas)
    
        hbox = gtk.HBox (False, 4)
        vbox.pack_start (hbox, False, False, 0)
    
        ''' Scroll to '''
    
        w = gtk.Label ("Scroll To:")
        hbox.pack_start (w, False, False, 0)
    
        w = gtk.Button ("50,50")
        hbox.pack_start (w, False, False, 0)
        w.connect ("clicked", self.scroll_to_50_50_clicked, canvas)
    
        w = gtk.Button ("250,250")
        hbox.pack_start (w, False, False, 0)
        w.connect ("clicked", self.scroll_to_250_250_clicked, canvas)
    
        w = gtk.Button ("500,500")
        hbox.pack_start (w, False, False, 0)
        w.connect ("clicked", self.scroll_to_500_500_clicked, canvas)
    
        ''' Scroll anchor '''
    
        w = gtk.Label ("Anchor:")
        hbox.pack_start (w, False, False, 0)
    
        group = gtk.RadioButton (None, "NW")
        hbox.pack_start (group, False, False, 0)
        group.connect ("toggled", self.anchor_toggled, canvas)
        group.set_data ("anchor", gtk.ANCHOR_NW)
    
        w = gtk.RadioButton (group, "N")
        hbox.pack_start (w, False, False, 0)
        w.connect ("toggled", self.anchor_toggled, canvas)
        w.set_data ("anchor", gtk.ANCHOR_N)
    
        w = gtk.RadioButton (group, "NE")
        hbox.pack_start (w, False, False, 0)
        w.connect ("toggled", self.anchor_toggled, canvas)
        w.set_data ("anchor", gtk.ANCHOR_NE)
    
        w = gtk.RadioButton (group, "W")
        hbox.pack_start (w, False, False, 0)
        w.connect ("toggled", self.anchor_toggled, canvas)
        w.set_data ("anchor", gtk.ANCHOR_W)
    
        w = gtk.RadioButton (group, "C")
        hbox.pack_start (w, False, False, 0)
        w.connect ("toggled", self.anchor_toggled, canvas)
        w.set_data ("anchor", gtk.ANCHOR_CENTER)
    
        w = gtk.RadioButton (group, "E")
        hbox.pack_start (w, False, False, 0)
        w.connect ("toggled", self.anchor_toggled, canvas)
        w.set_data ("anchor", gtk.ANCHOR_E)
    
        w = gtk.RadioButton (group, "SW")
        hbox.pack_start (w, False, False, 0)
        w.connect ("toggled", self.anchor_toggled, canvas)
        w.set_data ("anchor", gtk.ANCHOR_SW)
    
        w = gtk.RadioButton (group, "S")
        hbox.pack_start (w, False, False, 0)
        w.connect ("toggled", self.anchor_toggled, canvas)
        w.set_data ("anchor", gtk.ANCHOR_S)
    
        w = gtk.RadioButton (group, "SE")
        hbox.pack_start (w, False, False, 0)
        w.connect ("toggled", self.anchor_toggled, canvas)
        w.set_data ("anchor", gtk.ANCHOR_SE)
    
        
        ''' Layout the stuff '''
    
        scrolled_win = gtk.ScrolledWindow ()
        vbox.pack_start (scrolled_win, True, True, 0)
    
        scrolled_win.add(canvas)
    
        ''' Add all the canvas items. '''
        self.setup_canvas (canvas)
    
        return vbox

    def write_pdf_clicked (self, button, canvas):
        print "In write_pdf_clicked"

        surface = cairo.PDFSurface ("demo.pdf", 9 * 72, 10 * 72)
        cr = cairo.Context (surface)

        ''' Place it in the middle of our 9x10 page. '''
        cr.translate (20, 130)

        canvas.render (cr, None, 1.0)

        cr.show_page ()
    
    def setup_heading (self, root, text, pos):
        x = (pos % 3) * 200 + 100
        y = (pos / 3) * 150 + 5
        
        item = goocanvas.Text (text=text, 
                               x=x, 
                               y=y, 
                               width=-1,
                               anchor=gtk.ANCHOR_N,
                               font = "Sans 12")
        item.skew_y (30, x, y)
    
    def setup_divisions (self, root):
        group = goocanvas.Group (parent = root)
        group.translate (2, 2)
        
        item = goocanvas.Rect (parent = group,
                               x = 0,
                               y = 0,
                               width = 600,
                               height = 450,
                               line_width = 4.0)
        
        item = goocanvas.polyline_new_line (group, 0, 150, 600, 150,
                                            line_width = 4.0)
        
        item = goocanvas.polyline_new_line (group, 0, 300, 600, 300,
                                            line_width = 4.0)
        
        item = goocanvas.polyline_new_line (group, 200, 0, 200, 450,
                                            line_width = 4.0)
        
        item = goocanvas.polyline_new_line (group, 400, 0, 400, 450,
                                            line_width = 4.0)
        
        self.setup_heading(group, "Rectangles", 0)
        self.setup_heading(group, "Ellipses", 1)
        self.setup_heading(group, "Texts", 2)
        self.setup_heading(group, "Images", 3)
        self.setup_heading(group, "Lines", 4)
        self.setup_heading(group, "Polygons", 7)

    def create_stipple (self, color_name, stipple_data):
        color = gtk.gdk.color_parse (color_name)
        stipple_data[2] = stipple_data[14] = color.red >> 8
        stipple_data[1] = stipple_data[13] = color.green >> 8
        stipple_data[0] = stipple_data[12] = color.blue >> 8
        surface = cairo.ImageSurface.create_for_data (stipple_data, cairo.FORMAT_ARGB32, 2, 2, 8)
        pattern = cairo.SurfacePattern(surface)
        pattern.set_extend (cairo.EXTEND_REPEAT)
    
        return pattern    
    
    def setup_rectangles (self, root):
        stipple_data = array.array('i', [0, 0, 0, 255,   0, 0, 0, 0,   
                                         0, 0, 0, 0,   0, 0, 0, 255])
        
        item = goocanvas.Rect (parent = root,
                               x = 20,
                               y = 30,
                               width = 50,
                               height = 30,
                               stroke_color = "red",
                               line_width = 8.0)
        self.setup_item_signals (item)
        
        pattern = self.create_stipple ("mediumseagreen", stipple_data)
        item = goocanvas.Rect (parent = root,
                               x = 90,
                               y = 40,
                               width =  90,
                               height =  60,
                               fill_pattern = pattern,
                               stroke_color = "black",
                               line_width = 4.0)
        self.setup_item_signals (item)
        
        item = goocanvas.Rect (parent = root,
                               x = 10,
                               y = 80,
                               width = 70,
                               height = 60,
                               fill_color = "steelblue")
        self.setup_item_signals (item)
    
        item = goocanvas.Rect (parent = root,
                               x = 20,
                               y = 90,
                               width = 70,
                               height = 60,
                               fill_color_rgba = 0x3cb37180,
                               stroke_color = "blue",
                               line_width = 2.0)
        self.setup_item_signals (item)
    
        item = goocanvas.Rect (parent = root,
                               x = 110,
                               y = 80,
                               width = 50,
                               height = 30,
                               radius_x = 20.0,
                               radius_y = 10.0,
                               stroke_color = "yellow",
                               fill_color_rgba = 0x3cb3f180)
        self.setup_item_signals (item)
    
        item = goocanvas.Rect (parent = root,
                               x = 30,
                               y = 20,
                               width = 50,
                               height = 30,
                               fill_color = "yellow")
        self.setup_item_signals (item)
        
    def setup_ellipses (self, root):
        stipple_data = array.array('i', [0, 0, 0, 255,   0, 0, 0, 0,   
                                         0, 0, 0, 0,   0, 0, 0, 255])
        ellipse1 = goocanvas.Ellipse (parent = root,
                                      center_x = 245,
                                      center_y = 45,
                                      radius_x = 25,
                                      radius_y = 15,
                                      stroke_color = "goldenrod",
                                      line_width = 8.0)
        self.setup_item_signals (ellipse1)
        
        self.ellipse2 = goocanvas.Ellipse (parent = root,
                                           center_x = 335,
                                           center_y = 70,
                                           radius_x = 45,
                                           radius_y = 30,
                                           fill_color = "wheat",
                                           stroke_color = "midnightblue",
                                           line_width = 4.0,
                                           title = "An ellipse")
        self.setup_item_signals (self.ellipse2)
        
        pattern = self.create_stipple ("cadetblue", stipple_data)
        ellipse3 = goocanvas.Ellipse (parent = root,
                                      center_x = 245,
                                      center_y = 110,
                                      radius_x = 35,
                                      radius_y = 30,
                                      fill_pattern = pattern,
                                      stroke_color = "black",
                                      line_width = 1.0)
        self.setup_item_signals (ellipse3)    

    def polish_diamond (self, root):
        group = goocanvas.Group (parent = root,
                                 line_width = 1.0,
                                 line_cap = cairo.LINE_CAP_ROUND)
        group.translate (270, 230)
        self.setup_item_signals (group)
        
        i = 0
        while i < self.VERTICES:
            a = 2.0 * math.pi * i / self.VERTICES
            x1 = self.RADIUS * math.cos (a)
            y1 = self.RADIUS * math.sin (a)
            i += 1
            j = i+1
            while j < self.VERTICES:
                a = 2.0 * math.pi * j / self.VERTICES
                x2 = self.RADIUS * math.cos (a)
                y2 = self.RADIUS * math.sin (a)
                item = goocanvas.polyline_new_line (group, x1, y1, x2, y2)
                j += 1

    def make_hilbert (self, root):
        '''hilbert = "urdrrulurulldluuruluurdrurddldrrruluurdrurddldrddlulldrdldrrurd"
        stipple_data = array.array('i', [0, 0, 0, 255,   0, 0, 0, 0,   
                                         0, 0, 0, 0,   0, 0, 0, 255])
        points = goocanvas.Poiints([(340, 290),])
        pp = len(hilbert)+1
        p = pp*2'''
        pass
    
    def setup_lines (self, root):
        self.polish_diamond (root)
        self.make_hilbert (root)
        
        ''' Arrow tests '''
        p = goocanvas.Points ([(340.0, 170.0), (340.0, 230.0), 
                                    (390.0, 230.0), (390.0, 170.0)])
        polyline1 = goocanvas.Polyline (parent = root,
                                        points = p,
                                        close_path = False,
                                        stroke_color = "midnightblue",
                                        line_width = 3.0,
                                        start_arrow = True,
                                        end_arrow = True,
                                        arrow_tip_length =3.0,
                                        arrow_length = 4.0,
                                        arrow_width = 3.5)
        self.setup_item_signals (polyline1)
        
        p = goocanvas.Points ([(356.0, 180.0), (374.0, 220.0)])
        polyline2 = goocanvas.Polyline (parent = root,
                                        points = p,
                                        close_path = False,
                                        stroke_color = "blue",
                                        line_width = 1.0,
                                        start_arrow = True,
                                        end_arrow = True,
                                        arrow_tip_length =5.0,
                                        arrow_length = 6.0,
                                        arrow_width = 6.5)
        self.setup_item_signals (polyline2)
        
        p = goocanvas.Points ([(356.0, 220.0), (374.0, 180.0)])
        polyline3 = goocanvas.Polyline (parent = root,
                                        points = p,
                                        close_path = False,
                                        stroke_color = "blue",
                                        line_width = 1.0,
                                        start_arrow = True,
                                        end_arrow = True,
                                        arrow_tip_length =5.0,
                                        arrow_length = 6.0,
                                        arrow_width = 6.5)
        self.setup_item_signals (polyline3)

        ''' Test polyline without any coords. '''
        polyline4 = goocanvas.Polyline (parent = root)
        self.setup_item_signals (polyline4)

        ''' Test polyline with 1 coord and arrows. '''
        p = goocanvas.Points ([(356.0, 220.0),])
        polyline5 = goocanvas.Polyline (parent = root,
                                        points = p,
                                        start_arrow = True,
                                        end_arrow = True)
        self.setup_item_signals (polyline5)
    
    def setup_polygons (self, root):
        stipple_data = array.array('i', [0, 0, 0, 255,   0, 0, 0, 0,   
                                         0, 0, 0, 0,   0, 0, 0, 255])
        points = goocanvas.Points ([(210.0, 320.0), (210.0, 380.0), 
                                    (260.0, 350.0)])
        pattern = self.create_stipple ("blue", stipple_data)
        polyline1 = goocanvas.Polyline (parent = root,
                                        close_path = True,
                                        line_width = 1.0,
                                        points = points,
                                        fill_pattern = pattern,
                                        stroke_color = "black")
        self.setup_item_signals (polyline1)
        
        points = goocanvas.Points ([(270.0, 330.0), (270.0, 430.0),
                                    (390.0, 430.0), (390.0, 330.0),
                                    (310.0, 330.0), (310.0, 390.0),
                                    (350.0, 390.0), (350.0, 370.0),
                                    (330.0, 370.0), (330.0, 350.0),
                                    (370.0, 350.0), (370.0, 410.0),
                                    (290.0, 410.0), (290.0, 330.0)])
        polyline2 = goocanvas.Polyline (parent = root,
                                        close_path = True,
                                        line_width = 1.0,
                                        points = points,
                                        fill_color = "tan",
                                        stroke_color = "black")
        self.setup_item_signals (polyline2)    

    def make_anchor (self, root, x, y):
        trans = cairo.Matrix(0.8, 0.2, -0.3, 0.5, x, y)

        group = goocanvas.Group (parent = root)

        group.translate (x, y)

        group.props.transform = trans

        item = goocanvas.Rect (parent = group,
                               x = -2.5,
                               y = -2.5,
                               width = 4,
                               height = 4,
                               line_width = 1.0)
        self.setup_item_signals (item)

        return group

    def setup_texts (self, root):
        stipple_data = array.array('i', [0, 0, 0, 255,   0, 0, 0, 0,   
                                         0, 0, 0, 0,   0, 0, 0, 255])
        pattern = self.create_stipple ("blue", stipple_data)
        par = self.make_anchor (root, 420.0, 20.0)
        item = goocanvas.Text (parent = par,
                               text = "Anchor NW",
                               x = 0, 
                               y = 0,
                               width = -1,
                               anchor = gtk.ANCHOR_NW,
                               font = "Sans Bold 24",
                               fill_pattern = pattern)
        self.setup_item_signals (item)
        
        par = self.make_anchor (root, 470, 75)
        item = goocanvas.Text (parent = par,
                               text = "Anchor center\nJustify center\nMultiline text\nb8bit text",
                               x = 0,
                               y = 0,
                               width = -1,
                               anchor = gtk.ANCHOR_CENTER,
                               font = "monospace bold 14",
                               alignment = pango.ALIGN_CENTER,
                               fill_color = "firebrick")
        self.setup_item_signals (item);
        
        par = self.make_anchor (root, 420, 240)
        textitem = goocanvas.Text (parent = par,
                                   text = "This is a very long paragraph that will need to be wrapped over several lines so we can see what happens to line-breaking as the view is zoomed in and out.",
                                   x = 0,
                                   y = 0,
                                   width = 180,
                                   anchor = gtk.ANCHOR_W,
                                   font = "Sans 12",
                                   fill_color = "goldenrod")
        self.setup_item_signals (textitem)
        
        textitem = goocanvas.Text (parent = root,
                                   text = "Ellipsized text.",
                                   x = 20,
                                   y = 420,
                                   width = 115,
                                   anchor = gtk.ANCHOR_W,
                                   font = "Sans 12",
                                   fill_color = "blue",
                                   ellipsize = pango.ELLIPSIZE_END)
        self.setup_item_signals (textitem)
        

    def setup_invisible_texts (self, root):
        text = goocanvas.Text (parent = root,
                               text = "Visible above 0.8x",
                               x = 500,
                               y = 330,
                               width = -1,
                               anchor = gtk.ANCHOR_CENTER,
                               visibility = goocanvas.ITEM_VISIBLE_ABOVE_THRESHOLD,
                               visibility_threshold = 0.8)
        
        goocanvas.Rect (parent = root,
                        x = 410.5,
                        y = 322.5,
                        width = 180,
                        height = 15,
                        line_width = 1.0,
                        visibility = goocanvas.ITEM_VISIBLE_ABOVE_THRESHOLD,
                        visibility_threshold = 0.8)
        
        text = goocanvas.Text (parent = root,
                               text = "Visible above 1.5x",
                               x = 500,
                               y = 350,
                               width = -1,
                               anchor = gtk.ANCHOR_CENTER,
                               visibility = goocanvas.ITEM_VISIBLE_ABOVE_THRESHOLD,
                               visibility_threshold = 1.5)

        goocanvas.Rect (parent = root,
                        x = 410.5,
                        y = 342.5,
                        width = 180,
                        height = 15,
                        line_width = 1.0,
                        visibility = goocanvas.ITEM_VISIBLE_ABOVE_THRESHOLD,
                        visibility_threshold = 1.5)

        text = goocanvas.Text (parent = root,
                               text = "Visible above 3.0x",
                               x = 500,
                               y = 370,
                               width = -1,
                               anchor = gtk.ANCHOR_CENTER,
                               visibility = goocanvas.ITEM_VISIBLE_ABOVE_THRESHOLD,
                               visibility_threshold = 3.0)

        goocanvas.Rect (parent = root,
                        x = 410.5,
                        y = 362.5,
                        width = 180,
                        height = 15,
                        line_width = 1.0,
                        visibility = goocanvas.ITEM_VISIBLE_ABOVE_THRESHOLD,
                        visibility_threshold = 3.0)
        
        ''' This should never be seen. '''
        text = goocanvas.Text (parent = root,
                               text = "Always Invisible",
                               x = 500,
                               y = 390,
                               width = -1,
                               anchor = gtk.ANCHOR_CENTER,
                               visibility = goocanvas.ITEM_INVISIBLE)

        goocanvas.Rect (parent = root,
                        x = 410.5,
                        y = 350.5,
                        width = 180,
                        height = 15,
                        line_width = 1.0,
                        visibility = goocanvas.ITEM_INVISIBLE)

    def plant_flower (self, root, x, y, anchor):
        surface = cairo.ImageSurface.create_from_png ("../images/flower.png")

        w = surface.get_width ()
        h = surface.get_height ()
        
        pattern = cairo.SurfacePattern(surface)
        
        image = goocanvas.Image (parent = root,
                                 x = x, 
                                 y = y,
                                 pattern = pattern,
                                 width = w,
                                 height = h)
        self.setup_item_signals (image)

    def setup_images (self, root):
        im = gtk.gdk.pixbuf_new_from_file ("../images/toroid.png")
        
        if im:
            w = im.get_width ()
            h = im.get_height ()
            image = goocanvas.Image (parent = root,
                                     pixbuf = im,
                                     x = 100.0 - w / 2,
                                     y = 225.0 - h / 2,
                                     width = w,
                                     height = h)
            self.setup_item_signals (image)
        else:
            print "Could not find the toroid.png sample file"
        self.plant_flower (root,  20.0, 170.0, gtk.ANCHOR_NW)
        self.plant_flower (root, 180.0, 170.0, gtk.ANCHOR_NE)
        self.plant_flower (root,  20.0, 280.0, gtk.ANCHOR_SW)
        self.plant_flower (root, 180.0, 280.0, gtk.ANCHOR_SE)

    def setup_canvas (self, canvas):
        root = canvas.get_root_item ()
        root.connect("button_press_event", self.on_background_button_press)
        self.setup_divisions (root)
        self.setup_rectangles (root)
        self.setup_ellipses (root)
        self.setup_lines (root)
        self.setup_polygons (root)
        self.setup_texts (root)
        self.setup_invisible_texts (root)
        self.setup_images(root)

if __name__ == "__main__":
    mycanvas = MyCanvas()
    mycanvas.main()
