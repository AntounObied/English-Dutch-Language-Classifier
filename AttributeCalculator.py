def no_duplicates(list):
    """
    Removes all duplicates from a list
    :param list: List with duplicates
    :return: List with no duplicates
    """
    no_duplicate_list = []
    for i in list:
        if i not in no_duplicate_list:
            no_duplicate_list.append(i)
    return no_duplicate_list


def remove_all_occurences(element, list):
    """
    Removes all occurences of a certain element from a list
    :param element: element to be removed
    :param list: List to be checked
    :return: List with all occurrences of element removed
    """
    result = []
    for i in list:
        if i != element:
            result.append(i)
    return result


def normalize_data(data):
    """
    Normalize data
    :param data: Data to be normalized
    :return: Normalized set of data
    """
    total = sum(data)
    normalized = []
    for i in data:
        normalized.append((i / total))
    return normalized


def get_max_key(list, key):
    """
    Gets the maximum number from a list
    :param list: List to be checked
    :param key: Key with the max val
    :return: Max item
    """
    return max(list, key=lambda x: x)


def average_word_length(sentence):
    """
    Average length of an English word is just under 5, while for Dutch word it is just over 5
    :param sentence: The sentence to check average word length
    :return: True if length < 5, false otherwise
    """
    words_in_sentence = sentence.split()
    total_word_length = 0
    number_of_words = 0

    for word in words_in_sentence:
        number_of_words += 1
        total_word_length += len(word)
    average_length = total_word_length / number_of_words

    if average_length < 5:
        return True
    else:
        return False


def contains_q(sentence):
    """
    Least used alphabets in Dutch are Q and X
    :param sentence: Sentence to check if Q is present
    :return: True if Q is in sentence, false otherwise
    """
    if "Q" in sentence or "q" in sentence:
        return True
    else:
        return False


def contains_x(sentence):
    """
    Least used alphabets in Dutch are Q and X
    :param sentence: Sentence to check if X is present
    :return: True if X is in sentence, false otherwise
    """
    if "X" in sentence or "x" in sentence:
        return True
    else:
        return False


def contains_most_common_english_words(sentence):
    """
    Checks if sentence contains some of the most common English words
    Source: https://www.rypeapp.com/most-common-english-words/
    :param sentence: Sentence to check if "the" is present
    :return: True if present, false otherwise
    """
    common_words = ["the", "of", "and", "to", "I", "you", "that", "it", "he", "she",
                    "for", "are", "with", "his", "her", "they", "this", "have", "from", "had"]

    words_in_sentence = sentence.split()
    for word in words_in_sentence:
        if word.lower().strip(",") in common_words:
            return True
        else:
            return False


def contains_most_common_dutch_words(sentence):
    """
    Checks if sentence contains some of the most common Dutch words
    Source: https://www.101languages.net/dutch/most-common-dutch-words/
    :param sentence: Sentence to check if "the" is present
    :return: True if present, false otherwise
    """
    common_words = ["ik", "je", "het", "de", "dat", "een", "niet", "en", "wat", "ze", "op", "te",
                    "hij", "zijn", "maar", "heb", "voor", "als", "mijn", "u", "dit", "aan", "die"]

    words_in_sentence = sentence.split()
    for word in words_in_sentence:
        if word.lower().strip(",") in common_words:
            return False
        else:
            return True


def contains_double_vowels(sentence):
    if "aa" in sentence or "ee" in sentence or "Aa" in sentence or "Ee" in sentence or "uu" in sentence or "Uu" in sentence:
        return False
    else:
        return True


def contains_ij(sentence):
    if "ij" in sentence:
        return False
    else:
        return True


def contains_oe(sentence):
    if "oe" in sentence:
        return False
    else:
        return True


def contains_z(sentence):
    if "z" in sentence or "Z" in sentence:
        return False
    else:
        return True


def contains_kk(sentence):
    if "kk" in sentence:
        return False
    else:
        return True


def contains_jn(sentence):
    if "jn" in sentence:
        return False
    else:
        return True


def contains_ch(sentence):
    if "ch" in sentence:
        return False
    else:
        return True


def word_ends_with_en(sentence):
    words_in_sentence = sentence.split()
    for word in words_in_sentence:
        if word.endswith("en"):
            return False
        else:
            return True


def contains_kt(sentence):
    if "kt" in sentence:
        return False
    else:
        return True


def contains_dt(sentence):
    if "dt" in sentence:
        return False
    else:
        return True


def sentences_to_boolean_attributes(sentences):
    """
    Used to convert sentences to boolean attributes for training algorithm
    :param sentences: List of sentences
    :return:List of attributes
    """
    attributes = []

    for sentence in sentences:

        sentence = sentence.split("|")
        language = sentence[0]
        sentence = sentence[1]

        s = [average_word_length(sentence), contains_q(sentence), contains_x(sentence),
             contains_most_common_english_words(sentence), contains_most_common_dutch_words(sentence),
             contains_double_vowels(sentence), contains_ij(sentence), contains_oe(sentence), contains_z(sentence),
             contains_kk(sentence), language]

        attributes.append(s)

    return attributes

def sentences_to_boolean_attributes_predict(sentences):
    """
    Used to convert the sentences into boolean attributes for prediction
    :param sentences: List of sentences
    :return: List of attributes
    """
    attributes = []

    for sentence in sentences:
        s = [average_word_length(sentence), contains_q(sentence), contains_x(sentence),
             contains_most_common_english_words(sentence), contains_most_common_dutch_words(sentence),
             contains_double_vowels(sentence), contains_ij(sentence), contains_oe(sentence), contains_z(sentence),
             contains_kk(sentence)]

        attributes.append(s)

    return attributes