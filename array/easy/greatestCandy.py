
def kidsWithCandies(candies, extraCandies):
    l = []
    maxNum = max(candies)

    for num in candies:
        if num + extraCandies >= maxNum:
            l.append(True)
        else:
            l.append(False)

    return l
