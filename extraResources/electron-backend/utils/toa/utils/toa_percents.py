import re
from utils.toa.get_statute import get_statute


def getPercentFromComparison(entry, nameOfCase):

    if nameOfCase == None:
        return 0

    if entry == nameOfCase:
        return 100
    else:
        # remove the white spaces and check if the name of the case is in the entry, the entry contains crap afterwards
        entryWithoutWhite = re.sub(' ', '', entry)
        nameOfCaseWithoutWhite = re.sub(' ', '', nameOfCase)
        if nameOfCaseWithoutWhite in entryWithoutWhite:
            return 100

        entryToLower = entry.lower()
        nameOfCaseToLower = nameOfCase.lower()

        percent = getPercentFromSplit(entryToLower, nameOfCaseToLower)
        return percent


def getPercentFromSplit(entry, nameOfCase):
    splitEntry = entry.split(' ')
    splitNameOfCase = nameOfCase.split(' ')

    splitEntry = makeVersusTheSame(splitEntry)
    splitNameOfCase = makeVersusTheSame(splitNameOfCase)

    count = 0
    percentOfEach = 100 / len(splitNameOfCase)
    # This was added because of incorrect bookmarking. The example was Moody v NY City / Mirand v City of New York...
    # Moody was matching better with Mirand despite having the first part of the name correct and not because of
    # where NY was abbreviated and New York was not. We give bonus count to the case if the first part matches.
    if splitEntry[0] == splitNameOfCase[0]:
        count += 2

    for i in splitNameOfCase:
        if i in splitEntry:
            count += 1

    percent = count * percentOfEach
    if percent > 60:
        return percent
    elif percent > 33:
        # check individual words and get a closer percentage
        newPercent = getPercentFromLetters(splitEntry, splitNameOfCase)
        return newPercent
    else:
        possible_statute = get_statute(entry, nameOfCase)
        count = 0
        for i in possible_statute['name_of_case']:
            if i in possible_statute['entry']:
                count += 1
        percent = count * percentOfEach
        if percent > 33:
            return percent

        return count * percentOfEach


def getPercentFromLetters(entry, nameOfCase):
    combinedEntry = ''.join(map(str, entry))
    combinedNameOfCase = ''.join(map(str, nameOfCase))
    count = 0
    percentOfEach = 100 / len(combinedNameOfCase)
    for i in range(0, len(combinedNameOfCase)):
        try:
            if combinedNameOfCase[i] == combinedEntry[i]:
                count += 1
        except:
            # If combinedNameOfCase is longer than combinedEntry
            continue
    percent = count * percentOfEach
    return percent


def makeVersusTheSame(arr):
    for i in range(0, len(arr)):
        if 'v' == arr[i] or 'v.' == arr[i]:
            arr[i] = 'v'
            return arr
    return arr
