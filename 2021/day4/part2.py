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
        num, bingo = findLastBingo(nums, cards)
        print(num * remainingSum(bingo))
        print(f"correct answer: 17435")

def findHit(card, calledNum):
    for i in range(len(card)):
        for j in range(len(card[i])):
            if card[i][j] == calledNum: card[i][j] = -1

def isBingo(card):
    colChecks = [0]*len(card[0])
    for line in card:
        check = 0
        for i, num in enumerate(line):
            check += num
            colChecks[i] += num
        if check == -5: return True
    for col in colChecks:
        if col == -5: return True
    return False

def removeBingos(cards):
    indices = []
    for cardIndex, card in enumerate(cards):
        if isBingo(card):
            indices.append(cardIndex)
    if indices:
        if len(indices) > 1:
            indices.reverse()
        for i in indices:
            del cards[i]

def findLastBingo(nums, cards):
    for i, num in enumerate(nums):
        for card in cards:
            findHit(card, num)
            if not len(cards) == 1:
                removeBingos(cards)
            elif isBingo(card):
                return num, card

def remainingSum(card):
    result = 0
    for line in card:
        for num in line:
            if not num == -1: result += num
    return result


if __name__ == "__main__":
    main()