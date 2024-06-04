#!/bin/bash

# The following are commonly used options for running jobs. Remove one "#"
# from the "##SBATCH" lines (changing it to "#SBATCH") to enable an options.
# Unused SBATCH options can safely be removed.

# The number of CPUs (cores) used by your task. Defaults to 1.
##SBATCH --cpus-per-task=1
# The amount of RAM used by your task. Tasks are automatically assigned 15G
# per CPU (set above) if this option is not set.
##SBATCH --mem=15G
# Set a maximum runtime in hours:minutes:seconds. No default limit.
##SBATCH --time=1:00:00
# Request a GPU on the GPU code. Use `--gres=gpu:a100:2` to request both GPUs.
##SBATCH --partition=gpuqueue --gres=gpu:a100:1
# Run a set of tasks. For example --array=1-23, --array=1,5,10, and more.
# The current task ID is available as the variable ${SLURM_ARRAY_TASK_ID}
##SBATCH --array=

# Brackets forces entire script to be read
{
set -o nounset  # Exit on unset variables
set -o pipefail # Exit on unhandled failure in pipes
set -o errtrace # Have functions inherit ERR traps
# Print debug message and terminate script on non-zero return codes
trap 's=$?; echo >&2 "$0: Error on line "$LINENO": $BASH_COMMAND"; exit $s' ERR

# Your commands go here:
echo "Hello, world!"

# Prevent the script from continuing if the file has changed
exit $?
}
