def generate_random_sequences(num_sequences=10, length=5):
    sequences = [''.join(random.choices("ACGT", k=length)) for _ in range(num_sequences)]
    return sequences

random_sequences = generate_random_sequences(10, 5)
for seq in random_sequences:
    print(seq)
