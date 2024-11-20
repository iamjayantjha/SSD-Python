import os
from submodule_1 import read_and_process_file
from submodule_2 import calculate_normalized_frequencies
from submodule_3 import calculate_similarity

def main(directory, n):
    # Gather file paths from the provided directory
    file_paths = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.txt')]

    # Read and preprocess files
    file_data = {}
    for file_path in file_paths:
        words = read_and_process_file(file_path)
        file_data[file_path] = calculate_normalized_frequencies(words)

    # Compute similarities
    similarities = []
    for i, file1 in enumerate(file_paths):
        for j, file2 in enumerate(file_paths):
            if i < j:
                similarity = calculate_similarity(file_data[file1], file_data[file2])
                similarities.append((file1, file2, similarity))

    # Sort and output top N similar pairs
    top_n_similar = sorted(similarities, key=lambda x: x[2], reverse=True)[:n]
    output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "text_files", "text_file.txt")
    for pair in top_n_similar:
        print(f"{pair[0]} and {pair[1]}: Similarity Index = {pair[2]:.4f}")
        with open(output_path, "w") as f:
            for pair1 in top_n_similar:
                #f.write(f"{pair1[0]} and {pair1[1]}: Similarity Index = {pair1[2]:.4f}\n")
                f.write(f"Similarity Index = {pair1[2]:.4f}\n")

if __name__ == "__main__":
    # Define the relative path to the 'data' directory
    directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    n = int(input("Enter the number of most similar pairs to report: "))
    main(directory, n)