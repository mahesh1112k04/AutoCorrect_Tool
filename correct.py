import textdistance

# Define a list of correct words
correct_words = ["apple", "banana", "cherry", "orange", "grape"]

# Function to correct misspelled words or suggest the nearest correct word
def correct_word(word):
    # Calculate the Levenshtein distance between the given word and all correct words
    distances = [(textdistance.levenshtein.normalized_distance(word, correct_word), correct_word) for correct_word in correct_words]
    
    # Sort the distances in ascending order
    sorted_distances = sorted(distances, key=lambda x: x[0])
    
    # Get the nearest correct word
    nearest_word = sorted_distances[0][1]
    
    return nearest_word

# Test the correction function
misspelled_word = "aple"
corrected_word = correct_word(misspelled_word)

print(f"Original word: {misspelled_word}")
print(f"Corrected word: {corrected_word}")
