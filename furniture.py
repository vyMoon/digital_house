# 3. Skapa en klass för möbler
# Möbel objekten ska ha en variabel för namn
# Möbel objekten ska ha en variabel för beskrivning
# Möbel objekten ska ha en funktion som returnerar namn och beskrivning
# Möbel objekten ska ha en funktion som "använder" möbel objektet

class Furniture:
  _actions = ['använda']

  def __init__(self, name, description,):
    self.name = name
    self.description = description

  def __str__(self):
    return f'{self.description} {self.name}'

  def __len__(self):
    return len(self._actions)
  
  def getCollection(self):
    return self._actions
  
  def getDescription(self):
    return f'{self.description} {self.name}'

  def use(self):
    print(f'{self.name} användes')

# m = Furniture('sofa', 'fin')

# print(m.getDescription())
# m.use()