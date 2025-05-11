# LAB1_Kunitz_project
## Overview
This project aims to build and evaluate profile Hidden Markov Models (HMMs) to identify the Kunitz-type protease inhibitor domain in protein sequences (Pfam ID: PF00014). The Kunitz domain is a small, structurally conserved domain involved in protease inhibition and found in a wide range of proteins.\
The model is based on a structure-derived multiple alignment of representative domains from the Protein Data Bank (PDB), aligned using PDBeFold and trained with HMMER.\
Model performance was assessed through 5-fold cross-validation on curated positive and negative datasets, demonstrating excellent predictive accuracy.

The work was carried out as part of the Laboratory of Bioinformatics 1 course during the MSc in Bioinformatics at the University of Bologna.

## Required Tools & Packages

To reproduce this project, the following software and dependencies are required.

### System tools

The following command-line tools are required to run the pipeline:

- `cd-hit`: for clustering redundant sequences
- `BLAST+`: for sequence similarity searches (`makeblastdb`, `blastp`)
- `HMMER`: for HMM construction and scanning (`hmmbuild`, `hmmsearch`)

### Python 3 packages

Python was used for sequence filtering, dataset generation, and performance analysis.

Required Python packages:
- `pandas`: for parsing `.class` files
- `matplotlib`: for plotting performance metrics
- `argparse`: used in `performance.py` scripts

## Repository Structure

The repository is organized into the following directories:

- `raw_data/`: input sequences and metadata downloaded from UniProt and PDB (FASTA and CSV files).
- `hmm_model/`: files used for and generated during the construction of the HMM (e.g., alignments, profile).
- `blast_results/`: output from BLAST used to filter sequences based on similarity to training data.
- `results/`: performance evaluation files, plots (e.g., MCC vs threshold), and structural analysis images.
- `scripts/`: Python scripts used for sequence filtering (`get_seq.py`), metric computation (`performance.py`), and the notebook with the full pipeline (`script.ipynb`).


## Methodology

### Data Collection

- A total of 21 Kunitz domain-containing protein structures were retrieved from the **Protein Data Bank (PDB)** using the Pfam ID `PF00014`, with filters applied for resolution (≤3Å) and sequence length (50–80 residues).
- Metadata and sequences were exported into a CSV file available at [`rcsb_pdb_custom_report_2025...csv`](raw_data/rcsb_pdb_custom_report_2025...csv).
- In parallel, a comprehensive set of 395 **reviewed UniProt entries** annotated with `PF00014` was downloaded and saved in [`kunitz_sequences.fasta`](raw_data/kunitz_sequences.fasta).

### Data Processing

- The UniProt-derived positive set was split into:
  - Human sequences: [`human_kunitz_sequences.fasta`](raw_data/human_kunitz_sequences.fasta)
  - Non-human sequences: [`nothuman_kunitz_sequences.fasta`](raw_data/nothuman_kunitz_sequences.fasta)
- Redundancy among the PDB sequences was removed using `cd-hit` at 90% identity, and the representative set was saved in [`pdb_kunitz_rp.fasta`](hmm_model/pdb_kunitz_rp.fasta).
- A **BLAST search** was performed to compare the PDB sequences used for HMM construction against all UniProt Kunitz entries. The goal was to identify and exclude highly similar sequences (≥95% identity, ≥50% coverage) from the test set. The full alignment output is available at [`pdb_kunitz_nr_23.blast`](blast_results/pdb_kunitz_nr_23.blast).

### Structural Alignment

- A curated set of non-redundant PDB structures containing the Kunitz domain were aligned structurally using **PDBeFold** (SE PUOI inserisci tmp_pdb...ids.txt).
- The multiple alignment was cleaned and saved as a formatted version available at [`pdb_kunitz_rp_formatted.ali`](hmm_model/pdb_kunitz_rp_formatted.ali).

### HMM Construction

- A profile HMM was built using **HMMER**.
- The final model is available at [`structural_model.hmm`](hmm_model/structural_model.hmm).

### Evaluation

- Model performance was assessed using **5-fold cross-validation** (SICURA??)
- Predictions were made with `hmmsearch`, and results were evaluated using:
  - **Accuracy**
  - **Matthews Correlation Coefficient (MCC)**
  - **F1-score**

## Results

The structural profile HMM was evaluated through a custom pipeline based on two balanced test sets, each composed of 183 positive and ~286,000 negative sequences. Performance was assessed using different E-value thresholds, and metrics such as **Accuracy**, **Recall**, **Precision**, and **Matthews Correlation Coefficient (MCC)** were computed using a dedicated Python script.

### Summary of Results (Set 1 and Set 2)

At the optimal threshold of **1e-05**, both sets showed high predictive power:

| Metric     | Set 1     | Set 2     |
|------------|-----------|-----------|
| Accuracy   | 0.99998   | 0.99998   |
| Recall     | 0.9836    | 0.9836    |
| Precision  | 1.0000    | 1.0000    |
| MCC        | 0.9918    | 0.9918    |
| FP         | 0         | 0         |
| FN         | 3         | 3         |

### Performance at Multiple Thresholds

The Matthews Correlation Coefficient (MCC) remained optimal (MCC = 1.0) for thresholds between **1e-10** and **1e-08**, and above 0.986 for all other tested values, confirming the robustness of the model even under relaxed cutoffs.

### Additional Files

All performance data are available in the [`results/`](results/) folder:

- [`performance_set1_thresholds.txt`](results/performance_set1_thresholds.txt)
- [`performance_set2_thresholds.txt`](results/performance_set2_thresholds.txt)
- [`MCC_vs_thresholds.py`](results/MCC_vs_thresholds.py): script to plot performance at multiple thresholds
- [`mcc_vs_thresholds.png`](results/mcc_vs_thresholds.png): plot that describes performance at multiple thresholds
- [`FP_superimposition.png`](results/FP_superimposition.png): Chimera-generated superimposition of the false positive structure.
