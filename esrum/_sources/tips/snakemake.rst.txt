.. _p_tips_snakemake:

##########################
 Using Snakemake on Esrum
##########################

This page describes how to best use Snakemake on the Esrum cluster. As
this suggests setting a number of options (described below), a basic
profile file is provided below to automatically set these.

Snakemake must either be run in a Slurm job or Snakemake must be
configured to run the individual rules in the ``Snakefile`` via Slurm as
described below.

**********************************
 Running snakemake jobs via Slurm
**********************************

The recommended way to use Snakemake with Slurm is to use the
``--slurm`` and ``--jobs N`` options, where the ``N`` is the maximum
number of jobs you want to queue simultaneously:

.. code::

   $ module load snakemake/7.30.1
   $ snakemake --slurm --jobs 32

This command will queue at most 32 jobs on Slurm. Note that we do not
need to specify the maximum number of CPUs (via ``--cores``), since
Slurm will take care that.

.. note::

   Some older tutorials may suggest setting Slurm options via the
   Snakemake ``--cluster`` option and similar. However, with modern
   versions of Snakemake it is sufficient to add ``--slurm`` when
   running Snakemake and that is the method we recommend using.

Running Snakemake with ``--slurm`` has a number of advantages over
running Snakemake in a Slurm job (via ``sbatch`` or ``srun``) or in an
interactive session on a compute node:

-  Resources are only reserved for the duration of individual rules,
   meaning other jobs (yours and those of other users) can make use of
   those resources.

-  Your can run more jobs simultaneously than can fit on a single
   compute node.

-  You can run a mix of jobs that require GPUs and jobs that do not
   require GPUs.

However, there are also some disadvantages:

-  Running a rule via Slurm adds some overhead, which may result in a
   significant increase in the runtime for very brief rules.

-  Rules queued via Slurm are not necessarily terminate if you stop
   snakemake, meaning that you may have to terminate these yourself. See
   the :ref:`p_usage_slurm_basics` page for information about how to
   query and scancel running/queued jobs on Slurm.

Requesting CPUs
===============

Snakemake will automatically request a number of CPUs corresponding to
the number of threads used by a rule:

.. code:: python

   rule my_rule:
       input: ...
       output: ...
       threads: 8

Snakemake will in other words reserve 8 CPUs for the above rule when
submitting it through Slurm.

Requesting memory
=================

Snakemake will by default estimate the amount of memory needed for a
rule as a function of the input data (``max(2*input.size_mb, 1000)``),
corresponding to two times the size of the input but no less than 1000
MB.

This is, however, frequently less than the Slurm default of ~16 GB per
CPU reserved, and we therefore recommend overriding this default using
the ``--default-resources`` option:

.. code:: console

   snakemake --default-resources mem_mb_per_cpu=15948

This corresponds to the behavior of ``sbatch`` and ``srun``.

Should a job require more memory than the default ~16 GB per CPU, then
you can request additional memory using the ``resources`` section of
your rule:

.. code:: python

   rule my_rule:
       input: ...
       output: ...
       resources:
           mem_mb: 65536

The ``mem_mb`` specifies a *total* amount of memory to reserve in MB and
the above example therefore requests 64 GB for this specific rule.

Using the GPU/high-MEM queue
============================

Running a job on the GPU/high-MEM is accomplished by specifying that you
want to use the ``gpuqueue`` by adding ``slurm_partition="gpuqueue"`` to
the ``resources`` section of your rule. Once you have done so, you can
reserve GPUs as shown below:

.. code:: python

   rule gpu_example:
       input: "my_input.dat"
       output: "my_output.dat"
       shell: "my-command {input} > {output}"
       resources:
           # Run this task on the GPU queue
           slurm_partition="gpuqueue",
           # Reserve 1 GPU for this job
           slurm_extra="--gres=gpu:1",

If you need memory rather than GPUs, then you specify the amount needed
in MB using the ``mem_mb`` resource as described above:

.. code:: python

   rule high_mem_example:
       input: "my_input.dat"
       output: "my_output.dat"
       shell: "my-command {input} > {output}"
       resources:
           # Run this task on the GPU queue
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

.. code:: python

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
   wont suddenly break when new versions of modules are added.

***************************
 Other recommended options
***************************

This section describes a handful of settings that

-  ``--latency-wait 60``: This option increases the length of time
   snakemake will wait for missing output files to appear. This is
   required when using ``--slurm`` since a job will be running on a
   different node than snakemake itself and since it may take some
   amount of times for files to propagate over the network filesystem.

-  ``--rerun-incomplete``: This option ensures that snakemake reruns
   jobs that were not run to completion.

The profile below enables you to automatically set these options.

*******************
 Snakemake profile
*******************

The recommended profile is also available at
``/projects/cbmr_shared/apps/config/snakemake/latest``. This is a
symlink pointing to the latest version of the profile

.. code:: yaml

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

.. code:: console

   $ snakemake --profile /projects/cbmr_shared/apps/config/snakemake/latest

Options specified in this profile can be overridden on the command-line
simply by specifying the option again:

.. code:: console

   $ snakemake --profile /projects/cbmr_shared/apps/config/snakemake/latest --jobs 16
