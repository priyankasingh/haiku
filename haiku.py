import re
book = open('book.txt', 'r')

dictionary={}

booklist = []

with open('book.txt','r') as f:
    for line in f:
        for word in line.split():
            if word.isalpha():
                booklist.append(word.lower())

def add_to_dictionary(key, value):
    if not key in dictionary:
        dictionary[key] = []
    dictionary[key].append(value)

for i in range(len(booklist)):
    if i > 1:
        add_to_dictionary(booklist[i-2] + " " + booklist[i-1], booklist[i])
        add_to_dictionary(booklist[i-1], booklist[i])

words = dictionary


import random
import sys

def count_syllables(word):
    vowels = ['a', 'e', 'i', 'o', 'u']

    on_vowel = False
    in_diphthong = False
    minsyl = 0
    maxsyl = 0
    lastchar = None

    word = word.lower()
    for c in word:
        is_vowel = c in vowels

        if on_vowel == None:
            on_vowel = is_vowel

        # y is a special case
        if c == 'y':
            is_vowel = not on_vowel

        if is_vowel:
            if not on_vowel:
                # We weren't on a vowel before.
                # Seeing a new vowel bumps the syllable count.
                minsyl += 1
                maxsyl += 1
            elif on_vowel and not in_diphthong and c != lastchar:
                # We were already in a vowel.
                # Don't increment anything except the max count,
                # and only do that once per diphthong.
                in_diphthong = True
                maxsyl += 1

        on_vowel = is_vowel
        lastchar = c

    # Some special cases:
    if word[-1] == 'e':
        minsyl -= 1
    # if it ended with a consonant followed by y, count that as a syllable.
    if word[-1] == 'y' and not on_vowel:
        maxsyl += 1

    return maxsyl
    return minsyl, maxsyl


syllables = {word: count_syllables(word) for word in words.keys()}

# print syllables

one_syllable_words = [k for k,v in syllables.items() if v == 1]

# print one_syllable_words

def get_next_word(key, remaining_number_of_syllables):
    possible_next_word = filter(lambda w : syllables.get(w, 9999) < remaining_number_of_syllables and syllables.get(w, 9999) != count_syllables(start_word) and not w == key, words.get(key, []))
    if len(possible_next_word) == 0:
        possible_next_word = filter(lambda w : syllables.get(w, 9999) < remaining_number_of_syllables and not w == key, words.get(key, []))
    if len(possible_next_word) == 0:
        return None
    return random.choice(possible_next_word)

def generate_line(start_word, number_of_syllables):
    start_syllables = count_syllables(start_word)
    next_word = start_word
    remaining_number_of_syllables = number_of_syllables - start_syllables
    line = start_word
    last_word = None
    while remaining_number_of_syllables > 0:
        if last_word == None:
            last_word = next_word
            next_word = get_next_word(next_word, remaining_number_of_syllables)
        else:
            key = last_word + " " + next_word
            last_word = next_word
            next_word = get_next_word(key, remaining_number_of_syllables)
            if not next_word:
                next_word = get_next_word(next_word, remaining_number_of_syllables)


        # print next_word, possible_next_word
        if not next_word:
            next_word = random.choice(one_syllable_words)

        line += " " + next_word
        remaining_number_of_syllables -= syllables[next_word]
    return line

def generate_haiku(start_word):
    line1 = generate_line(start_word, 5)
    line2 = generate_line(random.choice(words.keys()), 7)
    line3 = generate_line(random.choice(words.keys()), 5)
    return "%s\n%s\n%s" % (line1, line2, line3)

start_word = raw_input("Start word: ")

if start_word == "":
    start_word = random.choice(words.keys())

line = generate_haiku(start_word)
print line