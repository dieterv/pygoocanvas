import goocanvas
import cairo
import unittest
import pango
import gtk

class TestImage(unittest.TestCase):
    def make_image_item(self, **kwargs):
        item = goocanvas.Image(**kwargs)
        return item

    ''' Test goocanvas.Image properties '''
    
    def test_image_x_property(self):
        item = self.make_image_item(x=100)
        self.failUnlessEqual(item.props.x, 100.0)
        item.props.x = 200
        self.failUnlessEqual(item.props.x, 200.0)

    def test_image_y_property(self):
        item = self.make_image_item(y=100)
        self.failUnlessEqual(item.props.y, 100.0)
        item.props.y = 200
        self.failUnlessEqual(item.props.y, 200.0)

    def test_image_width_property(self):
        item = self.make_image_item(width=100)
        self.failUnlessEqual(item.props.width, 100.0)
        item.props.width = 200
        self.failUnlessEqual(item.props.width, 200.0)

    def test_image_height_property(self):
        item = self.make_image_item(height=100)
        self.failUnlessEqual(item.props.height, 100.0)
        item.props.height = 200
        self.failUnlessEqual(item.props.height, 200.0)

    def test_image_height_pattern(self):
        linear = cairo.LinearGradient(50, 50, 300, 300)
        linear.add_color_stop_rgba(0.0,  1, 1, 1, 0)
        item = self.make_image_item(pattern=linear)
        pattern = item.props.pattern.get_matrix()
        self.failUnlessEqual(linear.get_matrix(), pattern)

    ## FIXME: I need a smart way to test pixbuf property
    def test_image_height_pixbuf(self):
        pass
