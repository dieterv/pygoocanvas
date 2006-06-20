import gtk
import goocanvas

PIECE_SIZE = 50

win = gtk.Window()
win.connect("destroy", gtk.main_quit)

vbox = gtk.VBox(False, 4)
vbox.set_border_width(4)

alignment = gtk.Alignment(0.5, 0.5, 0.0, 0.0)
vbox.pack_start(alignment, True, True, 0)

frame = gtk.Frame()
frame.set_shadow_type(gtk.SHADOW_IN)
alignment.add(frame)

def on_item_view_created (view, item_view, item):
    item_view.connect("button_press_event", piece_button_press)

def piece_button_press(view, target_view, event):
    item = view.get_item()
    canvas = view.get_canvas_view()
    board = canvas.get_data("board")
    num = item.get_data("piece_num")
    pos = item.get_data("piece_pos")
    text = item.get_data("text")

canvas_model = goocanvas.CanvasModelSimple()

canvas = goocanvas.CanvasView()
canvas.connect("item-view-created", on_item_view_created)
canvas.set_model(canvas_model)
canvas.set_size_request(PIECE_SIZE * 4 + 1, PIECE_SIZE * 4 + 1)
canvas.set_bounds(0, 0, PIECE_SIZE * 4 + 1, PIECE_SIZE * 4 + 1)

board = []

root = canvas_model.get_root_item()
canvas.set_data("board", board)

frame.add(canvas)

def get_piece_color(piece):
    y = i / 4
    x = i % 4
    r = ((4 - x) * 255) / 4
    g = ((4 - y) * 255) / 4
    b = 128

    buf = "#%02x%02x%02x" % (r, g, b)

    return buf

i = 0

while i < 15:
    y = i / 4;
    x = i % 4;

    gr = goocanvas.Group()
    board.append(gr)
    root.add_child(board[i])
    
    board[i].translate(x * PIECE_SIZE, y * PIECE_SIZE)
    
    rect = goocanvas.Rect(x=0, y=0,
                          width=PIECE_SIZE, height=PIECE_SIZE,
                          fill_color = get_piece_color (i),
                          stroke_color = "black",
                          line_width = 1.0)
    board[i].add_child(rect)

    buf = "%d" % (i+1)

    text = goocanvas.Text(text = buf,
					    x = PIECE_SIZE / 2.0,
					    y = PIECE_SIZE / 2.0,
					    font = "Sans bold 24",
					    anchor = gtk.ANCHOR_CENTER,
					    fill_color = "black")
    board[i].add_child(text)
    
    board[i].set_data("text", text)
    board[i].set_data("piece_pos", i)
    board[i].set_data("piece_num", i)

    i += 1

win.add(vbox)
win.show_all()

gtk.main()
