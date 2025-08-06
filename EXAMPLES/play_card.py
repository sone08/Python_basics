class card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

        # properties and getters/setters. 

    @property
    def rank(self):
        return self._rank
    @property
    def suit(self):
        return self._suit
    
    @rank.setter
    def rank(self, value):
        if isinstance(value, str):
            self._rank = value
        else:
            raise TypeError("Rank must be a string")
    @suit.setter
    def suit(self, value):
        if isinstance(value, str):
            self._suit = value
        else:
            raise TypeError("Suit must be a string")
        
        def __str__(self):
            return f"{self.rank} of {self.suit}"
    def __repr__(self):
        return f"card({self.rank!r}, {self.suit!r})"

if __name__ == "__main__":
    c1 = card('A', 'Hearts')
    c2 = card('8', 'Diamonds')
    print(f"{c1.rank = }")
    print(f"{c1.suit = }")
    print(f"{c2.rank = }")
    print(f"{c2.suit = }")
    c1.rank = "K"
    print(f"{c1 = }")
    
