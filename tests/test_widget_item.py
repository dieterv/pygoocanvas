import goocanvas
import cairo
import unittest
import pango
import gtk

class TestWidget(unittest.TestCase):    
    def make_widget_item(self, **kwargs):
        item = goocanvas.Widget(**kwargs)
        return item

    ''' Test goocanvas.Widget properties '''

    def test_widget_anchor_property(self):
        item = self.make_widget_item()
        
        ## Testing default value gtk.ANCHOR_NORTH_WEST
        self.failUnlessEqual(item.props.anchor, gtk.ANCHOR_NORTH_WEST)
        item.props.anchor = gtk.ANCHOR_NORTH_EAST
        self.failUnlessEqual(item.props.anchor, gtk.ANCHOR_NORTH_EAST)

    def test_widget_height_property(self):
        item = self.make_widget_item()

        ## Testing default value -1
        self.failUnlessEqual(item.props.height, -1)
        item.props.height = 50
        self.failUnlessEqual(item.props.height, 50)

    def test_widget_widget_property(self):
        entry = gtk.Entry()
        item = self.make_widget_item(widget=entry)
        self.failUnlessEqual(item.props.widget, entry)

    def test_widget_width_property(self):
        item = self.make_widget_item()

        ## Testing default value -1
        self.failUnlessEqual(item.props.width, -1)
        item.props.width = 50
        self.failUnlessEqual(item.props.width, 50)

    def test_widget_x_property(self):
        item = self.make_widget_item()

        ## Testing default value 0
        self.failUnlessEqual(item.props.x, 0)
        item.props.x = 50
        self.failUnlessEqual(item.props.x, 50)

    def test_widget_y_property(self):
        item = self.make_widget_item()

        ## Testing default value 0
        self.failUnlessEqual(item.props.y, 0)
        item.props.y = 50
        self.failUnlessEqual(item.props.y, 50)
