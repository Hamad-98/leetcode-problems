def arrayRankTransform(arr):
       
  newArray = sorted(set(arr))
  d = {}
  l = []

  for i in range(len(newArray)):
    d[newArray[i]] = i+1

  for num in arr:
    l.append(d[num])

  return l 
