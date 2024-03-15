.. _p_usage_slurm_gpu:

###########################
 Using the GPU/hi-MEM node
###########################

This section describes how to schedule a task on the GPU/hi-MEM node.
The GPU node is intended for tasks that need to use GPUs and for tasks
that have very high memory requirements (more than 2 TB).

To schedule a task on the GPU node you need to select the GPU queue and
(optionally) specify the number of Nvidia A100 GPUs needed (1 or 2). For
example, the following command queues the command ``my-gpu-command`` and
requests a single A100 GPU:

.. code-block::

   $ srun --partition=gpuqueue --gres=gpu:a100:1 -- my-gpu-command

Alternatively you may reserve both GPUs:

.. code-block::

   $ srun --partition=gpuqueue --gres=gpu:a100:2 -- my-gpu-command

If you on not need to use a GPU, then you can omit the ``--gres``
option:

.. code-block::

   $ srun --partition=gpuqueue -- my-command

As above you must also specify your CPU and RAM requirements using
``--cpus-per-task`` and ``--mem``.

****************************
 Monitoring GPU utilization
****************************

   .. warning::

      Due to changes to Slurm settings, to ensure that jobs cannot
      access resources that were not reserved for them, it is currently
      not possible to monitor GPUs usage from a different job using the
      instructions below. The documentation will be updates shortly.

Slurm does not provide any means of monitoring the actual GPU
utilization, but tools such as ``nvidia-smi`` can be used to monitor
performance metrics. And since we are not going to actually *use* the
GPU, we can simply omit the ``--gres`` option.

.. warning::

   If you need to make use of GPU resources (passive monitoring
   excluded), then you *must* also specify the appropriate ``--gres``
   option. Failure to do so will result in your jobs being terminated!

This allows slurm to run the monitoring task even when the GPUs are
reserved:

.. code-block::

   $ srun --partition=gpuqueue -- nvidia-smi -l 5
   Thu Jun  8 12:18:15 2023
   +-----------------------------------------------------------------------------+
   | NVIDIA-SMI 525.60.13    Driver Version: 525.60.13    CUDA Version: 12.0     |
   |-------------------------------+----------------------+----------------------+
   | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
   | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
   |                               |                      |               MIG M. |
   |===============================+======================+======================|
   |   0  NVIDIA A100 80G...  On   | 00000000:27:00.0 Off |                    0 |
   | N/A   43C    P0    47W / 300W |      0MiB / 81920MiB |      0%      Default |
   |                               |                      |             Disabled |
   +-------------------------------+----------------------+----------------------+
   |   1  NVIDIA A100 80G...  On   | 00000000:A3:00.0 Off |                    0 |
   | N/A   43C    P0    45W / 300W |      0MiB / 81920MiB |      0%      Default |
   |                               |                      |             Disabled |
   +-------------------------------+----------------------+----------------------+

   +-----------------------------------------------------------------------------+
   | Processes:                                                                  |
   |  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
   |        ID   ID                                                   Usage      |
   |=============================================================================|
   |  No running processes found                                                 |
   +-----------------------------------------------------------------------------+

The ``gpustat`` tool provides a more convenient overview but must be
installed via ``pip``:

..
   TODO: Update when gpustats has been added as a module

.. code-block::

   $ pip install gpustat
   $ srun --partition=gpuqueue --pty -- gpustat -i 5
   esrumgpun01fl.unicph.domain  Thu Jun  8 12:20:24 2023  525.60.13
   [0] NVIDIA A100 80GB PCIe | 43°C,   0 % |     0 / 81920 MB |
   [1] NVIDIA A100 80GB PCIe | 43°C,   0 % |     0 / 81920 MB |

The ``--pty`` option is used in order to support colored, full-screen
output despite not running an interactive actual shell. As an
alternative, you can also start an interactive shell on the GPU node and
run ``gpustats`` or ``nvidia-smi`` that way:

.. code-block::

   $ srun --partition=gpuqueue --pty -- /bin/bash
   $ gpustat -i 5

Troubleshooting
===============

******************************************************
 Error: Requested node configuration is not available
******************************************************

See the Slurm Basics :ref:`s_slurm_basics_troubleshooting` section.
