import os
import random
from collections import defaultdict


class Player:
    answers = defaultdict(lambda: [])
    score = 0

    def choose(self, category, answer):
        self.answers[category].append(answer)


class Game:
    alphabet = 'abcdefghijklmnopqrstuvxyzåäö'
    letter = alphabet[random.randint(0,len(alphabet)-1)]
    series = [
             'actor',
             'scientist',
             'musician',
             'bishop'
             ]
    players = []
    
    def run(self):
        no_of_players = int(input('How many are playing? '))
        for _ in range(no_of_players):
            self.players.append(Player())
        os.system('clear')

        for category in self.series:
            for player in self.players:
                answer = input('Choose and {} starting on the letter {}: '.format(category, self.letter))
                player.choose(category, answer.lower())
                os.system('clear')
        
        all_answers = defaultdict(lambda: [])

        for player in self.players:
            for category in self.series:
                all_answers[category].extend(player.answers)

        for player in self.players:
            for category, answers in all_answers.items():
                occurences = answers.count(player.answers[category])
                player.score += no_of_players - occurences + 1

        for i, player in enumerate(self.players):
            print('Player {} got a score of {}'.format(i+1, player.score))



if __name__=='__main__':
    game = Game()
    try:
        game.run()
    except Exception as e:
        print(str(e))




