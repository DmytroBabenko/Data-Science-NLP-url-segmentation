from trie import Trie


class WordBreaker:

    def __init__(self, trie: Trie):
        self.trie = trie

    def word_break(self, input_str: str):
        print(input_str)

        #key - position, value - word
        words_dict = dict()

        broken = self._word_break_helper(input_str, 0, words_dict)

        words = []
        true_pos = 0
        for key in words_dict:
            if key == true_pos:
                words.append(words_dict[key])
                true_pos += len(words_dict[key])

        return broken, words

    def _word_break_helper(self, input_str: str, origin_pos : int, words_dict: dict):
        size = len(input_str)

        if size == 0:
            return True


        for i in range(1, size + 1):

            sub_str = input_str[0:i]

            if  WordBreaker._is_int_or_float(sub_str) or self.trie.search(sub_str):
                words_dict[origin_pos] = sub_str

                if self._word_break_helper(input_str[i: size], origin_pos + i, words_dict) is True:
                    return True

        return False

    @staticmethod
    def _is_int_or_float( string):
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



if __name__== "__main__":
    dictionary = ["mobile", "samsung", "sam", "man", "mango",  "icecream", "and", "go", "i", "like", "ice", "cream"]

    trie = Trie.create_trie(dictionary)
    word_breaker = WordBreaker(trie)

    broken, words = word_breaker.word_break("ilikesamsung")

    a = 10

