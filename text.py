import re


def get_words():
    set_words = set()
    with open("C:\\Users\\Лада\\PycharmProjects\\spellchecker\\Texts\\t.txt", "r", encoding='utf8') as f:
        for i in f.readlines():
            s = re.findall(r"([-|\w]*)", i.lower())
            for j in s:
                if len(j) > 1:
                    set_words.add(j)
            if len(set_words) < 100:
                return set_words


def open_text(set_words):
    with open("4.txt", "w") as a:
        for word in set_words:
            print(word)
            a.write(word + "\n")


z = get_words()
open_text(z)