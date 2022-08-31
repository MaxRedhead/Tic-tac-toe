print("                                     __________________________________________________________________________")
print('                                                     Добро пожаловать в игру "Крестики-нолики" !')
print('                                        В игре учавствуют два человека, один ходит крестиками, другой ноликами.')
print('                                            Побеждает тот игрок, кто первый соберёт три свои символа в ряд.')
print("                                     __________________________________________________________________________")

board = list(range(1, 10))


def game_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


def player(player_symbol):
    valid = False
    while not valid:
        player_answer = int(input("Куда поставим " + player_symbol + "? "))
        if 1 > player_answer < 9:
            print(print("Некорректный ввод. Вы уверены, что ввели правильную координату?"))
            continue

        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_symbol
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def win_three_in_a_row(a):
    win_combination = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for one_of_combination in win_combination:
        if a[one_of_combination[0]] == a[one_of_combination[1]] == a[one_of_combination[2]]:
            return a[one_of_combination[0]]
    return False


def game(win):
    counter = 0
    win = False
    while True:
        game_board(board)
        if counter % 2 == 0:
            player("X")
        else:
            player("O")
        counter += 1
        if counter > 4:
            tmp = win_three_in_a_row(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    game_board(board)


game(board)

input("Нажмите Enter для выхода!")
