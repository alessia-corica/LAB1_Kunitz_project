# Building a Profile Hidden Markov Model for the Kunitz-type protease inhibitor domain

## Overview

This project aims to build a structure-informed profile Hidden Markov Model (HMM) able to identify Kunitz-tyoe protease inhibitor domains. The Kunitz domain is a highly conserved motif involved in the inhibition of serine proteases, found across diverse species and protein architectures.

By leveraging structural information from experimentally resolved proteins, the model is designed to capture key conserved features of this domain.

The pipeline includes:
- Selection and clustering of PDB structures annotated with PF00014
- Structural alignment using PDBeFold to generate a structure-based MSA
- HMM training using HMMER
- Evaluation on curated positive and negative UniProt/SwissProt datasets
- Performance metrics: MCC, accuracy, precision, recall, and ROC analysis
- Structural validation of misclassified sequences using ChimeraX and AlphaFold models

All scripts, data files, output tables, figures, and the final report are available in this repository.

> This work was developed as part of the Laboratory of Bioinformatics 1 course during the MSc in Bioinformatics at the University of Bologna.


## Required Tools & Packages

The pipeline was built using a combination of command-line tools and custom Python scripts:

### System tools
- **HMMER 3.3.2**: Used for building the HMM profile.
  - `hmmbuild`: to train the HMM from a multiple sequence alignment.
  - `hmmsearch`: to query protein sequences against the HMM.
  - `--max` and `-Z 1000`: options used to increase sensitivity and normalize scores.
- **PDBeFold**: Used to perform multiple structure alignment of PDB chains containing the Kunitz domain.

- **CD-HIT**: Used to cluster sequences at ≥90% identity and remove redundancy from the dataset.

- **BLAST**: Used to filter out sequences highly similar to the training set (`blastp`, `makeblastdb`).

- **WebLogo / Skylign**: Tools for generating sequence logos from the aligned sequences.

- **ChimeraX**: Used to visualize and structurally superimpose predicted false positives and false negatives againstj the BPTI reference structure (PDB ID: 3TGI).

### Python dependencies
- `pandas`, `numpy`: For handling tabular data and numerical computations.
- `matplotlib`, `seaborn`: For plotting results and visualizations.
- `scikit-learn`: For computing classification performance metrics.

> Ensure all dependencies are installed before running the analysis.


## Repository Structure

### `final_report/` 
- PDF containing the final report

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

### `results/figures/logo/`
- `logo_alignment-png`, `sequence_logo.png`: Sequence logos showing residue conservation across the aligned Kunitz domains.

### `results/figures/`
- `ROC_curve.png`: Receiver Operating Characteristic (ROC) curve.
- `alignment_quality.png`: Quality plot of structural alignment (RMSD, residue coverage).
- `mcc_thresholds_.png`: Plot of MCC values across E-value thresholds.


### `scripts/`
- `script.ipynb`: Main notebook with the full workflow and explanation.
- `get_seq.py`: Extracts sequences from a FASTA based on a list of UniProt IDs.
- `performance.py`: Computes MCC, accuracy, precision, recall from `.class` files.
- `confusion_matrix.py`: Generates confusion matrix plots from classification files.
- `alignment_quality.py`: Evaluates structural alignment metrics.
- `ROC_curve.py`: Generates the ROC curve.
- `MCC_script.py`: Plots MCC across different thresholds.
