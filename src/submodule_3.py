def calculate_similarity(file1_words, file2_words):
    """
    Calculates the similarity index between two files based on their common words.
    Returns the similarity score.
    """
    common_words = set(file1_words.keys()).intersection(file2_words.keys())
    similarity = sum(file1_words[word] + file2_words[word] for word in common_words)
    return similarity