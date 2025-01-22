import matplotlib.pyplot as plt

def read_fasta(file_path):
    """Read a FASTA file and return all sequences as a single string."""
    sequences = []
    with open(file_path, 'r') as f:
        for line in f:
            if not line.startswith('>'):  # Skip headers
                sequences.append(line.strip())
    return ''.join(sequences)

def calculate_frequencies(sequence):
    """Calculate the frequency of each nucleotide in the sequence."""
    nucleotides = ['A', 'T', 'G', 'C']
    total_length = len(sequence)
    frequencies = {nt: sequence.count(nt) / total_length * 100 for nt in nucleotides}
    return frequencies

def plot_frequencies(frequencies, output_file):
    """Plot a bar chart of nucleotide frequencies."""
    plt.figure(figsize=(8, 6))
    plt.bar(frequencies.keys(), frequencies.values(), color=['blue', 'orange', 'green', 'red'])
    plt.title('Nucleotide Frequencies')
    plt.xlabel('Nucleotide')
    plt.ylabel('Frequency (%)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig(output_file)
    plt.show()

# Input and output files
fasta_file = "genbank_sequences.fasta"
output_image = "nucleotide_frequencies.png"

# Read the FASTA file and calculate nucleotide frequencies
sequence = read_fasta(fasta_file)
frequencies = calculate_frequencies(sequence)

# Plot the frequencies
plot_frequencies(frequencies, output_image)
print(f"Nucleotide frequency bar chart saved as {output_image}")
