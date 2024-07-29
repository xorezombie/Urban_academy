def single_root_words(root_word, *other_words):
    root_word_lower = root_word.lower()
    same_words = []
    for word in other_words:
        word_lower = word.lower()
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)
    return same_words
result_1 = (single_root_words('корм', 'кормить', 'Комбикорм', 'Карма'))
result_2 = (single_root_words('Автомашинально', 'авто', 'машина', 'шина', 'Автомат', 'том'))
print(result_1)
print(result_2)