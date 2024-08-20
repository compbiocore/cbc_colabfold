# Local MSA Generation

For larger-scale protein structure predictions, in order to avoid issues with rate limiting on the public MSA server, it is best to run the MSA predictions locally, then feed them to the ColabFold notebook for processing. The following steps will guide you through this process. Note that you will need your input protein sequence as a ```.fasta``` file.

**Note: This feature is a work-in-progress until the ColabFold databases are uploaded to OSCAR (upon which this note will be removed).**

## Run MSA Generation Script

As MSA generation is CPU- and memory-intensive, the MSA generation script must be run separately first. This has been packaged as a batch script for easy use (it requests 256gb of memory and 32 cores for 12 hours).

The batch script ```generate_msas.sh``` is included in the repo. In that directory on OSCAR, run the following to have this run as a batch script. Replace ```/path/to/input_sequence.fasta``` with the path to your input .fasta file.

```bash
sbatch generate_msas.sh /path/to/input_sequence.fasta /path/to/databases msas
```

## Add MSA Filepath and Run Notebook

Open the ColabFold Jupyter notebook as normal (see [Quickstart](quickstart.md)), and run the first cell to display the widgets. Then, in the ```custom_msas``` field, insert the path to your MSAs (it will probably be something like ```msas/(NAME_OF_MSAS).a3m```. Finally, run all following cells as per normal.


