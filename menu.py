from tools import requestNumberBetween
import random

# 6. Skapa en meny
# I menyn ska användaren ha valet att kunna få veta beskrivningen på ett hus objekt och dess rum
# I menyn ska användaren ha valet att kunna få veta beskrivningen på ett hus objekts rum objekt och dess möbler
# I menyn ska användaren ha valet att kunna få veta beskrivningen på ett rum objekts möbelobjekt
# I menyn ska användaren ha valet att använda ett möbelobjekt
# Använd menyn för att utforska hus(et) skapat i uppgift del 5

class Menu:
  index = {
    'itemStart': 1,
    'exit': 0,
    'goUp': -1,
    'tornado': 5000
  }

  def __init__(self, houses):
    self.houses = houses

  def __str__(self):
    return 'Välkommen in till vår fastighetsbyrå'

  def __len__(self):
    return len(self.houses)

  def getCollection(self):
    return self.houses

  def start(self):
    self.showHouses()
  
  def printItems(self, items):
    for i, item in enumerate(items, start=self.index['itemStart']):
      print(f'{i} - {item}')
    
  def showHouses(self):
    choice = self.printInfo(
      self,
      'Välj ett hus att utforska',
      False
    )

    if choice == self.index['exit']:
      return
    if choice == self.index['tornado']:
      self.tornado()
      self.showHouses()
    else:
      return self.showHouse(
        self.houses[choice - 1]
      )

  # prints available potions
  # request users choice and return it 
  def printInfo(
    self,
    item,
    message,
    canGoUp = True,
    showTornado = True
  ):
    print('\n')
    print(item)    
    print(message)
    self.printItems(item.getCollection())
    if showTornado:
      print(f'{self.index['tornado']} - kör tornado')
    print(f'{self.index['exit']} - Avsluta')
    if canGoUp:
      print(f'{self.index['goUp']} - Gå upp')
    
    return requestNumberBetween(
      len(item.getCollection()),
      self.index['goUp'] if canGoUp else self.index['exit'],
      [self.index['tornado']] if showTornado else []
    )
  
  def showHouse(self, house):
    choice = self.printInfo(
      house,
      'Välj ett rum att utforska'
    )

    if choice == self.index['exit']:
      return
    elif choice == self.index['goUp']:
      return self.showHouses()
    elif choice == self.index['tornado']:
          self.tornado()
          self.showHouse(house)
    else:
      return self.showRoom(
        house.rooms[choice - 1],
        house
      )

  def showRoom(self, room, house):
    choice = self.printInfo(
      room,
      'Välj ett möbelobjekt att utforska'
    )

    if choice == self.index['exit']:
      return
    elif choice == self.index['goUp']:
      return self.showHouse(house)
    elif choice == self.index['tornado']:
      self.tornado()
      self.showRoom(room, house)
    else:
      return self.showFurniture(
        room.furniture[choice - 1],
        room,
        house
      )

  def showFurniture(self, furniture, room, house):
    choice = self.printInfo(
      furniture,
      f'Vill du använda {furniture}',
      True,
      False
    )

    if choice == self.index['exit']:
      return
    elif choice == self.index['goUp']:
      return self.showRoom(room, house)
    else:
      furniture.use()
      self.showFurniture(furniture, room, house)

  def getRandomIndex(self, arr):
    return random.randint(0, len(arr) - 1)
  
  def tornado(self):
    # lists to store all the furniture items and room items  
    furniture = []
    rooms = []
    # the code lower works because all the list is stored by references 
    # lists all the houses
    for house in self.houses:
      # adds all the rooms to the rooms list 
      rooms.extend(house.rooms)
      # and lists all the rooms in the current house
      for room in house.rooms:
        # adds the furniture to the furniture list
        furniture.extend(room.furniture)
        # and make the list empty
        room.removeFurniture()

    # here we have the all rooms in the all houses with no furniture
    # while there is furniture in the furniture list
    while len(furniture):
      # adds to random room
      rooms[
        self.getRandomIndex(rooms)
      # random furniture item which is removed from the list
      ].addFurniture(
        furniture.pop(self.getRandomIndex(furniture))
      )

    print('\nTornadon har k;rts. Kolla på möbelobjekt')
