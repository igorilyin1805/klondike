'''
    Дана строка, разбить ее на слова. Слова разделены одним пробелом
    "Александр Сергеевич Пушкин" -> ["Александр", "Сергеевич", "Пушкин"]

def get_words(input_s: str) -> list[str]:
    curr_word = ""
    words = []
    for s in input_s:
        if s != " ":
            curr_word += s
        else:
            words.append(curr_word)
            curr_word = ""
    if curr_word:
        words.append(curr_word)

    return words
'''


def get_words(input_s: str) -> list[str]:
    return  input_s.split()


