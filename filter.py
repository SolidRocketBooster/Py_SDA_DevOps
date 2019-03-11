
def filter_long_words(word_lng, words_list):
    return [word for word in words_list if len(word) > word_lng]


assert filter_long_words(5, ['piwo', 'wino', 'czasopisma', 'ubrania', 'napoje']) == ['czasopisma', 'ubrania', 'napoje']

