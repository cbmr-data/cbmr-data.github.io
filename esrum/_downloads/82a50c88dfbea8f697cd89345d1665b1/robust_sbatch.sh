#!/bin/bash

##############################################################################
# The following are commonly used options for running jobs. Remove one "#"
# from the "##SBATCH" lines (changing it to "#SBATCH") to enable an options.

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
# Avoid jobs with invalid dependencies hanging around forever (recommended)
#SBATCH --kill-on-invalid-dep=yes

##############################################################################
# [1/6] Force entire script to be cached if used as a standalone script
{
	# [2/6] Exit on unset variables
	set -o nounset
	# [3/6] Exit on unhandled failure in pipes
	set -o pipefail
	# [4/6] Have functions inherit ERR traps
	set -o errtrace
	# [5/6] Print debug message and terminate script on non-zero return codes
	trap 's=$?; echo >&2 "$0: Error on line "$LINENO": $BASH_COMMAND"; exit $s' ERR

	##############################################################################
	# Your commands go here:
	echo "Hello world!"

	# [6/6] Prevent Bash from reading past this point once script is done
	exit $?
}
