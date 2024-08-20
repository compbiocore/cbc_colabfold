#!/bin/bash

#SBATCH -t 12:00:00
#SBATCH -n 32
#SBATCH --mem=256g
#SBATCH -N 1
#SBATCH -J msa_generation
#SBATCH -o %x-%j.out
#SBATCH -e %x-%j.err

singularity exec -B /oscar/home/$USER,/oscar/scratch/$USER,/oscar/data cbc_colabfold_latest.sif colabfold_search "$1" "$2" msas

