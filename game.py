class Game:
    """
    This class contains game logics and scoring table for this game. It helps deciding correct guesses from the user.

    :parameter
        -------
        frequency : it a distionary of letters that contains its freqency, this helps in deciding the score of a
                    particular game.
    Methods:
    :current_game_choice_l
    --------
        this  methods take a letter as input and check if it fits or not

    : current_game_choice_g
    -------
        this method takes a word and checks if it matches or not

    :get_first_score
    -------
        It calculates the initial score of the word and returns the score

    :get_updated_score
    -------
        It calculates the score as per the game progresses and returns the score

    """
    frequency_table = {'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70, 'f': 2.23, 'g': 2.02, 'h': 6.09,
                       'i': 6.97,
                       'j': 0.15, 'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51, 'p': 1.93, 'q': 0.10,
                       'r': 5.99,
                       's': 6.33, 't': 9.06, 'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97, 'z': 0.07}

    # noinspection PyMethodMayBeStatic
    def current_game_choice_g(self, current_word):
        guessed_word = input('Please enter your guessed word\n')
        if guessed_word == current_word:
            return 'success'
        else:
            return 'bad_guess'

    # noinspection PyMethodMayBeStatic
    def current_game_choice_l(self, current_word):
        guessed_letter = input('Please enter your guessed letter\n')
        hit_letters = []
        hit = False
        update_score = 0
        for i in range(len(current_word)):
            if guessed_letter == current_word[i]:
                hit_letters.append(current_word[i])
                update_score = update_score + Game.frequency_table[guessed_letter]
                hit = True
            else:
                hit_letters.append('-')
        if not hit:
            update_score = 2
        return hit_letters, hit, update_score

    # noinspection PyMethodMayBeStatic
    def get_first_score(self, word):
        score = 0
        for letters in word:
            score = score + Game.frequency_table[letters]
        return score

    # noinspection PyMethodMayBeStatic
    def get_updated_score(self, word, unfold_word):
        score = 0
        counter = 0
        for i in range(len(unfold_word)):
            if unfold_word[i] == '-':
                score = score + Game.frequency_table[word[i]] + 2
                counter = counter + 1
        return score
