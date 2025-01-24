###############################
 The Esrum HPC cluster at CBMR
###############################

.. toctree::
   :hidden:

   contact
   overview
   guidelines
   troubleshooting

.. toctree::
   :hidden:
   :caption: Using the cluster

   usage/access/access
   usage/access/connecting
   usage/filesystem
   usage/slurm/index
   usage/modules
   usage/transfers

.. toctree::
   :hidden:
   :caption: Resources

   resources/cohorts

..
   resources/common

.. toctree::
   :hidden:
   :caption: Other services

   services/r
   services/jupyter
   services/containers
   services/shiny

.. toctree::
   :hidden:
   :caption: Tips and tricks

   tips/modules
   tips/tmux
   tips/batching_commands
   tips/robust_scripts
   tips/snakemake

.. toctree::
   :hidden:
   :caption: Outreach

   communications/messages
   communications/presentations

Welcome to the Esrum high-performance computing (HPC) cluster at The
Novo Nordisk Foundation Center for Basic Metabolic Research (CBMR_). The
Esrum cluster is managed by the `Data Analytics Platform`_ (formerly the
Phenomics Platform) and is available to employees at CBMR as well as
collaborators visiting CBMR.

You are always welcome to :ref:`contact us <p_contact>` if you have
questions or problems relating to the cluster, cohorts, other services
or resources provided by the platform.

We kindly ask that you acknowledge the use of services or resources
provided by the Data Analytics Platform. See :ref:`p_guidelines` for
more information.

.. note::

   This documentation assumes some familiarity with using Linux and bash
   (the default command-line). Users who lack this familiarity may
   benefit from taking the `Mastering the terminal with Bash and Unix`_
   course offered by the Center for Health Data Science (HeaDS_) at
   SUND. If you intend to make use of R or the RStudio servers, then you
   may also benefit from the `From Excel to R`_ offered by HeaDS.

*****************
 Getting started
*****************

We hold an intro-workshop for the Esrum cluster a few times a year,
based on interest, so please :ref:`let us know <p_contact>` if you'd
like to attend a workshop. Future workshops will be announced to all
employees at CBMR, while slides from past workshops are made available
on the :ref:`presentations <p_outreach_presentations>` page.

However, this documentation is explicitly written to help you get
started with using Esrum, so you do not need to wait for the intro
workshop to be announced:

-  Before you continue, please read our :ref:`p_guidelines`. You are
   expected our guidelines while using the Esrum cluster.

-  To get access to Esrum, you must first apply for access as described
   in :ref:`p_usage_access_applying`. Once you have access, you can
   connect to the cluster as described in :ref:`connecting to the
   cluster <p_usage_connecting>` page.

-  Connecting to Esrum gives you access to your personal home folder and
   to project and data set folders as described in
   :ref:`p_usage_filesystem`.

-  Users of Esrum have access to a large library of scientific and other
   software. This software is available via environment modules as
   described in :ref:`p_usage_modules`.

-  To run this or other software on Esrum, you must make use of the
   Slurm_ queuing system as described in :ref:`p_usage_slurm`.

-  Finally, :ref:`p_transfers` describes how to transfer your data to
   and from Esrum, to and from services like SIF and Computerome.

In addition, this documentation contains an overview of the
:ref:`cluster architecture and features <p_overview>`, describes the
various other services accessible as part of the HPC cluster, such as
:ref:`Rstudio servers <p_service_r>`, :ref:`Shiny servers
<p_usage_shiny>`, and :ref:`persistent podman containers
<p_containers>`.

.. _cbmr: https://cbmr.ku.dk/

.. _creative commons cc-by 4.0 license: https://creativecommons.org/licenses/by/4.0/

.. _data analytics platform: https://cbmr.ku.dk/research-facilities/data-analytics/

.. _from excel to r: https://heads.ku.dk/course/from-excel-to-r/

.. _heads: https://heads.ku.dk/

.. _mastering the terminal with bash and unix: https://heads.ku.dk/course/unix_bash_terminal/

.. _slurm: https://slurm.schedmd.com/overview.html

.. _ucph computing/hpc systems: https://kunet.ku.dk/work-areas/research/Research%20Infrastructure/research-it/ucph-computing-hpc-systems/Pages/default.aspx
