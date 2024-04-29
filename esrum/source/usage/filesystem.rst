.. _p_usage_filesystem:

##################################
 Projects, data, and home folders
##################################

This section describes the layout of your home folder on Esrum, as well
as the location and layout of projects and data-shares.

.. warning::

   Every folder described below is located on a network drive, except
   for the per-node ``/scratch`` folders. A consequence of this is that
   a file created on one node may not be visible on other nodes until
   some time later. This typically takes in the order of 10-20 seconds
   depending on the network load.

.. _s_home_folder:

******************
 Your home folder
******************

Your home folder can hold 100GB of data and is meant to store your
personal programs and related caches, configuration files, and similar
files that are not related to your projects.

We recommended that you to keep your non-project related scripts and
other such files in your group project folder. Project folders are
preserved even after you have left CBMR, so any scripts or other files
that your colleagues may depend on should be stored there.

.. warning::

   Only you have access to your home folder! Do **not** put project
   related files or anything else your colleagues may depend on in your
   home folder!

.. tip::

   You can check the remaining capacity in your home folder using the
   ``df -h ~`` command.

KU network drives
=================

When you login to Esrum for the first time, your home folder should
contain a single folder named ``ucph``. This folder in turn contains
your KU network drives (formerly ``H:`` and ``N:``).

.. warning::

   Note that these drives are only accessible from the head node. If you
   need to analyze data located on either of these shared drives, then
   you will need to copy it an appropriate projects folder.

   Note furthermore that access to these folders will not be available
   if you login using Kerberos (GSSAPI). See the
   :ref:`p_usage_connecting` page for instructions for how to disable
   this feature if you are using MobaXterm.

.. _s_project_folders:

**********************
 Your project folders
**********************

The majority of your work on Esrum should take place in project folder
corresponding either to your research group or to actual projects. This
ensures that your collaborators can access your results and that nobody
else can!

Project folders are located in the ``/projects`` folder:

.. code::

   $ ls -1 /projects
   phenomics-AUDIT
   genotyping
   ...

The ``-AUDIT`` suffix indicates that the phenomics project has been
configured for work on GDPR data. All work on GDPR data should take
place in project or data-shares (see below) marked with ``-AUDIT`` and
*nowhere else*!

To apply for access to a specific project follow the instructions in the
:ref:`s_applying_for_access` section, using the name of the project in
the form ``COMP-PRJ-genotyping``, replacing ``genotyping`` with the name
of your project.

Projects folder always contain the following four sub-folders:

-  ``/projects/<project-name>/people``

   Every member of a project has their own folder in ``people``. It is
   suggested that you keep your scripts, configuration files,
   documentation, and the like in this folder. The ``people`` folder is
   automatically backed up every day.

-  ``/projects/<project-name>/apps``

   The apps folder is intended for storing software shared between
   project members. See :ref:`p_tips_modules` for how to setup a shared
   repository of software that can be used with the module system. The
   ``apps`` folder is automatically backed up every day.

-  ``/projects/<project-name>/data``

   The ``data`` folder is intended for datasets shared between project
   members. This could be your raw data or your results files from
   processing your raw data. The ``data`` folder is automatically backed
   up every day.

-  ``/projects/<project-name>/scratch``

   The ``scratch`` folder is intended for temporary files, as it is
   *not* backed up. It is also suitable for other files that do not need
   to be backed up, including for example publicly available datasets,
   large index files, and such.

Unlike your ``/home`` folder, there are no limits on how much you store
in these folders.

*****************
 Scratch folders
*****************

Every node on esrum (including the head node) has a 1.5-3 TB scratch
drive available at ``/scratch``. This is intended for short-lived
temporary files generated as part of jobs running on the cluster, and
can provide a significant performance benefit if a job for example
writes a lot of small temporary files.

.. note::

   Note that unlike your home folder, ``/projects``, and ``/datasets``,
   the ``/scratch`` folders are physically located on each node. Files
   written to ``/scratch`` on one node are therefore *not* accessible on
   other nodes.

It is recommended that you create a sub-folder containing your KU-IT
username when using the scratch-drive as part of your scripts:

.. code:: console

   # Create temporary folder in the form /scratch/abc123
   mkdir -p "/scratch/${USER}"
   # Some software use the TMPDIR to place temporary files
   export TMPDIR="/scratch/${USER}"
   # Other software has options for where to place temporary files
   mysoftware --in "mydata" --out "myresults" --temp "/scratch/${USER}"

.. warning::

   The scratch-drives have limited capacity and are *only* intended for
   short-lived, temporary files. Do not use it to store results and
   please remember to clean up after your jobs. Files left on the
   scratch-drive *will* be deleted.

*********
 Backups
*********

Backups are available your home folder and in project folders ``/apps``,
``/data``, and ``/people`` via special hidden ``.snapshot`` folders in
the root of each of these folders. For example, to access the snapshots
of the ``/data`` folder in the project ``phenomics``:

.. code:: shell

   $ cd /projects/phenomics/data/.snapshot
   $ ls
   42-Research-hourly-7D-2023-09-01_02:00
   42-Research-daily-30D-2023-09-02_02:00
   42-Research-weekly-104W-2023-09-03_02:00

Each timestamped folder contains a full snapshot of the parent folder
(``/home``, ``/apps``, etc.) and you can copy data from these snapshots
should you need to restore deleted or modified files.

Snapshots of audited projects are only accessible for a limited time and
you may therefore need to contact KU-IT to restore deleted data for such
projects.

.. warning::

   Please contact KU-IT should you need to restore a large amount of
   deleted data.

.. _red hat enterprise linux: https://en.wikipedia.org/wiki/Red_Hat_Enterprise_Linux

.. _slurm: https://slurm.schedmd.com/overview.html
