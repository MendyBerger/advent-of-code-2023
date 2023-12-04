input = open("./input.txt", "r").read().split("\n")


def main():
    card_counts = get_counts(len(input))

    for card in input:
        [id, card] = card.split(":")
        id = int(id[4:])
        [a, b] = card.split("|")
        a = into_int_set(a)
        b = into_int_set(b)
        overlap_count = len(a.intersection(b))
        for i in range(id+1, id+overlap_count+1):
            card_counts[i] += card_counts[id]

    return sum(card_counts.values())


def into_int_set(s):
    output = set()
    for num in s.split(" "):
        if num.isdigit():
            output.add(int(num))
    return output

def get_counts(len):
    output = {}
    for i in range(1,len+1):
        output[i] = 1
    return output


print(main())
