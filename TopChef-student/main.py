import os
from top_chef.adt import TopChef
from top_chef.word_dictionary import WordDictionary


def read_int_option(message: str, start: int, end: int) -> int:
    """
    Shows an input message and reads the option of the user

    :param message: input message
    :param start: minimum value the user can enter
    :param end: maximum value the user can enter
    :return: the option chosen by the user
    """

    option = input(message)
    try:
        option = int(option)

    except ValueError:
        option = None

    else:
        if option < start or option > end:
            option = None

    return option


def load_topchef_data(top_chef):

    print("select your file")

    file_list = os.listdir("data")

    for idx, filename in enumerate(file_list):
        print("  {}. {}".format(idx + 1, filename))

    filename = None
    cancel = False
    while not cancel and not filename:
        option = read_int_option("Choose a N value: (0 to cancel)\n", 0, len(file_list))
        if option:
            filename = file_list[option - 1]
            try:
                top_chef.load_data(os.path.join("data", filename))

            except Exception as ex:
                print(ex)
        elif option == 0:
            cancel = True
            print("Operation cancelled!")

        else:
            print("Invalid option, try again.")

def add_word_dictionary(top_chef):
    word_dict = WordDictionary()

    print("select your file")

    foder_name = "data"
    file_list = os.listdir(foder_name)

    for idx, filename in enumerate(file_list):
        print("  {}. {}".format(idx + 1, filename))

    filename = None
    cancel = False
    while not cancel and not filename:
        option = read_int_option("Choose a data file: (0 to cancel)\n", 0, len(file_list) + 1)
        if option:
            filename = file_list[option - 1]
            try:
                word_path = os.path.join(foder_name, filename)
                word_dict.load_words(word_path)
                top_chef.compute_scores(word_dict)
                top_chef.sort_structures()
            except Exception as ex:
                print(ex)

        elif option == 0:
            cancel = True
            print("Operation cancelled!")

        else:
            print("Invalid option, try again.")



def show_topn_chefs(top_chef):
    option = 0
    cancel = False
    while not cancel and not option:
        option = read_int_option("Choose a N value: (0 to cancel)\n", 0, 100)
        if option:
            try:
                list = top_chef.get_top_n_chefs(option)
                top_chef.show_chefs(list)

            except Exception as ex:
                print(ex)

        elif option == 0:
            cancel = True
            print("Operation cancelled!")

        else:
            print("Invalid option, try again.")

def show_topn_recipes(top_chef):
    option = 0
    cancel = False
    while not cancel and not option:
        option = read_int_option("Choose a N value: (0 to cancel)\n", 0, 100)
        if option:

            try:
                list = top_chef.get_top_n_recipes(option)
                top_chef.show_recipes(list)

            except Exception as ex:
                print(ex)


        elif option == 0:
            cancel = True
            print("Operation cancelled!")

        else:
            print("Invalid option, try again.")

def show_topn_reviews(top_chef):
    option = 0
    cancel = False
    while not cancel and not option:
        option = read_int_option("Choose a N value: (0 to cancel)\n", 0, 100)
        if option:

            try:
                list = top_chef.get_top_n_reviews(option)
                top_chef.show_reviews(list)

            except Exception as ex:
                print(ex)

        elif option == 0:
            cancel = True
            print("Operation cancelled!")

        else:
            print("Invalid option, try again.")


def show_menu(top_chef):
    """
    Shows all the different menu options. This function also calls to the read_int_option function and calls to
    the chosen option
    """

    options = [
        {"message": "Exit", "function": None},
        {"message": "Load TopChef Data", "function": load_topchef_data},
        {"message": "Load Words & Compute Score", "function": add_word_dictionary},
        {"message": "Show Top N Chefs", "function": show_topn_chefs},
        {"message": "Show Top N Recipes", "function": show_topn_recipes},
        {"message": "Show Top N Reviews", "function": show_topn_reviews},
    ]

    exit_program = False
    while not exit_program:

        print("\nMain menu:")
        for idx, option in enumerate(options[1:]):
            print("  {}.- {}".format(idx+1, option["message"]))

        print("  {}.- {}".format(0, options[0]["message"]))

        option = read_int_option("What do you want to do? Choose an option:\n", 0, len(options))
        if option is None:
            print("Invalid option, try again.")

        elif option == 0:
            exit_program = True

        else:
            option_function = options[option]["function"]
            try:
                option_function(top_chef)

            except Exception as e:
                print("Unexpected error: {}", e)
                raise

            input("\nPress Enter to continue...")

if __name__ == '__main__':
    top_chef = TopChef()
    show_menu(top_chef)


