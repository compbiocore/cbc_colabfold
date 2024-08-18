ARG CUDA_VERSION=12.2.0
ARG COLABFOLD_VERSION=1.5.5
FROM --platform=linux/amd64 nvidia/cuda:${CUDA_VERSION}-base-ubuntu22.04

RUN apt-get update && apt-get install -y wget cuda-nvcc-$(echo $CUDA_VERSION | cut -d'.' -f1,2 | tr '.' '-') --no-install-recommends --no-install-suggests && rm -rf /var/lib/apt/lists/* && \
    wget -qnc https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh && \
    bash Mambaforge-Linux-x86_64.sh -bfp /usr/local && \
    rm -f Mambaforge-Linux-x86_64.sh && \
    CONDA_OVERRIDE_CUDA=$(echo $CUDA_VERSION | cut -d'.' -f1,2) mamba create -y -n colabfold -c conda-forge -c bioconda ipykernel ipywidgets notebook mmseqs2 jax[cuda12] rsync git zip colabfold=$COLABFOLD_VERSION jaxlib==*=cuda* && \
    mamba clean -afy

ENV PATH=/usr/local/envs/colabfold/bin:$PATH
ENV MPLBACKEND=Agg
ENV ENABLE_PJRT_COMPATIBILITY=true
# ENV SINGULARITY_BINDPATH="/oscar/home/$USER,/oscar/scratch/$USER"

VOLUME cache
ENV MPLCONFIGDIR=/cache
ENV XDG_CACHE_HOME=/cache

# COPY ColabFold.ipynb /
# COPY ColabFold_nowidgets.ipynb /
RUN mamba run -n colabfold python -m ipykernel install --user --name=colabfold
