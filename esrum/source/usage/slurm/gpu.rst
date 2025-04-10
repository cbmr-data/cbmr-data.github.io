.. _p_usage_slurm_gpu:

########################
 GPU / high-memory jobs
########################

The cluster currently includes 1 node with 2x A100 Nvidia GPUs and 4 TB
of RAM, and 3 nodes with 2x H100 Nvidia GPUs and 2 TB of RAM. We refer
to these as the GPU and/or high-memory nodes, and this page describes
how to use them.

These nodes are intended for tasks that make use of GPUs, and for
individual jobs that require more than the 2 TB of RAM available on the
regular compute nodes.

********************************************
 Running jobs on the GPU / high-memory node
********************************************

By default, jobs submitted via Slurm will only run on regular nodes,
even if you ask for more than 2 TB of RAM or ask for a GPU. Attempting
to run such a task will instead result in a ``Requested node
configuration is not available`` error message.

This is because the GPU / high-memory node is located on its own queue,
to in order prevent normal use of the cluster from blocking access to
these resources. You must therefore select use the option
``--partition=gpuqueue`` to select the correct queue. This might look as
follows in a sbatch script:

.. code-block:: bash
   :linenos:
   :emphasize-lines: 2

   #!/bin/bash
   #SBATCH --partition=gpuqueue

   my-memory-hungry-command

While running on the GPU queue, you can reserve up to 3920 GB of RAM and
up to two GPUs (see below) per job. The GPU / high-memory nodes
otherwise use the same defaults as the other nodes (~16 GB of RAM per
CPU reserved).

For example, to run a job using 2.5 TB of RAM on the GPU / high-memory
node:

.. code-block:: bash
   :linenos:
   :emphasize-lines: 2

   #!/bin/bash
   #SBATCH --partition=gpuqueue
   #SBATCH --mem 2560G

   my-memory-hungry-command

This script can then be submitted as usual:

.. code-block:: console

   $ sbatch my_hi_mem_job.sh
   Submitted batch job 217217

See the :ref:`p_usage_slurm_basics` and :ref:`p_usage_slurm_advanced`
pages for information about reserving additional CPUs, more RAM, and for
setting other Slurm settings for your jobs.

We ask that you do not reserve all available CPUs or all RAM on the GPU
/ high-memory node, unless it is actually required for your analyses,
since leaving some unused resources permits other users to utilize the
GPUs while your tasks are running.

****************
 Reserving GPUs
****************

Requesting GPUs is done with the ``--gres`` option and also requires
that using the ``--partition=gpuqueue`` option to select the correct
queue, as described above. This might look as follows in a ``sbatch``
script:

.. code-block:: bash
   :linenos:
   :emphasize-lines: 2

   #!/bin/bash
   #SBATCH --partition=gpuqueue --gres=gpu:1

   nvidia-smi -L

The ``--gres=gpu:1`` in the above asks Slurm to make 1 GPU available to
our job. This can be increased to ``2`` to reserve both GPUs on the
node, but because of the limited number of GPUs we ask that you only
reserve 1 GPU per job, which is normally also more efficient.

This script can then be submitted as usual:

.. code-block:: console

   $ sbatch my_gpu_job.sh
   Submitted batch job 217218
   $ cat slurm-217218.out
   GPU 0: NVIDIA A100 80GB PCIe (UUID: GPU-4f2ff8df-0d18-a99b-9fb8-67aa0867f7a3)

Requesting specific GPUs
========================

As indicated above, the GPU nodes includes both Nvidia H100 and A100
GPUs. By default, your job will be assigned to the first idle GPU(s),
but it is also possible to request a specific GPU type.

To request an A100 GPU, replace the ``--gres=gpu:1`` option with
``--gres=gpu:a100:1``, and to request an H100 GPU, replace the
``--gres=gpu:1`` option with ``--gres=gpu:h100:1``. For example,

.. code-block:: bash
   :linenos:
   :emphasize-lines: 2

   #!/bin/bash
   #SBATCH --partition=gpuqueue --gres=gpu:h100:1

   nvidia-smi -L

This script can then be submitted as usual:

.. code-block:: console

   $ sbatch my_h100_job.sh
   Submitted batch job 217219
   $ cat slurm-217219.out
   GPU 0: NVIDIA H100 NVL (UUID: GPU-c43d0655-2d15-7e66-90b3-9b732a1d13ba)

We recommend looking at current GPU utilization before submitting your
job, as any time saved by running on a faster (H100) GPU may be lost
from having to wait for them to be idle. See ``slurmboard`` utility
described in the :ref:`s_monitoring_slurm` section provides a simple way
to see GPU reservations.

Running an interactive session
==============================

While it is possible to run an interactive session on the GPU /
high-memory node, we ask that you limit the usage of such sessions as
much as possible. If at all possible, prefer using ``sbatch`` or
non-interactive ``srun`` instead. This ensures that the resources are
available for use when you (or other users) are not actively using them.

To start an interactive session using a GPU you simply apply the same
``--partition`` and (optionally) the same ``--gres`` options as above if
you need a GPU, as well as other resource options described in the
:ref:`reserving_resources` section:

.. code-block:: console

   $ srun --pty --partition=gpuqueue -- /bin/bash

See the :ref:`s_interactive_session` section for information about
interactive sessions, including information about running programs with
graphical interfaces.

.. warning::

   Interactive sessions left running on the GPU node may be terminated
   without warning.

****************************
 Monitoring GPU utilization
****************************

Please see the :ref:`s_monitoring_gpu_utilization` section on the
:ref:`p_usage_slurm_monitor` page.

*****************
 Troubleshooting
*****************

Error: Requested node configuration is not available
====================================================

See the Slurm Basics :ref:`s_slurm_basics_troubleshooting` section.
