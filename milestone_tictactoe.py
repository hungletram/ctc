def tictactoe():
    position = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    board = lambda p: print('+-----------+\n| {} | {} | {} |\n|---|---|---|\n| {} | {} | {} |\n|---|---|---|\n| {} | {} | {} |\n+-----------+'.format(p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8]))
    print('WELCOME TO TIC-TAC-TOE!')
    board([i for i in range(1,10)])
    pick_marker = str(input('Player 1 picks (X/O): ')).upper()
    m1 = 'X' if pick_marker != 'O' else 'O'
    m2 = 'O' if m1 == 'X' else 'X'
    nextmove = lambda p: ' ' in p
    def winning(position):
        p = []
        for i in position:
            p += [i] if i != ' ' else ['']
        c1 = ''.join([p[0],p[1],p[2]]) in ['XXX','OOO']
        c2 = ''.join([p[3],p[4],p[5]]) in ['XXX','OOO']
        c3 = ''.join([p[6],p[7],p[8]]) in ['XXX','OOO']
        c4 = ''.join([p[0],p[3],p[6]]) in ['XXX','OOO']
        c5 = ''.join([p[1],p[4],p[7]]) in ['XXX','OOO']
        c6 = ''.join([p[2],p[5],p[8]]) in ['XXX','OOO']
        c7 = ''.join([p[0],p[4],p[8]]) in ['XXX','OOO']
        c8 = ''.join([p[2],p[4],p[6]]) in ['XXX','OOO']
        return any([c1,c2,c3,c4,c5,c6,c7,c8])
    phase = 1
    while nextmove(position) and not winning(position):
        board(position)
        p = int(input("Player {}'s turn (1-9): ".format([0,1,2][phase])))
        while position[p-1] != ' ':
            p = int(input("Occupied space, pick another (1-9): "))
        position[p-1] = ['',m1,m2][phase]
        phase *= -1
    else:
        board(position)
        return 'Player {} wins.'.format([0,1,2][phase]) if winning(position) else "It's a draw."
print(tictactoe())
