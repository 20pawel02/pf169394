import re
from collections import Counter


def find_most_frequent_word(text):
    # Use regex to find words and convert them to lowercase
    words = re.findall(r'\w+', text.lower())
    if not words:
        return None
    # Count the frequency of each word
    word_counts = Counter(words)
    # Find the word with the highest frequency
    most_frequent_word = word_counts.most_common(1)[0][0]
    return most_frequent_word 