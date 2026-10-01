from house import House
from room import Room
from furniture import Furniture
from interaction_furniture import InteractiveFurniture
from menu import Menu

# 5. Möblera ett hus
# Skapa minst 1 hus objekt
# Skapa minst 3 rum objekt och tilldela dem till hus objekts variabel för sekvens av rum
# Skapa minst 6 möbel objekt och tilldela dem till rum objekts variabel för sekvens av möbler
# Skapa minst 3 interaktiva möbel objekt och tilldela dem till rum objekts variabel för sekvens av möbler

tv = InteractiveFurniture(
  'TV Sharp',
  'plat och svart',
  ['påslagen', 'visar en film']
)
radio = InteractiveFurniture(
  'Radio Phillips',
  'liten men högljudd',
  ['påslagen', 'spelar musik']
)
stove = InteractiveFurniture(
  'Spis',
  'ren och svart',
  ['påslagen', 'värms upp']
)

vacuumCleaner = InteractiveFurniture(
  'Dammsugare',
  'röd',
  ['påslagen', 'surrar']
)
washingMachine = InteractiveFurniture(
  'Tvätt maskin',
  'vit',
  ['påslagen', 'Tvättar']
)
airConditioner = InteractiveFurniture(
  'Luftkonditionering',
  'kall',
  ['påslagen', 'blåser']
)

bed = Furniture('Säng', 'mjuk')
bedsideTable = Furniture('Soffbord', 'liten')
chair = Furniture('Stol', 'hög')
tvBank = Furniture('TV bänk', 'Vit')
lamp = Furniture('Lampa', 'grön')
table = Furniture('Bord', 'träig')

catHouse = Furniture('Cat hus', 'hög')
cupboard = Furniture('Skåp', 'grå')
microWave = Furniture('Micron', 'mörkblå')
officeTable = Furniture('Arbetsbord', 'grön')
officeChair = Furniture('Dator stol', 'mjuk')
tableLamp = Furniture('Bords lampa', 'liten')

library = Room(
  'Bibliotek',
  'Med trägolv',
  [tableLamp, catHouse, vacuumCleaner]
)
workingRoom = Room(
  'Arbetsrum',
  'Med tre fönstren',
  [officeChair, officeTable, airConditioner]
)
pantry = Room(
  'Förråd',
  'utan fönstren med dörren finns',
  [cupboard, washingMachine, microWave]
)

room = Room(
  'Vardagsrum',
  'stort och ljust',
  [tv, tvBank, radio]
)
bedRoom = Room(
  'Sovrum',
  'lItet och mörkt',
  [bed, bedsideTable, lamp]
)
kitchen = Room(
  'Kök',
  'med gröna vägg',
  [stove, table, chair]
)

house_1 = House(
  'Gaffelseglet',
  44,
  'Värmt',
  [bedRoom, kitchen, room]
)

house_2 = House(
  'Kokos kakan',
  14,
  'Stort',
  [library, workingRoom, pantry]
)

# print(house_2.getdescription())
# print(house_1.roomsDescription)

m = Menu([house_1, house_2])
m.start()

