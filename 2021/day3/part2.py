DAY = 3 #TODO: change to correct day
PATH = f"day{DAY}\input.txt"

def main():
    with open(PATH) as file:
        lines = [line.rstrip() for line in file]
        o2Rating = o2RatingRecursive(lines, 0)[0]
        co2Rating = co2RatingRecursive(lines, 0)[0]
        print(int(o2Rating, 2) * int(co2Rating, 2))
        
def o2RatingRecursive(lines, bitPos):
    if (len(lines) == 1 or bitPos == len(lines[0])): return lines
    domBit = '0'
    count = sum(1 for line in lines if line[bitPos] == '1')
    if (count >= len(lines)/2): domBit = '1'
    return o2RatingRecursive([line for line in lines if line[bitPos] == domBit], bitPos +1)

def co2RatingRecursive(lines, bitPos):
    if (len(lines) == 1 or bitPos == len(lines[0])): return lines
    subBit = '0'
    count = sum(1 for line in lines if line[bitPos] == '1')
    if (count < len(lines)/2): subBit = '1'
    resultLines = [line for line in lines if line[bitPos] == subBit]
    return co2RatingRecursive(resultLines, bitPos +1)


if __name__ == "__main__":
    main()