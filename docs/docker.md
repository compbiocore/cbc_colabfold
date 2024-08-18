# Building Singularity Image from Docker

If you want to build the Singularity image yourself, a Dockerfile is included in the [Git repo](https://github.com/compbiocore/cbc_colabfold). Download this to your local machine. Also, make sure you have Docker up and running locally.

Make sure you have cloned the repo on OSCAR as well, as the Singularity image that will be built does not include the Jupyter notebook or its associated widgets.

## Build, Save, and Transfer Docker Image

Navigate to the ```cbc_colabfold``` repo folder on your local machine. and run the following commands to build the Docker image and save it as a .tar file. This may take >10 minutes.

```bash
docker build --platform linux/amd64 -f Dockerfile -t colabfold .
docker save colabfold -o colabfold.tar
```

Then, run this command to copy the file to your ```cbc_colabfold``` directory on OSCAR (the directory produced by cloning our Git repo on OSCAR). You may have to authenticate to SSH. Don't forget to replace ```(USERNAME)``` with your CS login and ```(COLABFOLD_DIRECTORY)``` with the path to the ```cbc_colabfold``` folder.
   
```bash
scp cbc_colabfold.tar (USERNAME)@ssh.ccv.brown.edu:(COLABFOLD_DIRECTORY)
```

## Build Singularity Image

On a **login node** on OSCAR, navigate to your ```cbc_colabfold``` directory and run the following command to build the Singularity image:

```
singularity build cbc_colabfold_latest.sif docker-archive://cbc_colabfold.tar
```

## Run Singularity Image and Notebook

From here, follow the instructions in [Quickstart](quickstart.md).
