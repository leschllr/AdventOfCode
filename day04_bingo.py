with open('input/bingo.txt') as f:
    bingo_input = [line.rstrip() for line in f]

drawn_numbers = [int(a) for a in bingo_input[0].split(',')]

#print(drawn_numbers)

def parse_line(line):
    numbers = line.split()
    return [int(val) for val in numbers]

boards = []
board = []
for i,line in enumerate(bingo_input[1:]):
    if line == '':
        if i != 0:
            boards.append(board)
        board = []
    else:
        row = parse_line(line)
        board.append(row)

#print(boards)

def check_board(board):
    rows = [0] * 5
    cols = [0] * 5
    remainder = sum([sum(val) for val in board])

    for i,draw in enumerate(drawn_numbers):
        for m,r in enumerate(board):
            for n,c in enumerate(r):
                if draw == c:
                    rows[m] += 1
                    cols[n] += 1
                    remainder -= draw
                    if rows[m] == 5 or cols[n] == 5:
                        #print(f'Bingo after {i} moves with number {draw} and remainder {remainder}')
                        return [i,draw,remainder]
    #print('No Bingo!')
    return False

quickest = 100
score = 0
winner = 0
for i,board in enumerate(boards):
    if check_board(board) == False:
        continue
    else:
        pos,number,remainder = check_board(board)
        if pos < quickest:
            quickest = pos
            winner = i
            score = number * remainder

print(f'Board number {winner} wins with a score of {score}')

slowest = 0
score = 0
winner = 0
for i,board in enumerate(boards):
    if check_board(board) == False:
        continue
    else:
        pos,number,remainder = check_board(board)
        if pos > quickest:
            quickest = pos
            winner = i
            score = number * remainder

print(f'Board number {winner} wins last with a score of {score}')