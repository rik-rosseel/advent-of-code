# Template for advent of code input handeling

DAY = 5 #TODO: change to correct day
PATH = f"day{DAY}\input.txt"

def main():
    sparceMatrix = {}
    with open(PATH) as file:
        while (line := file.readline().rstrip()):
            coords =[[int(coord) for coord in coordStrings.split(",")] for coordStrings in line.split(" -> ")]
            x1, x2 = coords[0][0], coords[1][0]
            y1, y2 = coords[0][1], coords[1][1]
            yStep, xStep = 1, 1
            if y1 > y2: 
                yStep = -1
                y2 -= 1
            elif y1 < y2: y2 += 1
            if x1 > x2: 
                xStep = -1
                x2 -= 1
            elif x1 < x2: x2 += 1

            if  x1 == x2:
                if x1 not in sparceMatrix: sparceMatrix[x1] = {}
                for y in range(y1, y2, yStep):
                    if y in sparceMatrix[x1]:
                        sparceMatrix[x1][y] += 1
                    else: sparceMatrix[x1][y] = 1
                continue
            
            if y1 == y2:
                xRange = range(x1, x2, xStep)
                for x in xRange:
                    if x in sparceMatrix: 
                        if y1 in sparceMatrix[x]: sparceMatrix[x][y1] += 1
                        else: sparceMatrix[x][y1] = 1
                    else: sparceMatrix[x] = {y1: 1}
                continue

    overlapCount = 0
    for col in sparceMatrix.values():
        for value in col.values():
            if value > 1:
                overlapCount += 1

    print(overlapCount)



if __name__ == "__main__":
    main()