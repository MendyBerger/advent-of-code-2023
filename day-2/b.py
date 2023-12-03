from collections import Counter

def main():
    input = open("input.txt", "r").read()

    output = 0

    for line in input.split("\n"):
        [id, data] = line.split(":")
        id = int(id[5:])
        game_counter = get_max_for_colors(data)
        output += total(game_counter)

    return output


def get_max_for_colors(game_data):
    counter = Counter()
    for round in game_data.split(';'):
        round = round.strip()
        for item in round.split(','):
            [count, color] = item.strip().split(" ")
            count = int(count.strip())
            color = color.strip()
            counter[color] = max(counter[color], count)
    return counter


def total(counter):
    output = 1
    for count in counter.values():
        output *= count
    return output


print(main())