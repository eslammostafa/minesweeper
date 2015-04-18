from cells_map import CellsMap

def main():
    cells_map = CellsMap(40, 10, 10)
    for row in cells_map.cells:
        for cell in cells_map.cells[row]:
            print cell,
        print
        
if __name__ == '__main__':
    main()
