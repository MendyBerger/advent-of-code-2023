input = open("./input.txt", "r").read()


def main():
    [time, distance] = input.split("\n")
    time = int(time[10:].replace(" ", ""))
    distance = int(distance[10:].replace(" ", ""))

    left = 1
    right = (time - 1) // 2
    while left < right - 1:
        middle = (right + left) // 2
        move = time - middle
        traveled = middle * move
        if traveled > distance:
            right = middle
        else:
            left = middle
    first = right

    left = (time - 1) // 2
    right = (time - 1)
    while left < right - 1:
        middle = (right + left) // 2
        move = time - middle
        traveled = middle * move
        if traveled < distance:
            right = middle
        else:
            left = middle
    last = left

    return last - first + 1


print(main())
