# use a dictionary for my word: count
import string


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def remove_punctuation(words):
    stripped_file = words.translate(str.maketrans('', '', string.punctuation))
    return stripped_file


def open_file(file):
    '''Uses 'open' to read a text file'''
    with open(file) as opened_file:
        # file remains open for the indentedxd lines under here
        read_file = opened_file.read()
    stripped_file = remove_punctuation(read_file).lower()
    # remove punctuation when it is still a string

    word_list = stripped_file.split()
    print(word_list)
    # use .split to return a list separrated at the spaces


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # calling the "open" function
    open_file(file)


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
