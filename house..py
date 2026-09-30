# 1. Skapa en klass för hus
# Hus klassen ska ha en variabel för väg adress
# Hus objekten ska ha en variabel för adress nummer
# Hus objekten ska ha en variabel för beskrivning
# Hus objekten ska ha en variabel för sekvens av rum
# Hus objekten ska ha en funktion som returnerar namn och beskrivning
from room import Room

class House:
  tmpStr = {
    'description': 'Ett {description} hus på {street}, {adressNumber} med {rooms} rum. {roomsDescription}'
  }
  def __init__(self, street, adressNumber, description, rooms):
    if len(rooms) == 0: raise ValueError('Rooms array should no be empty')

    self.street = street
    self.adressNumber = adressNumber
    self.description = description
    self.rooms = rooms

  def getdescription(self):
    return self.tmpStr['description'].format(
      description=self.description,
      street=self.street,
      adressNumber=self.adressNumber,
      rooms=len(self.rooms),
      roomsDescription=self.roomsDescription
    )

  @property
  def roomsDescription(self):
    descriptions = [room.getDescription() for room in self.rooms]
    return ', '.join(descriptions)

# h = House(
#   'Gaffelseglet',
#   22,
#   'Stort',
#   [Room('sovrum', 'Mörkt'), Room('Kök', 'stort')]
# )

# print(h.getdescription())