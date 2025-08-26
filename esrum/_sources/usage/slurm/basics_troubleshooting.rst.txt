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


X11 forwarding is working in MobaXterm
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
