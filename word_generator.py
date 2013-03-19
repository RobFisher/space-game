__author__ = 'rob'


# Table of which letters can follow a given letter
_letter_table = {
    'a': 'abcdefghjklmnpqrstvwxyz',
    'b': 'abehiloruy',
    'c': 'acehhhiklorsuwy',
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
    'p': 'aehhinrstuwy',
    'q': 'aeiouuuuuuuuuuuuuuuuuuuuuy',
    'r': 'aehioruy',
    's': 'accehhhhhilmnopqrtuwy',
    't': 'aehhhhhiorsuyz',
    'u': 'abcdefghjklmnopqrstuvwxyz',
    'v': 'aeiouy',
    'w': 'aehioruy',
    'x': 'aeiosuxyz',
    'y': 'abcdefghijklmnopqrstuvwxyz',
    'z': 'aehiosuz'
}

_new_syllable_after_vowel = 'bcdfghjklmnpqrstvwxyz'

_vowels = 'aaaeeeiioouy'
_consonants = 'bbccdddffgghjklmmnnppqrrsssttvwxyz'
_letters = _vowels + _consonants

# Exceptions to the rule that two consonants must be followed by a vowel
_double_consonants = {
    'ch': 'lr',
    'ph': 'lr',
    'sc': 'hlr',
    'sh': 'cklmnprtw',
    'th': 'r'
}


def _roll_d20(random):
    return random.randint(1, 20)


def _pick_letter(random, choices):
    index = random.randint(0, len(choices) - 1)
    return choices[index]


_new_syllable_chance = [0, 0, 5, 10, 15, 16, 17, 18, 19]


def _new_syllable(random, length, syllable):
    for letter in syllable:
        if letter in _vowels:
            if length >= len(_new_syllable_chance) or _roll_d20(random) < _new_syllable_chance[length]:
                return True
            break
    return False


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
    if max_length > 1:
        result += _pick_letter(random, _letter_table[result])
    syllable_length = 2
    while len(result) < length:
        if _new_syllable(random, syllable_length, result[0-syllable_length:]):
            syllable_length = 0
            if not result[-1:] in _vowels:
                result += _pick_letter(random, _letter_table[result[-1:]])
            else:
                result += _pick_letter(random, _new_syllable_after_vowel)
        elif not result[-1:] in _vowels:
            if _roll_d20(random) > 15:
                result += _pick_letter(random, _vowels)
            elif result[-2:-1] not in _vowels:
                consonant_pair = result[-2:]
                if consonant_pair in _double_consonants:
                    result += _pick_letter(random, _double_consonants[consonant_pair])
                else:
                    result += _pick_letter(random, _vowels)
            else:
                result += _pick_letter(random, _letter_table[result[-1:]])
        else:
            result += _pick_letter(random, _letter_table[result[-1:]])
        syllable_length += 1
    return result


if __name__ == '__main__':
    import random
    r = random.Random()
    for i in range(0, 200):
        print make_word(r, 2, 8)
