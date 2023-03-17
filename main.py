from tkinter import *
import random


def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == '' and check_winner() is False:

        if player == players[0]:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + ' turn'))

            elif check_winner() is True:
                label.config(text=(players[0] + ' wins'))

            elif check_winner() == 'Tie':
                label.config(text='Tie')

        else:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + ' turn'))

            elif check_winner() is True:
                label.config(text=(players[1] + ' wins'))

            elif check_winner() == 'Tie':
                label.config(text='Tie')


def check_winner():
    for _row in range(4):
        if buttons[_row][0]['text'] == buttons[_row][1]['text'] == buttons[_row][2]['text'] == buttons[_row][3]['text'] != '':
            buttons[_row][0].config(bg='green')
            buttons[_row][1].config(bg='green')
            buttons[_row][2].config(bg='green')
            buttons[_row][3].config(bg='green')
            return True

    for _column in range(4):
        if buttons[0][_column]['text'] == buttons[1][_column]['text'] == buttons[2][_column]['text'] == buttons[3][_column]['text'] != '':
            buttons[0][_column].config(bg='green')
            buttons[1][_column].config(bg='green')
            buttons[2][_column].config(bg='green')
            buttons[3][_column].config(bg='green')
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] == buttons[3][3]['text'] != '':
        buttons[0][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][2].config(bg='green')
        buttons[3][3].config(bg='green')
        return True

    elif buttons[0][3]['text'] == buttons[1][2]['text'] == buttons[2][1]['text'] == buttons[3][0]['text'] != '':
        buttons[0][3].config(bg='green')
        buttons[1][2].config(bg='green')
        buttons[2][1].config(bg='green')
        buttons[3][0].config(bg='green')
        return True

    elif empty_spaces() is False:
        for row_ in range(4):
            for column_ in range(4):
                buttons[row_][column_].config(bg='yellow')
        return 'Tie'

    else:
        return False


def empty_spaces():
    space = 16

    for _row in range(4):
        for _column in range(4):
            if buttons[_row][_column]['text'] != '':
                space -= 1

    if space == 0:
        return False
    else:
        return True


def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + ' turn')

    for _row in range(4):
        for _column in range(4):
            buttons[_row][_column].config(text='', bg='#F0F0F0')


window = Tk()
window.title('Tic-Tac-Toe')
players = ['X', 'O']
player = random.choice(players)
buttons = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

label = Label(text=player + " Turn", font=('arial', 20))
label.pack(side='top')

reset_buttons = Button(text='restart', font=('arial', 13), command=new_game)
reset_buttons.pack(side='top')

frame = Frame(window)
frame.pack()

for row in range(4):
    for column in range(4):
        buttons[row][column] = Button(
            frame,
            text='',
            font=('arial', 20),
            width=5, height=2,
            command=lambda row=row, column=column: next_turn(row, column)
        )

        buttons[row][column].grid(row=row, column=column)

window.mainloop()
