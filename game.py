from random import randint
from termcolor import colored


class Game:
    time = 0
    

def main():
    print("Hello Player! Don not get blown!")
    colors = {0: "grey", 1: "blue", 2: "green", 3: "yellow", 
            4: "cyan", 5: "magenta", 6: "white", 7: "cyan",  "*": "red"}
    mines = 200
    rows = 20
    columns = 40
    cells = populate_cells(mines, rows, columns)
    for row in cells:
	for column in row:
	    text = colored(column, colors[column])
            print text,
	print

def populate_cells(mines, rows, columns):
    cells = []
    #populate cells
    for row in range(0, rows):
	cells.append([])
	for column in range(0, columns):
	    cells[row].append('-')
    cells_count = rows * columns
    i = 0
    #plant mines
    while(i < mines):
	row = randint(0, rows-1)
	column = randint(0, columns-1)
	# check if the cell already has a mine, pass if true,
	# insert a mine if empty
	if cells[row][column] == '*':
	    continue
	else:
	    cells[row][column] = '*'
	i += 1
	# write numbers in empty cells
    length = columns
    for row, columns in enumerate(cells):	
        for cell, value in enumerate(columns):
            if cells[row][cell] == '*' :
                continue
            mines_around = 0
	    # counting mines above
            if row > 0:
                if cell != 0:
                    if cells[row-1][cell-1] == '*':
                        mines_around += 1
                if cells[row-1][cell] == '*':
                    mines_around += 1
                if cell < length-1:
                    if cells[row-1][cell+1] == '*':
					    mines_around += 1
	    # counting mines in the same row
            if cell != 0:
                if cells[row][cell-1] == '*':
                    mines_around += 1
                if cell < length - 1:
                    if cells[row][cell+1] == '*':
                        mines_around += 1
	    # counting mines in the next row
            if row < (rows - 1):
                if cell != 0:
                    if cells[row+1][cell-1] == '*':
                        mines_around += 1
                if cells[row+1][cell] == '*':
                    mines_around += 1
                if cell < length - 1:
                    if cells[row+1][cell+1] == '*':
                        mines_around += 1		
            # set cell value
            cells[row][cell] = mines_around
    return cells

if __name__ == '__main__':
    main()
