"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


"""

def isAnagram(s, t):
  d = {}
  e = {}
  for word in s:
      if word not in d:
          d[word] = 1
      else:
          d[word] += 1

  for word in t:
      if word not in e:
          e[word] = 1
      else:
          e[word] += 1


  if len(d) != len(e):
      return False

  return d == e
