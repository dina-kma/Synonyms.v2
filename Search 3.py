# Input word from the user
input_word = input("Enter a word to search for: ")

# File path to your tab-delimited .txt file
file_path = "word_synonyms.txt"  # Replace with the path to your file

# Initialize synonyms variable
synonyms = None

# Open the file for reading
with open(file_path, 'r') as file:
    for line in file:
        word, synonym_str = line.strip().split('\t', 1)
        synonyms_list = synonym_str.split(', ')

        # Check if the input word matches the word in the file (case-insensitive)
        if word.strip().lower() == input_word.strip().lower():
            synonyms = synonyms_list
            break

# Check if synonyms were found
if synonyms is not None:
    print(f"Synonyms for '{input_word}': {', '.join(synonyms)}")
else:
    print(f"'{input_word}' not found")
