import random


class StringDatabase:
    """
    This class takes care for the disk IOs. And it imports the random module of python
    It reads from the file name 'four_letters.txt' and creates a word list

    :returns
    --------
    it returns a random word selected from the list.
    """
    #  noinspection PyMethodMayBeStatic
    def get_random_word(self):
        reader = open("four_letters.txt", "r")
        data = reader.read()
        words_list = data.split()
        return random.choice(words_list)
