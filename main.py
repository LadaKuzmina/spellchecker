import argparse
import re
import unicodedata
from trie import Trie

with open('C:\\Users\\Лада\\PycharmProjects\\spellchecker\\Texts\\4.txt', 'r') as f:
    my_list = [line.strip() for line in f]
    dict_trie_words_correct = Trie.add(my_list)


def show(text):
    list_maybe_words = []
    min_dist = 1000000
    correct_word = ""
    if text == "esc":
        word = input('Добавить в словарь:')
        if word not in my_list:
            my_list.append(word)
            print("Слово добавлено в словарь")
        else:
            print("Такое слово уже в словаре")
    else:
        for i in range(0, len(my_list)):
            dis = levenshtein_distance(text, my_list[i])
            if min_dist == dis:
                list_maybe_words.append(my_list[i])
            if min_dist > dis:
                min_dist = dis
                list_maybe_words.clear()
                correct_word = my_list[i]
        if list_maybe_words:
            a = (" ".join(list_maybe_words))
            print(
                "Введенное слово: " + text + ' ' + "Корректное слово: " + correct_word +
                ' ' + "Возможные варианты: " + a)
        else:
            print("Введенное слово: " + text + ' ' + "Корректное слово: " + correct_word)


def levenshtein_distance(a, b):
    def recursive(i, j):
        if i == 0 or j == 0:
            return max(i, j)
        elif a[i - 1] == b[j - 1]:
            return recursive(i - 1, j - 1)
        else:
            return 1 + min(
                recursive(i, j - 1), recursive(i - 1, j), recursive(i - 1, j - 1))

    return recursive(len(a), len(b))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Проверка на орфографию")
    parser.add_argument("word", type=str, help="Введите текст")
    parser.add_argument("--check", help="Проверка")
    parser.add_argument("--check_file", help="Проверка на орфографию текстового файла")
    parser.add_argument('--file', type=argparse.FileType('r'))
    args = parser.parse_args()
    correct_words = []
    if args.check == "check":
        res = re.split(r"(.*?)[ \.:;,?!\n]", args.word)
        list_words = re.split(r"(.*?)[ \.:;,?!\n]", args.word)
        while '' in list_words:
            list_words.remove('')
        for k in list_words:
            bool_in_trie = Trie.in_trie(dict_trie_words_correct, k)
            if bool_in_trie:
                print("Введенное слово ptправильное: " + k)
            if not bool_in_trie:
                correct_words.append(show(k))
    if args.check_file == "check_file":
        try:
            with open(args.word, 'r', encoding='utf8') as s:
                list_text = s.read()
            list_text_1 = unicodedata.normalize('NFC', list_text)
            list_split_words = list_text_1.split()
            for k in list_split_words:
                bool_in_trie = Trie.in_trie(dict_trie_words_correct, k)
                if bool_in_trie:
                    print("Введенное слово правильное: " + k)
                if not bool_in_trie:
                    correct_words.append(show(k))
        except IOError:
            print("Не удалось прочитать файл", args.word)
