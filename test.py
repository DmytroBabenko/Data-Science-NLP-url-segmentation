from trie import Trie
from word_breaker import WordBreaker


def extract(url: str):
    if len(url) == 0:
        return url
    if url[0] == '#':
        url = url[1:]
    splitted = url.split('.')
    if "www." in url:
        return splitted[1]
    return splitted[0]


input_file = "input.txt"
lines = []
with open(input_file) as f:
  lines = f.readlines()

strings = [extract(line) for line in lines]


dict_words_file = "words.txt"
words_dict = []
with open(dict_words_file) as f:
    for line in f:
        words_dict.append(line.rstrip().lower())


trie = Trie.create_trie(words_dict)

word_breaker = WordBreaker(trie)


broken, words = word_breaker.word_break("businessweek29.5")
print(words)




# broken_list = []
# for string in strings:
#     broken, words = word_breaker.word_break(string)
#     if broken is True:
#         broken_list.append(words)
#     else:
#         broken_list.append('')