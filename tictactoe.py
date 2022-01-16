# Ryan Weinheimer 1/16/2022

def main():
    player = next_player("")
    game = create_game()
    while not (result_win(game) or result_draw(game)):
        game_display(game)
        make_move(player, game)
        player = next_player(player)
    game_display(game)
    print("Game won! Thanks for playing.")


def create_game():
    game = []
    for space in range(9):
        game.append(space + 1)
    return game


def game_display(game):
    print()
    print(f"{game[0]}|{game[1]}|{game[2]}")
    print('-|-|-')
    print(f"{game[3]}|{game[4]}|{game[5]}")
    print('-|-|-')
    print(f"{game[6]}|{game[7]}|{game[8]}")
    print()


def result_draw(game):
    for space in range(9):
        if game[space] != "x" and game[space] != "o":
            return False
    return True


def result_win(game):
    return (game[0] == game[1] == game[2] or
            game[3] == game[4] == game[5] or
            game[6] == game[7] == game[8] or
            game[0] == game[3] == game[6] or
            game[1] == game[4] == game[7] or
            game[2] == game[5] == game[8] or
            game[0] == game[4] == game[8] or
            game[2] == game[4] == game[6])


def make_move(player, game):
    space = int(input(f"{player}'s turn to choose a space (1-9): "))
    game[space - 1] = player


def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"


if __name__ == "__main__":
    main()
