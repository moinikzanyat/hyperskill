def print_field(field_str):
    print('---------')
    print('|', field_str[0], field_str[1], field_str[2], '|')
    print('|', field_str[3], field_str[4], field_str[5], '|')
    print('|', field_str[6], field_str[7], field_str[8], '|')
    print('---------')


def check_field(field_str):
    empty_cell = input_str.count('_') > 0
    lines = (input_str[:3], input_str[3:6], input_str[6:9], input_str[0:7:3], input_str[1:8:3], input_str[2:9:3],
             input_str[0:9:4], input_str[2:7:2])
    x_win = max(x.count('X') for x in lines) == 3
    o_win = max(x.count('O') for x in lines) == 3

    if x_win:
        print('X wins')
    elif o_win:
        print('O wins')
    elif empty_cell:
        print('Game not finished')
        return 1
    else:
        print('Draw')


def input_coordinates(loc_char):
    success_flag = False
    global input_str

    while not success_flag:
        success_flag = True
        x, y = input('Enter the coordinates: ').split()

        if x.isnumeric() and y.isnumeric:
            x = int(x)
            y = int(y)
            if x not in (1, 2, 3) or y not in (1, 2, 3):
                print('Coordinates should be from 1 to 3!')
                success_flag = False
            else:
                str_num = (x - 1) * 3 + y - 1
                if input_str[str_num] in ('X', 'O'):
                    print('This cell is occupied! Choose another one!')
                    success_flag = False
        else:
            print('You should enter numbers!')
            success_flag = False

    old_str = input_str
    input_str = ''
    for x in range(len(old_str)):
        if x != str_num:
            input_str += old_str[x]
        else:
            input_str += loc_char


input_str = '_________'
print_field(input_str)

next_char = 'X'
while check_field(input_str):
    input_coordinates(next_char)
    print_field(input_str)

    if next_char == 'X':
        next_char = 'O'
    else:
        next_char = 'X'
