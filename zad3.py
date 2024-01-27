import random
def generate_boards():
    board_list=[]
    while len(board_list)<4:
        board=[]
        while len(board)<7:
            x = random.randint(0,8)
            y = random.randint(0,8)
            if all(x !=c[0] and y != c[1] and abs(x-c[0]) != abs(y-c[1]) for c in board):
                board.append((x,y))
        board_list.append(board)
    return board_list

print(generate_boards())