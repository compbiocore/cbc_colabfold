# Quickstart

Welcome to ColabFold! The following instructions will help you get the ColabFold notebook set up on OSCAR.

## Clone Git Repo

First, clone our [Git repo](https://github.com/compbiocore/cbc_colabfold) into your desired directory on OSCAR.

## Set Up Notebook

### Option 1: Run via Jupyter Notebook for Apptainer Images

OSCAR's Open On-Demand provides a Jupyter Notebook for Apptainer Images app; this fairly conveniently runs our notebook from our Singularity/Apptainer image.

Under "Expert GUIs", click "Jupyter Notebook for Apptainer Images". In the "Path to apptainer image" field, provide the absolute path to your Singularity image (ColabFold.sif). Make sure that the following fields are filled out as follows:

- Partition: **gpu**
- Memory per job: **16G**
- Number of GPUs: at least **1**

### Option 2: Run on OOD Desktop

We can also access this Jupyter notebook via Open On-Demand Desktop. First, start an OOD Desktop session; we highly recommend choosing the **2 GPUs, 15GB memory** option. Then, in the Terminal app in this session, navigate to the directory where the Singularity image is located, and use the following command to activate the kernel for the Jupyter notebook:

	singularity run --nv -B /oscar/home/$USER /oscar/scratch/$USER ColabFold.sif

Once you are in the Singularity container, make sure you are in the directory where the Jupyter notebook is located, then run ```jupyter notebook``` to activate the Jupyter app, and finally navigate to your desired notebook.

## Run Notebook

Once all parameters have been customized to your liking, click the next cell, then go to "Run" on the menu bar and click **Run Selected Cell and All Below**. The output should be saved to a folder in your current directory named after the job name you provided.
