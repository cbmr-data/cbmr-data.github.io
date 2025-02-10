.. _p_overview:

#####################
 Overview of cluster
#####################

The Esrum cluster is a cluster managed by the `Data Analytics Platform`_
(formerly the Phenomics Platform) at CBMR_. Hosting and technical
support is handled by UCPH-IT_.

In addition to the documentation provided here, UCPH-IT also provides
documentation for the `UCPH computing/HPC Systems`_ on KUnet.

**************
 Architecture
**************

The cluster consists of a head node, 12 compute nodes, 1 GPU /
high-memory node, 2 GPU nodes, 2 :ref:`RStudio <s_service_rstudio>` web
servers, and 1 server for running containers. A :ref:`p_usage_shiny`
server managed by UCPH-IT is also available.

Users connect to the "head" node, from which jobs can be submitted to
the individual compute nodes using the Slurm_ Workload Manager:

+----+--------------------+------+-------------------------+---------------------+-----------------------------------+
|    | Node               | RAM  | CPUs                    | GPUs                | Name(s)                           |
+====+====================+======+=========================+=====================+===================================+
| 1  | Head               | 2 TB | 2x24 core AMD EPYC 7413 |                     | *esrumhead01fl*                   |
+----+--------------------+------+-------------------------+---------------------+-----------------------------------+
| 12 | Compute            | 2 TB | 2x32 core AMD EPYC 7543 |                     | *esrumcmpn01fl* - *esrumcmpn12fl* |
+----+--------------------+------+-------------------------+---------------------+-----------------------------------+
| 1  | GPU / high-memory  | 4 TB | 2x32 core AMD EPYC 75F3 | 2x NVIDIA A100 80GB | *esrumgpun01fl*                   |
+----+--------------------+------+-------------------------+---------------------+-----------------------------------+
| 2  | GPU                | 2 TB | 2x32 core AMD EPYC 9354 | 2x NVIDIA H100 80GB | *esrumgpun03fl*, *esrumgpun04fl*  |
+----+--------------------+------+-------------------------+---------------------+-----------------------------------+
| 2  | Rstudio            | 2 TB | 2x32 core AMD EPYC 7543 |                     | *esrumweb01fl*, *esrumweb02fl*    |
+----+--------------------+------+-------------------------+---------------------+-----------------------------------+
| 1  | Container*         | 2 TB | 2x32 core AMD EPYC 7543 |                     | *esrumcont01fl*                   |
+----+--------------------+------+-------------------------+---------------------+-----------------------------------+

\* *The container node is made available as a compute node when not in
use.*

**********
 Software
**********

The nodes all run Red Hat Enterprise Linux 8 and a range of scientific
and other software is made available using :ref:`environment modules
<p_usage_modules>`. Missing software can be requested via UCPH-IT.

**************************
 Projects and data-shares
**************************

Access is managed on a per-project level, and is administrated by the
individual project owners, with each project folder containing a
standard set of sub-folders (``apps``, ``data``, ``people``,
``scratch``).

Datasets used by several projects may be made available via read-only
network shares. As with projects, access is administered by the data
owner.

See the respective pages for :ref:`accessing <p_usage_access_applying>`
existing projects/data-shared and for :ref:`creating <p_usage_projects>`
new projects/data-shared.

****************************
 Backup policies and quotas
****************************

Your ``/home`` folder and the ``apps``. ``data``, and ``people`` folders
in projects are automatically backed up. The ``scratch`` folders are NOT
backed up. The specific frequency and duration of backups differ for
each type of folder and may also differ for individual projects.

As a rule, folders for projects involving GDPR protected data (indicated
by the project name ending with ``-AUDIT``) is subject to more frequent
backups. However, on-site backups are kept for a shorter time to prevent
the unauthorized recovery of intentionally deleted data.

See :ref:`p_usage_filesystem` for more information.

**********************
 Additional resources
**********************

-  Official `UCPH computing/HPC Systems`_ documentation on KUnet.

.. _cbmr: https://cbmr.ku.dk/

.. _data analytics platform: https://cbmr.ku.dk/research-facilities/data-analytics/

.. _environment modules: https://modules.readthedocs.io/en/latest/

.. _slurm: https://slurm.schedmd.com/

.. _ucph computing/hpc systems: https://kunet.ku.dk/work-areas/research/Research%20Infrastructure/research-it/ucph-computing-hpc-systems/Pages/default.aspx

.. _ucph-it: https://it.ku.dk
