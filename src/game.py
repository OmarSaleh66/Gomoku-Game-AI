class Game:
    def __init__(self, board_size=15):
        
        self.board_size = board_size
        self.board = [[None for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = 'B'  
        self.game_over = False
        self.winner = None
        self.move_history = []

    def reset_game(self):
       
        self.board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'B'
        self.game_over = False
        self.winner = None
        self.move_history = []

    def make_move(self, row, col):
       
        if self.game_over or not self.is_valid_move(row, col):
            return False

        self.board[row][col] = self.current_player
        self.move_history.append((row, col, self.current_player))
        
        if self.check_win(row, col):
            self.game_over = True
            self.winner = self.current_player
        elif self.is_board_full():
            self.game_over = True
        else:
            self.switch_player()
        
        return True

    def is_valid_move(self, row, col):
        
        return (
            0 <= row < self.board_size and 
            0 <= col < self.board_size and 
            self.board[row][col] is None
        )

    def switch_player(self):
       
        self.current_player = 'W' if self.current_player == 'B' else 'B'

    def check_win(self, row, col):
        
        directions = [
            (0, 1),   
            (1, 0),   
            (1, 1),   
            (1, -1)   
        ]

        player = self.board[row][col]
        
        for dr, dc in directions:
            count = 1  
            
         
            r, c = row + dr, col + dc
            while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == player:
                count += 1
                r += dr
                c += dc
            
          
            r, c = row - dr, col - dc
            while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == player:
                count += 1
                r -= dr
                c -= dc
            
            if count >= 5:
                return True
        
        return False

    def is_board_full(self):
        
        for row in self.board:
            if None in row:
                return False
        return True

    def get_board_state(self):
        """Return a copy of the current board state"""
        return [row[:] for row in self.board]

    def get_legal_moves(self):
        """Return a list of all legal moves (row, col)"""
        moves = []
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] is None:
                    moves.append((row, col))
        return moves

    def display_board(self):
        """Print the current board state to console (for debugging)"""
        print("  " + " ".join(str(i).rjust(2) for i in range(self.board_size)))
        for i, row in enumerate(self.board):
            print(str(i).rjust(2) + " " + " ".join('.' if cell is None else cell for cell in row))
