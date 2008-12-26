import goocanvas
import unittest

class TestGrid(unittest.TestCase):
    def make_grid_item(self, **kwargs):
        item = goocanvas.Grid(**kwargs)
        return item
    
    ''' Test goocanvas.Grid properties '''

    def test_grid_border_color_property(self):
        # Write only property
        item = self.make_grid_item(border_color="red")
        item.props.border_color = "mediumseagreen"

    def test_grid_border_color_rgba_property(self):
        item = self.make_grid_item(border_color_rgba=0xC3C3FF)
        self.failUnlessEqual(item.props.border_color_rgba, 0xC3C3FF)
        item.props.border_color_rgba = 0xC3C3AA
        self.failUnlessEqual(item.props.border_color_rgba, 0xC3C3AA)
