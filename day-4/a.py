input = open("./input.txt", "r").read()


def main():
    output = 0

    for card in input.split("\n"):
        card = card.split(":")[1]
        [a, b] = card.split("|")
        a = into_int_set(a)
        b = into_int_set(b)
        overlap_count = len(a.intersection(b))
        if overlap_count > 0:
            output += (2 ** (overlap_count - 1))
        

    return output


def into_int_set(s):
    output = set()
    for num in s.split(" "):
        if num.isdigit():
            output.add(int(num))
    return output


print(main())