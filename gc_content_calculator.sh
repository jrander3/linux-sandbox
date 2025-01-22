#!/bin/bash

# Check if the input file is provided
if [[ $# -eq 0 ]]; then
    echo "Usage: ./gc_content_calculator.sh <fasta_file>"
    exit 1
fi

fasta_file=$1
output_file="gc_content_results.txt"

# Initialize variables
sequence_name=""
sequence_content=""

# Clear the output file if it exists
> "$output_file"

# Process each line in the FASTA file
while read -r line; do
    case "$line" in
        '>'*)
            # If a sequence is already being processed, calculate its GC content
            if [[ -n $sequence_content ]]; then
                gc_count=$(echo "$sequence_content" | grep -o '[GC]' | wc -l)
                total_count=$(echo "$sequence_content" | tr -d '\n' | wc -c)
                gc_content=$(echo "scale=2; ($gc_count/$total_count)*100" | bc)
                echo "$sequence_name: $gc_content%" >> "$output_file"
            fi
            # Start processing a new sequence
            sequence_name=$line
            sequence_content=""
            ;;
        *)
            # Append the current line to the sequence content
            sequence_content+=$line
            ;;
    esac
done < "$fasta_file"

# Process the last sequence in the file
if [[ -n $sequence_content ]]; then
    gc_count=$(echo "$sequence_content" | grep -o '[GC]' | wc -l)
    total_count=$(echo "$sequence_content" | tr -d '\n' | wc -c)
    gc_content=$(echo "scale=2; ($gc_count/$total_count)*100" | bc)
    echo "$sequence_name: $gc_content%" >> "$output_file"
fi

echo "GC content for each sequence saved to $output_file."



