import pygame
import sys
import time

# Инициализация Pygame
pygame.init()

# Установка размера окна
width = 300
height = 300
display_surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Крестики-нолики")

# Цвета, которые мы будем использовать в игре
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
#/Users/razzle/PycharmProjects/XO/main.py
# Координаты клеток
board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

# Инициализация шрифтов
game_font = pygame.font.Font(None, 30)
winner_font = pygame.font.Font(None, 40)


# Отрисовка игровых клеток
def draw_board():
    for i in range(1, 3):
        # Горизонтальные линии
        pygame.draw.line(display_surface, white, (0, i * 100), (300, i * 100), 2)

        # Вертикальные линии
        pygame.draw.line(display_surface, white, (i * 100, 0), (i * 100, 300), 2)


# Отрисовка крестика
def draw_X(row, col):
    pygame.draw.line(display_surface, red, (col * 100 + 10, row * 100 + 10), (col * 100 + 90, row * 100 + 90), 2)
    pygame.draw.line(display_surface, red, (col * 100 + 90, row * 100 + 10), (col * 100 + 10, row * 100 + 90), 2)


# Отрисовка нолика
def draw_O(row, col):
    pygame.draw.circle(display_surface, white, (col * 100 + 50, row * 100 + 50), 40, 2)


# Проверка, есть ли победитель
def check_for_winner():
    winner = None

    # Проходим по строкам и столбцам
    for i in range(3):
        if all(board[i][j] == "X" for j in range(3)):
            winner = "X"

        elif all(board[i][j] == "O" for j in range(3)):
            winner = "O"

        elif all(board[j][i] == "X" for j in range(3)):
            winner = "X"

        elif all(board[j][i] == "O" for j in range(3)):
            winner = "O"

    # Проверяем диагонали
    if all(board[i][i] == "X" for i in range(3)):
        winner = "X"

    elif all(board[i][i] == "O" for i in range(3)):
        winner = "O"

    elif all(board[i][2 - i] == "X" for i in range(3)):
        winner = "X"

    elif all(board[i][2 - i] == "O" for i in range(3)):
        winner = "O"

    return winner


# Отрисовка окна победителя
def draw_winner_window(winner):
    winner_text = winner_font.render("{} победил!".format(winner), True, black)
    pygame.draw.rect(display_surface, black, (75, 100, 150, 100))
    pygame.draw.rect(display_surface, white, (80, 105, 140, 90))
    display_surface.blit(winner_text,
                         (width / 2 - winner_text.get_width() / 2, height / 2 - winner_text.get_height() / 2))
    pygame.display.update()
    time.sleep(2)


# Основной игровой цикл
def gameLoop():
    global board

    # Определить, кто начинает игру крестиками
    turn = "X"
    running = True

    # Отрисовка игрового поля
    draw_board()

    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Определяем позицию клика мыши
                x, y = pygame.mouse.get_pos()

                # Определяем строку и столбец выбранной клетки
                row = y // 100
                col = x // 100

                # Проверяем, что клетка свободна
                if board[row][col] == "":
                    board[row][col] = turn

                    # Отрисовка крестика или нолика
                    if turn == "X":
                        draw_X(row, col)
                        turn = "O"
                    elif turn == "O":
                        draw_O(row, col)
                        turn = "X"

        # Проверяем, есть ли победитель
        winner = check_for_winner()
        if winner is not None:
            draw_winner_window(winner)
            running = False

        # Обновляем экран
        pygame.display.update()

    # Закрываем окно
    pygame.quit()
    sys.exit()


# Запускаем игру
gameLoop()

