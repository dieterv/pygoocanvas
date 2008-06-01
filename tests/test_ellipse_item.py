import goocanvas
import cairo
import unittest
import pango
import gtk

class TestEllipse(unittest.TestCase):
    def make_ellipse_item(self, **kwargs):
        item = goocanvas.Ellipse(**kwargs)
        return item

    ''' Test goocanvas.Ellipse properties '''

    def test_ellipse_radius_x_property(self):
        item = self.make_ellipse_item(radius_x=100)
        self.failUnlessEqual(item.props.radius_x, 100.0)
        item.props.radius_x = 200
        self.failUnlessEqual(item.props.radius_x, 200.0)

    def test_ellipse_radius_y_property(self):
        item = self.make_ellipse_item(radius_y=100)
        self.failUnlessEqual(item.props.radius_y, 100.0)
        item.props.radius_y = 200
        self.failUnlessEqual(item.props.radius_y, 200.0)

    def test_ellipse_center_x_property(self):
        item = self.make_ellipse_item(center_x=100)
        self.failUnlessEqual(item.props.center_x, 100.0)
        item.props.center_x = 200
        self.failUnlessEqual(item.props.center_x, 200.0)

    def test_ellipse_center_y_property(self):
        item = self.make_ellipse_item(center_y=100)
        self.failUnlessEqual(item.props.center_y, 100.0)
        item.props.center_y = 200
        self.failUnlessEqual(item.props.center_y, 200.0)
