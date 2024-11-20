
# **Text File Similarity Finder**

## **Project Overview**
This project calculates the similarity between a collection of text files based on the normalized frequencies of the top 200 most frequent words (excluding stopwords). It identifies and reports the top `N` most similar pairs of text files based on a custom similarity measure.

---

## **Project Structure**

```
rollno_a3/
├── data/                        # Directory containing input text files
│   ├── file_1.txt
│   ├── file_2.txt
│   ├── file_N.txt
├── README.md                    # Project documentation
├── src/                         # Source code directory
│   ├── main.py                  # Main driver script
│   ├── submodule_1.py           # Module for reading and preprocessing text files
│   ├── submodule_2.py           # Module for calculating frequencies and normalization
│   ├── submodule_3.py           # Module for similarity calculation
├── text_file/                   # Directory to store output results
│   ├── text_file.txt            # Output file containing similarity results
```

---

## **Installation and Setup**

1. **Install Dependencies**:
    - Ensure you have Python 3.6+ installed.
    - Install required Python libraries:
      ```bash
      pip install nltk
      ```

2. **Prepare Input Files**:
    - Place your text files (`.txt`) in the `data/` directory. These files will be used to calculate similarities.

3. **Download NLTK Stopwords**:
    - Run the following in your Python environment to download stopwords:
      ```python
      import nltk
      nltk.download('stopwords')
      ```

---

## **How to Run**

1. Navigate to the `src/` directory:
   ```bash
   cd src
   ```

2. Run the program:
   ```bash
   python main.py
   ```

3. Enter the number of most similar pairs (`N`) when prompted.

4. **Output**:
    - Results will be saved in the `text_file/` directory as `text_file.txt`.

---

## **Modules Description**

### **1. `main.py`**
- **Purpose**: The main driver script that orchestrates the program execution.
- **Key Functions**:
    - Reads input text files from the `data/` directory.
    - Calls functions from the submodules to preprocess text, calculate word frequencies, and compute similarities.
    - Saves results in `text_file.txt`.

---

### **2. `submodule_1.py`**: File Reading and Preprocessing
- **Purpose**: Handles reading text files, converting text to uppercase, tokenizing words, and removing stopwords.
- **Key Function**:
    - `read_and_process_file(file_path)`: Reads a file and returns a list of preprocessed words.

---

### **3. `submodule_2.py`**: Frequency and Normalization
- **Purpose**: Calculates word frequencies and normalizes them.
- **Key Function**:
    - `calculate_normalized_frequencies(words, top_n=200)`: Returns the top 200 most frequent words and their normalized counts.

---

### **4. `submodule_3.py`**: Similarity Calculation
- **Purpose**: Computes the similarity index between two files based on common word frequencies.
- **Key Function**:
    - `calculate_similarity(file1_words, file2_words)`: Returns the similarity score for two dictionaries of normalized word frequencies.

---

## **Input and Output**

### **Input**
- Text files placed in the `data/` directory.
- Format: `.txt` files containing textual data.

### **Output**
- Results are saved in the `text_file/` directory as `text_file.txt`.
- Format:
  ```
  file_1.txt and file_2.txt: Similarity Index = 0.1234
  file_3.txt and file_4.txt: Similarity Index = 0.1122
  ```

---

## **How the Program Works**

1. **Input Text Preprocessing**:
    - Reads each file from the `data` folder.
    - Converts text to uppercase.
    - Tokenizes text and removes stopwords.

2. **Frequency and Normalization**:
    - Calculates word frequencies and normalizes them.
    - Keeps only the top 200 most frequent words for each file.

3. **Similarity Calculation**:
    - Computes the similarity index between each pair of files based on shared normalized word frequencies.
    - The similarity index is the sum of normalized values of common words.

4. **Output Results**:
    - Outputs the top `N` most similar pairs of files and their similarity indices in `text_file.txt`.

---



## **Error Handling**
- **File Encoding Errors**:
    - If a file cannot be decoded using UTF-8, the program falls back to `ISO-8859-1`.
- **Missing Directories**:
    - Automatically creates the `text_file/` directory if it does not exist.

---

## **Additional Notes**
- Ensure all text files are formatted correctly as `.txt`.
- Stopwords are language-specific. Modify the `stopwords` set in `submodule_1.py` if using non-English text.

---