#!/bin/bash

# Description: Setup script for creating conda environment and installing packages
# Arguments:
#   $1: cpu or gpu (default: gpu), use cpu for mac m1/m2
# Example usage:
#   $ bash setup.sh cpu

# Set environment variables
env_name=$(basename $PWD)
python_version=3.9

echo "Using environment name: $env_name"

# Create conda environment
conda create -n ${env_name} python=${python_version}
CONDA_BASE=$(conda info --base)
source $CONDA_BASE/etc/profile.d/conda.sh
conda activate $env_name

# Install packages
pip install -r requirements.txt

# Get argument for cpu or gpu
if [ "$1" == "cpu" ]; then
    echo "Installing torch with cpu only"
    pip install -r requirements_torch_cpu.txt
elif [ "$1" == "gpu" ]; then
    echo "Installing torch with gpu"
    pip install -r requirements_torch_gpu.txt
else
    echo "No argument provided. Installing torch with gpu"
    pip install -r requirements_torch_gpu.txt
fi

conda deactivate