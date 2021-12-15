DAY = 4 #TODO: change to correct day
PATH = f"day{DAY}\input.txt"

def main():
    with open(PATH) as file:
        nums = [int(num) for num in file.readline().rstrip().split(',')]
        cardsInput = [[int(num) for num in line.rstrip().split()] for line in file.readlines()]
        cards, card = [], []
        for line in cardsInput:
            if not line:
                if (card): cards.append(card)
                card = []
            else:
                card.append(line)
        num, bingo = playBingo(nums, cards)
        print(num* remainingSum(bingo))

def findHit(card, calledNum):
    for i in range(len(card)):
        for j in range(len(card[i])):
            if card[i][j] == calledNum: card[i][j] = -1

def findBingo(cards):
    for card in cards:
        colChecks = [0]*len(cards[0][0])
        for line in card:
            check = 0
            for i, num in enumerate(line):
                check += num
                colChecks[i] += num
            if check == -5: return card
        for col in colChecks:
            if col == -5: return card

def playBingo(nums, cards):
    for num in nums:
        for card in cards:
            findHit(card, num)
        bingo = findBingo(cards)
        if bingo: return num, bingo

def remainingSum(card):
    result = 0
    for line in card:
        for num in line:
            if not num == -1: result += num
    return result


if __name__ == "__main__":
    main()