from trie import Trie


class WordBreaker:

    def __init__(self, trie: Trie):
        self.trie = trie

    def word_break(self, input_str: str):

        #key - position, value - word
        all_words = list()

        self._word_break_helper(input_str, 0, all_words)

        words = WordBreaker._find_the_best_combination_of_words(all_words, len(input_str))

        return words

    def _word_break_helper(self, input_str: str, origin_pos : int, all_words: list):
        size = len(input_str)

        if size == 0:
            return

        for i in range(1, size + 1):
            sub_str = input_str[0:i]

            if WordBreaker._is_int_or_float(sub_str) or self.trie.search(sub_str):
                all_words.append((origin_pos, sub_str))
                self._word_break_helper(input_str[i: size], origin_pos + i, all_words)


    #TODO: implement it more elegant and optimizer using dynamic programmin
    @staticmethod
    def _find_the_best_combination_of_words(all_words, length):
        next_pos = 0
        all_combination = []
        words = []

        words_pos = WordBreaker._find_words_in_pos(all_words, next_pos)
        while len(words_pos) > 0:
            p, w = words_pos[-1]
            if len(words) == 0 or (p, w) != words[-1]:
                words.append((p, w))

            next_pos = p + len(w)

            tmp_words = WordBreaker._find_words_in_pos(all_words, next_pos)
            if len(tmp_words) == 0:
                if next_pos == length:
                    all_combination.append(words.copy())
                words.pop()
                if words_pos[-1] in all_words:
                    all_words.remove(words_pos[-1])

                words_pos.pop()

            words_pos += tmp_words

        min = 1000
        min_idx = -1
        for i in range(0, len(all_combination)):
            if len(all_combination[-1]) < min:
                min = len(all_combination[-1])
                min_idx = i

        result = []
        for (p, w) in all_combination[min_idx]:
            result.append(w)


        return result



    @staticmethod
    def _find_words_in_pos(all_words, pos):
        all = list()
        for i in range(0, len(all_words)):
            p, w = all_words[i]
            if p == pos:
                all.append(all_words[i])

        return all


    @staticmethod
    def _is_int_or_float(string):
        if string == '.':
            return True

        idx = ord(string[0])
        if idx < ord('0') or idx > ord('9'):
            return False

        try:
            val = float(string)
            return True
        except:
            return False



# if __name__== "__main__":
#
#
#     f = WordBreaker._is_int_or_float("week8")
#
#     dictionary = ["mobile", "samsung", "sam", "sung", "man", "mango",  "icecream", "and", "go", "i", "like", "ice", "cream", "us", "to", "a", "day", "today"]
#
#     trie = Trie.create_trie(dictionary)
#     word_breaker = WordBreaker(trie)
#
#     broken, words = word_breaker.word_break("usatoday")
#
#     a = 10

