import random

def generate_true_palindromic_dna(length=11):
    bases = ["A", "T", "C", "G"]
    half_length = (length + 1) // 2  # Get half (including center for odd lengths)
    first_half = [random.choice(bases) for _ in range(half_length)]
    
    # Mirror the first half to create a true palindrome
    second_half = list(reversed(first_half[:length // 2]))
    
    return "".join(first_half + second_half)

# Generate 10 true palindromic sequences
palindromic_sequences = [generate_true_palindromic_dna(11) for _ in range(10)]

# Print the sequences
for seq in palindromic_sequences:
    print(seq)
