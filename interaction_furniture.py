from furniture import Furniture
# 4. Skapa en klass för interaktiva möbler
# Interaktiva Möbel objekten ska ha en variabel för namn
# Interaktiva Möbel objekten ska ha en variabel för beskrivning
# Interaktiva Möbel objekten ska ha en variabel för beskrivning av alternativt tillstånd
# Interaktiva Möbel objekten ska ha en funktion som returnerar namn och beskrivning
# Interaktiva Möbel objekten ska ha en funktion som "använder" möbel objektet.
# När man använder funktionen ska variabeln för beskrivning 
# och variabeln för beskrivning av alternativt tillstånd växla

class InteractiveFurniture(Furniture):
  def __init__(self, name, description, conditions):
    if len(conditions) < 2:
      raise ValueError('less than 2 conditions provided')
    super().__init__(name, description)
    self._conditions = conditions
    self.currentCondition = conditions[0]

  @property
  def description(self):
    return f'{self._description}, {self.currentCondition}'

  @description.setter
  def description(self, description):
    self._description = description
  
  def getDescription(self):
    return f'{self.name}, {self.description}'

  def use(self):
    self.switchCurrentCondition()
    print(f'{self.name} används, {self.currentCondition}')

  def switchCurrentCondition(self):
    currentIndex = self._conditions.index(self.currentCondition)
    nextIndex = 0 if currentIndex == (len(self._conditions) - 1) else currentIndex + 1
    self.currentCondition = self._conditions[nextIndex]


# im = InteractiveFurniture('TV', 'flat', ['påslagen', 'visar en film'])
# print(im.getDescription())
# im.use()
# # im.use()
# print(im.getDescription())