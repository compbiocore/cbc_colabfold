## List of AlphaFold Databases

### 1. UniRef90

**Status**: AlphaFold2 and AlphaFold3 currently shares the same database. 

**Description**: The UniProt Reference Clusters (UniRef) provide clustered sets of sequences from the UniProt Knowledgebase (including isoforms) and selected UniParc records in order to obtain complete coverage of the sequence space at several resolutions while hiding redundant sequences from view.

UniRef90 is built by clustering UniRef100 sequences such that each cluster is composed of sequences that have at least 90% sequence identity to, and 80% overlap with, the longest sequence in the cluster (the seed sequence).

**Website**: https://www.uniprot.org/help/downloads

**URL**: `https://ftp.uniprot.org/pub/databases/uniprot/uniref/uniref90/uniref90.fasta.gz`

**Path**: `/gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_data/alphafold3_databases/uniref90_2022_05.fa`

### 2. Mgnify

**Status**: AlphaFold2 and AlphaFold3 currently shares the same database. 

**Description**: The MGnify protein database comprises non-redundant sequences predicted from assemblies generated from publicly available metagenomic datasets. It is a good place to search for putative proteins from uncultured unknown organisms, mostly bacteria and archaea. The current version is 2023_02, containing nearly 3 billion sequences and over 700 million clusters.

**Website**: http://ftp.ebi.ac.uk/pub/databases/metagenomics/peptide_database/

**URL**: `http://ftp.ebi.ac.uk/pub/databases/metagenomics/peptide_database/2023_02/mgy_clusters.fa.gz`

**Path**: `/gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_data/alphafold3_databases/mgy_clusters_2022_05.fa`

### 3. PDB MMCIF

**Status**: AlphaFold2 and AlphaFold3 currently shares the same database. 

**Description**: mmCIF (Macromolecular Crystallographic Information File) is a more comprehensive format for representing protein structures. It includes all the information in the PDB format plus additional data, such as experimental details, data block definitions, and more. AlphaFold uses mmCIF to store the predicted structure along with pLDDT scores. 

**Website**: `https://pdb101.rcsb.org/learn/guide-to-understanding-pdb-data/beginner%E2%80%99s-guide-to-pdbx-mmcif`

**URL**: `https://storage.googleapis.com/alphafold-databases/v3.0/pdb_2022_09_28_mmcif_files.tar.zst`, `https://files.wwpdb.org/pub/pdb/data/assemblies/mmCIF/all/`

**Path**: `/gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_data/alphafold3_databases/mmcif_files `


### 4. Obsolete MMCIF

**Status**: AlphaFold2 only use this list.

**Description**: List of obsolete MMCIF files. 

**Path**: `/gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_data/pdb_mmcif/obsolete.dat`


### 5. BFD Database

**Status**: AlphaFold2 and AlphaFold3 currently **do not** shares the same database because the formats are different. 

**Description**: BFD was created by clustering 2.5 billion protein sequences from Uniprot/TrEMBL+Swissprot, Metaclust and Soil Reference Catalog Marine Eukaryotic Reference Catalog assembled by Plass.

**Website**: https://bfd.mmseqs.com/

**URL**: `https://storage.googleapis.com/alphafold-databases/v3.0/bfd-first_non_consensus_sequences.fasta`, `https://bfd.mmseqs.com/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt.tar.gz`

**Path**:
- AF2: `/gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_data/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt*`
- AF3: `/gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_data/alphafold3_databases/bfd-first_non_consensus_sequences.fasta`

### 6. uniclust30

**Status**: AlphaFold2 and AlphaFold3 currently **do not** shares the same database. This is currently exclusively an AlphaFold2 database.

**Description**: The Uniclust90, Uniclust50, Uniclust30 databases cluster UniProtKB sequences at the level of 90%, 50% and 30% pairwise sequence identity. The clusterings show a high consistency of functional annotation owing to an optimised clustering pipeline that runs with our MMseqs2 software for fast and sensitive protein sequence searching and clustering.

**Website**: https://uniclust.mmseqs.com/

**URL**: `https://wwwuser.gwdguser.de/~compbiol/uniclust/2023_02/`

**Path**:
-AF2: `/gpfs/data/shared/databases/refchef_refs/alphafold_data/primary/alphafold_data/uniclust30/uniclust30_2018_08/uniclust30_2018_08*`


