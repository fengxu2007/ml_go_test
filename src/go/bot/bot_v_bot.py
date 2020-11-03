from go.agent import naive
from go.common import goboard
from go.common import gogame
from go.common import gotypes
from go.common.goprint import print_move, print_board, clear
import time

def main():
    board_size = 9
    game = gogame.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: naive.RandomBot(),
        gotypes.Player.white: naive.RandomBot()
    }
    
    while not game.is_over():
        time.sleep(0.3)
        #print(chr(27) + "[2J")
        #print('\033c')
        clear()
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)
        
if __name__ == '__main__':
    main()        
