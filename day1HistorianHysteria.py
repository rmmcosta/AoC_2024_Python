import sys

l1 = [3,4,2,1,3,3]
l2 = [4,3,5,3,9,3]

def calculateTotalDistance(l1, l2):
    sortedL1 = sort(l1)
    sortedL2 = sort(l2)
    print(l1,l2,sortedL1,sortedL2)

    sum = 0
    for i in range(len(l1)):
       sum+=abs(sortedL2[i]-sortedL1[i])

    print(sum)

def calculateSimilarityScore(l1, l2):
    """
    Calculate a total similarity score by adding up each number in the left list
    after multiplying it by the number of times that number appears in the right list.
    :param l1:
    :param l2:
    :return:
    """
    similarityScore = 0
    for lValue in l1:
        similarityScore+=lValue*findMatches(lValue,l2)
    print(similarityScore)
    return similarityScore

def findMatches(value, values):
    count = 0
    for currValue in values:
        if currValue == value:
            count+=1
    return count

def sort(unsortedList):
    hasSwapped = True
    while(hasSwapped):
        hasSwapped = False
        for i in range(len(unsortedList)-1):
            if unsortedList[i] > unsortedList[i+1]:
                hasSwapped = True
                temp = unsortedList[i]
                unsortedList[i] = unsortedList[i+1]
                unsortedList[i+1] = temp
    return unsortedList
    #unsortedListSize = len(unsortedList)
    #if unsortedListSize == 1:
    #    return [unsortedList[0]]
    #if unsortedListSize == 2:
    #    if unsortedList[0] > unsortedList[1]:
    #        return [unsortedList[1],unsortedList[0]]
    #    else:
    #        return [unsortedList[0],unsortedList[1]]
    #else:
    #    middle = int(unsortedListSize/2)
    #    return sort(unsortedList[:middle]) + sort(unsortedList[middle:])

def processData(filename):
    l1 = []
    l2 = []
    with open(filename,"r") as file:
        for line in file:
           parts = line.split()
           print(parts)
           l1.append(int(parts[0]))
           l2.append(int(parts[1]))
    calculateTotalDistance(l1,l2)
    calculateSimilarityScore(l1,l2)

#calculateTotalDistance(l1,l2)
#calculateSimilarityScore(l1,l2)

if len(sys.argv) > 1:
    filename = sys.argv[1]
    print(f"processing file {filename}...")
    processData(filename)
else:
    print("you need to specify the file that must be processed!")
