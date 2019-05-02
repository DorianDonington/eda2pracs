import string

class TopChefException(Exception):
    pass

#  Structure to hold a chef
class Chef:
    def __init__(self, chef_id=None, chef_name=None, chef_restaurant=None):
        """
        """
        self.id = chef_id
        self.name = chef_name
        self.restaurant = chef_restaurant
        self.score = 0.0

    def get_id(self):
        """
        """
        return self.id

    def add_score(self, score):
        """
        """
        self.score += score

    def get_name(self):
        """
        """
        return self.name

    def get_restaurant(self):
        """
        """
        return self.restaurant

    def get_score(self):
        """
        """
        return self.score

    def set_score(self, score):
        """
        """
        self.score = score

    def __str__(self):
        """
        """
        chef_str = "ID: %s; " % (str(self.id))
        chef_str += "NAME: %s; " % (self.name)
        chef_str += "RESTAURANT: %s; " % (self.restaurant)
        chef_str += "SCORE: %s" % (self.score)
        return chef_str

# Structure to hold all chefs
class Chefs:
    def __init__(self):
        """
        """
        self.chefs = {}
        self.next = 0
        self.sorted_chefs = []

    def exists(self, id):
        """
        Checks if the chef exist inside the dictionary by sorting it from his id
        :param id: chef id inputed by the user
        :return: boolean; if the chef exists, return True, else, return False
        """
        return id in self.get_ids()

    def get_ids(self):
        """
        Give the user the listed ids for every chef
        :return: a list of ids
        """
        return self.chefs.keys()

    def add_chef(self, name, restaurant):
        """
        Funcion que se encarga de generar un nuevo chef y añadirlo al direccionario
        :param name: nombre de chef
        :param restaurant: nombre de restaurante
        :return: id de nuevo chef generado.
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
        """
        Search for the chef by the input id, raise a TopChefException if the is no such id inside the dictionary.
        :param id: chef id input by the user.
        :return: the chef asked for.
        """
        if self.exists(id):
            return self.chefs[id]
        else:
            raise TopChefException("There is no chef assigned to that id")

    def is_sorted(self):
        """
        """
        # Complete this function
        #Necesito saber la puntuacion de cada chef
        return False

    def sort_chefs(self):
        """
        """
        # Complete this function
        #Lo mismo que la funcion de arriba!
        pass

    def get_top_n(self, n=1):
        """
        Returns the list of top chefs
        :param n: The number of top chefs you want to check
        :return: The list, sorted by the number of tops you want to check
        """
        if n > self.next:
            raise TopChefException("There is only %s chefs!" %(self.next))
        return self.sorted_chefs[0:n]

    def __str__(self):
        """
        """
        chefs_str = ""
        for chef in self.get_ids():
            chefs_str+= self.chefs[chef].__str__()
            chefs_str+= "\n"
                
        return chefs_str

    def __len__(self):
        """
        Prints the number of chefs that are inside the dictionary
        :return: the number of chefs, in a int type.
        """
        return len(self.chefs.keys())

# Structure to hold a recipe
class Recipe:
    def __init__(self, rec_id=None, rec_name=None, rec_chef_id=None):
        """
        """
        self.id = rec_id
        self.name = rec_name
        self.chef_id = rec_chef_id
        self.score = 0.0

    def get_id(self):
        """
        """
        return self.id

    def get_name(self):
        """
        """
        return self.name

    def get_score(self):
        """
        """
        return self.score

    def set_score(self, score):
        """
        """
        self.score = score

    def add_score(self, score):
        """
        """
        self.score += score

    def get_chef_id(self):
        """
        """
        return self.chef_id

    def __str__(self):
        """
        """
        rec_str = "ID: %s; " % (str(self.id))
        rec_str += "NAME: %s; " % (self.name)
        rec_str += "CHEF ID: %s; " % (self.chef_id)
        rec_str += "SCORE: %s" % (self.score)
        return rec_str

# Structure to hold the recipes
class Recipes:
    
    def __init__(self):
        """
        """
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
        """
        Get a list of recipes ids
        :return: a list of every recipe id
        """
        return self.recipes.keys()

    def exists(self, id):
        """
        Checks if the recipe exists in the recipes dictionary
        :param id: The id input by the user
        :return: a boolean; True if the id exists, False if it does not exist
        """
        return id in self.get_ids()

    def get_recipe(self, recipe_id):
        """
        Gives the user the recipe it is looking for, raise a TopChefException if there is no such id.
        :param recipe_id: id input by the user
        :return: the recipe the user looks for.
        """
        if self.exists(recipe_id):
            return self.recipes[recipe_id]
        else:
            raise TopChefException("There is no recipe assigned to that id!")

    def is_sorted(self):
        """
        """
        # Complete this function
        #Me faltan las puntuaciones
        return False

    def sort_recipes(self):
        """
        """
        # Complete this function
        #Me faltan las puntuaciones
        pass

    def get_top_n(self, n=1):
        """
        Gives the user a list with the top recipes.
        :param n: The number of top recipes that the user wants to check
        :return: a list of the top recipes.
        """
        return self.sorted_recipes[0:n]

    def __str__(self):
        """
        """
        rec_str = ""
        for recipe in self.get_ids():
            rec_str+= self.recipes[recipe].__str__()
            rec_str+= "\n"
        return rec_str

    def __len__(self):
        """
        Gives the user a int type with the number of recipes inside the dictionary.
        :return: the number of recipes inside the dictionary
        """
        return len(self.recipes.keys())

# Structure to hold a review
class Review:
    def __init__(self, rev_id=None, review=None, rec_id=None):
        """
        """
        self.id = rev_id
        self.review = review
        self.recipe_id = rec_id
        self.score = 0.0

    def get_id(self):
        """
        """
        return self.id

    def get_review(self):
        """
        """
        return self.review

    def get_recipe_id(self):
        """
        """
        return self.recipe_id

    def get_score(self):
        """
        """
        return self.score

    def set_score(self, score):
        """
        """
        self.score = score

    def __str__(self):
        """
        """
        recipe_str = "ID: %s; " % (str(self.id))
        recipe_str += "REVIEW: %s; " % (self.review)
        recipe_str += "RECIPE ID: %s; " % (self.recipe_id)
        recipe_str += "SCORE: %s" % (self.score)
        return recipe_str

# Structure to hold the reviews
class Reviews:
    def __init__(self):
        """
        """
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
        """
        Gives the user a list of ids to check for
        :return: a list of ids
        """
        return self.reviews.keys()

    def exists(self, id):
        """
        Checks if the id exists inside the dictionary
        :param id: the id input by the user to check if it exists
        :return: boolean type, True if it does exist, False if it doesn't exist.
        """
        return id in  self.get_ids()

    def get_review(self,rev_id):
        """
        Gives the user the requested review, raise a TopChefException if there is no such id inside the dictionary
        :param rev_id: the id for the requested review input by the user
        :return: the review assigned to that id.
        """
        if self.exists(rev_id):
            return self.reviews[rev_id]
        else:
            raise TopChefException("There is no such review assigned to that id")

    def array_scores(self):
        """
        """
        scores =[]
        for rev_id in self.get_ids():
            review = self.reviews[rev_id]
            scores.append(review.get_score())
        return scores

    def min_score(self):
        """
        """
        return min(self.array_scores())

    def max_score(self):
        """
        """
        return max(self.array_scores())

    def is_sorted(self):
        """
        """
        if self.sorted_reviews == []:
            return False
        return True

    def sort_reviews(self):
	    """
	    Funcion que genera una lista de reviews ordenado por score.
	    
		# Primero meter todos los elementos de diccionario a la lista en forma desordenado.
	    for review in self.reviews:
	    	review_temp = self.get_review(review)
	    	self.sorted_reviews.append(review_temp)

	    i = 1

        while i < len(self.sorted_reviews):
	    	j = i
    		while j > 0 and self.sorted_reviews[j].get_score()>self.sorted_reviews[j-1].get_score():
    			review_temp = self.sorted_reviews[j]
    			self.sorted_reviews[j] = self.sorted_reviews[j-1]
    			self.sorted_reviews[j - 1] = review_temp
    			j -= 1
    		i += 1
        """
        

    def get_top_n(self, n=1):
        """
        Gives the user the listed top reviews by looking at the number input by the user.
        :param n: the number of top reviews the user wants to check for.
        :return: a list of reviews.
        """
        return self.sorted_reviews[0:n]

    def __str__(self):
        """
        """
        rev_str = ""
        for review in self.get_ids():
            rev_str+= self.reviews[review].__str__()
            rev_str+= "\n"
        return rev_str


class TopChef:

    def __init__(self):
        """
        """
        self.chefs = Chefs()
        self.recipes = Recipes()
        self.reviews = Reviews()

    def load_data(self, path):
        """
        Funcion que se encarga de generar informaciones de chefs.
        :param path: Direccion de archivo de chefs
        """
        # Definir palabras clave.
        CHEF = "CHEF"
        COURSE = "COURSE"
        TAB = "\t"
        CONTROL = False

        with open(path) as fd: 
            for line in fd:
                if not CONTROL and CHEF in line:
                    CONTROL = True #Controlamos si estamos en el fichero correcto o no

                if CHEF in line and CONTROL:
                    stripped = line.strip() #Eliminamos el \n del final de la línea
                    chef_data = stripped.split(TAB) #Separamos el texto por \t 
                    chef_name = chef_data[1] #La primera palabra es el chef
                    chef_restaurant = chef_data[2] #La segunda palabra es el restaurante
                    current_chef_id = self.add_chef(chef_name,chef_restaurant) 
                    continue #Siguiente linea!
                
                elif COURSE in line and CONTROL:
                    stripped = line.strip() #Eliminamos el \n
                    recipe = stripped.replace(COURSE+TAB,"") #Eliminamos la palabra COURSE para quedarnos con el resto
                    current_recipe_id = self.add_recipe(current_chef_id,recipe)
                    continue

                elif CONTROL:
                    line = line.strip() #Eliminamos \n
                    review = line.translate(str.maketrans('', '', string.punctuation)).lower() #Eliminamos símbolos de puntuación y ponemos todo en minus
                    self.add_review(current_recipe_id, review)
                
                else:
                    self.clear() #Errores? Borramos todo
                    raise TopChefException("Wrong file!") #Control de errores de fichero correcto
        
    def clear(self):
        """
        """
        self.__init__()

    def add_chef(self, name, rest):
        """
        """
        return self.chefs.add_chef(name, rest)
        
    def add_recipe(self, id_chef, name):
        """
        """
        return self.recipes.add_recipe(id_chef, name)

    def add_review(self, id_rev,review):
        """
        """
        return self.reviews.add_review(id_rev,review)

    def compute_scores(self, word_dict):
        """
        """
        self.compute_reviews_score(word_dict)
        self.compute_recipes_score()
        self.compute_chefs_score()

    def compute_reviews_score(self, word_dict):
        """
        """
        if len(self.chefs)==0:
            raise TopChefException("No data yet!")

        for rev_id in self.reviews.get_ids():
            suma = 0
            review = self.reviews.get_review(rev_id)
            raw_data = review.get_review().split()
            for word in raw_data:
                if word_dict.exists(word):
                    word_score = word_dict.get_value(word)
                    suma += word_score

            review.set_score(round(suma,2))

        self.normalize_reviews_scores()

    def normalize_reviews_scores(self):
        """
        """
        max_score = self.reviews.max_score()
        min_score = self.reviews.min_score()

        for review_id in self.reviews.get_ids():
            review = self.reviews.get_review(review_id)
            review_score = review.get_score()
            review.set_score(round((review_score-min_score)/(max_score-min_score),2))

    def compute_recipes_score(self):
        """
        """
        for rev_id in self.reviews.get_ids():
            for rec_id in self.recipes.get_ids():

            review = self.reviews.get_review(rev_id)
            raw_data = review.get_review().split()
            for word in raw_data:
                if word_dict.exists(word):
                    word_score = word_dict.get_value(word)
                    suma += word_score

            review.set_score(round(suma,2))

        self.normalize_recipes_scores()

    def normalize_recipes_scores(self):
        """
        """
        # Complete this function
        pass

    def compute_chefs_score(self):
        """
        """
        # Complete this function
        for rec_id in self.recipes.get_ids():
            continue

    def normalize_chefs_scores(self):
        """
        """
        # Complete this function
        pass

    def sort_structures(self):
        """
        """
        self.chefs.sort_chefs()
        self.recipes.sort_recipes()
        self.reviews.sort_reviews()

    def get_top_n_chefs(self, n=1):
        """
        """
        return self.chefs.get_top_n(n)

    def get_top_n_recipes(self, n=1):
        """
        """
        return self.recipes.get_top_n(n)

    def get_top_n_reviews(self, n=1):
        """
        """
        return self.reviews.get_top_n(n)

    def show_chefs(self, chefs):
        """
        """
        print(chefs)

    def show_recipes(self, recipes):
        """
        """
        print(recipes)

    def show_reviews(self, reviews):
        """
        """
        print(reviews)
        