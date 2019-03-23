def eisner():
    return Hmm(
        ('H', 'C'), (1, 2, 3), {'H': .8, 'C': .2},
        {'H': {'H': .7, 'C': .3}, 'C': {'C': .6, 'H': .4}},
        {'H': {1: .2, 2: .4, 3: .4}, 'C': {1: .5, 2: .4, 3: .1}, }
    )


class Hmm:
    def __init__(self, states=None, symbols=None, initial_p=None, transition_p=None, emission_p=None):
        if states is None:
            states = ()
        if symbols is None:
            symbols = ()
        if initial_p is None:
            initial_p = {}
        if transition_p is None:
            transition_p = {}
        if emission_p is None:
            emission_p = {}
        self.states = states
        self.symbols = symbols
        self.p_initial = initial_p
        self.p_transition = transition_p
        self.p_emission = emission_p

    def tag(self, sentence):
