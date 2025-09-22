import random
import numpy as np
from messages import victory_messages, defeat_messages, draw_messages


class TicTacToe:
    # class constant
    WINNING_COMBINATIONS = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6]           # diagonals
    ]

    def __init__(self, game_mode=1, difficulty='easy', user_symbol='X', user_index=1):
        # Game state attributes
        self.board = [''] * 9                   # 9-element list representing board positions (0-8)
        self.turn = 0                           # current turn counter (even=player, odd=opponent)
        self.game_over = False                  # True when game ends (win/tie)
        self.winner = None                      # stores winner symbol ('X'/'O') or None

        # Game configuration attributes
        self._game_mode = None                  # will be set by setter
        self.game_mode = game_mode
        self._difficulty = None
        self.difficulty = difficulty

        # Player configuration attributes
        self._user_symbol = None                # will be set by setter
        self.opponent_symbol = None             # opponent is the Computer, case PvC, or another Player, case PvP
        self._user_index = None

        # Set player symbol using property setter for validation
        self.user_symbol = user_symbol          # triggers validation and opponent_symbol update
        self.user_index = user_index

    #### Properties
    @property
    def game_mode(self):               #GETTER
        return self._game_mode
    @game_mode.setter
    def game_mode(self, value):        #SETTER
        if value not in [1,2]:
            raise ValueError("you must type 1 (for PvC) or 2 (for PvP)")
        self._game_mode = value

    @property
    def difficulty(self):               #GETTER
        return self._difficulty
    @difficulty.setter
    def difficulty(self, value):        #SETTER
        if value not in ['easy','normal','hard']:
            raise ValueError("difficulty must be easy, normal or hard")
        self._difficulty = value
    
    @property                          
    def user_symbol(self):             #GETTER
        return self._user_symbol
    @user_symbol.setter                
    def user_symbol(self, value):      #SETTER
        if value not in ['X','O']:
            raise ValueError("player symbol must be X or O")
        self._user_symbol = value
        self.opponent_symbol = 'O' if value == 'X' else 'X'

    @property                          
    def user_index(self):              #GETTER
        return self._user_index
    @user_index.setter                 
    def user_index(self, value):       #SETTER
        if value not in [1,2]:
            raise ValueError("your answer must be 1 (being the first to play) or 2 (being the second)")
        self._user_index = value - 1   # converts to 0 or 1. Usefull when compared to "self.turn % 2"
        
    @property
    def current_player(self):
        # even turns = player 1, odd turns = player 2. The user_index tells which is which
        return self.user_symbol if self.turn % 2 == self.user_index else self.opponent_symbol


    #### Methods
    def display_board(self, show_numbers=True):
        # Display the current state of the board with position numbers for empty spaces

        display_item = []
        for i in range(9):
            if self.board[i] == '':
                display_item.append(str(i+1) if show_numbers else ' ')
            else:
                display_item.append(self.board[i])

        print(f" {display_item[0]} | {display_item[1]} | {display_item[2]} ")
        print("-----------")
        print(f" {display_item[3]} | {display_item[4]} | {display_item[5]} ")
        print("-----------")
        print(f" {display_item[6]} | {display_item[7]} | {display_item[8]} \n")
        
    def is_valid_move(self, position):
        # Check if position (1-9) is valid and empty.
        if position<1 or position>9:
            return False
        
        return self.board[position - 1] == ''

    def make_move(self, position, symbol = None):
        # Make a move at position (1-9). Returns True if successful.
        if symbol == None:
            symbol = self.current_player

        if not self.is_valid_move(position):
            return False
        
        self.board[position - 1] = symbol
        #self.turn += 1                                  # updates turn counter
        return True
    
    def has_winner(self, symbol = None):
        if symbol == None:
            symbol = self.current_player

        # Check if there's a winner. Updates game_over and winner attributes.
        for line in self.WINNING_COMBINATIONS:          # each line is a winning combination
            symbols = [self.board[i] for i in line]     # ex1: ['X','X','X']  | ex2: ['','','O']
            symbols = set(symbols)                      #      {'X'} => 1     |      {'','O'} => 2
            
            if len(symbols) == 1 and symbol in symbols: # winning condition
                self.winner = symbol
                self.game_over = True
                return True
            
        return False
    
    def clear_winner(self):
        self.winner = None
        self.game_over = False

    def is_board_full(self):
        # Check if there's still a empty position ('').
        return not '' in self.board
    
    def minimax(self, depth, is_max, alpha = -np.inf, beta = np.inf):
        # Evaluate if current state is a leaf ot the tree
        if self.has_winner(self.opponent_symbol):
            return 10-depth, None                   # the faster the victory (less depth) the better 
        elif self.has_winner(self.user_symbol):
            return depth-10, None                   # the slower the defeat (greater depth) the better 
        elif self.is_board_full():
            return 0, None
        
        # There are still branches to explore
        best_move = None

        if is_max:     #### MAX turn (computer): is_max is TRUE
            best_score = -np.inf

            for position in range(1,10):
                if self.is_valid_move(position):
                    self.board[position - 1] = self.opponent_symbol # make a move
                    score, _ = self.minimax(depth+1, False, alpha, beta) # child nodes with turn rotation
                    self.board[position - 1] = '' # undo the move
                    self.clear_winner()

                    if score > best_score:
                        best_score = score
                        best_move = position
                    
                    alpha = max(alpha, best_score)

                    if alpha >= beta:
                        break               #cut the other branches

        else:          #### MIN turn (user): is_max is FALSE 
            best_score = np.inf

            for position in range(1,10):
                if self.is_valid_move(position):
                    self.board[position - 1] = self.user_symbol # make a move
                    score, _ = self.minimax(depth+1, True, alpha, beta) # child nodes with turn rotation
                    self.board[position - 1] = '' # undo the move
                    self.clear_winner()

                    if score < best_score:
                        best_score = score
                        best_move = position

                    beta = min(beta, best_score)

                    if alpha >= beta:
                        break               #cut the other branches
            
        return best_score, best_move

    def computer_move(self):
        ###### EASY MODE ######
        if self.difficulty == 'easy':
            # Choses a random position
            while True:
                position = random.randint(1,9)
                if self.make_move(position):
                    return position

        ###### NORMAL MODE ######
        elif self.difficulty == 'normal':
            # Tries to win (if it's possible)
            for position in range(1,10):
                if self.make_move(position):
                    if self.has_winner():
                        return position
                    self.board[position-1] = ''

            # If can't win, tries to block player 1 victory (if it's possible)
            for position in range(1,10):
                if self.make_move(position, self.user_symbol): # We are using the user_symbol to check if the user is able to win
                    if self.has_winner(self.user_symbol):
                        self.clear_winner() #we dont want the game to end

                        self.board[position-1] = self.opponent_symbol 
                        return position
                    self.board[position-1] = ''

            # Choses a random position otherwise
            while True:
                position = random.randint(1,9)
                if self.make_move(position):
                    return position

        ###### HARD MODE ######
        else:
            _ , position = self.minimax(0,True)
            self.clear_winner()
            self.make_move(position)
            return position

def replay():
    #Asks the player if they want to play another game
    while True:
        try:
            replay = input("\nDo you want to play again? ").strip().lower()
            if replay in ('yes','y'):
                return True
            elif replay in ('no','n'):
                return False
            else:
                print("Invalid input. Please enter yes or no")
        except (KeyboardInterrupt, EOFError):
            print("\nGame interrupted. Exiting...")
            return False


def main():

    while True:

        game = TicTacToe()

        print("=== Tic Tac Toe ===\n\nSelect game mode:\n1) Player vs Computer (PvC)\n2) Player vs Player (PvP)")
        while True:         # ask (and repeat) for game mode until a valid answer is provided
            try:
                game.game_mode = int(input("Enter 1 or 2: ").strip())
                break     # if game.user_index is valid, it will break out of the loop
            except ValueError as e:
                print(f"Error: {e}")
        
        if game.game_mode == 1:
            print(f"You selected PvC\n")
            while True:     # ask (and repeat) for difficulty until a valid answer is provided
                try:
                    game.difficulty = input("Select difficulty of the game:\nEasy, Normal or Hard? ").strip().lower()
                    break     # if game.difficulty is valid, it will break out of the loop
                except ValueError as e:
                    print(f"Error: {e}")

            print(f"You selected {game.difficulty.upper()} game\n")
            while True:     # ask (and repeat) for user symbol until a valid answer is provided
                try:
                    game.user_symbol = input("Wanna be X or O? ").strip().upper()
                    break     # if game.user_symbol is valid, it will break out of the loop
                except ValueError as e:
                    print(f"Error: {e}")

            print(f"You chose {game.user_symbol}. Computer will be {game.opponent_symbol}\n")
            print("Who plays first?\n1) You (you are Player 1)\n2) Computer (you are Player 2)")
            while True:     # ask (and repeat) for players order until a valid answer is provided
                try:
                    game.user_index = int(input("Enter 1 or 2: ").strip())
                    break     # if game.user_index is valid, it will break out of the loop
                except ValueError as e:
                    print(f"Error: {e}")

            print(f"You are player {game.user_index + 1}. Computer is player {2 - game.user_index}\n")
        else:
            print(f"You selected PvC\n")
            print(f"Player 1 uses symbol X and play first\nPlayer 2 uses symbol O\n")

        print("Positions are numbered 1-9. Good luck!")
        game.display_board(show_numbers=True)

        while not game.game_over:

            if game.turn % 2 == game.user_index: # user's turn
                while True:  # ask (and repeat) for player1 to play until a valid answer is provided
                    try:
                        print(f"Player {game.user_index+1}'s turn")
                        position = int(input("Please enter an available position: ").strip())
                        if game.make_move(position):
                            break
                        else:
                            print("Invalid position. Try again!")
                    except ValueError:
                        print("Please enter a number!")
            elif game.game_mode == 1:
                position = game.computer_move()
                print(f"Computer chose {position}")
            else:
                while True:  # ask (and repeat) for player2 to play until a valid answer is provided
                    try:
                        print(f"Player {2 - game.user_index}'s turn")
                        position = int(input("Please enter an available position: ").strip())
                        if game.make_move(position):
                            break
                        else:
                            print("Invalid position. Try again!")
                    except ValueError:
                        print("Please enter a number!")

            game.display_board(show_numbers=False)

            if game.has_winner():
                if game.winner == game.user_symbol:
                    print(random.choice(victory_messages).format("Player " +str(game.user_index+1)))
                    #print(f"Player {game.user_index+1} won! Congratulations!!")
                elif game.game_mode == 1:
                    print(random.choice(defeat_messages))
                else:
                    print(random.choice(victory_messages).format("Player " + str(2-game.user_index)))
                    #print(f"Player {2-game.user_index} won! Congratulations!!")


            elif game.is_board_full():
                game.game_over = True
                print(random.choice(draw_messages))

            else:
                game.turn += 1            # game is not over yet, so it will have a next turn
    
        if not replay():
            print("Thanks for playing!")
            break

if __name__ == '__main__':
    main()
