import os


class Player:
    answers = []
    score = 0

    def choose(self, answer):
        self.answers.append(answer)


class Game:
    letter = 's'
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
                player.choose(answer.lower())
                os.system('clear')
        
        all_answers = []

        for player in self.players:
            all_answers.extend(player.answers)

        for player in self.players:
            for answer in player.answers:
                occurences = all_answers.count(answer)
                player.score += no_of_players - occurences + 1

        for i, player in enumerate(self.players):
            print('Player {} got a score of {}'.format(i+1, player.score))



if __name__=='__main__':
    game = Game()
    game.run()




