import matplotlib.pyplot as plt

def read_fasta(file_path):
    """Read a FASTA file and return a dictionary of sequence lengths."""
    sequences = {}
    with open(file_path, 'r') as f:
        current_header = None
        current_sequence = []
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if current_header:
                    sequences[current_header] = len(''.join(current_sequence))
                current_header = line[1:]  # Remove '>'
                current_sequence = []
            else:
                current_sequence.append(line)
        if current_header:  # Add the last sequence
            sequences[current_header] = len(''.join(current_sequence))
    return sequences

def plot_sequence_lengths(lengths, output_file):
    """Plot a histogram of sequence lengths."""
    plt.figure(figsize=(10, 6))
    plt.hist(lengths, bins=20, color='blue', edgecolor='black')
    plt.title("Sequence Length Distribution")
    plt.xlabel("Sequence Length (bp)")
    plt.ylabel("Frequency")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig(output_file)
    plt.show()

# Input and output files
fasta_file = "genbank_sequences.fasta"
output_image = "sequence_length_histogram.png"

# Read the FASTA file and get sequence lengths
sequence_lengths = read_fasta(fasta_file).values()

# Plot the histogram
plot_sequence_lengths(sequence_lengths, output_image)
print(f"Histogram saved as {output_image}")
