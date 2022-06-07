from random import shuffle
import copy

class SudokuGenerator:

    def __init__(self, grid=None):
        #Zähler der
        self.zaehler = 0
        #Leeres 9*9 Sudoku Feld wird erstellt
        self.grid = [[0 for a in range(9)] for b in range(9)]
        self.sudoku_fertig()
        self.original = copy.deepcopy(self.grid)

    def Erstelle_volles_sudoku(self, grid):
        # Erstellt ein voll ausgefülltes sudoku
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for a in range(0, 81):
            row = a // 9
            col = a % 9
            #findet das nächste leere kästchen
            if grid[row][col] == 0:
                #wählt zufällige Zahl in der Liste und kontrolliert ob sie an diesem Punkt richtig ist
                shuffle(number_list)
                for number in number_list:
                    if self.Zahl_position(grid, row, col, number):
                        #wenn sie dort richtig ist wird sie in das kästchen eingesetzt
                        grid[row][col] = number
                        #wenn nicht wird nach den nächsten freien Kästchen gesucht
                        if not self.finde_leeres_kästchen(grid):
                            return True
                        else:
                            #wenn das sudoku voll ausgefüllt wurde wird true zurückgegeben
                            if self.Erstelle_volles_sudoku(grid):
                                return True
                break
        grid[row][col] = 0
        return False

    def nummer_in_zeile (self, grid, row, number):
        # gibt aus ob die Zahl in der Zeile benutzt wurde
        if number in grid[row]:
            return True
        return False

    def nummer_in_spalte (self, grid, col, number):
        # gibt aus ob die Zahl in der Spalte benutzt wurde
        for a in range(9):
            if grid[a][col] == number:
                return True
        return False

    def num_used_in_subgrid(self, grid, row, col, number):
        # gibt aus ob die Zahl im Subgrid benutzt wurde
        sub_row = (row // 3) * 3
        sub_col = (col // 3) * 3
        for a in range(sub_row, (sub_row + 3)):
            for b in range(sub_col, (sub_col + 3)):
                if grid[a][b] == number:
                    return True
        return False

    def Zahl_position(self, grid, row, col, number):
        #Ruft die drei Funktionen zum check der Nummern auf
        if self.nummer_in_zeile(grid, row, number):
            return False
        elif self.nummer_in_spalte(grid, col, number):
            return False
        elif self.num_used_in_subgrid(grid, row, col, number):
            return False
        return True

    def finde_leeres_kästchen(self, grid):
        #gibt die koordinaten der nächsten leeren zelle zurück
        for a in range(9):
            for b in range(9):
                if grid[a][b] == 0:
                    return (a, b)
        return

    def test_sudoku(self, grid):
        # testet ob die zahl in der richtigen box ist
        for row in range(9):
            for col in range(9):
                num = grid[row][col]
                # entfernt die Nummer aus dem Sudoku um zu testen ob sie richtig ist
                grid[row][col] = 0
                if not self.Zahl_position(grid, row, col, num):
                    return False
                else:
                    #wenn sie richig ist wird sie wieder eingefügt
                    grid[row][col] = num
        return True

    def sudoku_lösung(self, grid):
        #löse das Sudoku durch backtracking
        for a in range(0, 81):
            row = a // 9
            col = a % 9
            # findet die nächste leere Zelle und checkt welche zahl dort hinein passt
            if grid[row][col] == 0:
                for number in range(1, 10):
                    if self.Zahl_position(grid, row, col, number):
                        grid[row][col] = number
                        if not self.finde_leeres_kästchen(grid):
                            self.zaehler += 1
                            break
                        else:
                            if self.sudoku_lösung(grid):
                                return True
                break
        grid[row][col] = 0
        return False

    def nicht_leere_Kästchen(self, grid):
        #gibt eine zufällige liste benutzter Kästchen aus
        volle_Kästchen = []
        for a in range(len(grid)):
            for b in range(len(grid)):
                if grid[a][b] != 0:
                    volle_Kästchen.append((a, b))
        shuffle(volle_Kästchen)
        return volle_Kästchen

    def entferne_nummern (self):
        #entfernt die nummern aus dem Sudoku
        # alles vollen kästchen werden gespeichert
        volle_Kaestchen = self.nicht_leere_Kästchen(self.grid)
        volle_kaestchen_zaehler = len(volle_Kaestchen)
        runden = 3
        while runden > 0 and volle_kaestchen_zaehler >= 17:
            row, col = volle_Kaestchen.pop()
            volle_kaestchen_zaehler -= 1
            entfernte_box = self.grid[row][col]
            self.grid[row][col] = 0
            # macht eine kopie des Sudokus
            grid_copy = copy.deepcopy(self.grid)
            # Lösungs zähler wird auf 0 gesetzt
            self.zaehler = 0
            self.sudoku_lösung(grid_copy)
            # wenn es mehr als eine lösung gibt wird die letzte benutze zahl wieder eingefügt
            if self.zaehler != 1:
                self.grid[row][col] = entfernte_box
                volle_kaestchen_zaehler += 1
                runden -= 1
        return

    def sudoku_ausgabe(self):
        for row in self.grid:
            print(row)
        return

    def sudoku_fertig (self):
        #Ruft die einzelnen Functions auf und Gibt das Sudoku am ende aus
        self.Erstelle_volles_sudoku(self.grid)
        self.entferne_nummern()
        self.sudoku_ausgabe()
        return

neues_Sudoku = SudokuGenerator()