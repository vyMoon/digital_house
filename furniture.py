# 3. Skapa en klass för möbler
# Möbel objekten ska ha en variabel för namn
# Möbel objekten ska ha en variabel för beskrivning
# Möbel objekten ska ha en funktion som returnerar namn och beskrivning
# Möbel objekten ska ha en funktion som "använder" möbel objektet

class Furniture:
  def __init__(self, name, description,):
    self.name = name
    self.description = description

  def getDescription(self):
    return f'{self.description} {self.name}'

  def use(self):
    print(f'{self.name} användes')

# m = Furniture('sofa', 'fin')

# print(m.getDescription())
# m.use()