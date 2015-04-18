from random import randint
from cell import Cell


class CellsMap:

    mines = 0
    rows = 0
    columns = 0
    cells = []
    
    def __init__(self, mines, rows, columns):
        self.mines = mines
        self.rows = rows
        self.columns = columns
        self._populate_cells()
        self._plant_mines()
        self._fill_safe_cells()
        
    def _populate_cells(self):
        """Create empty cells"""
        for row in range(0, self.rows):
	        self.cells.append([])
	        for column in range(0, self.columns):
	            cell = Cell()
	            cell.row = row
	            cell.col = column
	            self.cells[row].append(cell)
	            
    def _plant_mines(self):
        """Plant mines in random positions"""
        i = 0
        while i < self.mines:
            row = randint(0, self.rows - 1)
            col = randint(0, self.columns - 1)
            cell = self.cells[row][col]
            if not cell.isMine:
                cell.isMine = True
                i += 1
	
    def _fill_safe_cells(self):
	"""Fill empty(safe) cells with numbers of surronding mines"""
	for cell in self.cells:
	    mines_around = 0
	        
	# calculate cells in previous row
	if cell.row > 0:
	    # calculate previous cell, if not the first cell
	    if cell.col != 0:
	        if self.cells[cell.row-1][cell.col-1].isMine:
	            mines_around += 1
            # calculate next cell, if not last cell in row
            if cell.col != self.columns:
                if self.cells[cell.row-1][cell.col+1].isMine:
                    mines_around += 1
            # calculate above cell
            if self.cells[cell.row-1][cell.col].isMine:
                mines_around += 1
                        
	    # calculate cells in next row
	    if cell.row >= 0 and cell.row < self.rows:
	        # calculate previous cell, if not the first cell
	        if cell.col != 0:
	            if self.cells[cell.row+1][cell.col-1].isMine:
	                mines_around += 1
                # calculate next cell, if not last cell in row
                if cell.col != self.columns:
                    if self.cells[cell.row+1][cell.col+1].isMine:
                        mines_around += 1
                # calculate above cell
                if self.cells[cell.row+1][cell.col].isMine:
                    mines_around += 1
	        
	        # calculate cells in row
	        # calculate previous cell
            if cell.col != 0:
                if self.cells[cell.row][cell.col-1].isMine:
                    mines_around += 1
            # calculate next cell, if not last cell in row
            if cell.col != self.columns:
                if self.cells[cell.row][cell.col+1].isMine:
                    mines_around += 1
            # set the value of the cell to the number of mines found
            cell.value = mines_around

    def __len__(self):
	return self.rows
