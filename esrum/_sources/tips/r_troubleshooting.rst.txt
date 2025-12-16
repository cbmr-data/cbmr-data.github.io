######################################
 Dummy header to prevent reformatting
######################################

**************************************
 Dummy header to prevent reformatting
**************************************

libtk8.6.so: cannot open shared object file
===========================================

Users connecting to Esrum with X11 forwarding enabled, for example using
MobaXterm with default settings, may observe the following error when
running the ``install.packages``:

.. code-block:: text

   --- Please select a CRAN mirror for use in this session ---
   Error: .onLoad failed in loadNamespace() for 'tcltk', details:
     call: dyn.load(file, DLLpath = DLLpath, ...)
     error: unable to load shared object '/opt/software/R/4.3.1/lib64/R/library/tcltk/libs/tcltk.so':
     libtk8.6.so: cannot open shared object file: No such file or directory

If so, then you must disable graphical menus before running
``install.packages`` by first entering the following command:

.. code-block:: console

   > options(menu.graphics=FALSE)

Then simply run ``install.packages`` again.

You can also set the R option permanently by running the following in
your (bash) terminal:

.. code-block:: console

   $ echo 'options(menu.graphics=FALSE)' | tee -a ~/.Rprofile

libicui18n.so.73: cannot open shared object file: No such file or directory
===========================================================================

If you have conda installed, and if you are using R from an environment
module, then libraries may fail to install with the error message that
``libicui18n.so.73: cannot open shared object file: No such file or
directory``:

.. code-block:: text

   Error: package or namespace load failed for 'xml2' in dyn.load(file, DLLpath = DLLpath, ...): unable to load shared object '/home/abc1232/R/x86_64-pc-linux-gnu-library/4.5/00LOCK-xml2/00new/xml2/libs/xml2.so': libicui18n.so.73: cannot open shared object file: No such file or directory

To fix this, deactivate your conda environments (including ``base``)
before installing the library. For example, to install the ``xml2``
library:

.. code-block::

   (my-env) $ conda deactivate
   (base) $ conda deactivate
   $ R
   > install.packages("xml2")

libstdc++.so.6: version ``'GLIBCXX_3.4.26'`` not found
======================================================

If you build an R library on the head/compute nodes using a version of
the GCC module other than ``gcc/8.5.0``, then this library may fail to
load on the RStudio node or when ``gcc/8.5.0`` is loaded on the
head/compute nodes:

.. code-block:: console

   $ R
   > library(wk)
   Error: package or namespace load failed for ‘wk’ in dyn.load(file, DLLpath = DLLpath, ...):
   unable to load shared object '/home/abc123/R/x86_64-pc-linux-gnu-library/4.3/wk/libs/wk.so':
   /lib64/libstdc++.so.6: version `GLIBCXX_3.4.26' not found (required by /home/abc123/R/x86_64-pc-linux-gnu-library/4.3/wk/libs/wk.so)

To fix his, you will need to reinstall the affected R libraries using
one of two methods:

#. Connect to the RStudio server as described in the
   :ref:`s_service_rstudio` section, and simply install the affected
   packages using the ``install.packages`` function:

   .. code-block:: console

      > install.packages("wk")

   You may need to repeat this step multiple times, for every package
   that fails to load.

#. Connect to the head node or a compute node, and take care to load the
   correct version of GCC before loading R:

   .. code-block:: console

      $ module load gcc/8.5.0 R/4.3.2
      $ R
      > install.packages("wk")

The name of the affected module can be determined by looking at the
error message above. In particular, the path
``/home/abc123/R/x86_64-pc-linux-gnu-library/4.3/wk/libs/wk.so``
contains a pair of folders named ``R/x86_64-pc-linux-gnu-library``,
which specifies the kind of system we are running on. Immediately after
that we find the package name, namely ``wk`` in this case.

You can identify all affected packages in your "global" R library by
running the following commands:

.. code-block:: console

   $ module load gcc/8.5.0 R/4.3.2

#. ``cd`` to your R library

   .. code-block:: console

      $ cd ~/R/x86_64-pc-linux-gnu-library/4.3/

#. Test every installed library

   .. code-block:: console

      $ for lib in $(ls);do echo "Testing ${lib}"; Rscript <(echo "library(${lib})") > /dev/null;done

Output will look like the following:

.. code-block:: text

   Testing httpuv
   Testing igraph
   Error: package or namespace load failed for ‘igraph’ in dyn.load(file, DLLpath = DLLpath, ...):
   unable to load shared object '/home/abc123/R/x86_64-pc-linux-gnu-library/4.3/igraph/libs/igraph.so':
   /opt/software/gcc/8.5.0/lib64/libstdc++.so.6: version `GLIBCXX_3.4.29' not found (required by /home/abc123/R/x86_64-pc-linux-gnu-library/4.3/igraph/libs/igraph.so)
   Execution halted
   Testing isoband
   Error: package or namespace load failed for ‘isoband’ in dyn.load(file, DLLpath = DLLpath, ...):
   unable to load shared object '/home/abc123/R/x86_64-pc-linux-gnu-library/4.3/isoband/libs/isoband.so':
   /opt/software/gcc/8.5.0/lib64/libstdc++.so.6: version`GLIBCXX_3.4.29' not found (required by /home/abc123/R/x86_64-pc-linux-gnu-library/4.3/isoband/libs/isoband.so)
   Execution halted
   Testing labeling
   Testing later

Locate the error messages like the one shown above in the output and
reinstall the affected libraries using the ``install.packages`` command:

.. code-block:: console

   $ R
   > install.packages(c("igraph", "isoband"))
