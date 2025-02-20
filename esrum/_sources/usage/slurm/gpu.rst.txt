.. _p_usage_slurm_gpu:

###################################
 Using the GPU / high-memory nodes
###################################

This page describes how to schedule tasks on the dedicated GPU nodes and
on the combined GPU / high-memory node. The cluster currently includes 1
node with 2x A100 Nvidia GPUs and 4 TB of RAM, and 2 nodes with 2x H100
Nvidia and 2 TB of RAM.

These nodes are intended for tasks that can make use of GPUs, and for
tasks that require more than the 2 TB of RAM available on regular
compute nodes.

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
   :emphasize-lines: 2

   #!/bin/bash
   #SBATCH --partition=gpuqueue
   #SBATCH --mem 2560G

   my-memory-hungry-command

This script can then be submitted as usual:

.. code-block::

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
   :emphasize-lines: 2

   #!/bin/bash
   #SBATCH --partition=gpuqueue --gres=gpu:1

   nvidia-smi -L

The ``--gres=gpu:1`` in the above asks Slurm to make 1 GPU available to
our job. This can be increased to ``2`` to reserve both GPUs on the
node, but because of the limited number of GPUs we ask that you only
reserve 1 GPU per job, which is normally also more efficient.

This script can then be submitted as usual:

.. code-block::

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
   :emphasize-lines: 2

   #!/bin/bash
   #SBATCH --partition=gpuqueue --gres=gpu:h100:1

   nvidia-smi -L

This script can then be submitted as usual:

.. code-block::

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

.. code-block::

   $ srun --pty --partition=gpuqueue -- /bin/bash

See the :ref:`s_interactive_session` section for information about
interactive sessions, including information about running programs with
graphical interfaces.

.. warning::

   Interactive sessions left running on the GPU node may be terminated
   without warning.

.. _s_monitoring_gpu_utilization:

****************************
 Monitoring GPU utilization
****************************

Monitoring of GPU utilization is highly recommended when you run jobs on
the GPU node: To make full use of the hardware you want to keep GPU
utilization at 100% and to do so you typically want to load as much data
into GPU memory as possible. The exact way in which you can accomplish
this depends on the software you are running, but can often be
accomplished by increasing the size of the batches you are processing.

The way in which you are using the GPUs will affect how you can monitor
them, depending on whether you have reserved a GPU for an interactive
session:

Monitoring an interactive session
=================================

If you are running a job in an interactive session, then you can monitor
the reserved GPU(s) directly using the ``nvidia-smi`` command:

.. code-block::

   $ nvidia-smi -l 5
   Thu Apr  4 14:30:46 2024
   +---------------------------------------------------------------------------------------+
   | NVIDIA-SMI 545.23.08              Driver Version: 545.23.08    CUDA Version: 12.3     |
   |-----------------------------------------+----------------------+----------------------+
   | GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
   | Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
   |                                         |                      |               MIG M. |
   |=========================================+======================+======================|
   |   0  NVIDIA A100 80GB PCIe          On  | 00000000:27:00.0 Off |                    0 |
   | N/A   57C    P0             307W / 300W |  52357MiB / 81920MiB |         99%  Default |
   |                                         |                      |             Disabled |
   +-----------------------------------------+----------------------+----------------------+
   |   1  NVIDIA A100 80GB PCIe          On  | 00000000:A3:00.0 Off |                    0 |
   | N/A   56C    P0             298W / 300W |  58893MiB / 81920MiB |        100%  Default |
   |                                         |                      |             Disabled |
   +-----------------------------------------+----------------------+----------------------+
   +---------------------------------------------------------------------------------------+
   | Processes:                                                                            |
   |  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
   |        ID   ID                                                                 Usage  |
   |=======================================================================================|
   |    0   N/A  N/A   2807877  C   dorado                                        52344MiB |
   |    1   N/A  N/A   2807849  C   dorado                                        58880MiB |
   +---------------------------------------------------------------------------------------+

This will print resource usage for the GPUs you have reserved for your
interactive session (and only for those GPUs), and continue to print it
every 5 seconds afterwards via the ``-l 5`` option. Other monitoring
tools are available (for example ``gpustat``), but are outside the scope
of this documentation.

Monitoring a Slurm job
======================

If you have started a standard (non-interactive) job via Slurm, then you
will not be able to directly run ``nvidia-smi`` nor will you be able to
join the running job using ``srun -j`` due to the way Slurm handles
special resources. We have therefore set up log-files on the GPU nodes
node that contains the output from the ``nvidia-smi`` command as shown
above.

To watch the content of this log-file, firstly determine the job ID of
your job running on the GPU node:

.. code-block::

   $ squeue --me --partition=gpuqueue
    JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
   570316  gpuqueue     bash   abc123  R      13:55      1 esrumgpun01fl

Then we use ``srun`` with the ``--overlap`` option to run a command
*inside* this job, which we specify using the ``--jobid 570316`` option.
The ``--gres=none`` option is required, since otherwise Slurm would try
to reserve the GPU our job already uses and eventually time out.

.. code-block::

   $ srun --overlap --jobid 570316 --gres=none --pty -- watch -n 15 -d cat /scratch/gpus/nvidia-smi.txt

.. warning::

   Remember to replace the ``570316`` with the ID of *your* job!

This prints the contents of the log-file every 15 seconds (which is how
often the files are updated) and optionally highlights the changes since
the last ``nvidia-smi`` run. To disable the highlighting, simply remove
the ``-d`` option from the command.

This command does not take up additional resources on the GPU node and
will automatically exit when your job finishes. See the
:ref:`s_monitoring_processes_in_jobs` for more information.

*****************
 Troubleshooting
*****************

Error: Requested node configuration is not available
====================================================

See the Slurm Basics :ref:`s_slurm_basics_troubleshooting` section.
