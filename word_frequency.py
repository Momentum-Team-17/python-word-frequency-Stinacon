# use a dictionary for my word: count
import string


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

# def remove_punctuation(s):
#     for punc in PUNCTUATION:
#         s = s.replace(punc, "")
#     return s


def remove_punctuation(words):
    stripped_file = words.translate(str.maketrans('', '', string.punctuation))
    return stripped_file


def remove_stop_words(word_list):
    cleaned_list = []
    for word in word_list:
        if word not in STOP_WORDS:
            cleaned_list.append(word)
    return cleaned_list


def open_file(file):
    '''Uses 'open' to read a text file'''
    with open(file) as opened_file:
        # file remains open for the indentedxd lines under here
        read_file = opened_file.read()
    stripped_file = remove_punctuation(read_file).lower()
    # remove punctuation when it is still a string

    word_list = stripped_file.split()
    # use .split to return a list separated at the spaces
    cleaned_list = remove_stop_words(word_list)
    # print(cleaned_list)
    return cleaned_list

# count the frequency of each word in the file

    # word: words_to_count.count(word)


def sort_dictionary(dictionary):
    sorted_word_count_by_frequency = sorted(
        dictionary.items(), key=lambda x: x[1], reverse=True)
    # print(sorted_word_count_by_frequency)
    return sorted_word_count_by_frequency


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # calling the "open" function
    words_to_count = open_file(file)
    word_count = {}
    for word in words_to_count:
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1
    sorted_word_count = sort_dictionary(word_count)
    print(sorted_word_count)
    return sorted_word_count
# we have to iterate through our list of tuples and printed out a string
# first see if I can add the correct number of asterisks
# remember that tuples can be unpacked

# display a count in the console of words in descending frequency
#      we | 7 *******
#    each | 5 *****
#      or | 5 *****
#    need | 5 *****
#    love | 5 *****
#   about | 4 ****
#  praise | 4 ****
#    song | 4 ****
#     day | 3 ***
#     our | 3 ***
# Longest word + 1 dictates space from left. Spaces are
# characters.


# i removed the word "pass" - it is a placeholder to make an empty
# function not break.
# so i remove pass then put my code inside the above function!
# the existing code will call the function in later lines


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
