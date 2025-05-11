#!/usr/bin/env python3

import sys
from Bio import SeqIO

def get_ids(id_file):
    """
    Read the list of UniProt accession IDs from a text file.
    Returns a set of accession strings.
    """
    with open(id_file, 'r') as f:
        return {line.strip() for line in f if line.strip()}  # Read non-empty lines into a set

def get_seq(id_set, fasta_file, output_file):
    """
    Extract sequences whose accession is in id_set and write them to output_file in FASTA format.
    Assumes UniProt headers: >sp|ACCESSION|ENTRY_NAME ...
    """
    with open(fasta_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for record in SeqIO.parse(f_in, 'fasta'):  # Parse each record using Biopython
            try:
                accession = record.id.split('|')[1] if '|' in record.id else record.id  # Get the ACCESSION field
            except IndexError:
                continue  # Skip any malformed headers

            if accession in id_set:
                SeqIO.write(record, f_out, 'fasta')  # Write matching records to output file

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 get_seq.py id_list.txt input.fasta output.fasta")
        sys.exit(1)  # Exit if incorrect number of arguments

    id_list = sys.argv[1]       # First argument: file with list of UniProt IDs
    input_fasta = sys.argv[2]   # Second argument: input FASTA file
    output_fasta = sys.argv[3]  # Third argument: output FASTA file to write results

    ids_to_extract = get_ids(id_list)  # Load IDs into a set
    get_seq(ids_to_extract, input_fasta, output_fasta)  # Extract and write sequences
