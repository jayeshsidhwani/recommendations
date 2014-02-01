from math import sqrt

class Recommendations():

    def __init__(self):
        self.critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
                                       'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 'The Night Listener': 3.0},
                        'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5,
                                        'Superman Returns': 5.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 3.5},
                        'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                                             'Superman Returns': 3.5, 'The Night Listener': 4.0},
                        'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                                         'The Night Listener': 4.5, 'Superman Returns': 4.0, 'You, Me and Dupree': 2.5},
                        'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0,
                                         'Superman Returns': 3.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 2.0},
                        'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'The Night Listener': 3.0,
                                          'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
                        'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}
        }

    def build_recommendations(self):
        pass

    def similarity(self, user_1, user_2):
        similar_items = []

        for movie in self.critics[user_1].keys():
            if self.critics[user_2].has_key(movie):
                similar_items.append(movie)

        sum_of_square_difference = sum( [pow(self.critics[user_1][movie] - self.critics[user_2][movie], 2) for movie in similar_items] )
        return  1/(1 + sqrt(sum_of_square_difference))