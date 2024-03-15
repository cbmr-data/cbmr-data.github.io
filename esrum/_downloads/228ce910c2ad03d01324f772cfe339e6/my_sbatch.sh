#!/bin/bash

# The following are commonly used options for running jobs. Remove one
# "#" from the "##SBATCH" lines (changing them to "#SBATCH") to enable
# a given option.

# The number of CPUs (cores) used by your task. Defaults to 1.
##SBATCH --cpus-per-task=1
# The amount of RAM used by your task. Tasks are automatically assigned 15G
# per CPU (set above) if this option is not set.
##SBATCH --mem=15G
# Set a maximum runtime in hours:minutes:seconds. No default limit.
##SBATCH --time=1:00:00
# Request a GPU on the GPU code. Use `--gres=gpu:a100:2` to request both GPUs.
##SBATCH --partition=gpuqueue --gres=gpu:a100:1
# Send notifications when job ends. Remember to update the email address!
##SBATCH --mail-user=abc123@ku.dk --mail-type=END,FAIL

########################
# Your commands go here:

echo "Hello world!"
