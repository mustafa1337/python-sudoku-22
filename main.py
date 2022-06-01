
def possible(row, column, number) :
    global sudoku
    #Is the number appearing in the given row?
    for i in range(0,9):
        if sudoku[row] [i] == number:
            return False
    #Is the number appearing in the given column?
    for i in range(0,9):
        if sudoku[i] [column] == number:
            return False
    #Is the number appearing in the given row?
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0,3):
        for j in range (0,3):
            if sudoku[y0+i] [x0+j] == number:
                return False
    return True

def solve() :
    global grid
    for row in range(0,9):
        for column in range(0,9):
            if sudoku[row] [column] == 0:
               for number in range(1,10):
                   if possible(row, column, number):
                       sudoku[row] [column] = number
                        solve()
                        sudoku[row] [column]= 0

                    return

#beispiel:

sudoku = [
[0, 0, 6, 0, 5, 4, 9, 0, 0],
[1, 0, 0, 0, 6, 0, 0, 4, 2],
[7, 0, 0, 0, 8, 9, 0, 0, 0],
[0, 7, 0, 0, 0, 5, 0, 8, 1],
[0, 5, 0, 3, 4, 0, 6, 0, 0],
[4, 0, 2, 0, 0, 0, 0, 0, 0],
[0, 3, 4, 0, 0, 0, 1, 0, 0],
[9, 0, 0, 8, 0, 0, 0, 5, 0],
[0, 0, 0, 4, 0, 0, 3, 0, 7]
]
#output:

[2, 3, 6, 8, 5, 4, 9, 1, 7]
[1, 8, 9, 5, 6, 7, 0, 4, 2]
[7, 1, 2, 4, 8, 9, 6, 3, 5]
[3, 7, 6, 2, 9, 5, 4, 8, 1]
[8, 5, 1, 3, 4, 7, 6, 2, 9]
[4, 6, 2, 9, 1, 3, 7, 0, 0]
[5, 3, 4, 6, 2, 7, 1, 9, 8]
[9, 2, 4, 8, 3, 7, 0, 5, 0]
[6, 9, 5, 4, 8, 1, 3, 2, 7]
