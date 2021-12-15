DAY = 1 #TODO: change to correct day
PATH = f"day{DAY}\input.txt"

def main():
    with open(PATH) as file:
        incrementsAmount = 0
        previousValue = int(file.readline().rstrip())
        while (line := file.readline().rstrip()):
           value = int(line)
           if (value > previousValue): incrementsAmount += 1
           previousValue = value
        print(incrementsAmount)

if __name__ == "__main__":
    main()