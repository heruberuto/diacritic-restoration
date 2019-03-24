import json

import accents


def eisner():
    return Hmm(
        ('H', 'C'),
        [1, 2, 3],
        {'H': .8, 'C': .2},
        {'H': {'H': .7, 'C': .3}, 'C': {'C': .6, 'H': .4}},
        {'H': {1: .2, 2: .4, 3: .4}, 'C': {1: .5, 2: .4, 3: .1}, }
    )


def princess():
    return Hmm(
        ('healthy', 'sick'),
        ['well', 'weak', 'dying'],
        {'healthy': 0.6, 'sick': 0.4},
        {'healthy': {'healthy': 0.7, 'sick': 0.3}, 'sick': {'healthy': 0.4, 'sick': 0.6}, },
        {'healthy': {'well': 0.5, 'weak': 0.4, 'dying': 0.1}, 'sick': {'well': 0.1, 'weak': 0.3, 'dying': 0.6}, }
    )


def simple_diacritics():
    dummy = 1 / len(accents.SUPPORTED)
    trigrams = ['bou', 'our', 'ure', 're ', 'e p', ' pr']
    return Hmm(
        accents.SUPPORTED,
        trigrams,
        {accent: dummy for accent in accents.SUPPORTED},
        {accent_a: {accent_b: dummy for accent_b in accents.SUPPORTED} for accent_a in accents.SUPPORTED},
        {accent: {trigram: 1 / 6 for trigram in trigrams} for accent in accents.SUPPORTED},
    )


class Hmm:
    def __init__(self, states=None, symbols=None, initial_p=None, transition_p=None, emission_p=None):
        if states is None: states = ()
        if symbols is None: symbols = []
        if initial_p is None: initial_p = {}
        if transition_p is None: transition_p = {}
        if emission_p is None: emission_p = {}
        self.states, self.symbols = states, symbols
        self.initial_p, self.transition_p, self.emission_p = initial_p, transition_p, emission_p

    def tag(self, sentence):
        V = [{}]
        for state in self.states:
            V[0][state] = self.initial_p[state] * self.emission_p[state][sentence[0]], None
        for t in range(1, len(sentence)):
            V.append({})
            for state in self.states:
                max_tr_prob, prev_st_selected = -1, None
                for prev_st in self.states:
                    tr_prob = V[t - 1][prev_st][0] * self.transition_p[prev_st][state]
                    if tr_prob > max_tr_prob:
                        max_tr_prob = tr_prob
                        prev_st_selected = prev_st

                max_prob = max_tr_prob * self.emission_p[state][sentence[t]]
                V[t][state] = max_prob, prev_st_selected

        opt = []
        # The highest probability
        max_prob = max(value[0] for value in V[-1].values())
        previous = None
        # Get most probable state and its backtrack
        for state, data in V[-1].items():
            if data[0] == max_prob:
                opt.append(state)
                previous = state
                break
        # Follow the backtrack till the first sentenceervation
        for t in range(len(V) - 2, -1, -1):
            opt.insert(0, V[t + 1][previous][1])
            previous = V[t + 1][previous][1]

        return opt, max_prob

    def save(self, filename):
        with open(filename, 'w', encoding='utf8') as file:
            json.dump({
                "states": self.states,
                "symbols": self.symbols,
                "initial_p": self.initial_p,
                "transition_p": self.transition_p,
                "emission_p": self.emission_p
            }, file)
            return True

    @staticmethod
    def load(filename):
        with open(filename, 'r', encoding='utf8') as file:
            data = json.load(file)
            return Hmm(data["states"], data["symbols"], data["initial_p"],
                       data["transition_p"], data["emission_p"])


principesa = Hmm.load("prince.json")
print(principesa.tag(["well", "weak", "dying"]))
principesa.save("prince2.json")
