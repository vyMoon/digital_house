# 2. Skapa en klass för rum
# Rum objekten ska ha en variabel för namn
# Rum objekten ska ha en variabel för beskrivning
# Rum objekten ska ha en variabel för sekvens av möbler
# Rum objekten ska ha en funktion som returnerar namn och beskrivning
from furniture import Furniture 

class Room:
  tmplStr = {
    'description': 'Ett {name}, {description}. {furniture} finns i rummet.'
  }

  def __init__(self, name, description, furniture = []):
    self.name = name
    self.description = description
    self.furniture = furniture

  def stringifyFurniture(self):
    furniture = [item.getDescription() for item in self.furniture]
    return ', '.join(furniture) if len(furniture) else 'inget'
  
  def getDescription(self):
    return self.tmplStr['description'].format(
      name=self.name,
      description=self.description ,
      furniture=self.stringifyFurniture()
    )


# r = Room(
#   'sovrum',
#   'fint',
#   [Furniture('säng', 'mjuk'), Furniture('sofbord', 'trädig')]
# )

# r = Room(
#   'sovrum',
#   'fint',
#   []
# )

# print(r.getDescription())