# LAB1_Kunitz_project
## Overview
This project aims to identify Kunitz-type protease inhibitor domains by building a structure-informed profile Hidden Markov Model (HMM). The Kunitz domain is a highly conserved structural motif involved in the inhibition of serine proteases, and it appears across diverse species and protein architectures. By leveraging structural information from experimentally resolved proteins, the model is designed to capture key functional and conserved features of this domain.\
The objective of this study was to build a profile HMM trained on experimentally resolved structures of proteins annotated with the PF00014 domain. The alignment was derived from multiple structure superposition, aiming to preserve key functional and structural features (e.g., disulfide bridges). After training the model with HMMER, we tested it against curated positive and negative sets from UniProt/SwissProt. Final evaluation was performed using Matthews Correlation Coefficient (MCC), accuracy, precision, recall, and ROC analysis.\
Misclassifications were further investigated through structural alignment using ChimeraX.

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

### `hmm_model/` – Files used for building and storing the HMM profile
- `pdb_kunitz_rp.ali`: Structural alignment of Kunitz domains obtained with PDBeFold.
- `pdb_kunitz_rp_formatted.ali`: Alignment file reformatted for compatibility with HMMER's `hmmbuild`.
- `structural_model.hmm`: Final profile HMM built from the formatted alignment.


### `processed_data/` – Intermediate processed files prepared for alignment and model building
- `pdb_kunitz_customreported.fasta`: Complete set of Kunitz domain sequences extracted from PDB entries.
- `pdb_kunitz_rp.fasta`: Non-redundant representative sequences selected for structural alignment.
- `tmp_pdb_efold_ids.txt`: List of PDB codes and chain IDs uploaded to PDBeFold for structural alignment.


### `raw_data/` – Original input datasets retrieved from external databases
- `human_kunitz_sequences.fasta`: Reviewed human protein sequences annotated with the Kunitz domain (PF00014).
- `kunitz_sequences.fasta`: Full set of reviewed SwissProt protein sequences containing the Kunitz domain.
- `nothuman_kunitz_sequences.fasta`: Reviewed non-human protein sequences with Kunitz domain.
- `rcsb_pdb_custom_report_*.csv`: CSV report from RCSB PDB with metadata of Kunitz domain structures with filtered characteristics.


### `results/blast/` – Files from BLAST filtering
- `pdb_kunitz_nr_23.blast`: BLAST output comparing non-redundant PDB-derived sequences against the full set of Kunitz sequences from SwissProt.
- `to_keep.ids`: IDs of non-redundant Kunitz sequences selected from BLAST output.
- `ok_kunitz.fasta`: Final positive used for HMM evaluation.


### `results/classifications/` – Results of HMM searches and data prepared for evaluation
- `pos_1.class`, `pos_2.class`: Results of HMM search on positive sets (fold 1 and 2).
- `neg_1.class`, `neg_2.class`: Results of HMM search on negative sets (fold 1 and 2).
- `set_1.class`, `set_2.class`: Combined classification sets for performance evaluation.


### `results/errors/` – Misclassified sequences
- `fn_pos1.txt`, `fn_pos2.txt`: False negatives at 1e-5 threshold from fold 1 and 2.
- `fp_neg2.txt`: False positives from negative set 2 (set 1 produced no false positives).


### `results/figures/confusion_matrices/`
- `confusion_matrix_fold1.png`, `confusion_matrix_fold2.png`: Confusion matrices for each fold.

### `results/figures/superimpositions/`
- `Superimposition_fn.png`, `Superimposition_fp.png`: Structural alignment of selected false negatives and false positives against the reference BPTI domain, used to visually assess similarity despite classification errors.

### `results/figures/`
- `ROC_curve.png`: Receiver Operating Characteristic (ROC) curve.
- `alignment_quality.png`: Quality plot of structural alignment (RMSD, residue coverage).
- `mcc_thresholds_.png`: Plot of MCC values across E-value thresholds.


### `scripts/` – All scripts used in the pipeline
- `script.ipynb`: Main notebook with the full workflow and explanation.
- `get_seq.py`: Extracts sequences from a FASTA based on a list of UniProt IDs.
- `performance.py`: Computes MCC, accuracy, precision, recall from `.class` files.
- `confusion_matrix.py`: Generates confusion matrix plots from classification files.
- `alignment_quality.py`: Evaluates structural alignment metrics.
- `ROC_curve.py`: Generates the ROC curve.
- `MCC_script.py`: Plots MCC across different thresholds.
