# ColabFold on OSCAR

ColabFold is a fast, powerful algorithm based on Google's AlphaFold2 designed to predict a protein's 3D structure from its protein sequence. Using slightly different methods in MSA (multiple-sequence alignment), ColabFold runs up to 3-5x faster than the original AlphaFold with comparable results.

Both ColabFold and AlphaFold work by querying large databases of existing protein sequences to find those most similar to the input amino acid sequence; this process is known as a multiple-sequence alignment (MSA). ColabFold further uses the software suite MMseqs2 to speed up this MSA creation. Following this, both use a deep-learning "Evoformer" to turn this MSA into a feasible 3D structure for our input sequence. This algorithm, like many other deep-learning algorithms, is greatly sped up by GPU use.

While the original ColabFold is located on a Google Colab notebook and uses databases and GPUs directly from Google Cloud, this implementation runs the entire processing pipeline locally on OSCAR, from MSA generation to structure building. Furthermore, through having the script on a Jupyter notebook, the input parameters are easily customizable for a wide variety of uses.

## Quickstart

Note that this requires a session with at least 128gb RAM.

* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files

## References

[GitHub](https://github.com/compbiocore/cbc_colabfold)
