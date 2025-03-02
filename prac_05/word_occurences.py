"""
Word Occurrences
Estimate: 30 minutes
Actual:   40 minutes
"""

word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
letters = list(word_to_count.keys())
max_word_length = max([len(word) for word in letters])
letters.sort()
for word in letters:
    thing, width, other_thing = word, max_word_length, word_to_count[word]
    print(f"{thing:{width}} : {other_thing}")
    # print(f"{word:{max_word_length}} : {word_to_count[word]}")