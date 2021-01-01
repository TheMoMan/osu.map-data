def getIndexOfPartial(array: [str], substring: str):
  try:
    return [index for index, element in enumerate(array) if substring in element][0]
  except IndexError:
    return -1

def getElementFromPartial(array: [str], substring: str):
  try:
    return [s for s in array if substring in s][0]
  except IndexError:
    return ''

def getRightOfColon(string: str):
  try:
    return string.split(':')[1].strip()
  except:
    return ''
