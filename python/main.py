import re


# funcção que monta um vetor com todas as palavras diferentes dado um arquivo e um vetor de palavras
def check_words_on_files(file_name, vocabulary, sequence_words):
    with open(file_name, 'r') as file:
        for line in file:
            line_spread = []
            for line_iteration in line.split():
                line_spread += line_iteration.split('-')
            for index, word in enumerate(line_spread):
                if sequence_words == 2:
                    if index < len(line_spread) - 1:
                        word_test = re.sub('\W+', '', word).lower()
                        word_test_next = re.sub('\W+', '', line_spread[index + 1]).lower()
                        word_test_if = word_test + ' ' + word_test_next
                        if not word_test_if in vocabulary:
                            vocabulary.append(word_test + ' ' + word_test_next)
                else:
                    word_test = re.sub('\W+', '', word).lower()
                    if not word_test in vocabulary:
                        vocabulary.append(word_test)
    return vocabulary


def file_to_string(file_name, sequence_words):
    string_return = []
    with open(file_name, 'r') as file:
        for line in file:
            line_spread = []
            for line_iteration in line.split():
                line_spread += line_iteration.split('-')
            for index, word in enumerate(line_spread):
                if sequence_words == 2:
                    if index < len(line_spread) - 1:
                        word_test = re.sub('\W+', '', word).lower()
                        word_test_next = re.sub('\W+', '', line_spread[index + 1]).lower()
                        string_return.append(word_test + ' ' + word_test_next)
                else:
                    word_test = re.sub('\W+', '', word).lower()
                    string_return.append(word_test)
    return string_return


def count_words_on_file(file_name, words_list, sequence_words):
    list_of_counted_words = []
    words_in_file = file_to_string(file_name, sequence_words)
    for word_to_count in words_list:
        list_of_counted_words.append(words_in_file.count(word_to_count))
    return list_of_counted_words


words = check_words_on_files('text1.txt', [], 1)
words = check_words_on_files('text2.txt', words, 1)
words_text1 = check_words_on_files('text1.txt', [], 1)
words_text2 = check_words_on_files('text2.txt', [], 1)
list_words1 = count_words_on_file('text1.txt', words, 1)
list_words2 = count_words_on_file('text2.txt', words, 1)

print('\n=== PALAVRAS ISOLADAS ===')
print('Vocabulário')
print('Texto 1: ', words_text1)
print('Texto 2: ', words_text2)
print('Texto 1 e 2: ', words)
print('Vetor de palavras')
print('Texto 1: ', list_words1)
print('Texto 2: ', list_words2)

print('\n=== PALAVRAS EM SEQUENCIA ===')
words_2seq = check_words_on_files('text1.txt', [], 2)
words_2seq = check_words_on_files('text2.txt', words_2seq, 2)
words_text1_2seq = check_words_on_files('text1.txt', [], 2)
words_text2_2seq = check_words_on_files('text2.txt', [], 2)
list_words1_2seq = count_words_on_file('text1.txt', words_2seq, 2)
list_words2_2seq = count_words_on_file('text2.txt', words_2seq, 2)

print('Vocabulário')
print('Texto 1: ', words_text1_2seq)
print('Texto 2: ', words_text2_2seq)
print('Texto 1 e 2: ', words_2seq)
print('Vetor de palavras')
print('Texto 1: ', list_words1_2seq)
print('Texto 2: ', list_words2_2seq)