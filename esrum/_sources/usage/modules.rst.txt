.. _p_usage_modules:

###################
 Software on Esrum
###################

A wide range of software (scientific and otherwise) is made available on
Esrum via so-called `Environment modules`_. Environment modules allow
you "load" specific software, and specific *versions* of software, as
needed. If used correctly this can help to both document your analyses
and to make them more reproducible.

Modules on Esrum are primarily provided by UCPH-IT, who add new tools
and new versions of tools when requested (see
:ref:`s_requesting_missing_modules`). A browser-based `list of modules`_
provided by UCPH-IT is available. Users can also set up their own
private or shared environment modules as described in the
:ref:`p_tips_modules` section.

A collection of software managed by the Data Analytics team is also
available. See the :ref:`s_shared_modules` section below.

*************
 Basic usage
*************

This section briefly describe how to carry out common tasks using the
module system: Finding what modules are available, loading a module, and
unloading them again. For more information see the `official
documentation`_.

Finding available modules
=========================

The first step is to determine what modules are available on the server.
This is accomplished with the ``module avail`` command, that lists all
available modules by default:

.. code-block:: console

   $ module avail
   -------------------------- /opt/software/modules --------------------------
   anaconda2/4.0.0            libpng/1.6.39               texlive/2023
   anaconda3/4.0.0            libtool/2.4.7               tiff/4.5.0
   anaconda3/5.3.1            libuv/1.44.2                topspin/4.1.4
   anaconda3/2020.11          libxkbcommon/1.3.0          trimgalore/0.6.6
   anaconda3/2021.05          libxscrnsaver/1.0.0         trnascan-se/2.0.11
   [...]

The ``avail`` command can also be used to list module versions by name:

.. code-block:: console

   $ module avail samtools
   -------------------------- /opt/software/modules --------------------------
   samtools/1.12  samtools/1.17

Additionally, auto-completion is available in the bash shell if you
press tab after a module (partial) name when running `module load` (see
below).

If you are not sure of the exact name of a module, then the ``search``
command can be used to search module names and descriptions:

.. code-block:: console

   $ module search conda
    -------------------------- /opt/software/modules ---------------------------
        cellranger/3.1.0: a set of analysis pipelines that process [...]
        cellranger/6.1.1: a set of analysis pipelines that process [...]
        cellranger/6.1.2: a set of analysis pipelines that process [...]
             mamba/1.4.1: a fast, robust, and cross-platform package [...]
            mamba/23.3.1: a fast, robust, and cross-platform package [...]
         miniconda/4.9.2: free minimal installer for conda
        miniconda/4.10.4: free minimal installer for conda

.. warning::

   Software modules are added/updated on request and not necessarily
   when a new version of a tool is released. It is therefore highly
   recommended to always check that the available versions of tools fit
   your needs before starting a project.

If the software you need or the *version* of the software you need is
missing, then you can request that a module be added for that software
as described in the :ref:`s_requesting_missing_modules` section below.

Loading a module
================

The modules are loaded using the ``module load`` command. This command
adds the executable to your PATH and performs any other setup required
to run the software.

.. code-block:: console

   $ samtools
   -bash: samtools: command not found
   $ module load samtools
   $ samtools
   Program: samtools (Tools for alignments in the SAM format)
   Version: 1.17 (using htslib 1.17)
   [...]

Specifying the exact version of a module that you want to load is highly
recommended. This ensures that your results are reproducible:

.. code-block:: console

   $ module load samtools/1.12
   $ samtools
   Program: samtools (Tools for alignments in the SAM format)
   Version: 1.12 (using htslib 1.12)
   [...]

.. warning::

   New versions of software are added whenever people request them. This
   means that, if you do *not* specify a version when loading software,
   the results of your analyses may change in subtle or not so subtle
   ways while you are still working on a project.

   You should therefore *always* specify exact versions for the tools
   you use when loading modules.

In some cases one module will require another module:

.. code-block:: console

   $ module load bcftools/1.16
   Loading bcftools/1.16
   ERROR: bcftools/1.16 cannot be loaded due to missing prereq.
      HINT: the following module must be loaded first: perl

In that case you simply need to load the required module first. This can
be done in done manually:

.. code-block:: console

   $ module load perl
   $ module load bcftools/1.16

Or automatically:

.. code-block:: console

   $ module load --auto bcftools
   Loading bcftools/1.16
     Loading requirement: perl/5.26.3

Additional activation steps
===========================

Some modules require additional steps before you can use them. If so,
then this is typically described in the ``module display`` text:

.. code-block:: console
   :emphasize-lines: 11

   $ module display cellect/1.0

       /opt/software/modules/cellect/1.0:

       module-whatis   {CELL-type Expression-specific integration for Complex Traits (CELLECT) is a computational toolkit for identifying likely etiologic cell-types underlying complex traits.}
       conflict        cellect
       prereq          miniconda/4.12.0
       prepend-path    PATH /opt/software/cellect/1.0
       setenv          CELLECT /opt/software/cellect/1.0

       This module relies on snakemake which is available using: module load miniconda/4.12.0 followed by conda activate snakemake. You will need to provide your own config-file specifying an outdir.
       To read more about cellect go to https://github.com/perslab/CELLECT?tab=readme-ov-file

Thus, if we wanted to use ``cellect/1.0``, we would need to perform the
following steps:

.. code-block:: console

   $ module display cellect/1.0
   $ module load miniconda/4.12.0
   $ conda activate snakemake

.. warning::

   Modules that make use of conda environments may cause conflict with
   other modules and/or your own conda environments. For this reason, if
   you need to use multiple modules and one or more of them uses conda,
   creating a personal conda environment containing all the software you
   need is recommended. This minimizes the risk of conflicts and errors.

Listing and unloading loaded modules
====================================

The modules you have loaded can be listed using the ``module list``
command:

.. code-block:: console

   $ modules list
   Currently Loaded Modulefiles:
    1) perl/5.26.3   2) bcftools/1.16   3) samtools/1.12

To remove a module that you no longer need, use the ``module unload``
command to unload a single module:

.. code-block:: console

   $ module unload samtools

Alternatively, you can use the ``module purge`` command to unload all
modules:

.. code-block:: console

   $ module purge
   $ modules list
   No Modulefiles Currently Loaded.

***********************************
 Making your analyses reproducible
***********************************

As described above you can load modules with or without versions
specified. For a lot of software it is not very important that a
specific version used, but even so it is highly recommended that you
keep using the same versions of modules throughout a project.

#. This ensures that your results do not suddenly change if a new
   version of a piece of software is installed.
#. It ensures that you can accurately report what versions of software
   were used when it is time to publish your results.

The following section describes using the built-in ``save/restore``
commands to record and restoring your used modules, but it is also
possible to do this by hand.

Managing modules with ``module save/restore``
=============================================

To export a list of your currently used models, use the following
command:

.. code-block:: console

   $ module config collection_pin_version 1
   $ module save ./modules.txt

There are two important points here: Firstly, the ``module config
collection_pin_version 1`` command *must* be run first. If this is not
done, then the specific versions of modules are not recorded.

Secondly, the filename used in the second command (``./modules.txt``)
*must* contain a directory component (e.g. ``./``). If this is not done,
then the list is saved in a local database rather than as a file. Saving
the list as a local file is recommended as it allows other users to see
what software you used.

If used correctly, the ``./modules.txt`` file will contain the currently
loaded modules, e.g:

.. code-block:: console

   $ module list
   Currently Loaded Modulefiles:
   1) gcc/11.2.0   2) samtools/1.17   3) perl/5.26.3   4) bcftools/1.16
   $ module config collection_pin_version 1
   $ module save ./modules.txt
   $ cat modules.txt
   module use --append /opt/software/modules
   module load gcc/11.2.0
   module load samtools/1.17
   module load perl/5.26.3
   module load bcftools/1.16

To load the saved modules, simply run ``module restore`` with the same
filename (and a directory component):

.. code-block:: console

   $ module list
   No Modulefiles Currently Loaded.
   $ module restore ./modules.txt
   $ module list
   Currently Loaded Modulefiles:
   1) gcc/11.2.0   2) samtools/1.17   3) perl/5.26.3   4) bcftools/1.16

Alternative, use the ``.`` command or the ``source`` command to execute
the content of the file in your current shell. This has the same effect
as running ``module restore``:

.. code-block:: console

   $ . ./modules.txt

or

.. code-block:: console

   $ source ./modules.txt

Simply running the script with ``bash modules.sh`` will not work.

.. _s_shared_modules:

*********************
 Shared CBMR modules
*********************

The Data Analytics team manages a small collection of modules for custom
tools in the ``cbmr_shared`` project, located under
``/projects/cbmr_shared/apps/modules``. You should have access to these
modules by default. If that is not the case, then please contact
:ref:`contact us <p_contact>`.

These modules should be listed first when you use the ``module avail``
command:

.. code-block:: console

   ---------------- /projects/cbmr_shared/apps/modules/modulefiles ----------------
   add_dbsnp_ids/20231206_1  msconvert/20250218_1    sacct-usage/20240603_1
   annovep/20230808          pgs-calc/1.5.4          slurmboard/0.0.1
   [...]

   ---------------------------- /opt/software/modules -----------------------------
   ABC/1.0.0                         macs/3.0.0                       zlib/1.2.11
   adapterremoval/2.3.3              mageck/0.5.9.4                   zlib/1.2.13
   [...]

Should the modules not be listed, then you can manually register them
using the ``module use`` command:

.. code-block:: console

   $ module use --prepend /projects/cbmr_shared/apps/modules/modulefiles/

You can add the ``module use`` command to the end of your ``~/.bashrc``
file to make the shared modules available every time you connect to
Esrum.

.. _s_requesting_missing_modules:

*****************************
 Requesting software modules
*****************************

If the software you need is not available as a module, or if the
specific version you need is not available, then you can request it
through UCPH-IT as described below.

Software modules managed by UCPH-IT are available to the entirety of
UCPH, so if you need modules for software with licenses that do not
permit this, or if you need modules tailored for your specific needs,
then you are also welcome to :ref:`contact us <p_contact>` for
assistance.

To request software through UCPH-IT,

#. Log in to the UCPH `IT Serviceportal`_.
#. Click the ``Create Ticket`` / ``Opret Sag`` button.
#. Tick/select the ``Research IT`` / ``Forsknings IT`` category in the
   category/filters list on the left side of the screen.
#. Click the ``Research Applications Counseling and Support`` /
   ``Forskningsapplikationer Rådgivning og support`` button.
#. Click the ``REQUEST`` / ``Bestil`` button.
#. List what software you wish to have installed in the "Please
   describe" text-box (see below).
#. Write "esrumhead01fl.unicph.domain" in the System name text-box.
#. Click the ``Review & submit`` / ``Gennemse & bestil`` button.
#. Review your ticket and then click the ``Submit`` / ``Bestil`` button.

Your request should include the following information:

#. The name of the software.
#. The specific version requested (if any).
#. The homepage of the software.

A request may look like the following:

.. code-block:: text

   Requesting the addition of environment modules for the following software:

   1. seqtk v1.4 (https://github.com/lh3/seqtk)
   2. jq v1.5 (https://stedolan.github.io/jq/)
   3. igzip v2.30.0 (https://github.com/intel/isa-l)

.. warning::

   If you are not an employee at CBMR you may not have permission to
   open a ticket as described above. In that case simply
   :ref:`p_contact` us with your request, and we will forward it to
   UCPH-IT.

.. _environment modules: https://modules.sourceforge.net/

.. _it serviceportal: https://serviceportal.ku.dk/

.. _list of modules: https://fssw.ku.dk/envmod.html

.. _official documentation: https://modules.readthedocs.io/en/v4.5.2/
