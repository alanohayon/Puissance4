# board.py

class Board:
    ROWS = 6
    COLUMNS = 7
    EMPTY_SLOT = ' '

    def __init__(self):
        """Initialise le plateau avec des cases vides."""
        self.grid = [[self.EMPTY_SLOT for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]

    def display(self):
        """Affiche le plateau dans la console."""
        for row in self.grid:
            print('| ' + ' | '.join(row) + ' |')
        print('  ' + '   '.join([str(i+1) for i in range(self.COLUMNS)]))  # Numéro des colonnes

    def drop_piece(self, column, piece):
        """Ajoute un pion dans une colonne donnée."""
        for row in reversed(self.grid):
            if row[column] == self.EMPTY_SLOT:
                row[column] = piece
                return True
        return False

    def is_full(self):
        """Vérifie si le plateau est plein."""
        return all(row[column] != self.EMPTY_SLOT for column in range(self.COLUMNS) for row in self.grid)

    def check_winner(self, piece):
        """Vérifie si un joueur a gagné."""
        # Vérification horizontale
        for row in self.grid:
            for col in range(self.COLUMNS - 3):
                if row[col] == row[col + 1] == row[col + 2] == row[col + 3] == piece:
                    return True

        # Vérification verticale
        for col in range(self.COLUMNS):
            for row in range(self.ROWS - 3):
                if self.grid[row][col] == self.grid[row + 1][col] == self.grid[row + 2][col] == self.grid[row + 3][col] == piece:
                    return True

        # Vérification diagonale (haut gauche à bas droite)
        for row in range(self.ROWS - 3):
            for col in range(self.COLUMNS - 3):
                if self.grid[row][col] == self.grid[row + 1][col] == self.grid[row + 2][col] == self.grid[row + 3][col] == piece:
                    return True

        # Vérification diagonale (haut droite à bas gauche)
        for row in range(self.ROWS - 3):
            for col in range(3, self.COLUMNS):
                if self.grid[row][col] == self.grid[row + 1][col] == self.grid[row + 2][col] == self.grid[row + 3][col] == piece:
                    return True

        return False
