def finalValueAfterOperations(operations):
  final = 0
  for word in operations:
      if word == '--X' or word == 'X--':
          final -= 1
      elif word == 'X++' or word == '++X':
          final += 1
  return final
