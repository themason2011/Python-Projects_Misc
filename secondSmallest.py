def secondSmallest(aList):
    firstSmallest = aList[0]
    firstSmallestIndex = 0

    for i in range(len(aList)): #Find the smallest number
        if aList[i] < firstSmallest:
            firstSmallest = aList[i]
            firstSmallestIndex = i

    aList.pop(firstSmallestIndex)   #Remove smallest number from list
    secondSmallest = aList[0]

    for item in aList:  #Find second smallest (now smallest) number in the list
        if item < secondSmallest:
            secondSmallest = item

    return secondSmallest
