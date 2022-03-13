def isSumEqual(firstWord, SecondWord, targetWord):
  alphabet = {'a' : '0',  'b' : '1', 'c' : '2', 'd' : '3', 'e' : '4', 
              'f' : '5', 'g' : '6', 'h' : '7', 'i' : '8',  'j' : '9',  }

  def convertValue(string): # function that converts string to numerical value. Ie 'acb' -> '021'
      newString = ''
      
      for word in string:
          word = alphabet[word]
          newString += word
          
      return int(newString)

    
  firstWord = convertValue(firstWord)
  secondWord = convertValue(secondWord)
  targetWord = convertValue(targetWord)

  if firstWord + secondWord == targetWord:
      return True
  return False



"""
firstWord = 'acb' -> '021'
secondWord = 'cba' -> '210'
targetWord = 'cdb' -> '231

return true because '21' + '210' = '231'

"""
