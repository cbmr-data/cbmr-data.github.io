.. _p_usage_filesystem:

#######################
 Data storage on Esrum
#######################

.. toctree::
   :hidden:

   projects

This section describes the layout of your home folder on Esrum, as well
as the location and layout of projects, shared datasets, and per-node
"scratch" folders. Briefly, the file system looks as follows:

.. code-block:: text

   /home/
     abc123/
       ucph/
         hdir/
         ndir/
         sdir/
   /projects/
     my-project/
       apps/
       data/
       people/
       scratch/
     my-human-project-AUDIT/
       ...
   /datasets/
     my-dataset/
     my-human-dataset-AUDIT/
   /scratch/

When you are first given access to Esrum, you will by default have
access to your home folder, the scratch folders on each node, and the
CBMR wide project folder (``/projects/cbmr_shared``). Please see the
:ref:`p_usage_access_applying` page for information about applying for
access to additional projects and datasets.

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

Your home folder can hold 100 GB of data and is meant to store your
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

.. _s_ucph_network_drives:

UCPH network drives (``H:``, ``N:``, and ``S:``)
================================================

The "old" UCPH network drives are available in your home folder under
the ``ucph`` subfolder:

-  ``H:`` as ``~/ucph/hdir``.
-  ``N:`` as ``~/ucph/ndir``.
-  ``S:`` as ``~/ucph/sdir``.

By default, these network drives are only accessible from the head node,
and access is furthermore limited to about 10 hours after you logged in.
Additionally, these drives may not be available if you do not log in by
typing your password.

For more information, including instructions on how to make these drives
accessible (again) on other nodes, see the :ref:`p_network_drives` page.

.. tip::

   You can also access your network drives online via
   https://webfile.ku.dk/.

.. _s_project_folders:

*****************
 Project folders
*****************

The majority of your work on Esrum should take place in project folder
corresponding either to your research group or to actual projects. This
ensures that your collaborators can access your results and that nobody
else can! See the :ref:`p_usage_access_applying` page for instructions
on how to apply for access to projects.

Projects on Esrum are located in the ``/projects`` folder:

.. code-block:: console

   $ ls -1 /projects
   phenomics-AUDIT
   genotyping
   ...

The ``-AUDIT`` suffix indicates that the ``phenomics`` project has been
configured for work on GDPR data. All work on GDPR data should take
place in project or data-shares (see below) marked with ``-AUDIT`` and
*nowhere else*!

Projects folder always contains the following four sub-folders:

-  ``/projects/<project-name>/people``

   Every member of a project has their own folder in ``people``. It is
   suggested that you keep your scripts, configuration files,
   documentation, and the like in this folder. The ``people`` folder is
   automatically backed up every day.

-  ``/projects/<project-name>/apps``

   The ``apps`` folder is intended for storing software shared between
   project members. See :ref:`p_tips_modules` for how to set up a shared
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

There is currently no limits on how much you store in these folders.
However, as UCPH has indicated that they will charge for storage in the
future, we recommend regularly cleaning up your project folders.

See the :ref:`p_usage_projects` page for how to request a new project
folder.

**********
 Datasets
**********

Unlike projects, datasets are meant for static data that may be accessed
by multiple parties. Access to datasets is therefore segregated into
users who only have read access and users with read and write access
(the owners). Examples of datasets include shared resources, cohorts, as
well as automatically deposited instrument data.

Datasets on Esrum are located in the ``/datasets`` folder. Unlike
projects, where you will find four standard folders, the directory
structure of ``/datasets`` folders are entirely up to the owner.

Similarly to projects, dataset folders (meant for) containing GDPR data
are marked by the ``-AUDIT`` suffix. GDPR datasets must be stored in
such folders and *nowhere else*!

There is currently no limits on how much you store in these folders.
However, as UCPH has indicated that they will charge for storage in the
future, we recommend only storing data that you actually need.

See the :ref:`p_usage_projects` page for how to request a new dataset
folder.

*****************
 Scratch folders
*****************

Every node on Esrum (including the head node) has a 1.5-3 TB scratch
drive available at ``/scratch``. This is intended for short-lived
temporary files generated as part of jobs running on the cluster, and
can provide a significant performance benefit if a job, for example,
writes a lot of small temporary files.

.. note::

   Note that unlike your home folder, ``/projects``, and ``/datasets``,
   the ``/scratch`` folders are physically located on each node. Files
   written to ``/scratch`` on one node are therefore *not* accessible on
   other nodes.

It is recommended that you create a sub-folder containing your UCPH-IT
username when using the scratch-drive as part of your scripts:

.. code-block:: bash
   :linenos:

   # Create temporary folder in the form /scratch/abc123
   mkdir -p "/scratch/${USER}"
   # Some software use the TMPDIR to place temporary files
   export TMPDIR="/scratch/${USER}"
   # Other software has options for where to place temporary files
   mysoftware --in "mydata" --out "myresults" --temp "/scratch/${USER}"

.. warning::

   The scratch-drives have limited capacity and are *only* intended for
   short-lived, temporary files. Do not use it to store results, and
   please remember to clean up after your jobs. Files left on the
   scratch-drive *will* be deleted.

*********
 Backups
*********

Backups are available your home folder, in project folders (excluding
the ``scratch`` folder), in datasets, and in your network drive folders.
These are stored in special, hidden ``.snapshot`` folders in the root of
each of these folders. For example,

-  ``/datasets/cbmr_shared/.snapshot/``
-  ``/projects/cbmr_shared/apps/.snapshot/``
-  ``/projects/cbmr_shared/data/.snapshot/``
-  ``/projects/cbmr_shared/people/.snapshot/``
-  ``~/.snapshot``
-  ``~/ucph/hdir/.snapshot/``
-  ``~/ucph/ndir/SUN-CBMR-Shared-Info/.snapshot/``
-  ``~/ucph/sdir/SUN-CBMR-Shared/.snapshot/``

These folders do not appear when you list the content of the parent
folder, even you use ``ls -a``, but they can be accessed like any other
folder:

.. code-block:: console

   $ cd /projects/cbmr_shared/data/.snapshot
   $ ls
   42-Research-hourly-7D-2023-09-01_02:00
   42-Research-daily-30D-2023-09-02_02:00
   42-Research-weekly-104W-2023-09-03_02:00
   [...]

Each timestamped folder contains a full snapshot of the parent folder,
and you can copy data from these snapshots should you need to restore
deleted or modified files.

Snapshots of audited projects are only accessible for a limited time,
and you may therefore need to contact UCPH-IT to restore deleted data
for such projects.

.. warning::

   Please contact UCPH-IT should you need to restore a large amount of
   deleted data.

.. _s_filesystem_troubleshooting:

*****************
 Troubleshooting
*****************

.. include:: /services/networkdrives_troubleshooting.rst

.. _red hat enterprise linux: https://en.wikipedia.org/wiki/Red_Hat_Enterprise_Linux

.. _slurm: https://slurm.schedmd.com/overview.html
