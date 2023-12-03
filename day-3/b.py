input = open("./input.txt", "r").read().split("\n")


def main():
    output = 0
    touching_gears = {}

    for row_i, row in enumerate(input):
        start_col = 0
        for i, char in enumerate(row):
            if char.isdigit():
                if i == len(row) - 1 or not row[i+1].isdigit():
                    gear = gear_adjacent(row_i, start_col, i)
                    if gear:
                        num = int(row[start_col:i+1])
                        if gear in touching_gears:
                            output += (num * touching_gears[gear])
                        touching_gears[gear] = num
            else:
                start_col = i + 1

    return output



def gear_adjacent(row, start_col, end_col):
    start = max(0, start_col-1)
    end = min(len(input[0])-1, end_col+2)
    if row > 0:
        for col in range(start, end):
            if input[row-1][col] == "*":
                return (row-1, col)
    if row < len(input) - 1:
        for col in range(start, end):
            if input[row+1][col] == "*":
                return (row+1, col)
    if start_col > 0:
        if input[row][start_col-1] == "*":
            return (row, start_col-1)
    if end_col < len(input[0]) - 2:
        if input[row][end_col+1] == "*":
            return (row, end_col+1)



print(main())