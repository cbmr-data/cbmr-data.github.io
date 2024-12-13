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

.. code:: shell

   $ module avail
   -------------------------- /opt/software/modules --------------------------
   anaconda2/4.0.0            libpng/1.6.39               texlive/2023
   anaconda3/4.0.0            libtool/2.4.7               tiff/4.5.0
   anaconda3/5.3.1            libuv/1.44.2                topspin/4.1.4
   anaconda3/2020.11          libxkbcommon/1.3.0          trimgalore/0.6.6
   anaconda3/2021.05          libxscrnsaver/1.0.0         trnascan-se/2.0.11
   [...]

The ``avail`` command can also be used to list module versions by name:

.. code:: shell

   $ module avail samtools
   -------------------------- /opt/software/modules --------------------------
   samtools/1.12  samtools/1.17

Additionally, auto-completion is available in the bash shell if you
press tab after a module (partial) name when running `module load` (see
below).

If you are not sure of the exact name of a module, then the ``search``
command can be used to search module names and descriptions:

.. code:: shell

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

.. code:: shell

   $ samtools
   -bash: samtools: command not found
   $ module load samtools
   $ samtools
   Program: samtools (Tools for alignments in the SAM format)
   Version: 1.17 (using htslib 1.17)
   [...]

It is highly recommended to specify the exact version of a module that
you want to load. This ensure that your results are reproducible:

.. code:: shell

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

.. code:: shell

   $ module load bcftools/1.16
   Loading bcftools/1.16
   ERROR: bcftools/1.16 cannot be loaded due to missing prereq.
      HINT: the following module must be loaded first: perl

In that case you simply need to load the required module first. This can
be done in done manually:

.. code:: shell

   $ module load perl
   $ module load bcftools/1.16

Or automatically:

.. code:: shell

   $ module load --auto bcftools
   Loading bcftools/1.16
     Loading requirement: perl/5.26.3

Note that it is *not* recommended to use the ``--auto`` option when
loading R; see the :ref:`p_service_r` page for more information.

Listing and unloading loaded modules
====================================

The modules you have loaded can be listed using the ``module list``
command:

.. code:: shell

   $ modules list
   Currently Loaded Modulefiles:
    1) perl/5.26.3   2) bcftools/1.16   3) samtools/1.12

To remove a module that you no longer need, use the ``module unload``
command to unload a single module or the ``module purge`` command to
unload all modules:

.. code:: shell

   # Unload the samtools module
   $ module unload samtools
   # Unload the remaining modules
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

.. code:: shell

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

.. code:: shell

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

.. code:: shell

   $ module list
   No Modulefiles Currently Loaded.
   $ module restore ./modules.txt
   $ module list
   Currently Loaded Modulefiles:
   1) gcc/11.2.0   2) samtools/1.17   3) perl/5.26.3   4) bcftools/1.16

Alternative, use the ``.`` or ``source`` command to execute the content
of the file in your current shell. This has the same effect as running
``module restore``:

.. code:: shell

   $ source ./modules.txt

or

.. code:: shell

   $ . ./modules.txt

Simply running the script with ``bash modules.sh`` will not work.

.. _s_shared_modules:

*********************
 Shared CBMR modules
*********************

The Data Analytics team manages a small collection of modules for custom
tools in the `cbmr_shared` project folder. If you have not already been
given access to this project, then please :ref:`contact us <p_contact>`
and we will grant you access to the project.

To make use of these modules, run the following command in your
terminal:

.. code-block:: shell

   $ module use --prepend /projects/cbmr_shared/apps/modules/modulefiles/

A small helper script is also available to run this command:

.. code-block:: shell

   $ source /projects/cbmr_shared/apps/modules/activate.sh
   Using modules in '/projects/cbmr_shared/apps/modules/modulefiles/'

You can add the ``module use`` command to the end of your ``~/.bashrc``
file to make the shared modules available every time you connect to
Esrum.

.. _s_requesting_missing_modules:

*****************************
 Requesting software modules
*****************************

If the software you need is not available as a module, or if the
specific version you need is not available as a module, then you you can
request it through UCPH-IT as described below. You are also welcome to
:ref:`p_contact` us if you need help determining the exact software
and/or versions you need to request, or if you have other questions.

To request software,

#. Login to the UCPH `IT Serviceportal`_.
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

.. code::

   Requesting the addition of environment modules for the following software:

   1. seqtk v1.4 (https://github.com/lh3/seqtk)
   2. jq v1.5 (https://stedolan.github.io/jq/)
   3. igzip v2.30.0 (https://github.com/intel/isa-l)

.. warning::

   If you are not an employee at CBMR you may not have permission to
   open a ticket as described above. In that case simply
   :ref:`p_contact` us with your request and we will forward it to
   UCPH-IT.

.. _environment modules: https://modules.sourceforge.net/

.. _it serviceportal: https://serviceportal.ku.dk/

.. _list of modules: https://fssw.ku.dk/envmod.html

.. _official documentation: https://modules.readthedocs.io/en/v4.5.2/
