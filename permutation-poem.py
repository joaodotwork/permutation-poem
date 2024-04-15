import json

def generate_permutations(words, index, permute):
    if index == len(words):
        permute.append(words.copy())
    else:
        for i in range(index, len(words)):
            words[i], words[index] = words[index], words[i]
            generate_permutations(words, index + 1, permute)
            words[i], words[index] = words[index], words[i]

# Prompt the user to enter the sentence
sentence = input("Enter the sentence: ")

def generate_permutations(words, index, permute):
    if index == len(words):
        permute.append(words.copy())
    else:
        for i in range(index, len(words)):
            words[i], words[index] = words[index], words[i]
            generate_permutations(words, index + 1, permute)
            words[i], words[index] = words[index], words[i]

# Split the sentence into words
words = sentence.split()
# Create an empty list to store all permutations
permutations = []
# Generate all permutations using the recursive function
generate_permutations(words, 0, permutations)

# Create a dictionary to store the results
result = {
    "title": sentence,
    "permutations": permutations
}

# Save the results in a tokenized .ndjson file
with open("output.ndjson", "w") as file:
    file.write(json.dumps(result) + "\n")

# Print all permutations
for permutation in permutations:
    print(" ".join(permutation))

# Split the sentence into words
words = sentence.split()

# Create an empty list to store all permutations
permutations = []

# Generate all permutations using the recursive function
generate_permutations(words, 0, permutations)

# Print all permutations
for permutation in permutations:
    print(" ".join(permutation))
