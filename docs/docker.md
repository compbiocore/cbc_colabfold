# Building Singularity Image from Docker

If you want to build the Singularity image yourself, a Dockerfile is included in the [Git repo](https://github.com/compbiocore/cbc_colabfold). Download this to your local machine instead of OSCAR. Also, make sure you have Docker up and running locally.

## Copy Jupyter Notebook

To get the ColabFold Jupyter notebook on OSCAR, you can either clone the repo directly on OSCAR, or you can take your local copy of the Jupyter notebook and copy it to OSCAR. Don't forget to replace ```(OSCAR_DIRECTORY)``` with the directory you want to save this to on OSCAR.

```bash
scp ColabFold.ipynb (USERNAME)@ssh.ccv.brown.edu:(OSCAR_DIRECTORY) # or ColabFold_nowidgets.ipynb
```

## Build, Save, and Transfer Docker Image

Run the following commands to build the image, save it as a .tar file, and transfer the .tar file to OSCAR. Don't forget to replace ```(USERNAME)``` with your CS login and ```(OSCAR_DIRECTORY)``` with the directory you want to save this to on OSCAR.

```bash
docker build --platform linux/amd64 -f Dockerfile -t colabfold .
docker save colabfold -o colabfold.tar
scp colabfold.tar (USERNAME)@ssh.ccv.brown.edu:(OSCAR_DIRECTORY)
```

## Build Singularity Image

On a **login node** on OSCAR, navigate to the directory containing our .tar file, and run ```singularity build ColabFold.sif docker-archive://colabfold.tar```.

## Run Singularity Image and Notebook

From here, follow the instructions in [Quickstart](quickstart.md).
