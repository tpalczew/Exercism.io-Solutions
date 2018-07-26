class Allergies(object):

    # Class Attribute
    scores = {'eggs':1, 'peanuts':2, 'shellfish':4, 'strawberries':8, 'tomatoes':16, 'chocolate':32, 'pollen':64, 'cats':128}

    # Initializer / Instance Attributes
    def __init__(self, score):
        self.score = score
        self.lst = list(allergy for allergy in self.scores if self.is_allergic_to(allergy))

    # Instance Method
    def is_allergic_to(self, item):
        if self.scores[item] & self.score == self.scores[item]:
            return True
        if self.scores[item] & self.score == 0:
            return False
        return self.scores[item] & self.score

