input = open("./input.txt", "r").read()


def main():
    [times, distances] = input.split("\n")
    times = [int(time) for time in times.split()[1:]]
    distances = [int(distance) for distance in distances.split()[1:]]

    output = 1

    for i in range(len(times)):
        time = times[i]
        distance = distances[i]
        ways = 0
        for speed in range(1, time):
            move = time - speed
            if speed * move > distance:
                ways += 1
        output *= ways

    return output


print(main())
