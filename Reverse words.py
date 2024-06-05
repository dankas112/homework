# def reverse_words(text):
#     splited_text = text.split(' ')
#     reversed_text = []
#     print(splited_text)
#     for x in splited_text:
#         c = x[::-1]
#         reversed_text.append(c)
#     print(reversed_text)
#     textR = reversed_text[0] +


# def reverse_words(text):
#     print(text[::-1])

# print(text.find(' '))
#
# def reverse_words(text):
#     jopa = ''
#     for x in text:
#         if x.isalpha():
#             jopa += '1'
#         else:
#             jopa += '0'
#     print(jopa)
#     a = 0
#     b = 0
#     for x in jopa:
#         if jopa
#
# чпек:
def reverse_words(sentence):
    words = sentence.split(" ")
    reversed_words = [word[::-1] for word in words]  # Разворачиваем каждое слово
    return " ".join(reversed_words)  # Объединяем слова обратно в строку с пробелами


# Пример использования функции
sentence = "This is an example!"
print(reverse_words(sentence))


def reverse_words(text):
    words = text.split(' ')
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)
