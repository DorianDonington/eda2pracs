class TopChefException(Exception):
    pass

#  Structure to hold a chef
class Chef:
    def __init__(self, chef_id=None, chef_name=None, chef_restaurant=None):
        self.id = chef_id
        self.name = chef_name
        self.restaurant = chef_restaurant
        self.score = 0.0

    def get_id(self):
        return self.id

    def add_score(self, score):
        self.score += score

    def get_name(self):
        return self.name

    def get_restaurant(self):
        return self.restaurant

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def __str__(self):
        chef_str = "ID: %s; " % (str(self.id))
        chef_str += "NAME: %s; " % (self.name)
        chef_str += "RESTAURANT: %s; " % (self.restaurant)
        chef_str += "SCORE: %s" % (self.score)
        return chef_str

# Structure to hold all chefs
class Chefs:
    def __init__(self):
        self.chefs = {}
        self.next = 0
        self.sorted_chefs = []

    def exists(self, id):
        # Complete this function
        return False

    def get_ids(self):
        # Complete this function
        return None

    def add_chef(self, name, restaurant):
        """
        Funcion que se encarga de generar un nuevo chef y añadirlo al direccionario
        :param name: nombre de chef
        :param restaurant: nombre de restaurante
        :return: id de nuevo chef generado .
        """
        # Genera un nueva instancia chef
        new_Chef = Chef(self.next, name, restaurant)
        # Consultar id de nuevo chef
        chef_id = new_Chef.get_id()
        # Gudarda nuevo chef al diccionario
        self.chefs[chef_id] = new_Chef
        # incrementa contador de ids.
        self.next += 1
        # Devuelve chef_id
        return chef_id

    def get_chef(self, id):
        # Complete this function
        return None

    def is_sorted(self):
        # Complete this function
        return False

    def sort_chefs(self):
        # Complete this function
        pass

    def get_top_n(self, n=1):
        # Complete this function
        return None

    def __str__(self):
        # Complete this function
        chefs_str = ""
        return chefs_str

    def __len__(self):
        # Complete this function
        return None

# Structure to hold a recipe
class Recipe:
    def __init__(self, rec_id=None, rec_name=None, rec_chef_id=None):
        self.id = rec_id
        self.name = rec_name
        self.chef_id = rec_chef_id
        self.score = 0.0

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def add_score(self, score):
        self.score += score

    def get_chef_id(self):
        return self.chef_id

    def __str__(self):
        rec_str = "ID: %s; " % (str(self.id))
        rec_str += "NAME: %s; " % (self.name)
        rec_str += "CHEF ID: %s; " % (self.chef_id)
        rec_str += "SCORE: %s" % (self.score)
        return rec_str

# Structure to hold the recipes
class Recipes:
    def __init__(self):
        self.recipes = {}
        self.next_recipe = 0
        self.sorted_recipes = []

    def add_recipe(self, chef_id, name):
        """
        Funcion que se encarga de generar nuevo receta y añadirlo al diccionario recipes.
        :param chef_id: id del chef
        :param name: nombre de receta
        :return: id de nueva receta generado.
        """
        # Genera nueva instancia de recipe y consultar su id.
        new_recipe = Recipe(self.next_recipe, name, chef_id)
        recipe_id = new_recipe.get_id()

        # Guardar nueva recipe a diccionario de recipes.
        self.recipes[recipe_id] = new_recipe
        # Incrementa id de recipe.
        self.next_recipe += 1
        # Devuelve id de nueva recipe.
        return recipe_id

    def get_ids(self):
        # Complete this function
        return None

    def exists(self, id):
        # Complete this function
        return False

    def get_recipe(self, recipe_id):
        # Complete this function
        return None

    def is_sorted(self):
        # Complete this function
        return False

    def sort_recipes(self):
        # Complete this function
        pass

    def get_top_n(self, n=1):
        # Complete this function
        return None

    def __str__(self):
        # Complete this function
        rec_str = ""
        return rec_str

    def __len__(self):
        # Complete this function
        return None

# Structure to hold a review
class Review:
    def __init__(self, rev_id=None, review=None, rec_id=None):
        self.id = rev_id
        self.review = review
        self.recipe_id = rec_id
        self.score = 0.0

    def get_id(self):
        return self.id

    def get_review(self):
        return self.review

    def get_recipe_id(self):
        return self.recipe_id

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def __str__(self):
        recipe_str = "ID: %s; " % (str(self.id))
        recipe_str += "REVIEW: %s; " % (self.review)
        recipe_str += "RECIPE ID: %s; " % (self.recipe_id)
        recipe_str += "SCORE: %s" % (self.score)
        return recipe_str

# Structure to hold the reviews
class Reviews:
    def __init__(self):
        self.reviews = {}
        self.next_review = 0
        self.sorted_reviews = []

    def add_review(self, rec_id, review):
        """
        Funcion que se encarga generar nueva review con informaciones que tenemos y añadirlo a diccionario Reviews.
        :param rec_id: id de recipe.
        :param review: string de review.
        :return: id de nueva review generado.
        """
        # Generar nueva review y consutal su id.
        new_review = Review(self.next_review, review, rec_id)
        review_id = new_review.get_id()
        # Añadir nueva review a diccionario de reviews.
        self.reviews[review_id] = new_review
        # Incrementa id de review.
        self.next_review += 1
        # devuelve id de review.
        return review_id

    def get_ids(self):
        # Complete this function
        return None

    def exists(self, id):
        # Complete this function
        return False

    def get_review(self,rev_id):
        # Complete this function
        return None

    def min_score(self):
        # Complete this function
        return None

    def max_score(self):
        # Complete this function
        return None

    def is_sorted(self):
        # Complete this function
        return False

    def sort_reviews(self):
        # Complete this function
        pass

    def get_top_n(self, n=1):
        # Complete this function
        return None

    def __str__(self):
        # Complete this function
        rev_str = ""
        return rev_str


class TopChef:

    def __init__(self):
        self.chefs = Chefs()
        self.recipes = Recipes()
        self.reviews = Reviews()

    def load_data(self, path):
        """
        Funcion que se encarda de generar informaciones de chefs.
        En caso de que archivo que recibimos tiene formato correcto lanza un mensaje de error.
        :param path: Direccion de archivo de inforacioens de chefs
        """
        # Definir palabras clave.
        CHEF = "CHEF"
        COURSE = "COURSE"
        TAB = "\t"
        CONTROL = False

        with open(path) as fd:
            for line in fd:
                if not CONTROL and CHEF in line:
                    CONTROL = True

                if CHEF in line and CONTROL:
                    stripped = line.strip()
                    chef_data = stripped.split(TAB)
                    chef_name = chef_data[1]
                    chef_restaurant = chef_data[2]
                    current_chef_id = self.chefs.add_chef(chef_name,chef_restaurant)
                    continue
                
                elif COURSE in line and CONTROL:
                    stripped = line.strip()
                    recipe = stripped.replace(COURSE+TAB,"")
                    current_recipe_id = self.recipes.add_recipe(current_chef_id,recipe)
                    continue

                elif CONTROL:
                    review = line.strip()
                    self.reviews.add_review(current_recipe_id, review)
                
                else:
                    raise TopChefException("Wrong file!")
        
    def clear(self):
        # Complete this function
        pass

    def add_chef(self, name, rest):
        # Complete this function
        return None

    def add_recipe(self, id_chef, name):
        # Complete this function
        return None

    def add_review(self, id_rev,review):
        # Complete this function
        return None

    def compute_scores(self, word_dict):
        self.compute_reviews_score(word_dict)
        self.compute_recipes_score()
        self.compute_chefs_score()

    def compute_reviews_score(self, word_dict):
        # Complete this function

        for rev_id in self.reviews.get_ids():
            continue

        self.normalize_reviews_scores()

    def normalize_reviews_scores(self):
        # Complete this function
        pass

    def compute_recipes_score(self):
        # Complete this function
        for rev_id in self.reviews.get_ids():
            continue
        self.normalize_recipes_scores()

    def normalize_recipes_scores(self):
        # Complete this function
        pass

    def compute_chefs_score(self):
        # Complete this function
        for rec_id in self.recipes.get_ids():
            continue

    def normalize_chefs_scores(self):
        # Complete this function
        pass

    def sort_structures(self):
        self.chefs.sort_chefs()
        self.recipes.sort_recipes()
        self.reviews.sort_reviews()

    def get_top_n_chefs(self, n=1):
        # Complete this function
        return None

    def get_top_n_recipes(self, n=1):
        # Complete this function
        return None

    def get_top_n_reviews(self, n=1):
        # Complete this function
        return None

    def show_chefs(self, chefs):
        # Complete this function
        pass

    def show_recipes(self, recipes):
        # Complete this function
        pass

    def show_reviews(self, reviews):
        # Complete this function
        pass