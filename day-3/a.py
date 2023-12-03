input = open("./input.txt", "r").read().split("\n")


def main():
    output = 0

    for row_i, row in enumerate(input):
        start_col = 0
        for i, char in enumerate(row):
            if char.isdigit():
                if i == len(row) - 1 or not row[i+1].isdigit():
                    if symbol_adjacent(row_i, start_col, i):
                        output += int(row[start_col:i+1])
            else:
                start_col = i + 1

    return output



def symbol_adjacent(row, start_col, end_col)-> bool:
    start = max(0, start_col-1)
    end = min(len(input[0])-1, end_col+2)
    if row > 0:
        for char in input[row-1][start:end]:
            if is_symbol(char):
                return True
    if row < len(input) - 1:
        for char in input[row+1][start:end]:
            if is_symbol(char):
                return True
    if start_col > 0:
        if is_symbol(input[row][start_col-1]):
            return True
    if end_col < len(input[0]) - 2:
        if is_symbol(input[row][end_col+1]):
            return True
    return False



def is_symbol(char) -> bool:
    return not char.isdigit() and char != "."



print(main())