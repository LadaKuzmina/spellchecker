_end = '_end_'


class Trie:
    def add(words):
        root = dict()
        for word in range(len(words)):
            current_dict = root
            for letter in words[word]:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[_end] = _end
        return root

    def in_trie(trie_dict, words):
        current_dict = trie_dict
        for word in range(len(words)):
            for letter in words[word]:
                if letter not in current_dict:
                    return False
                current_dict = current_dict[letter]
        return _end in current_dict
