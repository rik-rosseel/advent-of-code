DAY = 2 #TODO: change to correct day
PATH = f"day{DAY}\input.txt"

def main():
    with open(PATH) as file:
        pos, depth = 0, 0
        while (line := file.readline().rstrip().split()):
            match line[0]:
                case 'up':
                    depth -= int(line[1])
                case 'down':
                    depth += int(line[1])
                case 'forward':
                    pos += int(line[1])
        print(pos * depth)


if __name__ == "__main__":
    main()