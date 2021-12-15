from collections import deque

DAY = 1 #TODO: change to correct day
PATH = f"day{DAY}\input.txt"

def main():
    with open(PATH) as file:
        incrementsAmount = 0
        vals = deque()
        val1 = int(file.readline().rstrip())
        val2 = int(file.readline().rstrip())
        val3 = int(file.readline().rstrip())
        vals.append(val1 + val2 + val3)
        vals.append(val2 + val3)
        vals.append(val3)
        vals.append(0)

        while (line := file.readline().rstrip()):
           val = int(line)
           vals[1] += val
           vals[2] += val
           vals[3] = val
           if (vals[0] < vals[1]): incrementsAmount += 1
           vals.rotate(-1)
        print(incrementsAmount)

if __name__ == "__main__":
    main()