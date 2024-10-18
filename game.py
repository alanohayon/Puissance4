# game.py

from board import Board
from player import Player

class Game:
    def __init__(self):
        """Initialise le jeu avec deux joueurs et un plateau."""
        self.board = Board()
        self.players = [
            Player(input("Nom du joueur 1 : "), 'X'),
            Player(input("Nom du joueur 2 : "), 'O')
        ]
        self.current_player_idx = 0

    def switch_player(self):
        """Change le tour du joueur."""
        self.current_player_idx = (self.current_player_idx + 1) % 2

    def play(self):
        """Boucle principale du jeu."""
        game_over = False
        while not game_over:
            self.board.display()
            current_player = self.players[self.current_player_idx]
            valid_move = False

            while not valid_move:
                column = current_player.get_move()
                if 0 <= column < self.board.COLUMNS:
                    valid_move = self.board.drop_piece(column, current_player.piece)
                if not valid_move:
                    print("Coup invalide. Essayez une autre colonne.")

            if self.board.check_winner(current_player.piece):
                self.board.display()
                print(f"Félicitations, {current_player.name} a gagné!")
                game_over = True
            elif self.board.is_full():
                self.board.display()
                print("Match nul!")
                game_over = True
            else:
                self.switch_player()
