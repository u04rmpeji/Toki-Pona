# toki pona name generator
from random import choice
def generator(amount) -> list[str]:
    # the structure of toki pona syllables is (C)V(N), where C is a consonant, V is a vowel, and N is a nasal sound
    # double consonants and double vowels are forbidden
    # n and m can't be next to each other. in other words, nn, mm, nm, mn are forbidden
    # official words are not used to avoid confusion
    consontants = ['p', 't', 'k', 's', 'm', 'n', 'l', 'w', 'j']
    vowels = ['a', 'e', 'i', 'o', 'u']
    forbidden = ['ti', 'ji', 'wo', 'wu']
    with open('Toki Pona/TokiPonaWords.txt', 'r') as f:
        words = f.read().splitlines()
    
    def random_syllable(ends_in: str = None) -> str:
        while True:
            syllable = choice(consontants) + choice(vowels) 
            if syllable not in forbidden:
                if choice([True, False]):
                    syllable += 'n'
                if {ends_in, syllable[0]} not in [{'m', 'n'}, {'n', 'n'}, {'m', 'm'}]:
                    return syllable
    names = []
    for _ in range(amount):
        while True: # make sure the name is not a official word also not duplicated
            name = ''
            start_with_vowel = choice([True, False])
            if start_with_vowel:
                name += choice(vowels)
                if choice([True, False]):
                    name += 'n'
            else:
                name += random_syllable()
            # determine how many syllables are in the name
            while True:
                name += random_syllable(name[-1])
                if choice([True, True, False]):
                    break
            
            if name not in words and name.capitalize() not in names:
                names.append(name.capitalize())
                break
    
    return sorted(names)
        
with open('Toki Pona/output.txt', 'w') as f:
    for name in generator(100):
        f.write(name + '\n')
