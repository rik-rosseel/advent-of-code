# Template for advent of code input handeling

DAY = 6 #TODO: change to correct day
PATH = f"day{DAY}\input.txt"

def main():
    fishes = [0]*9
    with open(PATH) as file:
        line = [int(x) for x in file.readline().rstrip().split(',')]
    for fish in line:
        fishes[fish] += 1
    day = 0
    while day < 256:
        day += 1
        temp = fishes[0]
        for i in range(1, len(fishes)):
            fishes[i-1] = fishes[i]
        fishes[6] += temp
        fishes[8] = temp
    print(sum(fishes))




if __name__ == "__main__":
    main()