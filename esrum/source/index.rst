###############################
 The Esrum HPC cluster at CBMR
###############################

.. toctree::
   :hidden:

   Front page <self>
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
   usage/transfers/index

.. toctree::
   :hidden:
   :caption: Resources

   resources/cohorts
   resources/common

.. toctree::
   :hidden:
   :caption: Other services

   services/rstudio
   services/networkdrives
   services/jupyter
   services/containers
   services/shiny

.. toctree::
   :hidden:
   :caption: Tips and tricks

   tips/ports
   tips/modules
   tips/tmux
   tips/batching_commands
   tips/robust_scripts
   tips/snakemake
   tips/r

.. toctree::
   :hidden:
   :caption: Outreach

   communications/messages
   communications/presentations

Welcome to the Esrum high-performance computing (HPC) cluster at The
Novo Nordisk Foundation Center for Basic Metabolic Research (CBMR_).
Esrum is managed by the `Data Analytics Platform`_ (DAP), and is
available to all employees at CBMR and their collaborators.

In addition to the Esrum HPC cluster, the platform also provides two
:ref:`RStudio <p_service_rstudio>` servers, access to more than 80
:ref:`human cohorts <p_human_cohorts>`, a `project registry`_ for
tracking your projects at CBMR, and `open source tools and pipelines`_.
We kindly ask that you acknowledge the use of services and resources
that we provide. See the :ref:`acknowledgements <s_acknowledgements>`
section on the :ref:`p_guidelines` page for more information.

You are also always welcome to :ref:`contact us <p_contact>` if you have
questions or problems relating to the cluster, cohorts, other services
or resources provided by the platform. Additionally, we will gladly
assist with general bioinformatics issues.

*****************
 Getting started
*****************

We hold intro-workshops for Esrum based on interest, so please :ref:`let
us know <p_contact>` if you'd like to attend; upcoming workshops are
announced to all employees at CBMR. Slides from past workshops are
available via the :ref:`presentations <p_outreach_presentations>` page.

However, this documentation is explicitly written to help you get
started with using Esrum, so you do not need to wait for the next intro
workshop to use Esrum:

#. Please read the :ref:`p_guidelines` for using Esrum before you
   continue.

#. To get access to Esrum and related resources, please see the
   :ref:`p_usage_access_applying` page

#. Once your request has been approved, you can connect to the cluster
   as described in the :ref:`connecting to the cluster
   <p_usage_connecting>` page.

#. On Esrum, you'll find your home folder, datasets, projects, and
   network drives laid out as described on the :ref:`p_usage_filesystem`
   page.

#. Users of Esrum have access to a large library of software provided by
   DAP and UCPH-IT. The :ref:`p_usage_modules` page describes how to
   access this software, and how to request software that is not
   currently available.

#. To run software on Esrum, you must make use of the Slurm_ queuing
   system as described in :ref:`p_usage_slurm`.

#. Finally, the :ref:`p_transfers` page describes how to transfer your
   data to and from Esrum, and to and from services like SIF or
   Computerome.

See the Table of Content for various other services, tips and trips for
using Esrum, and more.

.. tip::

   This documentation assumes some familiarity with using Linux and bash
   (the default command-line). Users who lack this familiarity may
   benefit from taking the `Mastering the terminal with Bash and Unix`_
   course offered by the Center for Health Data Science (HeaDS_) at
   SUND. If you intend to make use of `R <p_tips_r>`_ or the `RStudio
   <p_service_rstudio>`_ servers, then you may also benefit from the
   `From Excel to R`_ and `R for Data Science`_ courses.

.. _cbmr: https://cbmr.ku.dk/

.. _creative commons cc-by 4.0 license: https://creativecommons.org/licenses/by/4.0/

.. _data analytics platform: https://cbmr.ku.dk/research-facilities/data-analytics/

.. _from excel to r: https://heads.ku.dk/course/from-excel-to-r/

.. _heads: https://heads.ku.dk/

.. _mastering the terminal with bash and unix: https://heads.ku.dk/course/unix_bash_terminal/

.. _open source tools and pipelines: https://github.com/cbmr-data/

.. _project registry: https://cbmrcat.unicph.domain/projects/

.. _r for data science: https://heads.ku.dk/course/r4ds/

.. _slurm: https://slurm.schedmd.com/overview.html

.. _ucph computing/hpc systems: https://kunet.ku.dk/work-areas/research/Research%20Infrastructure/research-it/ucph-computing-hpc-systems/Pages/default.aspx
