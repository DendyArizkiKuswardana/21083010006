# Memasukkan nama pemain
nama = input("Hai! Siapa namamu Sobat? : ")
print("Halo!" ,nama, ",Saatnya bermain TIC TAC TOE bersamaku <3")

# Menampilkan  tabel Tic Tac Toe
print(20*' ',"~PETUNJUK PERMAINAN~")
print(20*' ','     |    |      ') 
print(20*' ','  1  | 2  | 3    ')
print(20*' ',"-----+----+----- ")
print(20*' ',"     |    |      ")
print(20*' ',"  4  | 5  | 6    ")
print(20*' ',"-----+----+----- ")
print(20*' ',"     |    |      ")
print(20*' ',"  7  | 8  | 9    \n")

# Menampilkan tabel Tic Tac Toe
def display_board():
    print()
    print('                          ~PETUNJUK PERMAINAN~')
    print('     |    |     ',10*' ','     |    |   ',)
    print('  '+board[1]+'  | '+board[2]+'  | '+board[3]+'   ',10*' ','  1  | 2  | 3  ')
    print('-----+----+-----',10*' ',"-----+----+-----")
    print('     |    |     ',10*' ',"     |    |     ")
    print('  '+board[4]+'  | '+board[5]+'  | '+board[6]+'   ',10*' ',"  4  | 5  | 6   ")
    print('-----+----+-----',10*' ',"-----+----+-----")
    print('     |    |     ',10*' ',"     |    |      ")
    print('  '+board[7]+'  | '+board[8]+'  | '+board[9]+'   ',10*' ',"  7  | 8  | 9    \n\n")


# Membuat pilihan jawaban pemain
def human_input(mark):
    while True:
        inp = input(f"[Giliranmu] '{mark}' pilih penempatan karaktermu, sesuai petunjuk:")
        if inp.isdigit() and int(inp) <10 and int(inp) >0:
            inp = int(inp)
            if board[inp] == " ":
                return inp
            else:
                print(f"[Giliranmu] '{mark}' Pilihanmu sudah terisi. Coba angka lain")
        else:
            print(f"[Giliranmu] '{mark}' Kamu harus memilih angka 1 - 9!!!")


def winning(mark,board):
    winning_place = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == mark:
            return True


def win_move(i,board,mark):
    temp_board = list(board)
    temp_board[i] = mark
    if winning(mark,temp_board):
        return True
    else:
        return False


def cpu_input(cpu , human , board):
    for i in range(1,10):
        if board[i] == ' ' and win_move(i,board,cpu):
            return i
    for i in range(1,10):
        if board[i] == ' ' and win_move(i,board,human):
            return i
    for i in [5,1,7,3,2,9,8,6,4]:
        if board[i] == ' ':
            return i

def new_game():
    while True:
        nxt = input('Mau maen lagi?(y/n):')
        if nxt in['y','Y']:    # Jika bermain lagi, maka akan permainan segera dimulai kembali
            again = True
            break
        elif nxt in ['n','N']:     # Jika tidak bermain lagi, maka permaianan akan usai
            print('KOK BUYAR SIH' ,nama, ">//<" )
            again = False
            break
        else:
            print('Enter correct input')
    if again:    
        print('		______________________________')
        print('		|                             |')
        print('		|      BABAK SELANJUTNYA      |')
        print('		|_____________________________|')
        main_game()
    else:
        return False

 
def win_check(human , cpu):
    winning_place = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == human:
            print('SELAMAT' ,nama, '! ,Kamu MENANG')
            if not new_game():
                return False
        elif board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == cpu:
                print('KAMU KALAH!')
                if not new_game():
                    return False
    if ' ' not in board:
        print('MATCH DRAW!!')
        if not new_game():
            return False
    return True

print("Sebelum bermain," ,nama, "pilih karaktermu dulu ya")

def user_choice():
    while True:
        inp = input(' mau "x" apa "o" nih?: ')
        if inp in ['x' , 'X']:
            print('Kamu memilih "X".\n Kamu boleh jalan dulu')
            return 'x','o'
        elif inp in ['O','o']:
            print('Kamu memilih "O".\n aku jalan duluan.')
            return 'o','x'
        else:
            print('kamu salah memasukkan pilihan[x/o]!')


def main_game():
    global board
    play = True
    board =['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    human , cpu = user_choice()
    display_board()
    while play:
        if human == 'x':
            x = human_input(human)
            board[x] = human
            display_board()
            play = win_check(human , cpu)
            if play:
                o = cpu_input(cpu , human , board)
                print(f'Aku pilih:{o}')
                board[o] = cpu
                display_board()
                play = win_check(human , cpu)
        else:
            x = cpu_input(cpu , human , board)
            print(f'Aku pilih:{x}')
            board[x] = cpu
            display_board()
            play = win_check(human , cpu)
            if play:
                o = human_input(human)
                board[o] = human
                display_board()
                play = win_check(human , cpu)

           
if __name__ == '__main__':
    main_game()
