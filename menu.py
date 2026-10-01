from tools import requestNumberBetween
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
  }

  def __init__(self, houses):
    self.houses = houses
    self.showHouses()

  def printExitOption(self):
    print(f'0 - Avsluta')
  
  def printGoUpOption(self):
    print(f'-1 - Gå upp')
  
  def printItems(self, items):
    for i, item in enumerate(items, start=self.index['itemStart']):
      print(f'{i} - {item}')
    
  def showHouses(self):
    choice = self.printInfo(
      None,
      self.houses,
      'Välj ett hus att utforska',
      False
    )

    if choice == 0:
      return
    else:
      return self.showHouse(
        self.houses[choice - 1]
      )
  
  def printInfo(self, item, items, message, canGoUpp = True):
    if item:
      print(item)
    print(message)
    self.printItems(items)
    self.printExitOption()
    if canGoUpp:
      self.printGoUpOption()
    
    return requestNumberBetween(
      len(items),
      self.index['goUp'] if canGoUpp else self.index['exit']
    )
  
  def showHouse(self, house):
    choice = self.printInfo(
      house,
      house.rooms,
      'Välj ett rum att utforska'
    )

    if choice == 0:
      return
    if choice == -1:
      return self.showHouses()
    else:
      return self.showRoom(
        house.rooms[choice - 1],
        house
      )

  def showRoom(self, room, house):
    choice = self.printInfo(
      room,
      room.furniture,
      'Välj ett möbelobjekt att utforska'
    )

    if choice == 0:
      return
    if choice == -1:
      return self.showHouse(house)
    else:
      return self.showFurniture(
        room.furniture[choice - 1],
        room,
        house
      )

  def showFurniture(self, furniture, room, house):
    choice = self.printInfo(
      furniture,
      ['använda'],
      f'Vill du använda {furniture}',
    )

    if choice == 0:
      return
    elif choice == -1:
      return self.showRoom(room, house)
    else:
      furniture.use()
      self.showFurniture(furniture, room, house)