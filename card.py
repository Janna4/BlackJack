class Card(object):

    #
    # Note: if the user tries to make a card without one of these suits as the suit, it'll
    # cause issues later on. Same problem with the card types
    #
    suits = {'hearts': {'color': 'red', 'symbol': '\u2665'},
             'diamonds': {'color': 'red', 'symbol': '\u2666'},
             'spades': {'color': 'black', 'symbol': '\u2660'},
             'clubs': {'color': 'black', 'symbol': '\u2663'}}

    values = {'ace': {'hardValue': 11, 'softValue': 1},
              'two': {'hardValue': 2, 'softValue': 2},
              'three': {'hardValue': 3, 'softValue': 3},
              'four': {'hardValue': 4, 'softValue': 4},
              'five': {'hardValue': 5, 'softValue': 5},
              'six': {'hardValue': 6, 'softValue': 6},
              'seven': {'hardValue': 7, 'softValue': 7},
              'eight': {'hardValue': 8, 'softValue': 8},
              'nine': {'hardValue': 9, 'softValue': 9},
              'ten': {'hardValue': 10, 'softValue': 10},
              'jack': {'hardValue': 10, 'softValue': 10},
              'queen': {'hardValue': 10, 'softValue': 10},
              'king': {'hardValue': 10, 'softValue': 10}}

    def __init__(self, name, suit):
        self.__name = name
        self.__suit = suit
        self.__color = Card.suits[self.__suit]['color']
        self.__hard_value = Card.values[self.__name]['hardValue']
        self.__soft_value = Card.values[self.__name]['softValue']
        self.__visible = False

    def __str__(self):
        string = str(self.__name)
        string += " "
        string += suits[self.__suit]['symbol']
        return string

    def get_name(self):
        if self.__visible:
            return self.__name
        else:
            return "unknown"

    def get_suit(self):
        if self.__visible:
            return self.__suit
        else:
            return "unknown"

    def get_color(self):
        if self.__visible:
            return self.__color
        else:
            return "unknown"

    def get_hard_value(self):
        if self.__visible:
            return self.__hard_value
        else:
            return "unknown"

    def get_soft_value(self):
        if self.__visible:
            return self.__soft_value
        else:
            return "unknown"

    def get_visibility(self):
        return self.__visible

    def set_visible(self, visible):
        if isinstance(visible, bool):
            self.__visible = visible
        else:
            raise TypeError('visible must be boolean.')

    def flip(self):
        if self.__visible == True:
            self.set_visible(False)
        elif self.__visible == False:
            self.set_visible(True)
        else:
            raise TypeError('self.__visible must be boolean.')