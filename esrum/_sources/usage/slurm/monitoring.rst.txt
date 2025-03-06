.. _p_usage_slurm_monitor:

#######################
 Monitoring slurm jobs
#######################

This section describes the techniques for monitoring jobs running
through slurm, the amount of resources they are currently using (CPUs,
RAM, and GPUs), the overall amount of resources used by completed jobs,
and whether jobs have started running, have finished running, or have
failed.

Additionally, it is described how to monitor the overall activity level
of the cluster, to help inform how many resources you can reasonably
reserve for a set of jobs. See the :ref:`s_best_practice_resources`
section.

****************************************
 E-mail notifications on job completion
****************************************

In addition to actively monitoring your jobs using ``squeue``, it is
possible to receive email notifications when your jobs are started,
finish, fail, are re-queued, or some combination. This is accomplished
by using the ``--mail-user`` and ``--mail-type`` options:

.. code-block::

   $ sbatch --mail-user=abc123@ku.dk --mail-type=END,FAIL my_script.sh
   Submitted batch job 8503

These options can naturally also be embedded in your sbatch script:

.. code-block:: bash

   #!/bin/bash
   #SBATCH --mail-user=abc123@ku.dk --mail-type=END,FAIL

   my-commands

and queued as usual:

.. code-block:: console

   $ sbatch my-script.sh
   Submitted batch job 8504

When these options are enabled, Slurm will send a notification to
``abc123@ku.dk`` account when the job is completed or if it fails. The
possible values for ``--mail-type`` are ``NONE`` (the default),
``BEGIN``, ``END``, ``FAIL``, ``REQUEUE``, ``ALL``, or some combination
as shown above.

.. warning::

   Remember to use your own ``@ku.dk`` email address as the recipient,
   instead of ``abc123@ku.dk``. It is possible to use email addresses
   outside ``@ku.dk``, but some providers will silently block these
   emails, and we therefore recommend using your ``@ku.dk`` address.

*******************************************
 Monitoring overall resource usage by jobs
*******************************************

The ``sacct`` command may be used to review the average CPU usage, the
peak memory usage, disk I/O, and more for completed jobs. This makes it
easier to verify that you are not needlessly reserving resources:

.. code-block::

   $ sacct -o JobID,Elapsed,State,AllocCPUS,AveCPU,ReqMem,MaxVMSize

A full description of the data printed by ``sacct`` command can be found
in the `sacct manual`_, but briefly, this prints the job ID, the amount
of time the job has been running, the state of the job (queued, running,
completed, etc.), number of CPUs allocated, the CPU utilization
(preferably this should be the number of CPUs allocated times the
elapsed time), the amount of memory requested, and the peak virtual
memory size.

Alternatively, we provide a helper that summarizes some of this
information in a more easily readable form:

.. code-block::

   $ module load sacct-usage
   $ sacct-usage
         Age  User    Job   State         Elapsed  CPUs  CPUsWasted  ExtraMem  ExtraMemWasted  CPUHoursWasted
   13:32:04s  abc123  1     FAILED     252:04:52s     8         6.9     131.4           131.4         4012.14
   10:54:32s  abc123  2[1]  COMPLETED   02:49:25s    32        15.7       0.0             0.0           44.38
   01:48:43s  abc123  3     COMPLETED   01:00:53s    24         2.4       0.0             0.0            2.43

The important information is found in the ``CPUsWasted`` column and the
``ExtraMemWasted`` column, which show the number CPUs that went unused
on average, and the amount of *extra* memory that went unused. Note that
``ExtraMem`` only counts memory above the default allocation of ~16 GB
of RAM per CPU, as our policy is that you shouldn't have to worry about
using less than that. If you want to see the full memory usage, then use
the ``--verbose`` option.

The final column indicates that number of CPU hours your job wasted,
calculated as the length of time your job ran multiplied by the number
of reserved CPUs and the number of CPUs that would have been able to get
the default 16 GB of RAM had ``ExtraMemWasted`` been zero.

Aim for your jobs to resemble the third job, not the second job and
especially not the first job in the example!

.. warning::

   The ``Wasted`` statistics are based on snapshots of resource usage
   produced by Slurm and are therefore not 100% accurate. Notably, the
   memory usage statistics are based on maximum memory usage of
   individual processes, rather than the maximum cumulative memory
   usage, and may therefore greatly overestimate wasted memory if you
   are running multiple simultaneous processes in a pipeline.

******************************************
 Monitoring individual processes in a job
******************************************

While ``sacct`` can report on the overall resource usage of you job, it
can also be helpful to track resource usage for individual commands that
you are running. This is particularly useful when attempting to optimize
the number of CPUs used commands run in a job.

One way of doing this is via the ``time`` command, which can report the
efficiency from using multiple threads and to show how much memory a
program used. This is acoomplished by pre-pending ``/usr/bin/time -f
"CPU = %P, MEM = %MKB"`` to the command that you want to measure, as
shown in this example, where we wish to measure the resource usage of
the ``my-command`` program:

.. code-block::

   $ /usr/bin/time -f "CPU = %P, MEM = %M" my-command --threads 1 ...
   CPU = 99%, MEM = 840563KB
   $ /usr/bin/time -f "CPU = %P, MEM = %M" my-command --threads 4 ...
   CPU = 345%, MEM = 892341KB
   $ /usr/bin/time -f "CPU = %P, MEM = %M" my-command --threads 8 ...
   CPU = 605%, MEM = 936324KB

In this example, increasing the number of threads/CPUs to 4 did not
result in a 4x increase in CPU usage, but only an 3.5x increase with 4
CPUs and only a 6x increase with 8 CPUs. This means that it would be
more efficient to run two tasks with 4 CPUs in parallel, rather than
running one task with 8 CPUs.

.. _s_live_monitoring:

**************************************
 Live monitoring of processes in jobs
**************************************

In addition to monitoring jobs at a high level, it is possible to
actively monitor the processes running in your jobs via (interactive)
shells running on the same node as the job you wish to monitor. This
allows us to estimate resource usage *before* a job has finished
running. In this example we will use the ``htop`` command to monitor our
jobs, but you can use basic ``top``, a ``bash`` shell, or any other
command you prefer.

The first option for directly monitoring jobs is to request a job on the
same server using the ``--nodelist`` option to specify the node your job
is running on. However, this will not work if all resources on the node
are reserved, and for that reason we recommend running ``htop`` *inside*
your existing job.

This is done using the ``--overlap`` and ``--jobid`` command-line
options for ``srun``, which tells Slurm that your new job should overlap
an existing job, and the ID of the job to overlap. The job ID can obtain
using for example the ``squeue --me`` command (from the ``JOBID``
column), as shown here:

.. code-block::

   $ squeue --me
   JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
    8503 standardq my_scrip   abc123  R       0:02      1 esrumcmpn03fl
   $ srun --pty --overlap --jobid 8503 --gres=none htop

The ``--pty`` option gives us an interactive session, which allows us to
interact directly with ``htop``. See the :ref:`s_interactive_session`
section for more information. The ``--gres=none`` option is required to
overlap jobs that reserve GPUs, since Slurm does not permit those to be
shared, even for overlapping jobs. See below for instructions on how to
monitor GPU utilization.

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

If you are running a job in an :ref:`interactive session
<s_interactive_session>`, then you can monitor the reserved GPU(s)
directly using the ``nvidia-smi`` command:

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
:ref:`s_live_monitoring` for more information.

.. _s_monitoring_slurm:

************************
 Monitoring the cluster
************************

The slurmboard_ utility is made available as part of the ``cbmr_shared``
project folder, in order to make it easy to monitor activity on the
cluster, for example to decide how many resources you can reasonably use
for a job (see :ref:`s_best_practice_resources`):

.. code-block::

   $ module load slurmboard
   $ slurmboard

.. image:: /usage/slurm/images/slurmboard.png
   :align: center

Briefly, this utility displays every node in the cluster, their status,
and available resources for each of these. The resources (CPUs, Memory,
and GPUs) columns are colored as follows: Yellow indicates resources
that have been reserved; green indicates resources that are actively
being used; purple indicates resources that may be inaccessible due to
other resources being reserved (e.g. RAM being inaccessible due to all
CPUs being reserved vice versa); and black indicates resources that are
unavailable due to nodes being offline or under maintenance.

.. note::

   The Data Analytics Platform uses this utility to monitor how busy the
   cluster is and how job are performing. In particular, we may reach
   out to you if we notice that your jobs consistently use significantly
   fewer resources than the amount reserved, in order to optimize
   resource utilization on the cluster.

.. _sacct manual: https://slurm.schedmd.com/archive/slurm-20.11.9/sacct.html

.. _slurmboard: https://github.com/cbmr-data/slurmboard
