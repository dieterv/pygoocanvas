import goocanvas
import cairo
import unittest

class TestItem(unittest.TestCase):
    def make_rect_item(self, **kwargs):
        item = goocanvas.Rect(**kwargs)
        return item

    def make_group_item(self, **kwargs):
        item = goocanvas.Group(**kwargs)
        return item

    def make_text_item(self, **kwargs):
        item = goocanvas.Text(**kwargs)
        return item

    def make_table_item(self, **kwargs):
        item = goocanvas.Table(**kwargs)
        return item

    ## Test goocanvas.Item methods using a rect item
    
    ## Cannot test:
    ##      goo_canvas_item_request_update
    ##      goo_canvas_item_ensure_update
    ##      goo_canvas_item_paint
    ##      goo_canvas_item_animate
    ##      goo_canvas_item_stop_animation

    def test_add_get_child(self):
        item = self.make_group_item()
        rect = self.make_rect_item()
        item.add_child(rect, -1)
        res = item.get_child(0)
        self.failUnlessEqual(res, rect)

    ## TODO: test_allocate area
    
    def test_find_child(self):
        c = goocanvas.Canvas()
        c.show()
        r = c.get_root_item()
        i = self.make_rect_item(parent=r, x=100, y=100, height=100, width=100)
        t = self.make_text_item(parent=r, x=100, y=100, width=100)
        res = r.find_child(t)
        self.failUnlessEqual(res, 1)
        res = r.find_child(i)
        self.failUnlessEqual(res, 0)
    
    def test_find_child_property(self):
        item = self.make_table_item(column_spacing=5)
        child = self.make_rect_item(parent=item)
        item.set_child_property(child, "bottom_padding", 5)
        p = item.find_child_property("bottom_padding")
        self.failUnlessEqual(getattr(p, "name"), "bottom-padding")

    def test_get_bounds(self):
        c = goocanvas.Canvas()
        r = c.get_root_item()
        i = self.make_rect_item(parent=r, x=100, y=100, height=100, width=100)
        c.show()
        res = i.get_bounds()
        self.failUnlessEqual(res.x1, 99)
        self.failUnlessEqual(res.x2, 201)
        self.failUnlessEqual(res.y1, 99)
        self.failUnlessEqual(res.y2, 201)

    def test_get_set_canvas(self):
        c = goocanvas.Canvas()
        r = c.get_root_item()
        i = self.make_rect_item(parent=r, x=100, y=100, height=100, width=100)
        res = i.get_canvas()
        self.failUnlessEqual(res, c)
        d = goocanvas.Canvas()
        f = self.make_rect_item(x=100, y=100, height=100, width=100)
        f.set_canvas(d)
        res1 = f.get_canvas()
        self.failUnlessEqual(res1, d)

    def test_get_items_at(self):
        c = goocanvas.Canvas()
        c.show()
        r = c.get_root_item()
        i = self.make_rect_item(parent=r, x=100, y=100, height=100, width=100)
        cr = c.create_cairo_context()
        res = r.get_items_at(150, 150, cr, False, False)
        self.failUnlessEqual(res[0], i)

    def test_get_n_children(self):
        c = goocanvas.Canvas()
        c.show()
        r = c.get_root_item()
        i = self.make_rect_item(parent=r, x=100, y=100, height=100, width=100)
        i2 = self.make_text_item(parent=r, x=100, y=400)
        res = r.get_n_children()
        self.failUnlessEqual(res, 2)

    def test_get_requested_area(self):
        c = goocanvas.Canvas()
        c.show()
        cr = c.create_cairo_context()
        r = c.get_root_item()
        i = self.make_rect_item(parent=r, x=100, y=100, height=100, width=100)
        bounds = i.get_requested_area(cr)
        self.failUnlessEqual(bounds.x1, 99)
        self.failUnlessEqual(bounds.x2, 201)
        self.failUnlessEqual(bounds.y1, 99)
        self.failUnlessEqual(bounds.y2, 201)

    def test_get_requested_height(self):
        c = goocanvas.Canvas()
        c.show()
        cr = c.create_cairo_context()
        r = c.get_root_item()
        i = self.make_text_item(parent=r, x=100, y=100, width=100, text="Test")
        height = i.get_requested_height(cr, 100)
        self.failUnlessEqual(height, 18.625)

    def test_get_set_child_properties(self):
        c = goocanvas.Canvas()
        r = c.get_root_item()
        t = goocanvas.Table(parent=r)
        i = self.make_rect_item(parent=t, x=100, y=100, height=100, width=100)
        t.set_child_properties(i, bottom_padding=3, columns=2, x_align=0.4)
        res = t.get_child_properties(i, "bottom_padding", "columns", "x_align")
        self.failUnlessEqual(res, (3.0, 2, 0.4))

    def test_get_set_child_property(self):
        c = goocanvas.Canvas()
        r = c.get_root_item()
        t = goocanvas.Table(parent=r)
        i = self.make_rect_item(parent=t, x=100, y=100, height=100, width=100)
        t.set_child_property(i, "bottom_padding", 3)
        res = t.get_child_property(i, "bottom_padding")
        self.failUnlessEqual(res, 3.0)

    def test_get_set_model(self):
        i = self.make_rect_item(x=100, y=100, height=100, width=100)
        res = i.get_model()
        self.failUnlessEqual(res, None)
        m = goocanvas.RectModel()
        i.set_model(m)
        rm = i.get_model()
        self.failUnlessEqual(rm, m)

    def test_get_set_parent(self):
        g = self.make_group_item()
        i = self.make_rect_item(x=100, y=100, height=100, width=100)
        i.set_parent(g)
        res = i.get_parent()
        self.failUnlessEqual(res, g)

    ## TODO: test_get_set_style

    def test_get_set_transform(self):
        item = self.make_rect_item()
        transform = cairo.Matrix(0.8, 0.2, -0.3, 0.5)
        item.set_transform(transform)
        result = item.get_transform()
        self.failUnlessEqual(transform, result)

    ## TODO: test_get_transform_for_child

    def test_get_set_simple_transform(self):
        item = self.make_rect_item(x=100, y=100, height=100, width=100)
        item.set_simple_transform(20, 30, 40, 50)
        result = item.get_simple_transform()
        self.failUnlessEqual(result, (20, 30, 40, 50))

    ## TODO: test_install_child_property

    def test_is_visible(self):
        c = goocanvas.Canvas()
        r = c.get_root_item()
        i = self.make_rect_item(parent=r, x=100, y=100, height=100, width=100)
        c.show()
        self.failUnlessEqual(i.is_visible(), True)
    
    def test_is_container(self):
        c = goocanvas.Canvas()
        r = c.get_root_item()
        i = self.make_rect_item(parent=r, x=100, y=100, height=100, width=100)
        self.failUnlessEqual(i.is_container(), False)
        self.failUnlessEqual(r.is_container(), True)
    
    def test_list_child_properties(self):
        item = self.make_table_item(column_spacing=5)
        i = item.list_child_properties()
        self.failUnlessEqual(isinstance(i, list), True)

    ## TODO: test_lower
    ## TODO: test_move_child
    ## TODO: test_raise
    ## TODO: test_remove
    ## TODO: test_remove_child
    
    def test_rotate(self):
        item = self.make_rect_item(x=100, y=100, height=100, width=100)
        item.rotate(45, 150, 150)
        M = item.get_transform()
        self.failUnlessAlmostEqual(M[0], 0.707, places=3)
        self.failUnlessAlmostEqual(M[1], 0.707, places=3)

    def test_scale(self):
        item = self.make_rect_item(x=100, y=100, height=100, width=100)
        item.scale(100, 200)
        M = item.get_transform()
        self.failUnlessEqual(M[0], 100.0)
        self.failUnlessEqual(M[3], 200.0)

    def test_skew_x(self):
        item = self.make_rect_item(x=100, y=100, height=400, width=400)
        item.skew_x(10, 250, 250)
        M = item.get_transform()
        self.failUnlessAlmostEqual(M[2], 0.176327, places=4)
        self.failUnlessAlmostEqual(M[4], -44.0817, places=4)
        
    def test_skew_y(self):
        item = self.make_rect_item(x=100, y=100, height=400, width=400)
        item.skew_y(10, 250, 250)
        M = item.get_transform()
        self.failUnlessAlmostEqual(M[1], 0.176327, places=4)
        self.failUnlessAlmostEqual(M[5], -44.0817, places=4)

    def test_translate(self):
        item = self.make_rect_item(x=100, y=100)
        item.translate(100, 200)
        M = item.get_transform()
        self.failUnlessEqual(M[4], 100.0)
        self.failUnlessEqual(M[5], 200.0)

    ## TODO: test_update
