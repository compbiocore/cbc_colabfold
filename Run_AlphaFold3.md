# Running AlphaFold3 on OSCAR

## Overview

This document covers how to run AlphaFold3.

## Quick Start

```commandline
singularity exec \
--bind /gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_data/alphafold3_databases:/root/public_database \
--bind /gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_data/alphafold3_image/af_inputs:/root/af_inputs \
--bind /gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_data/alphafold3_image/af_outputs:/root/af_outputs \
--bind /gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_data/alphafold3_databases/models:/root/models \
--nv /gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_data/alphafold3_image/alphafold3.sif \
python /app/alphafold/run_alphafold.py \
--json_path=/root/af_inputs/fold_input.json \
--db_dir=/root/public_database \
--output_dir=/root/af_outputs \
--model_dir=/root/models \ 
--flash_attention_implementation = xla
```

## Orientation

### I. Databases
All of the databases are located here: `/gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_data/alphafold3_databases`:
Downloaded from the database script here: https://github.com/google-deepmind/alphafold3/blob/main/fetch_databases.sh
```commandline
bfd-first_non_consensus_sequences.fasta
nt_rna_2023_02_23_clust_seq_id_90_cov_80_rep_seq.fasta
rfam_14_9_clust_seq_id_90_cov_80_rep_seq.fasta
uniprot_all_2021_04.fa
mgy_clusters_2022_05.fa
pdb_seqres_2022_09_28.fasta
rnacentral_active_seq_id_90_cov_80_linclust.fasta
uniref90_2022_05.fa
models/ #pdb_2022_09_28_mmcif_files.tar
```

### II. Model
The AlphaFold3 weights are located here: `/gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_data/alphafold3_databases/model`.

You can request the weights here: https://docs.google.com/forms/d/e/1FAIpQLSfWZAgo1aYk0O4MuAXZj8xRQ8DafeFJnldNOnh_13qAx2ceZw/viewform


### III. Inputs

```commandline
{
  "name": "2PV7",
  "sequences": [
    {
      "protein": {
        "id": ["A", "B"],
        "sequence": "GMRESYANENQFGFKTINSDIHKIVIVGGYGKLGGLFARYLRASGYPISILDREDWAVAESILANADVVIVSVPINLTLETIERLKPYLTENMLLADLTSVKREPLAKMLEVHTGAVLGLHPMFGADIASMAKQVVVRCDGRFPERYEWLLEQIQIWGAKIYQTNATEHDHNMTYIQALRHFSTFANGLHLSKQPINLANLLALSSPIYRLELAMIGRLFAQDAELYADIIMDKSENLAVIETLKQTYDEALTFFENNDRQGFIDAFHKVRDWFGDYSEQFLKESRQLLQQANDLKQG"
      }
    }
  ],
  "modelSeeds": [1],
  "dialect": "alphafold3",
  "version": 1
}
```

### IV. Running the Program

The only input you need to specify is the `$INPUT` json file as specified in the above section. 

```commandline
singularity exec \
--bind /gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_data/alphafold3_databases:/root/public_database \
--bind /gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_data/alphafold3_image/af_inputs:/root/af_inputs \
--bind /gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_data/alphafold3_image/af_outputs:/root/af_outputs \
--bind /gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_data/alphafold3_databases/models:/root/models \
--nv /gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_data/alphafold3_image/alphafold3.sif \
python /app/alphafold/run_alphafold.py \
--json_path=$INPUT \
--db_dir=/root/public_database \
--output_dir=/root/af_outputs \
--model_dir=/root/models \
--flash_attention_implementation = xla
```