import game
import stringDatabase


class Guess:
    """
            This Class is the driver method for the game that includes the menu for the as well.

            :start_game
            ------------
            It contains 4 choices:
            If 'l' is inputted it will go for letter guessing, 't' for giving up the game,
            'g' for guessing and 'q' for quiting.

            This also calls stringDatabase file for getting new random word and calls game.py file for different
            game logic like calculating the score, etc.

            This method also contains the database i.e. a list of dictionaries
            Parameters:
                -----------
                database[ current_game_statistics {}] : this contains all the game progress like status, score, etc
                new_word : it fetches a random word from the stringDatabase file
                new_score : it calculates the score and keeps updating score field of the database
                choice : for inputing users choices

            Return:
                -----
                There is no return type for this method

            This method prints all the game overview at the end, detailing the game details.
        """

    # noinspection PyMethodMayBeStatic
    def start_game(self):
        # print(Guess.__doc__)
        print('Just a word about rules:\n if you missed a guessed letter 2 points will be deducted\n '
              'if you missed a guessed word 10% will be deducted \n '
              'and if you quit or gave up you will loose all the points of the uncovered letters \n')
        print('Lets start playing the guessing game! Are you ready?'.center(80, '#'))
        print('\nCurrent Guess: ----\n \nPlease enter a choice to begin')
        # choice = input('g = guess, t = tell me, l for a letter, and q to quit\n')
        current_guess = '----'
        game_obj = game.Game()
        string_obj = stringDatabase.StringDatabase()
        database = []
        new_word = string_obj.get_random_word()
        new_score = game_obj.get_first_score(new_word)
        current_game_statistics = {'game': 1, 'word': new_word, 'status': '', 'bad_guess': 0,
                                   'missed_letters': 0,
                                   'score': new_score}
        while True:
            choice = input('g = guess, t = tell me, l for a letter, and q to quit\n')
            print(new_word)
            if choice == 'l' or choice == 'L':
                result_l, hit, update_score = game_obj.current_game_choice_l(new_word)
                current_game_statistics['score'] = current_game_statistics['score'] - update_score
                string = ''
                if hit:
                    counter = 0
                    for i in range(len(result_l)):
                        if result_l[i] == '-':
                            string = string + current_guess[i]
                        elif current_guess[i] == '-':
                            counter += 1
                            string = string + result_l[i]
                            # current_game_statistics['score'] = current_game_statistics['score'] - update_score
                        else:
                            string = string + current_guess[i]
                    current_guess = string
                    current_game_statistics['status'] = 'playing'
                    print("You have got {:d} hit(s)!\n".format(counter))
                    print("Current Guess: " + current_guess + "\n \nPlease enter a choice")
                    if current_guess == new_word:
                        print("Letter by Letter!! You have guessed it right!".center(80, '#') + '\n')
                        current_game_statistics['status'] = 'Success'
                        current_game_statistics['score'] = current_game_statistics['score'] + 5
                        current_guess = '----'
                        database.append(current_game_statistics)
                        game_no = current_game_statistics['game']
                        new_word = string_obj.get_random_word()
                        new_score = game_obj.get_first_score(new_word)
                        current_game_statistics = {'game': game_no + 1, 'word': new_word, 'status': 'Started',
                                                   'bad_guess': 0,
                                                   'missed_letters': 0, 'score': new_score}
                        print(' New Game '.center(80, '#') + "\n")
                        print('New Guess: ----\n \nPlease enter a choice to begin the new game')
                else:
                    print("Hard Luck! no match found!")
                    current_game_statistics['status'] = 'playing'
                    current_game_statistics['missed_letters'] = current_game_statistics['missed_letters'] + 1
                    # current_game_statistics['score'] = current_game_statistics['score'] - update_score
            elif choice == 'g' or choice == 'G':
                result_g = game_obj.current_game_choice_g(new_word)
                if result_g == 'success':
                    print("Yes!!! You have guessed it right!".center(80, '#') + '\n')
                    current_game_statistics['status'] = 'Success'
                    current_guess = '----'
                    database.append(current_game_statistics)
                    game_no = current_game_statistics['game']
                    new_word = string_obj.get_random_word()
                    new_score = game_obj.get_first_score(new_word)
                    current_game_statistics = {'game': game_no + 1, 'word': new_word, 'status': 'Started', 'bad_guess': 0,
                                               'missed_letters': 0, 'score': new_score}
                    print(' New Game '.center(80, '#') + "\n")
                    print('New Guess: ----\n \nPlease enter a choice to begin the new game')
                else:
                    print("Sorry, Wrong guess!!! Pls. Try again".center(80, '#')+"\n")
                    current_game_statistics['status'] = 'playing'
                    current_game_statistics['bad_guess'] = current_game_statistics['bad_guess'] + 1
                    new_score = current_game_statistics['score']
                    new_score = 0.1 * new_score
                    current_game_statistics['score'] = current_game_statistics['score'] - new_score
            elif choice == 't' or choice == 'T':
                print('The word was : ' + new_word + '\n')
                update_score = game_obj.get_updated_score(new_word, current_guess)
                current_game_statistics['score'] = current_game_statistics['score'] - update_score
                current_game_statistics['status'] = 'Gave up'
                current_guess = '----'
                database.append(current_game_statistics)
                game_no = current_game_statistics['game']
                new_word = string_obj.get_random_word()
                new_score = game_obj.get_first_score(new_word)
                current_game_statistics = {'game': game_no + 1, 'word': new_word, 'status': 'Started', 'bad_guess': 0,
                                           'missed_letters': 0, 'score': new_score}
                print(' New Game '.center(80, '#') + "\n")
                print('New Guess: ----\n \nPlease enter a choice to begin the new game')
            elif choice == 'q' or choice == 'Q':
                if current_game_statistics['status'] == 'playing':
                    print('The word was : ' + new_word + '\n')
                    update_score = game_obj.get_updated_score(new_word, current_guess)
                    current_game_statistics['score'] = current_game_statistics['score'] - update_score
                    current_game_statistics['status'] = 'Quit'
                    database.append(current_game_statistics)
                print(' Game Overview '.center(80, '#') + '\n')
                print("{: >10} {: >10} {: >10} {: >10} {: >15} {: >15}".format(
                    *['Game', 'Word', 'Status', 'Bad Guess', 'Missed Letter', 'Score']))
                print("{: >10} {: >10} {: >10} {: >10} {: >15} {: >15}".format(
                    *['-----', '-----', '-----', '-----', '-----', '-----']))
                for data in database:
                    print("{: >10} {: >10} {: >10} {: >10} {: >15} {: >15f}".format(*data.values()))
                final_score = 0
                for data in database:
                    final_score = final_score + data['score']
                print('\nFinal Score : {: f}'.format(final_score))
                break
            else:
                print("\nCurrent Guess: " + current_guess + "\n \nSorry,s Please enter a correct choice")


if __name__ == "__main__":
    obj = Guess()
    obj.start_game()
