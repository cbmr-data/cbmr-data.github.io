Error: Requested node configuration is not available
====================================================

If you request too many CPUs (more than 128), or too much RAM (more than
1993 GB for compute nodes and more than 3920 GB for the GPU node), then
Slurm will report that the request cannot be satisfied:

.. code-block:: shell

   # More than 128 CPUs requested
   $ sbatch --cpus-per-task 200 my_script.sh
   sbatch: error: CPU count per node can not be satisfied
   sbatch: error: Batch job submission failed: Requested node configuration is not available

   # More than 1993 GB RAM requested on compute node
   $ sbatch --mem 2000G my_script.sh
   sbatch: error: Memory specification can not be satisfied
   sbatch: error: Batch job submission failed: Requested node configuration is not available

To solve this, simply reduce the number of CPUs and/or the amount of RAM
requested to fit within the limits described above. If your task does
require more than 1993 GB of RAM, then you need to run your task on the
GPU queue as described on the :ref:`p_usage_slurm_gpu` page.

Additionally, you may receive this message if you request GPUs without
specifying the correct queue or if you request too many GPUs:

.. code-block:: shell

   # --partition=gpuqueue not specified
   $ srun --gres=gpu:2 -- echo "Hello world!"
   srun: error: Unable to allocate resources: Requested node configuration is not available

   # More than 2 GPUs requested
   $ srun --partition=gpuqueue --gres=gpu:3 -- echo "Hello world!"
   srun: error: Unable to allocate resources: Requested node configuration is not available

To solve this error, simply avoid requesting more than 2 GPUs, and
remember to include the ``--partition`` option. See also the
:ref:`p_usage_slurm_gpu` section.
