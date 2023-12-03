from collections import Counter

POSSIBLE = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def main():
    input = open("input.txt", "r").read()

    output = 0

    for line in input.split("\n"):
        [id, data] = line.split(":")
        id = int(id[5:])
        game_counter = get_max_for_colors(data)
        if fits(game_counter):
            output += id

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


def fits(counter):
    for [color, count] in POSSIBLE.items():
        if counter[color] > count:
            return False
    return True


print(main())