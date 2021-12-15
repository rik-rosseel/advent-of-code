# Template for advent of code input handeling

DAY = 6 #TODO: change to correct day
PATH = f"day{DAY}\input.txt"

def main():
    with open(PATH) as file:
        fishes = [int(x) for x in file.readline().rstrip().split(',')]
        day = 0
        while day < 80:
            day += 1
            newFishes = []
            for i in range(len(fishes)):
                fishes[i] -= 1
                if fishes[i] < 0:
                    fishes[i] = 6
                    newFishes.append(8)
            fishes.extend(newFishes)
        print(len(fishes))




if __name__ == "__main__":
    main()