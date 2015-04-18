from gi.repository import Gtk
import game

class Window(Gtk.ApplicationWindow):
    def __init__(self):
        Gtk.Window.__init__(self, title="Mine Sweeper")
        self.width = 600
        self.height = 600
        self.grid = grid = Gtk.Grid()
        grid.set_hexpand(True)
        grid.set_vexpand(True)
        #self.set_default_size(300, 300)
        mines_count = 40
        self.mines_counter = Gtk.Label(mines_count)
        self.flags_counter = Gtk.Label("0")
        self.grid.attach(self.mines_counter, 0, 0, 1, 1)
        self.grid.attach(self.flags_counter, 1, 0, 1, 1)
        cells = CellsMap(mines_count, 10, 10)
        
        #self.draw_game_board(game.populate_cells(mines_count, 10, 10))
        self.add(grid)
        self.connect("delete-event", Gtk.main_quit)

    def draw_game_board(self, cells):
        #grid.set_row_homogeneous(True)
        #grid.set_row_spacing(20)
        row_count = 1
        for row in cells:
            column_count = 0
            for cell in row:
                btn = Gtk.Button(cell);
                btn.connect('clicked', self.on_btn_clicked)
                self.grid.attach(btn, column_count, row_count, 1, 1)
                column_count += 1
            row_count += 1
    
    
    def on_btn_clicked(self, btn):
        btn.set_sensitive(False)
        print btn.get_label()
        


if __name__ == '__main__':
    w = Window()
    w.show_all()
    Gtk.main()
