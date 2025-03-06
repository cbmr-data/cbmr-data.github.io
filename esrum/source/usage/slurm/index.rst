.. _p_usage_slurm:

##########################
 Running jobs using Slurm
##########################

In order to run jobs on the Esrum cluster, you must connect to the head
node (see :ref:`p_usage_connecting`) and queue them using the Slurm_ job
management system. Slurm_ takes care of automatically queuing and
distribute jobs on compute and GPU nodes when the required resources are
available.

While it is permitted to run small jobs directly on the head node, more
resource intensive jobs *must* be queued using Slurm. We *will*
terminate jobs running on the head node without prior warning, if it is
necessary to prevent them from impacting users of the cluster.

The documentation for running jobs is split into three sections:

#. The :ref:`p_usage_slurm_basics` section describes the basic procedure
   of queuing jobs using the ``sbatch`` command, how to request
   resources for your jobs, how to monitor your jobs, and how to run a
   shell on a compute node when you need to work interactively.

#. The :ref:`p_usage_slurm_advanced` section describes additional ways
   to monitor your jobs and the cluster as a whole, how to batch
   multiple, similar jobs using ``sbatch``, how to use ``srun`` for
   executing singular commands, and more.

#. The :ref:`p_usage_slurm_gpu` section describes how to run jobs on the
   GPU / high-memory node, including best practices for using this
   limited resource.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   basics
   advanced
   monitoring
   gpu

.. _slurm: https://slurm.schedmd.com/overview.html
