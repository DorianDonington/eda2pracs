import string

class TopChefException(Exception):
	pass

#  Structure to hold a chef
class Chef:
	def __init__(self, chef_id=None, chef_name=None, chef_restaurant=None):
		"""
		Initialize the class Chef data.
		:param chef_id: The chef ID.
		:param chef_name: The chef name.
		:param chef_restaurant: The chef's restaurant name.
		"""
		self.id = chef_id
		self.name = chef_name
		self.restaurant = chef_restaurant
		self.score = 0.0
		self.number_recipe = 0 #Número de reviews que tiene le dhef

	def get_id(self):
		"""
		:return: The chef ID.
		"""
		return self.id

	def add_score(self, score):
		"""
		Adds the score to the self.score initializated.
		:param score: The normalized score.
		:return: The score addition.
		"""
		self.score += score

	def get_name(self):
		"""
		:return: Returns the chef's name.
		"""
		return self.name
	def add_number_recipe(self):
		"""
		Adds another recipe to the recipe count.
		"""
		self.number_recipe += 1

	def get_number_recipe(self):
		"""
		:return: The recipes assigned to the selected chef.
		"""
		return self.number_recipe

	def get_restaurant(self):
		"""
		:return: The restaurant name of the selected chef.
		"""
		return self.restaurant

	def get_score(self):
		"""
		:return: The sum of the normalized scores.
		"""
		return self.score

	def set_score(self, score):
		"""
		Sets a score to the selected chef.
		:param score: Score we want to assign.
		:return: The assigned score.
		"""
		self.score = score

	def __str__(self):
		"""
		This funtion prints by screen a sorted way to show a chef's information.
		:return: The chef information in string format.
		"""
		chef_str = "-ID: %s; " % (str(self.get_id()))
		chef_str += "NAME: %s; " % (self.get_name())
		chef_str += "RESTAURANT: %s; " % (self.get_restaurant())
		chef_str += "SCORE: %s" % (round(self.get_score(),1))
		return chef_str

# Structure to hold all chefs
class Chefs:
	def __init__(self):
		"""
		Initializes the Chefs dictionary and adt.
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
		for chef in self.chefs: #Solo controlamos el caso mismo chef y mismo restaurante porque un chef puede tener 
			#dos restaurantes y dos chefs pueden compartir mismo restaurante
			if self.chefs[chef].get_restaurant() == restaurant and chef.get_name() == name:
				raise TopChefException("You have a repeated chef in your data file!")
		# Genera un nueva instancia chef
		new_Chef = Chef(self.next+1, name, restaurant)
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
		Comprobar si estan ordenado lista de recipes.
		"""
		if len(self.sorted_chefs) == 0:
			return False

		for i in range(len(self.sorted_chefs)-1):	#-1 Porque como en cada iteración comprobamos tambien el siguiente
													#hemos de calcular hasta el penúltimo.
			if self.sorted_chefs[i].get_score() < self.sorted_chefs[i+1].get_score():
				return False

		return True

	def sort_chefs(self):
		"""
		Funcion que genera una lista de reviews ordenado por score.
		"""
		# Primero meter todos los elementos de diccionario a la lista en forma desordenado.
		# Porque diccionario es objeto sin ordenes.

		for chef in self.chefs:
			chef_temp = self.get_chef(chef)
			# Para evitar cuando usuario carga mas de una vez el fichero de word.
			if chef_temp not in self.sorted_chefs:
				self.sorted_chefs.append(chef_temp)

		# Control de error: Si la lista ya esta ordenada, Para evitar hacer pasos inecesarios.
		if self.is_sorted():
			raise TopChefException("Chefs are sorted already!.")

		# Utilizando metodo de ordenar descendente por insercion para ordenar.
		# Va comparando elemento con su elemento anterior,
		# Si elemento es mayor que elemento anterior, cambio de posicion.
		# una vez cambiado de posicion, comprueba con el elemento anterior - 1. Hasta que anterior - 1 sea mayor que elemento que estamos recorriendo.
		# Si elemento no es mayor, elemento + 1, y entra siguiente vuelta de bucle
		# hasta termina recorrer toda la lista, i = len(lista).
		i = 1
		while i < len(self.sorted_chefs):
			j = i
			while j > 0 and self.sorted_chefs[j].get_score() > self.sorted_chefs[j - 1].get_score():
				chef_temp = self.sorted_chefs[j] # Guarda elemento mayor a un variable temporar
				self.sorted_chefs[j] = self.sorted_chefs[j - 1]
				self.sorted_chefs[j - 1] = chef_temp
				j -= 1
			i += 1

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
		Creates a string that shows por screen the Chefs information
		:return: The chefs in string format.
		"""
		chefs_str = ""
		for chef in self.get_ids():
			chefs_str+= str(self.chefs[chef])
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
		Initializes the class Recipe information.
		:param rec_id: the recipe id
		:param rec_name: the recipe name
		:param rec_chef_id: the chef ID assigned to every recipe.
		"""
		self.id = rec_id
		self.name = rec_name
		self.chef_id = rec_chef_id
		self.score = 0.0
		self.number_review = 0 #Number of reviews in each recipe

	def get_id(self):
		"""
		:return: The recipe ID.
		"""
		return self.id

	def get_name(self):
		"""
		:return: The recipe name.
		"""
		return self.name

	def get_score(self):
		"""
		:return: The score assigned to the recipe.
		"""
		return self.score

	def set_score(self, score):
		"""
		Assign a normalized score into the recipe.
		:param score: The score we want to assign.
		:return: The score.
		"""
		self.score = score

	def add_number_review(self):
		"""
		Adds a new review to the recipe
		"""
		self.number_review += 1

	def get_number_review(self):
		"""
		:return: The number of reviews assigned to the recipe.
		"""
		return self.number_review

	def add_score(self, score):
		"""
		Adds a new score to the assigned score.
		:param score: The score we want to add.
		:return: The sum of both scores.
		"""
		self.score += score

	def get_chef_id(self):
		"""
		:return: The chef ID assigned to the recipe.
		"""
		return self.chef_id

	def __str__(self):
		"""
		Prints the recipe information sorted by data.
		:return: The recipe in string format.
		"""
		rec_str = "-ID: %s; " % (str(self.id))
		rec_str += "NAME: %s; " % (self.name)
		rec_str += "CHEF ID: %s; " % (self.chef_id)
		rec_str += "SCORE: %s" % (round(self.get_score(), 1))
		return rec_str

# Structure to hold the recipes
class Recipes:

	def __init__(self):
		"""
		Initializes the Recipes adt.
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
		new_recipe = Recipe(self.next_recipe+1, name, chef_id)
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
		Comprobar si estan ordenado lista de recipes.
		"""
		if len(self.sorted_recipes) == 0:
			return False

		for i in range(len(self.sorted_recipes)-1):
			if self.sorted_recipes[i].get_score() < self.sorted_recipes[i+1].get_score(): #Mira los elementos a pares i comprueba que estén ordenados
				return False

		return True

	def sort_recipes(self):
		"""
		Funcion que genera una lista de reviews ordenado por score.
		"""
		# Primero meter todos los elementos de diccionario a la lista en forma desordenado.
		# Porque diccionario es objeto sin ordenes.
		for recipe in self.recipes:
			recipe_temp = self.get_recipe(recipe)
			# Para evitar cuando usuario carga mas de una vez el fichero de word.
			if recipe not in self.sorted_recipes:
				self.sorted_recipes.append(recipe_temp)

		if self.is_sorted():
			raise TopChefException("Recipes sorted already!")
		# Utilizando metodo de ordenar descendente por insercion para ordenar.
		# Va comparando elemento con su elemento anterior,
		# Si elemento es mayor que elemento anterior, cambio de posicion.
		# una vez cambiado de posicion, comprueba con el elemento anterior - 1. Hasta que anterior - 1 sea mayor que elemento que estamos recorriendo.
		# Si elemento no es mayor, elemento + 1, y entra siguiente vuelta de bucle
		# hasta termina recorrer toda la lista, i = len(lista).
		i = 1 
		while i < len(self.sorted_recipes):
			j = i
			while j > 0 and self.sorted_recipes[j].get_score() > self.sorted_recipes[j - 1].get_score():
				recipe_temp = self.sorted_recipes[j] # Guarda elemento mayor a un variable temporar
				self.sorted_recipes[j] = self.sorted_recipes[j - 1]
				self.sorted_recipes[j - 1] = recipe_temp
				j -= 1
			i += 1

	def get_top_n(self, n=1):
		"""
		Gives the user a list with the top recipes.
		:param n: The number of top recipes that the user wants to check
		:return: a list of the top recipes.
		"""
		if n > self.next_recipe:
			raise TopChefException("There is only %s recipes!" % (self.next_recipe))
		return self.sorted_recipes[0:n]

	def __str__(self):
		"""
		Prints by screen a sorted information of the recipes adt.
		:return: The adt in string format.
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
		Initializes the Review data.
		:param rev_id: the review id.
		:param review: what the review says.
		:param rec_id: The recipe id assigned to that review.
		"""
		self.id = rev_id
		self.review = review
		self.recipe_id = rec_id
		self.score = 0.0

	def get_id(self):
		"""
		:return: The review id.
		"""
		return self.id

	def get_review(self):
		"""
		:return: The review itself.
		"""
		return self.review

	def get_recipe_id(self):
		"""
		:return: The recipe id assigned to that review
		"""
		return self.recipe_id

	def get_score(self):
		"""
		:return: The score assigned to that review.
		"""
		return self.score

	def set_score(self, score):
		"""
		:return: Sets a score to that review.
		"""
		self.score = score

	def __str__(self):
		"""
		Prints by screen the sorted information of a review
		:return: The review in string format.
		"""
		review_str = "-ID: %s; " % (str(self.id))
		review_str += "REVIEW: %s; " % (self.review)
		review_str += "RECIPE ID: %s; " % (self.recipe_id)
		review_str += "SCORE: %s" % (round(self.get_score(), 1))
		return review_str

# Structure to hold the reviews
class Reviews:
	def __init__(self):
		"""
		Initializes the Reviews adt.
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
		new_review = Review(self.next_review+1, review, rec_id)
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

	def get_scores(self):
		"""
		Creates a new list that saves every score, so we can do a max and a min in every score.
		:return: the array of scores
		"""
		scores =[]
		for rev_id in self.get_ids():
			review = self.reviews[rev_id]
			scores.append(review.get_score())
		return scores

	def min_score(self):
		"""
		:return: The lowest score in the reviews
		"""
		return min(self.get_scores())

	def max_score(self):
		"""
		:return: the highest score in the reviews.
		"""
		return max(self.get_scores())

	def is_sorted(self):
		"""
		Comprobar si estan ordenado lista de reviews.
		:return: Booleano, si esta ordenado devuelve un True, sino devuelve un False.
		"""
		if len(self.sorted_reviews) == 0:
			return False

		for i in range(len(self.sorted_reviews)-1):
			if self.sorted_reviews[i].get_score() < self.sorted_reviews[i+1].get_score(): #Mira los elementos a pares i comprueba que estén ordenados
				return False

		return True


	def sort_reviews(self):
		"""
		Funcion que genera una lista de reviews ordenado por score.
		"""
		# Primero meter todos los elementos de diccionario a la lista en forma desordenado.
		# Porque diccionario es objeto sin ordenes.
		for review in self.reviews:
			review_temp = self.get_review(review)
			# Para evitar cuando usuario carga mas de una vez el fichero de word.
			if review_temp not in self.sorted_reviews:
				self.sorted_reviews.append(review_temp)

		if self.is_sorted():
			raise TopChefException("Reviews are sorted already! ")
		# Utilizando metodo de ordenar descendente por insercion para ordenar.
		# Va comparando elemento con su elemento anterior,
		# Si elemento es mayor que elemento anterior, cambio de posicion.
		# una vez cambiado de posicion, comprueba con el elemento anterior - 1. Hasta que anterior - 1 sea mayor que elemento que estamos recorriendo.
		# Si elemento no es mayor, elemento + 1, y entra siguiente vuelta de bucle
		# hasta termina recorrer toda la lista, i = len(lista).
		i = 1
		while i < len(self.sorted_reviews):
			j = i
			while j > 0 and self.sorted_reviews[j].get_score()>self.sorted_reviews[j-1].get_score():
				review_temp = self.sorted_reviews[j]
				self.sorted_reviews[j] = self.sorted_reviews[j-1]
				self.sorted_reviews[j - 1] = review_temp
				j -= 1
			i += 1

	def get_top_n(self, n=1):
		"""
		Gives the user the listed top reviews by looking at the number input by the user.
		:param n: the number of top reviews the user wants to check for.
		:return: a list of reviews.
		"""
		if n > self.next_review:
			raise TopChefException("There is only %s reviews!" % (self.next_review))
		return self.sorted_reviews[0:n]

	def __str__(self):
		"""
		Sorts the adt information for print intentions.
		:return: the reviews adt in string format.
		"""
		rev_str = ""
		for review in self.get_ids():
			rev_str+= self.reviews[review].__str__()
			rev_str+= "\n"
		return rev_str

	def __len__(self):
		"""
		Gives the user a int type with the number of reviews inside the dictionary.
		:return: the number of recipes inside the dictionary
		"""
		return len(self.reviews.keys())


class TopChef:

	def __init__(self):
		"""
		Initializes the TopChef class data.
		"""
		self.chefs = Chefs()
		self.recipes = Recipes()
		self.reviews = Reviews()
		self.recipes_scores = []
		self.chefs_scores = []

	def load_data(self, path):
		"""
		Funcion que se encarga de generar informaciones de chefs.
		:param path: Direccion de archivo de chefs
		"""
		self.clear() #Limpiamos el data antes de empezar con un load word
		# Definir palabras clave.
		CHEF = "CHEF"
		COURSE = "COURSE"
		TAB = "\t"
		CONTROL = False
		with open(path) as fd:
			for line in fd:
				if not CONTROL and CHEF in line:
					CONTROL = True #Controlamos si estamos en el fichero correcto o no

				# Generar Chefs
				if CHEF in line and CONTROL:
					stripped = line.strip() #Eliminamos el \n del final de la línea
					chef_data = stripped.split(TAB) #Separamos el texto por \t
					chef_name = chef_data[1] #La primera palabra es el chef
					chef_restaurant = chef_data[2] #La segunda palabra es el restaurante
					current_chef_id = self.add_chef(chef_name,chef_restaurant)
					continue #Siguiente linea!

				# Generar Recipes
				elif COURSE in line and CONTROL:
					stripped = line.strip() #Eliminamos el \n
					recipe = stripped.replace(COURSE+TAB,"") #Eliminamos la palabra COURSE para quedarnos con el resto
					current_recipe_id = self.add_recipe(current_chef_id,recipe)
					# Incrementa cantidad de recipe que contiene cada chef.
					new_chef = self.chefs.get_chef(current_chef_id)
					new_chef.add_number_recipe() 
					continue

				# Generar Reviwes
				elif CONTROL:
					line = line.strip() #Eliminamos \n
					review = line.translate(str.maketrans('', '', string.punctuation)).lower() #Eliminamos símbolos de puntuación y ponemos todos en minus
					review_id = self.add_review(current_recipe_id, review)
					# Incrementa cantidad de review que contiene cada recipe.
					new_recipe = self.recipes.get_recipe(current_recipe_id)
					new_recipe.add_number_review()

				else:
					self.clear() #Errores? Borramos todos
					raise TopChefException("Wrong file!") #Control de errores de fichero correcto

		print("Load data completed. ")

	def clear(self):
		"""
		Clears the TopChef class.
		:return: Reinitialize the hole class.
		"""
		self.__init__()

	def add_chef(self, name, rest):
		"""
		Adds a new chef into the Chefs class.
		:param name: The chef name
		:param rest: The chef's restaurant name.
		:return: The added chef.
		"""
		return self.chefs.add_chef(name, rest)

	def add_recipe(self, id_chef, name):
		"""
		Adds a recipe into the Recipes class
		:param id_chef: The chef ID assigned to that recipe.
		:param name: The recipe name.
		:return: The added recipe.
		"""
		return self.recipes.add_recipe(id_chef, name)

	def add_review(self, id_rep,review):
		"""
		Adds a review into the Reviews class
		:param id_rep: The recipe ID assigned to that review.
		:param review: The review.
		:return: The added review.
		"""
		return self.reviews.add_review(id_rep,review)

	def compute_scores(self, word_dict):
		"""
		Checks for every review inside the word_dict and returns the computed score of all reviews, recipes and chefs.
		:param word_dict: The word dictionary opened by the module word_dictionary.py.
		:return: The computed score of reviews, recipes and chefs.
		"""
		self.compute_reviews_score(word_dict)
		self.compute_recipes_score()
		self.compute_chefs_score()

	def compute_reviews_score(self, word_dict):
		"""
		Compute the score of the reviews.
		:param word_dict: The word dictionary opened by the module word_dictionary.py.
		:return: The normalized score.
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

			review.set_score(suma)

		self.normalize_reviews_scores()

	def normalize_reviews_scores(self):
		"""
		Normalizes the reviews score computed.
		:return: The normalized score.
		"""
		max_review = self.reviews.max_score()
		min_review = self.reviews.min_score()

		for review_id in self.reviews.get_ids():
			review = self.reviews.get_review(review_id)
			review_score = review.get_score()
			review.set_score((review_score-min_review)/(max_review-min_review))

	def compute_recipes_score(self):
		"""
		Compute the score of the recipes.
		:param word_dict: The word dictionary opened by the module word_dictionary.py.
		:return: The normalized score.
		"""

		for rev_id in self.reviews.get_ids():
			review = self.reviews.get_review(rev_id)
			recipe_id = review.get_recipe_id()
			recipe = self.recipes.get_recipe(recipe_id)
			recipe.set_score(recipe.get_score()+review.get_score())

		for rec_id in self.recipes.get_ids():
			recipe = self.recipes.get_recipe(rec_id)

			if recipe.get_number_review() !=0:
				media = recipe.get_score()/recipe.get_number_review()
				self.recipes_scores.append(media)
				recipe.set_score(media)

		self.normalize_recipes_scores()

	def normalize_recipes_scores(self):
		"""
		Normalizes the recipes scores.
		:return: The normalized recipe scores.
		"""
		max_review = max(self.recipes_scores)
		min_review = min(self.recipes_scores)
		
		for rec_id in self.recipes.get_ids():
			recipe = self.recipes.get_recipe(rec_id)
			if recipe.get_number_review() != 0:
				rec_score = recipe.get_score()
				recipe.set_score((rec_score-min_review)/(max_review-min_review))


	def compute_chefs_score(self):
		"""
		Computes the scores for  the chefs.
		:return: The normalized score.
		"""
		
		for rec_id in self.recipes.get_ids():
			recipe = self.recipes.get_recipe(rec_id)
			chef_id = recipe.get_chef_id()
			chef = self.chefs.get_chef(chef_id)
			chef.set_score(chef.get_score()+recipe.get_score())

		for chef_id in self.chefs.get_ids():
			chef = self.chefs.get_chef(chef_id)
			if chef.get_number_recipe() !=0:
				media = chef.get_score()/chef.get_number_recipe()
				chef.set_score(media)
				self.chefs_scores.append(media)

		self.normalize_chefs_scores()

	def normalize_chefs_scores(self):
		"""
		Normalize the chefs scores.
		:return: The normalized score.
		"""
		max_chef = max(self.chefs_scores)
		min_chef = min(self.chefs_scores)

		for chef_id in self.chefs.get_ids():
			chef = self.chefs.get_chef(chef_id)
			if chef.get_number_recipe() != 0:
				chef_score = chef.get_score()
				chef.set_score((chef_score-min_chef)/(max_chef-min_chef))


	def sort_structures(self):
		"""
		"""
		self.chefs.sort_chefs()
		self.recipes.sort_recipes()
		self.reviews.sort_reviews()

	def get_top_n_chefs(self, n=1):
		"""
		Funcion para consultar numero n de chefs con score mas alto.
		:param n: cantidad de chefs que consultamos.
		:return: lista de objetos chefs
		"""
		# Control de error: Si no hay chefs.
		if len(self.chefs) == 0:
			raise TopChefException("First load data.")

		if not self.chefs.is_sorted():
			raise TopChefException("You need load word.")

		return self.chefs.get_top_n(n)

	def get_top_n_recipes(self, n=1):
		"""
		"""
		# Control de error: Si no hay chefs.
		if len(self.recipes) == 0:
			raise TopChefException("First load data.")

		if not self.recipes.is_sorted():
			raise TopChefException("You need load word.")

		return self.recipes.get_top_n(n)

	def get_top_n_reviews(self, n=1):
		"""
		Checks if there are any recipes and if the reviews are sorted.
		:param n: The number of reviews the user wants to see.
		:return: The sorted list of reviews.
		"""
		# Control de error: Si no hay chefs.
		if len(self.recipes) == 0:
			raise TopChefException("First load data.")

		if not self.reviews.is_sorted():
			raise TopChefException("You need load word.")

		return self.reviews.get_top_n(n)

	def show_chefs(self, chefs):
		"""
		Mostrar por pantalla lista de N chefs
		:param recipes: Lista de objetos de chefs.
		"""
		for chef in chefs:
			print(chef)
			for recipe_id in self.recipes.get_ids():
				recipe = self.recipes.get_recipe(recipe_id)
				if recipe.chef_id == chef.id:
					print("\t{}".format(recipe))
					for review_ids in self.reviews.get_ids():
						review = self.reviews.get_review(review_ids)
						if review.recipe_id == recipe.id:
							print("\t\t{}".format(review))
			print("\n", end="")

	def show_recipes(self, recipes):
		"""
		Mostrar por pantalla lista de N recipes
		:param recipes: Lista de objetos de recipes.
		"""
		for recipe in recipes:
			print(recipe)
			for review in self.get_top_n_reviews(len(self.reviews)):
				if review.recipe_id == recipe.id:
					print("\t{}".format(review))
			print("\n", end="")

	def show_reviews(self, reviews):
		"""
		Mostrar por pantalla lista de N reviews.
		:param reviews: Lista de objetos de reviews.
		"""
		for review in reviews:
			print(review)
