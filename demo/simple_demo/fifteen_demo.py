import gtk
import goocanvas
import random

PIECE_SIZE = 50
SCRAMBLE_MOVES = 256

def test_win (board):
    i = 0
    while i < 15:
        if board[i] != i or board[i].get_data ("piece_num") != i:
            return

def piece_enter_notify (item, target, event):
    text = item.get_data ("text")
    text.props.fill_color = "white"
    return False

def piece_leave_notify (item, target, event):
    text = item.get_data ("text")
    text.props.fill_color = "black"
    return False

def piece_button_press (item, target, event):
    canvas = item.get_canvas ()
    board = canvas.get_data ("board")
    num = item.get_data ("piece_num")
    pos = item.get_data ("piece_pos")
    text = item.get_data ("text")

    y = pos / 4
    x = pos % 4
    
    move = True
    
    if ((y > 0) and (board[(y - 1) * 4 + x] == None)):
        dx = 0.0
        dy = -1.0
        y -= 1

    elif ((y < 3) and (board[(y + 1) * 4 + x] == None)):
        dx = 0.0
        dy = 1.0
        y += 1

    elif ((x > 0) and (board[y * 4 + x - 1] == None)):
        dx = -1.0
        dy = 0.0
        x -= 1

    elif ((x < 3) and (board[y * 4 + x + 1] == None)):
        dx = 1.0
        dy = 0.0
        x += 1
    else:
        move = False
        
    if (move):
        newpos = y * 4 + x
        board[pos] = None
        board[newpos] = item
        item.set_data("piece_pos", newpos)
        item.translate(dx * PIECE_SIZE, dy * PIECE_SIZE)

    test_win(board)

def setup_item_signals (item):
    item.connect ("enter_notify_event", piece_enter_notify)
    item.connect ("leave_notify_event", piece_leave_notify)
    item.connect ("button_press_event", piece_button_press)

def scramble(object, canvas):
    board = canvas.get_data("board")
    
    pos = 0
    i = 0
    
    while pos < 16:
        if board[pos] == None:
            break
        pos += 1

    while i < SCRAMBLE_MOVES:
            
        dir = random.randint(0, 3)
        
        x = 0
        y = 0
        
        if ((dir == 0) and (pos > 3)):
            y = -1
        elif ((dir == 1) and (pos < 12)):
            y = 1
        elif ((dir == 2) and ((pos % 4) != 0)):
            x = -1
        elif ((dir == 3) and ((pos % 4) != 3)):
            x = 1
        else:
            continue

        oldpos = pos + y * 4 + x
        board[pos] = board[oldpos]
        board[oldpos] = None
        board[pos].set_data("piece_pos", pos)
        board[pos].translate(-x * PIECE_SIZE, -y * PIECE_SIZE)
        pos = oldpos
        i += 1

def get_piece_color(piece):
    y = piece / 4
    x = piece % 4
    r = ((4 - x) * 255) / 4
    g = ((4 - y) * 255) / 4
    b = 128

    buf = "#%02x%02x%02x" % (r, g, b)

    return buf

def create_canvas_fifteen ():
    vbox = gtk.VBox(False, 4)
    vbox.set_border_width(4)
    
    alignment = gtk.Alignment(0.5, 0.5, 0.0, 0.0)
    vbox.pack_start(alignment, True, True, 0)
    
    frame = gtk.Frame()
    frame.set_shadow_type(gtk.SHADOW_IN)
    alignment.add(frame)
    
    canvas = goocanvas.Canvas()
    
    canvas.set_size_request(PIECE_SIZE * 4 + 1, PIECE_SIZE * 4 + 1)
    canvas.set_bounds(0, 0, PIECE_SIZE * 4 + 1, PIECE_SIZE * 4 + 1)
    
    board = []
    
    root = canvas.get_root_item()
    canvas.set_data("board", board)
    
    frame.add(canvas)
    
    button = gtk.Button("Scramble")
    button.set_data("board", board)
    button.connect("clicked", scramble, canvas)

    vbox.pack_start(button, False, False, 0)
    
    i = 0
    while i < 15:
        y = i / 4;
        x = i % 4;
    
        gr = goocanvas.Group()
        board.append(gr)
        root.add_child(board[i], -1)
        
        board[i].translate(x * PIECE_SIZE, y * PIECE_SIZE)
        setup_item_signals (board[i])
        
        rect = goocanvas.Rect(parent = board[i],
                              x=0, y=0,
                              width=PIECE_SIZE, height=PIECE_SIZE,
                              fill_color = get_piece_color (i),
                              stroke_color = "black",
                              line_width = 1.0)
        buf = "%d" % (i+1)
    
        text = goocanvas.Text(parent = board[i],
                              text = buf,
    					      x = PIECE_SIZE / 2.0,
    					      y = PIECE_SIZE / 2.0,
    					      font = "Sans bold 24",
    					      anchor = gtk.ANCHOR_CENTER,
    					      fill_color = "black")
        
        board[i].set_data("text", text)
        board[i].set_data("piece_pos", i)
        board[i].set_data("piece_num", i)
    
        i += 1
    
    board.append(None)
    
    return vbox

def main ():
    win = gtk.Window()
    win.connect("destroy", gtk.main_quit)
    
    vbox = create_canvas_fifteen ()
    
    win.add(vbox)
    win.show_all()
    
    gtk.main()

if __name__ == '__main__':
    main ()
