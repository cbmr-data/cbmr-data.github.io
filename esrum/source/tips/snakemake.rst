.. _p_tips_snakemake:

##########################
 Using Snakemake on Esrum
##########################

This page describes how to best use Snakemake on the Esrum cluster. As
this includes a number of suggested settings (described below), a basic
profile file is provided below to automatically set these.

Snakemake can either be run directly, where all rules (*i.e.* tasks) are
run on the same system as Snakemake itself, or Snakemake can be
configured to use Slurm to run the individual rules, allowing these to
be run on any compute node on Esrum. The choice between the two options
boils down to the following considerations:

-  If the steps in your Snakemake pipeline are very short, then you
   should run your pipeline *in* a regular ``sbatch`` script, via
   ``srun``, or *in* an interactive session. This is because Slurm adds
   some overhead to jobs, which for very short rules may result in a
   significant increase in the total runtime.

-  If your steps run for a longer time or take up significant amount of
   resources, then you should enable Slurm support when running your
   pipeline. This ensures that you only reserve resources for your rules
   *while* they are running and enables you to run more rules
   simultaneously than can fit on one compute node.

-  If any of your rules make use of GPUs, then you *must* enable Slurm
   support when running Snakemake. This ensures that GPUs are *only*
   reserved while they are actively being used, which we require since
   GPUs are a very limited resource on Esrum. See below for how to
   reserve GPUs for your rules.

For most bioinformatics pipelines, the most efficient choice is to run
Snakemake with Slurm support enabled.

**************************************
 Running Snakemake with Slurm support
**************************************

To run Snakemake with Slurm support enabled, simply pass the options
``--slurm`` and ``--jobs N``, where the ``N`` is the maximum number of
jobs you want to queue simultaneously. For example,

.. code-block:: console

   $ module load snakemake/7.30.1
   $ snakemake --slurm --jobs 32

This command will run your pipeline via Slurm and queue at most 32 jobs
at once. Note that we do not need to specify the maximum number of CPUs
(via ``--cores``), since Slurm will take care that (see below).

Note also that you *must* run Snakemake on the head node when using the
``--slurm`` option. This is required for Snakemake to be able to
interact with Slurm. Furthermore, you *should* be running it a ``tmux``
or ``screen`` session to ensure that Snakemake keeps running after you
log out. See the :ref:`p_tips_tmux` page for more information.

.. note::

   Some older tutorials may suggest setting Slurm options via the
   ``--cluster`` option. However, with modern versions of Snakemake it
   is sufficient to add ``--slurm`` when running Snakemake and that is
   the method we recommend using.

Requesting CPUs
===============

Snakemake will automatically request a number of CPUs corresponding to
the number of threads used by a rule:

.. code-block:: python
   :linenos:

   rule my_rule:
       input: ...
       output: ...
       threads: 8

Snakemake will in other words reserve 8 CPUs for the above rule when
submitting it through Slurm.

Requesting memory
=================

Snakemake will by default estimate the amount of memory needed for a
rule based on the size of the input data (``max(2*input.size_mb,
1000)``), which translates to two times the size of the input but no
less than 1000 MB.

This is, however, frequently less than the Slurm default of ~16 GB per
CPU reserved, and we therefore recommend overriding this default using
the ``--default-resources`` option:

.. code-block:: console

   $ snakemake --default-resources mem_mb_per_cpu=15948

This corresponds to the behavior of ``sbatch`` and ``srun``.

Should a job require more memory than the default ~16 GB per CPU, then
you can request additional memory using the ``resources`` section of
your rule:

.. code-block:: python
   :linenos:

   rule my_rule:
       input: ...
       output: ...
       resources:
           mem_mb: 64 * 1024

The ``mem_mb`` specifies a *total* amount of memory to reserve in MB and
the above example therefore requests 64 GB for this specific rule.

Using the GPU / high-memory nodes
=================================

Running a job on the GPU / high-memory nodes is accomplished by
specifying that you want to use the ``gpuqueue`` by adding
``slurm_partition="gpuqueue"`` to the ``resources`` section of your
rule. Once you have done so, you can reserve GPUs using the
``slurm_extra`` resource:

.. code-block:: python
   :linenos:

   rule gpu_example:
       input: "my_input.dat"
       output: "my_output.dat"
       shell: "my-command {input} > {output}"
       resources:
           # Run this rule on the GPU queue
           slurm_partition="gpuqueue",
           # Reserve 1 GPU for this job
           slurm_extra="--gres=gpu:1",

If you need memory rather than GPUs, then omit the ``slurm_extra``
resource and instead specify the amount of RAM needed in MB, using the
``mem_mb`` resource as described above:

.. code-block:: python
   :linenos:

   rule high_mem_example:
       input: "my_input.dat"
       output: "my_output.dat"
       shell: "my-command {input} > {output}"
       resources:
           # Run this rule on the GPU queue
           slurm_partition="gpuqueue",
           # Reserve 3 TB of memory (specified in MB)
           mem_mb=3 * 1024 * 1024,

.. warning::

   Do *not* reserve GPUs if you do not need to use them; we only have a
   few GPUs, so we will terminate jobs found to be unnecessarily
   reserving GPU resources.

***************************
 Using environment modules
***************************

Snakemake can automatically load environment required by a rule. This
requires either that the ``--use-envmodules`` option is specified on the
command-line or that ``use-envmodules`` is set to ``true`` in your
profile (see below). When that is done, Snakemake will automatically
load the environment modules listed in the ``envmodules`` section of a
rule:

.. code-block:: python
   :linenos:

   rule my_rule:
       input: "my_input.bam"
       output: "my_output.stats.txt"
       shell: "samtools stats {input} > {output}"
       envmodules:
           "libdeflate/1.18",
           "samtools-libdeflate/1.18",

.. tip::

   Remember to specify version numbers for the module you are using;
   this helps ensures that your analyses are reproducible and that they
   won't suddenly break when new versions of modules are added.

***************************
 Other recommended options
***************************

This section describes a handful of settings that we recommend using:

-  ``--latency-wait 60``: This option increases the length of time
   snakemake will wait for missing output files to appear. This is
   required when using ``--slurm`` since a job will be running on a
   different node than snakemake itself and since it may take some
   amount of times for files to propagate over the network file system.

-  ``--rerun-incomplete``: This option ensures that snakemake reruns
   jobs that were not run to completion.

The profile below enables you to automatically set these options.

*******************
 Snakemake profile
*******************

The recommended profile is also available at
``/projects/cbmr_shared/apps/config/snakemake/latest``. This is a
symlink pointing to the latest version of the profile

.. code-block:: yaml
   :linenos:

   # Maximum number of jobs to queue at once
   jobs: 32
   # Use slurm for queuing jobs
   slurm: true

   # (Optional) Enable the use of environmental modules
   use-envmodules: true
   # Wait up to 60 seconds for the network file system
   latency-wait: 60
   # Re-run incomplete jobs
   rerun-incomplete: True

   # Standard slurm resources; these match the `sbatch` defaults:
   default-resources:
     # Use standard queue by default (silences warning)
     - "slurm_partition=standardqueue"
     # Same mem-per-CPU as Slurm defaults
     - "mem_mb_per_cpu=15948"
     # (Optional) Runtime limit in minutes to catch jobs that hang
     #- "runtime=720"

This profile is also available at
``/projects/cbmr_shared/apps/config/snakemake/``.

To make use of the profile, run Snakemake with the ``--profile``
argument and the location of the folder containing your profile:

.. code-block:: console

   $ snakemake --profile /projects/cbmr_shared/apps/config/snakemake/latest

Options specified in this profile can be overridden on the command-line
simply by specifying the option again:

.. code-block:: console

   $ snakemake --profile /projects/cbmr_shared/apps/config/snakemake/latest --jobs 16

*****************
 Troubleshooting
*****************

.. include:: snakemake_troubleshooting.rst
