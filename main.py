# This is the first Python project Tic Tac Toe.
# Course B5.6

g_array = [[' '] * 3 for i in range(3)]  # array for input X or O
blank = " "  # better to use it for readability of the code


def main():
    print("Welcome to Tic Tac Toe")
    print("Tic-tac-toe, noughts and crosses, or Xs and Os is a paper-and-pencil game\n"
          "for two players who take turns marking the spaces in a three-by-three grid with X or O\n"
          "You should input X or 0 into the empty box\n"
          " by giving coordinates (separated by blank) from zero to two on axis x and y\n")

    array_output()

    step = 0

    while True:
        step += 1
        mark = check_turn(step)
        print(f"\n{mark} turn")
        x, y = input_x_and_y()
        if step % 2 == 1:
            g_array[x][y] = 'X'
        else:
            g_array[x][y] = 'O'

        array_output()

        if check_winner(g_array, mark):
            print(f"\n{check_turn(step)} is a winner\n"
                  f"Game is over")
            break

        if step == 9:
            print("\nDraw in the game\n"
                  "Game is over.")
            break

    print("\nThanks for playing")


def array_output():
    print("Array for input\n")

    print(f"  | 0 | 1 | 2 |")
    for y, x in enumerate(g_array):
        print(f"---------------")
        row_str = f"{y} | {' | '.join(x)} |"
        print(row_str)


def input_x_and_y():
    while True:
        input_list = input("Input coordinates from 0 to 2 separated by blank for: ").split()

        if len(input_list) != 2:
            print("Input two numbers separated by blank")
            continue

        x, y = input_list

        if not (x.isdigit()) or not (y.isdigit()):
            print("Input numbers please")
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Input coordinates in range from 0 to 2")
            continue

        if g_array[x][y] != blank:
            print("This box is occupied. Please try another box")
            continue

        return x, y


def check_turn(step):
    if step % 2 == 1:
        return 'X'
    else:
        return 'O'


def check_winner(a, mark):
    # print(a)
    return (((a[0][0] == a[0][1] == a[0][2]) == mark) or
            ((a[1][0] == a[1][1] == a[1][2]) == mark) or
            ((a[2][0] == a[2][1] == a[2][2]) == mark) or
            ((a[0][0] == a[1][0] == a[2][0]) == mark) or
            ((a[0][1] == a[1][1] == a[2][1]) == mark) or
            ((a[0][2] == a[1][2] == a[2][2]) == mark) or
            ((a[0][0] == a[1][1] == a[2][2]) == mark) or
            ((a[0][2] == a[1][1] == a[0][2]) == mark))


if __name__ == '__main__':
    main()
