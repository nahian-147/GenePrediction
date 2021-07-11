def findPotentialCodingSegments(sequence,stopList):
    potentialCodingSegments = []
    i,j = 0,0
    for _ in range(len(stopList)-1):
        i,j = stopList[_],stopList[_+1]
        start = sequence[i:j].find('ATG') + i
        if start > i and (j+3-start)%3==0 and j+3-start >= 50:
            seq = sequence[start:j]
            potentialCodingSegments.append(tuple([(i,j),seq]))
    return potentialCodingSegments