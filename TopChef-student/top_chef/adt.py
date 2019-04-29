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
        new_Chef = Chef(self.next, name, restaurant)
        self.chefs[name] = new_Chef
        chef_id = new_Chef.get_id()
        self.next += 1
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
        new_recipe = Recipe(self.next_recipe, name, chef_id)
        self.recipes[name] = new_recipe
        recipe_id = new_recipe.get_id()
        self.next_recipe += 1
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
        new_review = Review(self.next_review, review, rec_id)
        self.reviews[review] = new_review
        self.next_review += 1
        return new_review.get_id()

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

        # Abrir fichero para modificar.
        try:
            fb = open(path, "r")
        except:
            raise TopChefException("File not exist. ")
        #  Guarda todas las lineas de fichero en una lista
        fb_contents = fb.readlines()

        # Decidido usando bucle while, porque necesito leer siguiente linea para comprobar si contiene los palabra clave que necesitamos.
        line = 0
        # bucle hasta termina de leer todos los contenidos de fichero.
        # Comprobar los palabras claves para identificar lineas.
        while line < len(fb_contents)-1:
            # Cuando detecta linea de CHEFS, guarda su palabra clave, nombre de chef y nombre de restaurante.
            if CHEF in fb_contents[line]:
                CHEF, name, restaurant = fb_contents[line].strip().split("\t")
                chef_id = self.chefs.add_chef(name, restaurant)
            # Cuando detecta linea de recetas, guarda palabra clave y nombre de recetas.
                while COURSE in fb_contents[line+1]:
                    line += 1
                    COURSE, recipe = fb_contents[line].strip().split("\t")
                    recipr_id = self.recipes.add_recipe(chef_id, recipe)
                    # Prueba de leer siguiente linea, Si no es linea con palabras claves es linea de opiniones.
                    try:
                        while (COURSE not in fb_contents[line+1]) and (CHEF not in fb_contents[line+1]):
                            review = fb_contents[line+1].strip()
                            review_id = self.reviews.add_review(recipr_id, review)
                            line += 1
                    except:
                        break
            else:
                raise TopChefException("Invalid File. ")

            line += 1

        print("Completed. ")

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