# player.py

class Player:
    def __init__(self, name, piece):
        """Initialise un joueur avec un nom et son symbole."""
        self.name = name
        self.piece = piece

    def get_move(self):
        """Demande au joueur dans quelle colonne il veut jouer."""
        try:
            return int(input(f"{self.name}, choisissez une colonne (1-7) : ")) - 1
        except ValueError:
            return -1
