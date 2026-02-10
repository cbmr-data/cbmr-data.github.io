######################################
 Dummy header to prevent reformatting
######################################

**************************************
 Dummy header to prevent reformatting
**************************************

Error: Unable to allocate resources: Invalid account or account/partition combination specified
===============================================================================================

If you get this error while using ``sbatch`` or ``srun``, then ensure
that your ``sbatch`` or ``srun``, then please ensure that you are not
manually specifying an account.

If you are not specifying an account, but still get this error, then
please :ref:`\<contact us <p_contact>>`. Normally, a Slurm account
should automatically be created for you, but in some cases that may not
have happened, and we may have to fix it manually.

Error: Requested node configuration is not available
====================================================

If you request too many CPUs (more than 128), or too much RAM (more than
1993 GB for compute nodes and more than 3920 GB for the GPU node), then
Slurm will report that the request cannot be satisfied.

If more than 128 CPUs requested:

.. code-block:: console

   $ sbatch --cpus-per-task 200 my_script.sh
   sbatch: error: CPU count per node can not be satisfied
   sbatch: error: Batch job submission failed: Requested node configuration is not available

More than 1993 GB RAM requested on compute node:

.. code-block:: console

   $ sbatch --mem 2000G my_script.sh
   sbatch: error: Memory specification can not be satisfied
   sbatch: error: Batch job submission failed: Requested node configuration is not available

To solve this, simply reduce the number of CPUs and/or the amount of RAM
requested to fit within the limits described above. If your task does
require more than 1993 GB of RAM, then you need to run your task on the
GPU queue as described on the :ref:`p_usage_slurm_gpu` page.

Additionally, you may receive this message if you request GPUs without
specifying the correct queue or if you request too many GPUs.

If ``--partition=gpuqueue`` not specified:

.. code-block:: console

   $ srun --gres=gpu:2 -- echo "Hello world!"
   srun: error: Unable to allocate resources: Requested node configuration is not available

If more than 2 GPUs requested:

.. code-block:: console

   $ srun --partition=gpuqueue --gres=gpu:3 -- echo "Hello world!"
   srun: error: Unable to allocate resources: Requested node configuration is not available

To solve this error, simply avoid requesting more than 2 GPUs, and
remember to include the ``--partition`` option. See also the
:ref:`p_usage_slurm_gpu` section.

``srun`` fails with ``/bin/slurm_bcast_123456.0_esrumcmpn01fl: No such file or directory``
==========================================================================================

If you accidentally specify a folder as the first component of an
``srun`` command, then Slurm will fail with an error message complaining
that a ``slurm_bcast_*`` executable in that folder could not be found,
where the executable name contains the job ID and the node on which it
was run:

.. code-block::

   $ srun --pty /bin/
   slurmstepd: error: execve(): /bin/slurm_bcast_123456.0_esrumcmpn01fl: No such file or directory
   srun: error: esrumcmpn01fl: task 0: Exited with exit code 2

To fix this, ensure that you are running an executable and not a folder:

.. code-block::

   $ srun --pty /bin/bash

.. note::

   This failure relates to the ``--bcast`` option, that allow you to
   copy an executable from the head node to a folder on the node on
   which the job is executed. This is typically not required on Esrum,
   since all home, project, and dataset folders are shared across nodes.

X11 forwarding not working in MobaXterm
=======================================

Firstly right-click on ``Esrum`` in the list of ``User sessions`` and
select ``Edit session``. Make sure that the ``Advanced SSH settings``
tab is open and verify that X11 forwarding is enabled as shown:

.. image:: /usage/slurm/images/mobaxterm_x11_session.png
   :align: center

Secondly, press the ``OK`` button and open the ``Settings`` via the
gears icon on the main toolbar. Then select the ``X11`` tab and verify
that X11 support is configured as shown:

.. image:: /usage/slurm/images/mobaxterm_x11_settings.png
   :align: center
