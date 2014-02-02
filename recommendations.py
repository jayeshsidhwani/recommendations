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

    def __available_similarities__(self):
        return ['euclidean', 'pearson']

    def build_recommendations(self, user1, user2, type):
        type = type.lower()
        if type not in self.__available_similarities__():
            print "%s similarity is not implemented yet. Available options: %s" %(type.title(),
                                                                                  self.__available_similarities__())
            return

        self.user1 = user1
        self.user2 = user2
        return getattr(self, '%s_similarity' %type)()

    def find_similar_items(self):
        """
        Find items that have been rated by both the users

        :author Jayesh
        """
        similar_items = []

        for movie in self.critics[self.user1].keys():
            if self.critics[self.user2].has_key(movie):
                similar_items.append(movie)
        return similar_items

    def euclidean_similarity(self):
        """
        Find items that have been rated by both the users

        :formula 1 / [1 - sqrt(sum( (x-y)2 ))]
        :author Jayesh
        """

        similar_items = self.find_similar_items()
        if not similar_items:
            return  0

        sum_of_square_difference = sum( [pow(self.critics[self.user1][movie] - self.critics[self.user2][movie], 2)
                                         for movie in similar_items] )
        return  1/(1 + sqrt(sum_of_square_difference))

    def pearson_similarity(self):
        """
        This finds the correlation between the 2 users.
        Formula: [ sum(X.Y) - sum(X).sum(Y)/N ] / [ (sum(X)2 - sum(X)/N)*(sum(Y)2 - sum(Y)/N) ]

        :author Jayesh
        """
        similar_items = self.find_similar_items()

        total_similar_products = len(similar_items)

        sum_of_user1 = sum([self.critics[self.user1][item] for item in similar_items])
        sum_of_user2 = sum([self.critics[self.user2][item] for item in similar_items])

        sum_of_products = sum([self.critics[self.user1][item] * self.critics[self.user2][item] for item in similar_items])

        square_sum_of_user1 = sum([pow(self.critics[self.user1][item], 2) for item in similar_items])
        square_sum_of_user2 = sum([pow(self.critics[self.user2][item], 2) for item in similar_items])

        numerator = sum_of_products - (sum_of_user1 * sum_of_user2)/total_similar_products
        denominator = sqrt((square_sum_of_user1 - pow(sum_of_user1, 2)/total_similar_products)*(square_sum_of_user2 - pow(sum_of_user2, 2)/total_similar_products))

        return  numerator/denominator

