read = "         "
def print_game():
    print("---------")
    print("|", read[0], read[1], read[2], "|")
    print("|", read[3], read[4], read[5], "|")
    print("|", read[6], read[7], read[8], "|")
    print("---------")

print_game()

def ch_x():
    x = False
    for i in range(0, 6, 3):
        x = read[0 + i] == read[1 + i] == read[2 + i] == 'X'
        if x:
            return x
    for i in range(0, 3):
        x = read[0 + i] == read[3 + i] == read[6 + i] == 'X'
        if x:
            return x
    if read[0] == read[4] == read[8] == 'X':
        x = True
        return x
    elif read[2] == read[4] == read[6] == 'X':
        x = True
        return x
    return x

def ch_o():
    x = False
    for i in range(0, 6, 3):
        x = read[0 + i] == read[1 + i] == read[2 + i] == 'O'
        if x:
            return x
    for i in range(0, 3):
        x = read[0 + i] == read[3 + i] == read[6 + i] == 'O'
        if x:
            return x
    if read[0] == read[4] == read[8] == 'O':
        x = True
        return x
    elif read[2] == read[4] == read[6] == 'O':
        x = True
        return x
    return x




there_is_no_w = True
x_step = True

while there_is_no_w:

    if ch_x():
        print('X wins')
        break

    if ch_o():
        print('O wins')
        break

    if " " not in read:
        print("Draw")
        break

    test = ["one", "two", "three"]
    test2 = ["1", "2", "3", "4", "5", "7", "8", "9", "0"]
    read = [x for x in read]
    cord = input("Enter the coordinates: ").split()
    if cord[0] in test or cord[1] in test:
        print("You should enter numbers!")
    elif cord[0] and cord[1] in test2:
        cord = [int(i) for i in cord]


        def co_to_idx():
            x = int(cord[1])
            y = int(cord[0])
            idx = ((3 * y - 1 + x) - 3)
            return idx


        if x_step:
            if co_to_idx() > 8 or co_to_idx() < 0:
                print("Coordinates should be from 1 to 3!")
            elif read[co_to_idx()] == "X" or read[co_to_idx()] == "O":
                print("This cell is occupied! Choose another one!")
            elif read[co_to_idx()] == "_":
                read[co_to_idx()] = read[co_to_idx()].replace("_", "X")
                print_game()
            elif read[co_to_idx()] == " ":
                read[co_to_idx()] = read[co_to_idx()].replace(" ", "X")
                print_game()
            x_step = False
        else:
            if co_to_idx() > 8 or co_to_idx() < 0:
                print("Coordinates should be from 1 to 3!")
            elif read[co_to_idx()] == "X" or read[co_to_idx()] == "O":
                print("This cell is occupied! Choose another one!")
            elif read[co_to_idx()] == "_":
                read[co_to_idx()] = read[co_to_idx()].replace("_", "O")
                print_game()
                x_step = True
            elif read[co_to_idx()] == " ":
                read[co_to_idx()] = read[co_to_idx()].replace(" ", "O")
                print_game()
                x_step = True




