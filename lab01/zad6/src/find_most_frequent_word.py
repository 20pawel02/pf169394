def find_most_frequent_word(text):
    if not text:
        return None

    words = text.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    most_frequent_word = max(frequency, key=frequency.get)
    return most_frequent_word
