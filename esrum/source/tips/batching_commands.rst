.. _p_tips_batching:

###########################
 Batching commands in bash
###########################

This section describes way to batch commands without using Slurm. This
is intended to be used both with singular jobs and in conjunction with
Slurm job arrays (see the :ref:`s_job_arrays` section), for example when
you need to run a large number of small jobs.

Running tasks as described on this page has a lower overhead than jobs
scheduled tasks via Slurm, and is therefore well suited for running
many, small tasks. However, for larger jobs you should still prefer job
arrays if possible.

This section covers basic loops in bash and the `parallel` command.
Other options include xargs_, make_, snakemake_, and much, much more.

***************************************
 Running commands sequentially in bash
***************************************

If you need to run a number of (very) short running commands, then it is
likely more efficient to do so with a simple loop in your ``sbatch``
script. For example, this script runs the ``plonk`` command on a number
of population VCF files:

.. code-block:: bash

   #!/bin/bash
   module load plonk/3.14

   for pop in CHB FIN GBR JPT PUR YRI; do
     plonk --input "./my_data/${pop}.vcf" --output "./my_results/${pop}.out"
   done

The following command indexes a number of (small) BAM files in the
current directory:

.. code-block:: bash

   #!/bin/bash
   module load samtools/1.17

   for filename in ./*.bam; do
     samtools index ${filename}
   done

However, it is important to remember that the total runtime will be the
*sum* of run-times for each task, since they are run one after the
other. It is therefore not recommended to use loops like this for
commands that take more than a few of minutes to complete!

**************************************
 Running commands in parallel in bash
**************************************

The GNU parallel_ commands offers a range of options for running
commands in parallel.

.. code-block:: bash

   #!/bin/bash
   module load plonk/3.14
   module load parallel/20230822

   parallel -P ${SLURM_CPUS_PER_TASK} \
     plonk --input "./my_data/{}.vcf" --output "./my_results/{}.out" \
     ::: CHB FIN GBR JPT PUR YRI

The ``parallel`` command will then execute ``plonk`` once for each of
the values we specified after the ``:::`` and replace the text ``{}``
with the current value.

The second ``xargs`` example above can be run in parallel as follows:

.. code-block:: bash

   #!/bin/bash
   module load samtools/1.17
   module load parallel/20230822

   parallel -P ${SLURM_CPUS_PER_TASK} \
     samtools index "{}" \
     ::: ./*.bam

If no ``{}`` is specified the value will be appended to the command.
Additionally, ``parallel`` can read values from STDIN, meaning that the
above could also be written as

.. code-block:: bash

   #!/bin/bash
   module load samtools/1.17
   module load parallel/20230822

   ls ./*.bam | parallel -P ${SLURM_CPUS_PER_TASK} samtools index

Each line on STDIN is treated as one value.

Best practices for reserving resources
======================================

Note that when you reserve resources for a job using ``parallel`` that
you generally should not reserve enough cores to run all jobs at once.
This is because tasks are likely to take different amount of times to
run, sometimes significantly so, resulting in a (potentially large)
number of CPUs being idle until the last task has finished.

For this reason we advise that you do not reserve more CPUs than what is
needed to run 1/3 to 1/2 of your jobs at once. This also allows you to
queue that many more simultaneous jobs on Slurm, and will typically
result in a overall greater throughput than simply using the maximum
number of processes with ``parallel``.

Using the ``plonk`` example from above:

.. code-block:: bash

   #!/bin/bash
   module load plonk/3.14
   module load parallel/20230822

   parallel -P ${SLURM_CPUS_PER_TASK} \
     plonk --input "./my_data/{}.vcf" --output "./my_results/{}.out" \
     ::: CHB FIN GBR JPT PUR YRI

Let's say that ``plonk`` is able to use multiple threads and that I
decide to use 4 threads per process. In that case, I could reserve 12
threads for my job and then run 3 instances of ``plonk`` using
``parallel``.

.. code-block:: bash

   #!/bin/bash
   #SBATCH --cpus-per-task=12
   module load plonk/3.14
   module load parallel/20230822

   parallel -P 3 \
     plonk --threads 4 --input "./my_data/{}.vcf" --output "./my_results/{}.out" \
     ::: CHB FIN GBR JPT PUR YRI

This however has the disadvantage that you have to make sure that
``--cpus-per-task``, ``-P``, and ``--threads`` (or whatever option your
software uses) all line up.

.. _make: https://www.gnu.org/software/make/

.. _parallel: https://www.gnu.org/software/parallel/

.. _snakemake: https://snakemake.readthedocs.io/

.. _xargs: https://man7.org/linux/man-pages/man1/xargs.1.html
