.. _p_usage_modules:

#####################
 Environment modules
#####################

A wide range of scientific (and other) software is made available on
Esrum via so-called `Environment modules`_. While environment modules
add some complexity, they allow both different versions of software as
well as mutually exclusive pieces of software to coexist, and simplify
making your analyses reproducible.

Modules on Esrum are primarily provided by KU-IT (see below), but users
may also set up their own private or shared environment modules. See the
:ref:`p_tips_modules` section for more information.

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

The ``avail`` command can also be used to search for specific modules by
specifying one or more keywords:

.. code:: shell

   $ module avail sam
   -------------------------- /opt/software/modules --------------------------
   samtools/1.12  samtools/1.17

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

Multiple modules may be specified per ``module load`` command and it is
also possible to specify the exact version that you need, provided that
a module is available for that version:

.. code:: shell

   $ module load samtools/1.12
   $ samtools
   Program: samtools (Tools for alignments in the SAM format)
   Version: 1.12 (using htslib 1.12)
   [...]

In some cases one module will require another module:

.. code:: shell

   $ module load bcftools
   Loading bcftools/1.16
   ERROR: bcftools/1.16 cannot be loaded due to missing prereq.
      HINT: the following module must be loaded first: perl

In that case you simply need to load the required module first. This can
be done in done manually:

.. code:: shell

   $ module load perl
   $ module load bcftools

Or automatically:

.. code:: shell

   $ module load --auto bcftools
   Loading bcftools/1.16
     Loading requirement: perl/5.26.3

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
given access to this project, then please follow the steps outlined in
:ref:`s_applying_for_access` and apply for access to the
``COMP-PRJ-cbmr_shared`` project.

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

****************************
 Requesting missing modules
****************************

If the software you need is not available as a module, you you can
request it through KU-IT as described below. You are also welcome to
:ref:`p_contact` us if you need help determining the exact software
and/or versions you need to request, or if you have other questions.

To request software,

#. Login to the KU `IT Serviceportal`_.
#. Click the ``Create Ticket`` / ``Opret Sag`` button.
#. Select the ``Research IT`` / ``Forsknings-IT`` category.
#. Then select the ``Research Applications and Services`` /
   ``Forskningsapplikationer og Services`` subcategory.
#. Finally, select ``Consultancy and Support`` / ``Rådgivning og
   support``.
#. List what software you wish to have installed in the "Please
   describe" text-box (see below).
#. Write "esrumhead01fl.unicph.domain" in the System name text-box.
#. Click the ``ADD TO CART`` / ``TILFØJ TIL KURV`` button.
#. Click the ``SUBMIT ORDER`` / ``INDSEND ORDRE`` button.

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
   KU-IT.

.. _environment modules: https://modules.sourceforge.net/

.. _it serviceportal: https://serviceportal.ku.dk/

.. _official documentation: https://modules.readthedocs.io/en/v4.5.2/
