:orphan:

.. _p_tips_snakemake:

#################
 Using Snakemake
#################

This page describes ways to use Snakemake on the esrum cluster.

**********************************
 Running snakemake jobs via Slurm
**********************************

***************************
 Using environment modules
***************************

***************************************
 Limiting simultaneously running nodes
***************************************

*******************
 Suggested profile
*******************

.. code:: ini

   # Enable task execution using Slurm
   slurm: true
   # The maximum number of simultaneous jobs submitted to Slurm
   jobs: 16
   # Enable environment modules
   use-envmodules: true
   default-resources:
     # Use default mem per CPU (~15 GB)
     - "mem_mb_per_cpu=None"
     # Use standard (non-GPU) queue by default;
     # this is not required, but shuts up a warning
     - "slurm_partition=standardqueue"
   # Wait up to 60 seconds for files saved on the shared file system;
   # this is done to prevent Snakemake from failing if the network file-
   # system is loaded
   latency-wait: 60
   # Re-do incomplete tasks
   rerun-incomplete: True
