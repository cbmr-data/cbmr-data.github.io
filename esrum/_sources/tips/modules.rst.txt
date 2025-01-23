.. _p_tips_modules:

##############################
 Creating environment modules
##############################

This page gives a very brief run-down of how to create your own
`environment modules`_. For more information see the `official
documentation`_. However, for most part you should be requesting modules
from UCPH-IT (see :ref:`s_requesting_missing_modules`).

To simplify things, this example makes use of a generalized template
file (available for download :download:`here
<scripts/moduletemplate.tcl>`) for which only a handful of (highlighted)
lines need to be changed:

.. literalinclude:: scripts/moduletemplate.tcl
   :language: tcl
   :linenos:
   :emphasize-lines: 7-10,13-16

For the purpose of this example we will make our own module for
``seqtk`` version 1.4.

***********************************
 Creating a repository for modules
***********************************

The recommended location for custom modules is the ``apps`` folder in
the project for which the modules are meant to be used. In the following
examples, we will assume that the project is named ``my-project`` and
that the ``apps`` folder is therefore located at
``/projects/my-project/apps``.

The module repository will consist of two folders: A ``modulefiles``
folder containing the scripts needed to load software, and a
``software`` folder in which we will place the actual software loaded by
the module files. This organization is designed to simplify maintenance.

#. Create a subfolder in the ``apps`` for your modules:

   .. code-block::

      $ mkdir -p /projects/my-project/apps/modules

#. Create a subfolder for the ``seqtk`` module scripts and a folder in
   which we can build our own copy of ``seqtk``:

   .. code-block::

      $ mkdir -p /projects/my-project/apps/modules/modulefiles/seqtk
      $ mkdir -p /projects/my-project/apps/modules/software/seqtk/1.4

   Note that we create a folder containing the version in ``software``
   but *not* in ``modulefiles``!

#. Save the module template shown above as
   ``/projects/my-project/apps/modules/modulefiles/seqtk/1.23`` and
   update the root path, the description, and the PATH as shown below.
   Note that this file does *not* have an extension.

   .. literalinclude:: scripts/moduletemplate.seqtk.tcl
      :language: tcl
      :linenos:
      :emphasize-lines: 7-8,10

   As this is a very simple module we only need to set the ``PATH``
   environment variable.

#. Next download and compile ``seqtk 1.4``:

   .. code-block::

      $ cd /projects/my-project/apps/modules/software/seqtk/1.4
      $ wget "https://github.com/lh3/seqtk/archive/refs/tags/v1.4.tar.gz"
      $ tar xvzf v1.4.tar.gz
      $ cd seqtk-1.4
      $ module load gcc
      $ make

#. Place a symlink to the executable in a separate ``bin`` folder:

   .. code-block::

      $ cd /projects/my-project/apps/modules/software/seqtk/1.4
      $ mkdir bin
      $ cd bin
      $ ln -s ../seqtk-1.4/seqtk

   You can also make a copy of the executable in the ``bin`` folder, but
   using a symlink makes it simpler to recompile the software if needed.

   The location of this ``bin`` folder is already specified in the
   template above. While it *is* possible to specify the software
   directory directly (e.g. ``software/seqtk/1.4/seqtk-1.4/``), this is
   *not* recommended as it often includes files that do not belong in
   your PATH.

#. Finally, run ``module use`` to registers your module repository so
   that you can load your modules:

   .. code-block::

      $ module use --prepend /projects/my-project/apps/modules/modulefiles/
      $ module avail
      ----------- /projects/my-project/apps/modules/modulefiles/ -----------
      seqtk/1.4
      $ module load seqtk/1.4
      ./seqtk

      Usage:   seqtk <command> <arguments>
      Version: 1.4-r122

   The ``module use`` command can optionally be added to your
   ``.profile``, ``.bashrc``, or similar to automatically enable this
   module repository when you login.

****************************
 Dependencies and conflicts
****************************

Software may depend on other software to run (e.g. java based software
needing a Java Runtime Environment (JRE) to run) or may conflict with
other software (e.g. mamba and conda both providing the same commands).

The template above automatically conflicts with different versions of
the same program via the ``conflict "${name}"`` line, but it is also
possible to add additional conflicts.

To add a requirement, instead use ``prereq module`` where ``module`` is
the name of the module that your module depends on. For example, if your
program depends on ``perl``, then you may add ``prereq perl``. You may
optionally specify the version of said module, e.g. ``prereq
perl/5.24.3``.

************************************
 Building more complicated software
************************************

For more complicated software it is recommended to use the functionality
that is often built to install it directly in the target directory. An
example might look like the following:

.. code-block::

   $ tar xvzf my-software-1.23.tar.gz
   $ cd my-software-1.23
   $ ./configure --prefix=/projects/my-project/apps/modules/software/my-software/1.23
   $ make install

Refer to the documentation for the software you are installing for more
information.

****************************
 Installing Python software
****************************

Making modules for python software is a bit more complicated, but can
typically be accomplished as follows (using VisiData_ as an example):

.. code-block::

   # Basic setup
   $ mkdir -p /projects/my-project/apps/modules/software/visidata/2.11
   $ cd /projects/my-project/apps/modules/software/visidata/2.11
   # Load the required version of Python (if any)
   $ module load python/3.9.16
   # Create a virtual environment in `./venv` to contain our software
   $ python3 -m venv ./venv
   # Install our desired software
   $ ./venv/bin/pip install visidata
   # Create a bin folder as described above
   $ mkdir bin
   $ cd bin
   $ ln -s ../venv/bin/visidata

Then all you need to do is to create a matching module file and save it
as ``/projects/my-project/apps/modules/modulefiles/visidata/2.11``. The
python module loaded above *does not* need to be loaded before using
this software.

.. warning::

   Do not add the ``venv/bin`` folder to your PATH. This will override
   your default Python version and may result in accidental changes to
   the virtual environment, if you run ``pip`` or similar tools.

.. _environment modules: https://modules.sourceforge.net/

.. _official documentation: https://modules.readthedocs.io/en/v4.5.2/

.. _seqtk: https://github.com/lh3/seqtk

.. _visidata: https://www.visidata.org/
