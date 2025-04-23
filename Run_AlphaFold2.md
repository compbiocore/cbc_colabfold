# Running AlphaFold2 on OSCAR

## Overview

This document covers how to run AlphaFold2.


## Quick Start

1. Make a simple outdir in your home directory: `$HOME\out_dir`

2. Make a simple fasta file at :`$HOME\out_dir\T1050.fasta`
```commandline
>2PV7
GMRESYANENQFGFKTINSDIHKIVIVGGYGKLGGLFARYLRASGYPISILDREDWAVAESILANADVVIVSVPINLTLETIERLKPYLTENMLLADLTSVKREPLAKMLEVHTGAVLGLHPMFGADIASMAKQVVVRCDGRFPERYEWLLEQIQIWGAKIYQTN
ATEHDHNMTYIQALRHFSTFANGLHLSKQPINLANLLALSSPIYRLELAMIGRLFAQDAELYADIIMDKSENLAVIETLKQTYDEALTFFENNDRQGFIDAFHKVRDWFGDYSEQFLKESRQLLQQANDLKQG
```

3. Run the AlphaFold2 command:

```commandline
singularity exec \
--bind /gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_data:/root/public_database \
--bind $HOME/out_dir:/root/out_dir \
--nv /gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_v2.2.2.simg \
python /app/alphafold/run_alphafold.py \
--data_dir=/root/public_database \
--fasta_paths=/root/out_dir/T1050.fasta \
--output_dir=/root/out_dir \
--max_template_date=2022-01-01 \
--uniref90_database_path=/root/public_database/uniref90/uniref90.fasta \
--mgnify_database_path=/root/public_database/mgnify \
--template_mmcif_dir=/root/public_database/pdb_mmcif/mmcif_files \
--obsolete_pdbs_path=/root/public_database/pdb_mmcif/obsolete.dat \
--bfd_database_path=/root/public_database/bfd/bfd \
--uniclust30_database_path=/root/public_database/uniclust30/uniclust30 \
--pdb70_database_path=/root/public_database/pdb70/pdb70 \
--use_gpu_relax=True
```