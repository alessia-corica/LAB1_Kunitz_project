# LAB1_Kunitz_project
## Overview
This project aims to build and evaluate profile Hidden Markov Models (HMMs) to identify the Kunitz-type protease inhibitor domain in protein sequences (Pfam ID: PF00014). The Kunitz domain is a small, structurally conserved domain involved in protease inhibition and found in a wide range of proteins.\
The model is based on a structure-derived multiple alignment of representative domains from the Protein Data Bank (PDB), aligned using PDBeFold and trained with HMMER.\
Model performance was assessed through 5-fold cross-validation on curated positive and negative datasets, demonstrating excellent predictive accuracy.

The work was carried out as part of the Laboratory of Bioinformatics 1 course during the MSc in Bioinformatics at the University of Bologna.


## Methodology

### Data Preparation

- A set of 21 Kunitz domain-containing proteins was retrieved from the **Protein Data Bank (PDB)** using the Pfam ID `PF00014`, filtered by resolution (≤3Å), sequence length (50–80 aa), and absence of mutations. The metadata file is available at [`rcsb_pdb_custom_report_2025...csv`](raw_data/rcsb_pdb_custom_report_2025...csv).
- Protein sequences were extracted from the CSV using `awk`, converted to FASTA format, and filtered to remove redundancy with `cd-hit` at 90% identity.
- The resulting non-redundant dataset is saved in [`pdb_kunitz_rp.fasta`](hmm_model/pdb_kunitz_rp.fasta), containing representative sequences used for model building.

### Structural Alignment

- Representative sequences were aligned structurally using **PDBeFold**.
- The multiple alignment was cleaned and saved in Stockholm format as [`pdb_kunitz_rp.ali`](hmm_model/pdb_kunitz_rp.ali) and a formatted version is available at [`pdb_kunitz_rp_formatted.ali`](hmm_model/pdb_kunitz_rp_formatted.ali).

### HMM Construction

```bash
hmmbuild structural_model.hmm pdb_kunitz_rp.ali
