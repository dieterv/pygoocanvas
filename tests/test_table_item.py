import goocanvas
import cairo
import unittest
import pango
import gtk

class TestTable(unittest.TestCase):
    def make_table_item(self, **kwargs):
        item = goocanvas.Table(**kwargs)
        return item

    def make_ellipse_item(self, **kwargs):
        item = goocanvas.Ellipse(**kwargs)
        return item

    ''' Test goocanvas.Table properties '''

    def test_table_column_spacing_property(self):
        item = self.make_table_item(column_spacing=5)
        self.failUnlessEqual(item.props.column_spacing, 5)
        item.props.column_spacing = 10
        self.failUnlessEqual(item.props.column_spacing, 10)

    def test_table_height_property(self):
        item = self.make_table_item()
        self.failUnlessEqual(item.props.height, -1)
        item.props.height = 10
        self.failUnlessEqual(item.props.height, 10)
   
    def test_table_homogeneous_columns_property(self):
        item = self.make_table_item(homogeneous_columns=True)
        self.failUnlessEqual(item.props.homogeneous_columns, True)
        item.props.homogeneous_columns = False
        self.failUnlessEqual(item.props.homogeneous_columns, False)
   
    def test_table_homogeneous_rows_property(self):
        item = self.make_table_item(homogeneous_rows=True)
        self.failUnlessEqual(item.props.homogeneous_rows, True)
        item.props.homogeneous_rows = False
        self.failUnlessEqual(item.props.homogeneous_rows, False)

    def test_table_horz_grid_line_width_property(self):
        item = self.make_table_item(horz_grid_line_width=5)
        self.failUnlessEqual(item.props.horz_grid_line_width, 5)
        item.props.horz_grid_line_width = 10
        self.failUnlessEqual(item.props.horz_grid_line_width, 10)

    def test_table_row_spacing_property(self):
        item = self.make_table_item(row_spacing=5)
        self.failUnlessEqual(item.props.row_spacing, 5)
        item.props.row_spacing = 10
        self.failUnlessEqual(item.props.row_spacing, 10)

    def test_table_vert_grid_line_width_property(self):
        item = self.make_table_item(vert_grid_line_width=5)
        self.failUnlessEqual(item.props.vert_grid_line_width, 5)
        item.props.vert_grid_line_width = 10
        self.failUnlessEqual(item.props.vert_grid_line_width, 10)

    def test_table_width_property(self):
        item = self.make_table_item()
        self.failUnlessEqual(item.props.width, -1)
        item.props.width = 10
        self.failUnlessEqual(item.props.width, 10)

    def test_table_x_border_spacing_property(self):
        item = self.make_table_item(x_border_spacing=5)
        self.failUnlessEqual(item.props.x_border_spacing, 5)
        item.props.x_border_spacing = 10
        self.failUnlessEqual(item.props.x_border_spacing, 10)

    def test_table_y_border_spacing_property(self):
        item = self.make_table_item(y_border_spacing=5)
        self.failUnlessEqual(item.props.y_border_spacing, 5)
        item.props.y_border_spacing = 10
        self.failUnlessEqual(item.props.y_border_spacing, 10)

    ''' Test goocanvas.Table child properties '''

    def test_table_bottom_padding_child_property(self):
        item = self.make_table_item()
        child = self.make_ellipse_item(parent=item)

        ## Testing default value 0
        self.failUnlessEqual(item.get_child_property(child, "bottom_padding"), 0)
        item.set_child_property(child, "bottom_padding", 5)
        self.failUnlessEqual(item.get_child_property(child, "bottom_padding"), 5)

    def test_table_left_padding_child_property(self):
        item = self.make_table_item()
        child = self.make_ellipse_item(parent=item)

        ## Testing default value 0
        self.failUnlessEqual(item.get_child_property(child, "left_padding"), 0)
        item.set_child_property(child, "left_padding", 5)
        self.failUnlessEqual(item.get_child_property(child, "left_padding"), 5)

    def test_table_right_padding_child_property(self):
        item = self.make_table_item()
        child = self.make_ellipse_item(parent=item)
        
        ## Testing default value 0
        self.failUnlessEqual(item.get_child_property(child, "right_padding"), 0)
        item.set_child_property(child, "right_padding", 5)
        self.failUnlessEqual(item.get_child_property(child, "right_padding"), 5)

    def test_table_top_padding_child_property(self):
        item = self.make_table_item()
        child = self.make_ellipse_item(parent=item)

        ## Testing default value 0
        self.failUnlessEqual(item.get_child_property(child, "top_padding"), 0)
        item.set_child_property(child, "top_padding", 5)
        self.failUnlessEqual(item.get_child_property(child, "top_padding"), 5)

    def test_table_column_child_property(self):
        item = self.make_table_item()
        child = self.make_ellipse_item(parent=item)

        ## Testing default value 0
        self.failUnlessEqual(item.get_child_property(child, "column"), 0)
        item.set_child_property(child, "column", 5)
        self.failUnlessEqual(item.get_child_property(child, "column"), 5)

    def test_table_columns_child_property(self):
        item = self.make_table_item()
        child = self.make_ellipse_item(parent=item)

        ## Testing default value 1
        self.failUnlessEqual(item.get_child_property(child, "columns"), 1)
        item.set_child_property(child, "columns", 5)
        self.failUnlessEqual(item.get_child_property(child, "columns"), 5)

    def test_table_row_child_property(self):
        item = self.make_table_item()
        child = self.make_ellipse_item(parent=item)

        ## Testing default value 0
        self.failUnlessEqual(item.get_child_property(child, "row"), 0)
        item.set_child_property(child, "row", 5)
        self.failUnlessEqual(item.get_child_property(child, "row"), 5)

    def test_table_rows_child_property(self):
        item = self.make_table_item()
        child = self.make_ellipse_item(parent=item)

        ## Testing default value 1
        self.failUnlessEqual(item.get_child_property(child, "rows"), 1)
        item.set_child_property(child, "rows", 5)
        self.failUnlessEqual(item.get_child_property(child, "rows"), 5)

    def test_table_x_align_child_property(self):
        item = self.make_table_item()
        child = self.make_ellipse_item(parent=item)

        ## Testing default value 0.5
        self.failUnlessEqual(item.get_child_property(child, "x_align"), 0.5)
        item.set_child_property(child, "x_align", 1)
        self.failUnlessEqual(item.get_child_property(child, "x_align"), 1)

    def test_table_x_expand_child_property(self):
        item = self.make_table_item()
        child = self.make_ellipse_item(parent=item)

        ## Testing default value False
        self.failUnlessEqual(item.get_child_property(child, "x_expand"), False)
        item.set_child_property(child, "x_expand", True)
        self.failUnlessEqual(item.get_child_property(child, "x_expand"), True)

    def test_table_x_fill_child_property(self):
        item = self.make_table_item()
        child = self.make_ellipse_item(parent=item)

        ## Testing default value False
        self.failUnlessEqual(item.get_child_property(child, "x_fill"), False)
        item.set_child_property(child, "x_fill", True)
        self.failUnlessEqual(item.get_child_property(child, "x_fill"), True)

    def test_table_x_shrink_child_property(self):
        item = self.make_table_item()
        child = self.make_ellipse_item(parent=item)

        ## Testing default value False
        self.failUnlessEqual(item.get_child_property(child, "x_shrink"), False)
        item.set_child_property(child, "x_shrink", True)
        self.failUnlessEqual(item.get_child_property(child, "x_shrink"), True)

    def test_table_y_align_child_property(self):
        item = self.make_table_item()
        child = self.make_ellipse_item(parent=item)

        ## Testing default value 0.5
        self.failUnlessEqual(item.get_child_property(child, "y_align"), 0.5)
        item.set_child_property(child, "y_align", 1)
        self.failUnlessEqual(item.get_child_property(child, "y_align"), 1)

    def test_table_y_eypand_child_property(self):
        item = self.make_table_item()
        child = self.make_ellipse_item(parent=item)

        ## Testing default value False
        self.failUnlessEqual(item.get_child_property(child, "y_expand"), False)
        item.set_child_property(child, "y_expand", True)
        self.failUnlessEqual(item.get_child_property(child, "y_expand"), True)

    def test_table_y_fill_child_property(self):
        item = self.make_table_item()
        child = self.make_ellipse_item(parent=item)

        ## Testing default value False
        self.failUnlessEqual(item.get_child_property(child, "y_fill"), False)
        item.set_child_property(child, "y_fill", True)
        self.failUnlessEqual(item.get_child_property(child, "y_fill"), True)

    def test_table_y_shrink_child_property(self):
        item = self.make_table_item()
        child = self.make_ellipse_item(parent=item)

        ## Testing default value False
        self.failUnlessEqual(item.get_child_property(child, "y_shrink"), False)
        item.set_child_property(child, "y_shrink", True)
        self.failUnlessEqual(item.get_child_property(child, "y_shrink"), True)
