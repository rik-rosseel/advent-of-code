# Template for advent of code input handeling

DAY = 0 #TODO: change to correct day
PATH = f"day{DAY}\input.txt"

def main():
    with open(PATH) as file:
        while (line := file.readline().rstrip()):
            pass


if __name__ == "__main__":
    main()