## A valid board will have exactly one black king and exactly one white king
## Each player can only have at most 16 pieces, at most 8 pawns, and all pieces
## Must be on a valid space from '1a' to '8h'.


def evalChessBoard (board):
    pieces={'king':1,'queen':1,'bishop':2,'knight':2,'rook':2,'pawn':8}
    space=['a','b','c','d','e','f','g','h']
    players=['w','b']
    isLegit=0
    
    #check legit positions
    for pos in board.items():
        if(int(pos[0][0])<=8 and len(pos[0])== 2):
            for letter in space:
                if letter == pos[0][1]:
                    isLegit=1       
                    break
            if not isLegit:
                return False
            isLegit=0
        else:
            return False

    #Eval number of pieces
    for piece in pieces:
        for current_player in players:
            player_piece=current_player+piece
            count=0
            for board_piece in board.values():
                if player_piece == board_piece:
                    count+=1
                if count > pieces[piece]:
                    return False
    return True
                





print(evalChessBoard({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}))

print(evalChessBoard({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking','7f':'wpawn'}))

print(evalChessBoard({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking','4z':'wrook'}))

print(evalChessBoard({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'bking'}))


