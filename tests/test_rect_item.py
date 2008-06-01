import goocanvas
import cairo
import unittest
import pango
import gtk

class TestRect(unittest.TestCase):
    def make_rect_item(self, **kwargs):
        item = goocanvas.Rect(**kwargs)
        return item

    ''' Test goocanvas.Rect properties '''

    def test_rect_x_property(self):
        item = self.make_rect_item(x=100)
        self.failUnlessEqual(item.props.x, 100.0)
        item.props.x = 200
        self.failUnlessEqual(item.props.x, 200.0)

    def test_rect_y_property(self):
        item = self.make_rect_item(y=100)
        self.failUnlessEqual(item.props.y, 100.0)
        item.props.y = 200
        self.failUnlessEqual(item.props.y, 200.0)

    def test_rect_width_property(self):
        item = self.make_rect_item(width=100)
        self.failUnlessEqual(item.props.width, 100.0)
        item.props.width = 200
        self.failUnlessEqual(item.props.width, 200.0)

    def test_rect_height_property(self):
        item = self.make_rect_item(height=100)
        self.failUnlessEqual(item.props.height, 100.0)
        item.props.height = 200
        self.failUnlessEqual(item.props.height, 200.0)

    def test_rect_radius_x_property(self):
        item = self.make_rect_item(radius_x=1)
        self.failUnlessEqual(item.props.radius_x, 1.0)
        item.props.radius_x = 2
        self.failUnlessEqual(item.props.radius_x, 2.0)

    def test_rect_radius_y_property(self):
        item = self.make_rect_item(radius_y=1)
        self.failUnlessEqual(item.props.radius_y, 1.0)
        item.props.radius_y = 2
        self.failUnlessEqual(item.props.radius_y, 2.0)
