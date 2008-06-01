import goocanvas
import cairo
import unittest
import pango
import gtk

class TestText(unittest.TestCase):
    def make_text_item(self, **kwargs):
        item = goocanvas.Text(**kwargs)
        return item

    ''' Test goocanvas.Text properties '''

    def test_text_alignment_property(self):
        item = self.make_text_item(alignment=pango.ALIGN_LEFT)
        self.failUnlessEqual(item.props.alignment, pango.ALIGN_LEFT)

    def test_text_anchor_property(self):
        item = self.make_text_item()
        
        ## Testing default value gtk.ANCHOR_NORTH_WEST
        self.failUnlessEqual(item.props.anchor, gtk.ANCHOR_NORTH_WEST)
        item.props.anchor = gtk.ANCHOR_NORTH_EAST
        self.failUnlessEqual(item.props.anchor, gtk.ANCHOR_NORTH_EAST)

    def test_text_font_property(self):
        item = self.make_text_item(font="Sans 24")
        self.failUnlessEqual(item.props.font, "Sans 24")

    def test_text_font_desc_property(self):
        fd = pango.FontDescription()
        fd.set_family("Helvetica")
        item = self.make_text_item(font_desc=fd)
        self.failUnlessEqual(item.props.font_desc.get_family(), "Helvetica")

    def test_text_text_property(self):
        item = self.make_text_item(text="some text")
        self.failUnlessEqual(item.props.text, "some text")
    
    def test_text_use_markup_property(self):
        item = self.make_text_item(use_markup=True)
        self.failUnlessEqual(item.props.use_markup, True)
        item.props.use_markup = False
        self.failUnlessEqual(item.props.use_markup, False)
    
    def test_text_x_property(self):
        item = self.make_text_item(x=100)
        self.failUnlessEqual(item.props.x, 100.0)
        item.props.x = 200
        self.failUnlessEqual(item.props.x, 200.0)

    def test_text_y_property(self):
        item = self.make_text_item(y=100)
        self.failUnlessEqual(item.props.y, 100.0)
        item.props.y = 200
        self.failUnlessEqual(item.props.y, 200.0)

    def test_text_width_property(self):
        item = self.make_text_item(width=100)
        self.failUnlessEqual(item.props.width, 100.0)
        item.props.width = 200
        self.failUnlessEqual(item.props.width, 200.0)
