.. _p_usage_slurm:

##########################
 Running jobs using Slurm
##########################

In order to run jobs on the Esrum cluster, you must connect to the head
node (see :ref:`p_usage_connecting`) and queue them using the `Slurm
<l_slurm_>`_ job management system. Slurm takes care of automatically
queuing and distribute jobs on compute and GPU nodes when the required
resources are available.

.. attention::

    While it is permitted to run small jobs directly on the head node,
    it is not possible to use more 4 CPUs and 64 GB of RAM. These limits
    exist to reduce the impact on other users. For the same reason,
    transfers and jobs that involve reading/writing a lot of data should
    not be run on the head node. For transfers, instead see the
    :ref:`p_transfers` page.

The documentation for running jobs is split into three sections:

1. The :ref:`p_usage_slurm_basics` section describes the basic procedure
   of queuing jobs using the ``sbatch`` command, how to request
   resources for your jobs, how to monitor your jobs, and how to run a
   shell on a compute node when you need to work interactively.
2. The :ref:`p_usage_slurm_advanced` section describes how to batch
   multiple, similar jobs using ``sbatch``, how to use ``srun`` for
   executing singular commands, and more.
3. The :ref:`p_usage_slurm_monitor` section describes how to monitor
   your Slurm jobs, including how see their state, how to inspect
   processes running in your jobs, and how to get email notifications
   when your jobs start or finish.
4. The :ref:`p_usage_slurm_gpu` section describes how to run jobs on the
   GPU / high-memory node, including best practices for using this
   limited resource.

******************
 Table of content
******************

.. toctree::
    :titlesonly:

    basics
    advanced
    monitoring
    gpu

.. include:: /links.rst
