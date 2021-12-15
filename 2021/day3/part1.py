DAY = 3 #TODO: change to correct day
PATH = f"day{DAY}\input.txt"

def main():
    with open(PATH) as file:
        counts = [int(x) for x in file.readline().rstrip()]
        lineCount = 1
        while (line := file.readline().rstrip()):
            for i in range(len(counts)):
                counts[i] += int(line[i])
            lineCount += 1
        threshold = lineCount / 2
        gamma = ''.join('1' if x >= threshold else '0' for x in counts)
        epsilon = ''.join('1' if x == '0' else '0' for x in gamma)
        print(int(gamma, 2) * int(epsilon, 2))


if __name__ == "__main__":
    main()