import goocanvas
import cairo
import unittest
import pango
import gtk

class TestPolyline(unittest.TestCase):
    def make_polyline_item(self, **kwargs):
        item = goocanvas.Polyline(**kwargs)
        return item

    ''' Test goocanvas.Polyline properties '''
    
    def test_polyline_arrow_length_property(self):
        item = self.make_polyline_item(arrow_length=6)
        self.failUnlessEqual(item.props.arrow_length, 6)
        item.props.arrow_length = 4
        self.failUnlessEqual(item.props.arrow_length, 4)

    def test_polyline_arrow_tip_length_property(self):
        item = self.make_polyline_item(arrow_tip_length=6)
        self.failUnlessEqual(item.props.arrow_tip_length, 6)
        item.props.arrow_tip_length = 4
        self.failUnlessEqual(item.props.arrow_tip_length, 4)

    def test_polyline_arrow_width_property(self):
        item = self.make_polyline_item(arrow_width=6)
        self.failUnlessEqual(item.props.arrow_width, 6)
        item.props.arrow_width = 4
        self.failUnlessEqual(item.props.arrow_width, 4)

    def test_polyline_close_path_property(self):
        item = self.make_polyline_item(close_path=True)
        self.failUnlessEqual(item.props.close_path, True)
        item.props.close_path = False
        self.failUnlessEqual(item.props.close_path, False)

    def test_polyline_start_arrow_property(self):
        item = self.make_polyline_item(start_arrow=True)
        self.failUnlessEqual(item.props.start_arrow, True)
        item.props.start_arrow = False
        self.failUnlessEqual(item.props.start_arrow, False)

    def test_polyline_end_arrow_property(self):
        item = self.make_polyline_item(end_arrow=True)
        self.failUnlessEqual(item.props.end_arrow, True)
        item.props.end_arrow = False
        self.failUnlessEqual(item.props.end_arrow, False)

    def test_polyline_points_property(self):
        p = goocanvas.Points ([(340.0, 170.0), (340.0, 230.0), 
                                    (390.0, 230.0), (390.0, 170.0)])
        item = self.make_polyline_item(points=p)
        pr = item.props.points
        self.failUnlessEqual(p.coords[0], pr.coords[0])
        self.failUnlessEqual(p.coords[1], pr.coords[1])
        self.failUnlessEqual(p.coords[2], pr.coords[2])
        self.failUnlessEqual(p.coords[3], pr.coords[3])
    
    def test_polyline_num_points_property(self):
        p = goocanvas.Points ([(340.0, 170.0), (340.0, 230.0), 
                                    (390.0, 230.0), (390.0, 170.0)])
        item = self.make_polyline_item(points=p)
        np = item.props.points
        self.failUnlessEqual(p.num_points, 4)
