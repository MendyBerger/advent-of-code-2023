input = open("./input.txt", "r").read()


def main():
    seeds = input.split('\n')[0][7:].split()
    seeds = list(map(int, seeds))

    maps_lists = []

    sets = input.split("\n\n")[1:]
    for s in sets:
        map_list = []
        for line in s.split("\n")[1:]:
            map_list.append(get_line_map(line))
        maps_lists.append(map_list)
    
    for i, seed in enumerate(seeds):
        seeds[i] = walk_trough_map_lists(maps_lists, seed)

    return min(seeds)

def walk_trough_map_lists(map_lists, num):
    for map_list in map_lists:
        for map in map_list:
            if num in map.source:
                num = map.convert(num)
                break
    return num


class Map:
    def __init__(self, source, offset):
        self.source = source
        self.offset = offset

    def convert(self, num):
        if num in self.source:
            return num + self.offset
        return num


def get_line_map(line):
    line = list(map(int, line.split()))
    [destination, source, len] = line
    return Map(range(source, source+len), destination-source)



print(main())
