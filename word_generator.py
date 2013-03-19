__author__ = 'rob'


# Table of which letters can follow a given letter at the start of a syllable.
_start_letter_table = {
    'a': 'abcdefghjklmnpqrstvwxyz',
    'b': 'abehiloruy',
    'c': 'acehiklorsuwy',
    'd': 'adeijoruwy',
    'e': 'abcdefghijklmnopqrstuvwxyz',
    'f': 'aefhiloruwy',
    'g': 'aeghiloruwy',
    'h': 'aeiouy',
    'i': 'abcdefghjklmnopqrstuvwxyz',
    'j': 'aeiouy',
    'k': 'aehikloruwy',
    'l': 'aeilouy',
    'm': 'aehimopuwy',
    'n': 'aehinouy',
    'o': 'abcdefghijklmnopqrstuvwxyz',
    'p': 'aehinrstuwy',
    'q': 'aeiouuuuuuuuuuuuuuuuuuuuuy',
    'r': 'aehioruy',
    's': 'aeilmnopqrtuwy',
    't': 'aeiorsuyz',
    'u': 'abcdefghjklmnopqrstuvwxyz',
    'v': 'aeiouy',
    'w': 'aehioruy',
    'x': 'aeiosuxyz',
    'y': 'abcdefghijklmnopqrstuvwxyz',
    'z': 'aehiosuz'
}

_vowels = 'aaaeeeiioouy'
_consonants = 'bbccdddffgghjklmmnnppqrrsssttvwxyz'
_letters = _vowels + _consonants

# Exceptions to the rule that two consonants must be followed by a vowel
_double_consonants = {
    'ch': 'lr',
    'ph': 'lr',
    'sc': 'hlr',
    'sh': 'cklmnprtw'
}


def _roll_d20(random):
    return random.randint(1, 20)


def _pick_letter(random, choices):
    index = random.randint(0, len(choices) - 1)
    return choices[index]


def make_word(random, min_length=3, max_length=20):
    """Return a random word.

    :param random: A random number generator of type random.Random
    :type random: Random
    :param min_length: The minimum length of the word to return
    :param max_length: The maximum length of the word to return
    :rtype: str
    """
    length = random.randint(min_length, max_length)
    result = _pick_letter(random, _letters)
    while len(result) < length:
        if not result[-1:] in _vowels:
            if _roll_d20(random) > 10:
                result += _pick_letter(random, _vowels)
            elif len(result) > 1 and result[-2:-1] not in _vowels:
                consonant_pair = result[-2:]
                if consonant_pair in _double_consonants:
                    result += _pick_letter(random, _double_consonants[consonant_pair])
                else:
                    result += _pick_letter(random, _vowels)
            else:
                result += _pick_letter(random, _start_letter_table[result[-1:]])
        else:
            result += _pick_letter(random, _start_letter_table[result[-1:]])
    return result


if __name__ == '__main__':
    import random
    r = random.Random()
    for i in range(0, 200):
        print make_word(r)
