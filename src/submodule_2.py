from collections import Counter

def calculate_normalized_frequencies(words, top_n=200):
    """
    Calculates the normalized frequencies of words in the text.
    Returns the top N frequent words and their normalized counts.
    """
    total_words = len(words)
    word_counts = Counter(words)
    normalized_counts = {word: count / total_words for word, count in word_counts.items()}
    return dict(Counter(normalized_counts).most_common(top_n))