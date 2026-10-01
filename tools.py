toolsMessages = {
  'requestNumber':'Ange ett heltal',
  'errorNumber': 'Du har angett {inp} som inte ser ut som ett tal. Ta en till försök!',
  'betweenStart': 'Välj ett tal mellan {min} och {max}',
  'betweenErr': 'talet är inte mellan {min} och {max}. Ta en försök till.',
  # 'requestLetter': 'Ange en bokstav',
  # 'errLetter': '{value} ser inte ut som en bokstav. Ta en försök till!',
}


def wordsDeclension(self, amount, word, suffix, removeLast = False):
  if amount == 0 or amount > 1:
    res = word[0: -1] if removeLast else word
    res += suffix
    return res

  return word

def requestNumber():
  while True:
    inp = input(f'{toolsMessages["requestNumber"]} ')
    try:
      number = int(inp)
      return number
    except:
      print(toolsMessages['errorNumber'].format(inp=inp))
      continue
  
def requestNumberBetween(max, min = 0):
  print(toolsMessages['betweenStart'].format(min=min, max=max))
  
  while True:
    number = requestNumber()
    if number > max or number < min:
      print(toolsMessages['betweenErr'].format(min=min, max=max))
      continue
    return number
