# LAB1_Kunitz_project
## Overview
This project aims to build and evaluate profile Hidden Markov Models (HMMs) to identify the Kunitz-type protease inhibitor domain in protein sequences (Pfam ID: PF00014). The Kunitz domain is a small, structurally conserved domain involved in protease inhibition and found in a wide range of proteins.\
The model is based on a structure-derived multiple alignment of representative domains from the Protein Data Bank (PDB), aligned using PDBeFold and trained with HMMER.\
Model performance was assessed through 5-fold cross-validation on curated positive and negative datasets, demonstrating excellent predictive accuracy.

The work was carried out as part of the Laboratory of Bioinformatics 1 course during the MSc in Bioinformatics at the University of Bologna.


## Methodology

### Data Collection

- A total of 21 Kunitz domain-containing protein structures were retrieved from the **Protein Data Bank (PDB)** using the Pfam ID `PF00014`, with filters applied for resolution (≤3Å), sequence length (50–80 residues), and absence of mutations.
- Metadata and sequences were exported into a CSV file available at [`rcsb_pdb_custom_report_2025...csv`](raw_data/rcsb_pdb_custom_report_2025...csv).
- In parallel, a comprehensive set of 395 **reviewed UniProt entries** annotated with `PF00014` was downloaded and saved in [`kunitz_sequences.fasta`](raw_data/kunitz_sequences.fasta).

### Data Processing

- The UniProt-derived positive set was split into:
  - Human sequences: [`human_kunitz_sequences.fasta`](raw_data/human_kunitz_sequences.fasta)
  - Non-human sequences: [`nothuman_kunitz_sequences.fasta`](raw_data/nothuman_kunitz_sequences.fasta)
- Redundancy among the PDB sequences was removed using `cd-hit` at 90% identity, and the representative set was saved in [`pdb_kunitz_rp.fasta`](hmm_model/pdb_kunitz_rp.fasta).
- A **BLAST search** was performed to identify overlaps between the UniProt dataset and the PDB model set. The output is available at [`pdb_kunitz_nr_23.blast`](blast_results/pdb_kunitz_nr_23.blast).

### Structural Alignment

- Representative sequences were aligned structurally using **PDBeFold**.
- The multiple alignment was cleaned and saved in Stockholm format as [`pdb_kunitz_rp.ali`](hmm_model/pdb_kunitz_rp.ali) and a formatted version is available at [`pdb_kunitz_rp_formatted.ali`](hmm_model/pdb_kunitz_rp_formatted.ali).

### HMM Construction

- A profile HMM was built using **HMMER v3.4** with the following command:\
``` hmmbuild structural_model.hmm pdb_kunitz_rp.ali ```
- The final model is available at [`structural_model.hmm`](hmm_model/structural_model.hmm).

### Evaluation

- Model performance was assessed using **5-fold cross-validation**, implemented in the Jupyter notebook [`script.ipynb`](script.ipynb).
- Predictions were made with `hmmsearch`, and results were evaluated using:
  - **Accuracy**
  - **Matthews Correlation Coefficient (MCC)**
  - **F1-score**

The structural HMM model achieved a mean MCC of **0.995776**, indicating high robustness and generalization capacity.
