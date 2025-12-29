TRAIN_DATA = [

("Add 2 cups of rice to the pot.",
 {"entities": [(4, 5, "QUANTITY"), (6, 10, "UNIT"), (14, 18, "INGREDIENT")]}),

("Chop 1 onion finely.",
 {"entities": [(5, 6, "QUANTITY"), (7, 12, "INGREDIENT")]}),

("Boil water and add salt.",
 {"entities": [(19, 23, "INGREDIENT")]}),

("Mix 200 ml milk with 3 tablespoons sugar.",
 {"entities": [
     (4, 7, "QUANTITY"), (8, 10, "UNIT"), (11, 15, "INGREDIENT"),
     (21, 22, "QUANTITY"), (23, 35, "UNIT"), (36, 41, "INGREDIENT")
 ]}),

("Heat 2 tbsp oil in a pan.",
 {"entities": [(5, 6, "QUANTITY"), (7, 11, "UNIT"), (12, 15, "INGREDIENT")]}),

("Add one cup sugar gradually.",
 {"entities": [(4, 7, "QUANTITY"), (8, 11, "UNIT"), (12, 17, "INGREDIENT")]}),

("Pour 500 ml water into the bowl.",
 {"entities": [(5, 8, "QUANTITY"), (9, 11, "UNIT"), (12, 17, "INGREDIENT")]}),

("Use half teaspoon salt for seasoning.",
 {"entities": [(4, 8, "QUANTITY"), (9, 17, "UNIT"), (18, 22, "INGREDIENT")]}),

("Add tomatoes and onions to the curry.",
 {"entities": [(4, 12, "INGREDIENT"), (17, 23, "INGREDIENT")]}),

("Mix flour with milk and sugar.",
 {"entities": [(4, 9, "INGREDIENT"), (15, 19, "INGREDIENT"), (24, 29, "INGREDIENT")]}),

("Add 3 eggs and 200 g flour.",
 {"entities": [
     (4, 5, "QUANTITY"), (6, 10, "INGREDIENT"),
     (15, 18, "QUANTITY"), (19, 20, "UNIT"), (21, 26, "INGREDIENT")
 ]}),

("Fry onion in oil until golden.",
 {"entities": [(4, 9, "INGREDIENT"), (13, 16, "INGREDIENT")]}),

("Add 1 kg chicken to the pot.",
 {"entities": [(4, 5, "QUANTITY"), (6, 8, "UNIT"), (9, 16, "INGREDIENT")]}),

("Stir 250 ml cream gently.",
 {"entities": [(5, 8, "QUANTITY"), (9, 11, "UNIT"), (12, 17, "INGREDIENT")]}),

("Combine rice, lentils, and water.",
 {"entities": [(8, 12, "INGREDIENT"), (14, 21, "INGREDIENT"), (27, 32, "INGREDIENT")]}),

("Add butter as needed.",
 {"entities": [(4, 10, "INGREDIENT")]}),

("Pour 2 cups milk slowly.",
 {"entities": [(5, 6, "QUANTITY"), (7, 11, "UNIT"), (12, 16, "INGREDIENT")]}),

("Mix spices with yogurt.",
 {"entities": [(4, 10, "INGREDIENT"), (16, 22, "INGREDIENT")]}),

("Add 4 cloves garlic to the mix.",
 {"entities": [(4, 5, "QUANTITY"), (6, 12, "UNIT"), (13, 19, "INGREDIENT")]}),

("Use oil and salt for cooking.",
 {"entities": [(4, 7, "INGREDIENT"), (12, 16, "INGREDIENT")]}),

("Add 100 g cheese and butter.",
 {"entities": [
     (4, 7, "QUANTITY"), (8, 9, "UNIT"), (10, 16, "INGREDIENT"),
     (21, 27, "INGREDIENT")
 ]}),

("Mix 3 tbsp honey with lemon juice.",
 {"entities": [
     (4, 5, "QUANTITY"), (6, 10, "UNIT"), (11, 16, "INGREDIENT"),
     (22, 33, "INGREDIENT")
 ]}),

("Add coriander leaves on top.",
 {"entities": [(4, 20, "INGREDIENT")]}),

("Heat milk before adding sugar.",
 {"entities": [(5, 9, "INGREDIENT"), (24, 29, "INGREDIENT")]}),

("Add 2 sliced onions and tomatoes.",
 {"entities": [(4, 5, "QUANTITY"), (13, 19, "INGREDIENT"), (24, 32, "INGREDIENT")]}),

("Add 1 teaspoon salt.",
 {"entities": [(4, 5, "QUANTITY"), (6, 14, "UNIT"), (15, 19, "INGREDIENT")]}),

("Add 2 tablespoons oil.",
 {"entities": [(4, 5, "QUANTITY"), (6, 18, "UNIT"), (19, 22, "INGREDIENT")]}),

("Mix 3 tablespoons cocoa powder.",
 {"entities": [(4, 5, "QUANTITY"), (6, 18, "UNIT"), (19, 32, "INGREDIENT")]}),

("Pour 200 ml milk.",
 {"entities": [(5, 8, "QUANTITY"), (9, 11, "UNIT"), (12, 16, "INGREDIENT")]}),

("Add 1 tablespoon olive oil.",
 {"entities": [(4, 5, "QUANTITY"), (6, 16, "UNIT"), (17, 26, "INGREDIENT")]}),

("Mix 2 teaspoons baking powder.",
 {"entities": [(4, 5, "QUANTITY"), (6, 15, "UNIT"), (16, 30, "INGREDIENT")]}),

("Add 3 cloves minced garlic.",
 {"entities": [(4, 5, "QUANTITY"), (6, 12, "UNIT"), (20, 26, "INGREDIENT")]}),

("Stir 1 cup chopped onions.",
 {"entities": [(5, 6, "QUANTITY"), (7, 10, "UNIT"), (19, 25, "INGREDIENT")]}),

("Add 2 tablespoons melted butter.",
 {"entities": [(4, 5, "QUANTITY"), (6, 18, "UNIT"), (26, 32, "INGREDIENT")]}),

("Combine 1 cup fresh cream with sugar.",
 {"entities": [(8, 9, "QUANTITY"), (10, 13, "UNIT"), (14, 25, "INGREDIENT"),
               (31, 36, "INGREDIENT")]}),

("Mix 200 ml warm milk slowly.",
 {"entities": [(4, 7, "QUANTITY"), (8, 10, "UNIT"), (16, 20, "INGREDIENT")]}),

("Add half cup grated cheese.",
 {"entities": [(4, 8, "QUANTITY"), (9, 12, "UNIT"), (20, 26, "INGREDIENT")]}),

("Sprinkle 1 pinch salt on top.",
 {"entities": [(9, 10, "QUANTITY"), (11, 16, "UNIT"), (17, 21, "INGREDIENT")]}),

("Add 2 tablespoons soy sauce.",
 {"entities": [(4, 5, "QUANTITY"), (6, 18, "UNIT"), (19, 28, "INGREDIENT")]}),

("Mix 3 tablespoons cocoa powder with milk.",
 {"entities": [(4, 5, "QUANTITY"), (6, 18, "UNIT"), (19, 32, "INGREDIENT"),
               (38, 42, "INGREDIENT")]}),

("Add 1 teaspoon red chili powder.",
 {"entities": [(4, 5, "QUANTITY"), (6, 14, "UNIT"), (15, 32, "INGREDIENT")]}),

("Pour 250 ml coconut milk.",
 {"entities": [(5, 8, "QUANTITY"), (9, 11, "UNIT"), (12, 25, "INGREDIENT")]}),

("Add 2 cups chopped vegetables.",
 {"entities": [(4, 5, "QUANTITY"), (6, 10, "UNIT"), (19, 29, "INGREDIENT")]}),

("Mix 1 tablespoon lemon juice.",
 {"entities": [(4, 5, "QUANTITY"), (6, 16, "UNIT"), (17, 28, "INGREDIENT")]}),

]
