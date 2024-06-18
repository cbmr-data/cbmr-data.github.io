.. _p_usage_slurm_gpu:

###########################
 Using the GPU/hi-MEM node
###########################

This section describes how to schedule a task on the GPU/hi-MEM node.
The GPU node is intended for tasks that need to use GPUs and for tasks
that have very high memory requirements (more than 2 TB).

**********************************
 Running software on the GPU node
**********************************

It is possible to use the GPU node in an interactive session (see
below), but since we have few GPUs available we ask that you limit the
usage of interactive sessions *as much as possible*. This ensures that
the GPUs are available for use when you (or other users) are not
actively using them.

The recommended way to use the GPUs is therefore to submit a job to
Slurm using the ``sbatch`` command. To do so you need to specify two
options as part of your ``sbatch`` script:

.. code-block:: bash
   :emphasize-lines: 2

   #!/bin/bash
   #SBATCH --partition=gpuqueue --gres=gpu:1

   nvidia-smi -L

There are two required options:

#. The ``--partition=gpuqueue`` option ensures that we are running on
   the GPU Slurm job queue, which is distinct from the standard Slurm
   job queue that only has access to normal compute nodes.

#. The ``--gres=gpu:1`` asks Slurm to make 1 GPU available to our job.
   This can be increased to ``2`` to reserve both GPUs, but because of
   the limited number of GPUs we ask that you only reserve 1 GPU per
   job, which is normally also more efficient.

This script can then be submitted as usual:

.. code-block:: shell

   $ sbatch my_gpu_job.sh
   Submitted batch job 217218
   $ cat slurm-217218.out
   GPU 0: NVIDIA A100 80GB PCIe (UUID: GPU-4f2ff8df-0d18-a99b-9fb8-67aa0867f7a3)

See the :ref:`p_usage_slurm_basics` and :ref:`p_usage_slurm_advanced`
pages for information about reserving additional CPUs, more RAM, and for
setting other Slurm settings for your jobs.

Running an interactive session
==============================

It is also possible to reserve GPUs for interactive sessions should you
need to experiment with running a piece of software or should the
software itself be interactive. See the :ref:`s_interactive_session`
section for information about interactive sessions, including
information about running programs with graphical interfaces.

To start an interactive session using a GPU you simply apply the same
``--partition`` and ``--gres`` options as above:

.. code-block::

   $ srun --pty --partition=gpuqueue --gres=gpu:1 -- /bin/bash

Interactive sessions should only be used for tasks that *cannot* be run
via ``sbatch`` and the sessions should be closed as soon as you are done
running your software. This ensures that the GPUs are available to other
users.

.. warning::

   Interactive sessions left running on the GPU node may be terminated
   without warning.

.. _s_monitoring_gpu_utilization:

****************************
 Monitoring GPU utilization
****************************

It is highly recommended to monitor GPU utilization when you run jobs on
the GPU node: To make full use of the hardware you want to keep GPU
utilization at 100% and to do so you typically want to load as much data
into GPU memory as possible. The exact way in which you can accomplish
this depends on the software you are running, but can often be
accomplished by increasing the size of the batches you are processing.

The way in which you are using the GPUs will affect how you can monitor
them, depending on whether or not you have reserved a GPU for an
interactive session:

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
every 5 seconds afterwards via ``-l 5``. Other monitoring tools are
available (for example ``gpustat``), but are outside the scope of this
documentation.

Monitoring a Slurm job
======================

If you have started a standard (non-interactive) job via Slurm, then you
will not be able to directly run ``nvidia-smi`` nor will you be able to
join the running job using ``srun -j`` (due to the way Slurm handles
special resources). We have therefore setup a log-file on the
``esrumgpun01fl`` node that contains the output from the ``nvidia-smi``
command as shown above.

Use the following command to watch the content of this log-file:

.. code-block::

   $ srun --pty --partition=gpuqueue -- watch -n 15 -d cat /scratch/gpus/nvidia-smi.txt

This prints the contents of the log-file every 15 seconds and optionally
highlights the changes since the last ``nvidia-smi`` run (remove the
``-d`` option to disable).

This command does *not* reserve a GPU and while we ask that you remember
to terminate this command when you no longer need to monitor the GPUs,
it is not as urgent as for interactive sessions where you *have*
reserved a GPU.

*****************
 Troubleshooting
*****************

Error: Requested node configuration is not available
====================================================

See the Slurm Basics :ref:`s_slurm_basics_troubleshooting` section.
