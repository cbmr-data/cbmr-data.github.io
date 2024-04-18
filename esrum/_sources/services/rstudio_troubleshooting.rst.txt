
R: libtk8.6.so: cannot open shared object file
==============================================

Users connecting to Esrum with X11 forwarding enabled, for example using
mobaXterm with default settings, may observe the following error when
running the ``install.packages``:

.. code:: console

   --- Please select a CRAN mirror for use in this session ---
   Error: .onLoad failed in loadNamespace() for 'tcltk', details:
     call: dyn.load(file, DLLpath = DLLpath, ...)
     error: unable to load shared object '/opt/software/R/4.3.1/lib64/R/library/tcltk/libs/tcltk.so':
     libtk8.6.so: cannot open shared object file: No such file or directory

If so, then you must disable graphical menus before running
``install.packages`` by first entering the following command:

.. code:: console

   > options(menu.graphics=FALSE)

Then simply run ``install.packages`` again.

You can also set the R option permanently by running the following in
your (bash) terminal:

.. code:: console

   $ echo 'options(menu.graphics=FALSE)' | tee -a ~/.Rprofile

R: libstdc++.so.6: version ``'GLIBCXX_3.4.26'`` not found
=========================================================

If you build an R library on the head/compute nodes using a version of
the GCC module other than ``gcc/8.5.0``, then this library may fail to
load on the RStudio node or when ``gcc/8.5.0`` is loaded on the
head/compute nodes:

.. code-block::

   $ R
   > library(wk)
   Error: package or namespace load failed for ‘wk’ in dyn.load(file, DLLpath = DLLpath, ...):
   unable to load shared object '/home/abc123/R/x86_64-pc-linux-gnu-library/4.3/wk/libs/wk.so':
   /lib64/libstdc++.so.6: version `GLIBCXX_3.4.26' not found (required by /home/abc123/R/x86_64-pc-linux-gnu-library/4.3/wk/libs/wk.so)

To fix his, you will need to reinstall the affected R libraries using
one of two methods:

#. Connect to the RStudio server as described in the :ref:`s_rstudio`
   section, and simply install the affected packages using the
   ``install.packages`` function:

   .. code-block::

      > install.packages("wk")

   You may need to repeat this step multiple times, for every package
   that fails to load.

#. Connect to the head node or a compute node, and take care to load the
   correct version of GCC before loading R:

   .. code-block:: shell

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

.. code-block:: shell

   module load gcc/8.5.0 R/4.3.2
   # cd to your R library
   cd ~/R/x86_64-pc-linux-gnu-library/4.3/
   # Test every installed library
   for lib in $(ls);do echo "Testing ${lib}"; Rscript <(echo "library(${lib})") > /dev/null;done

Output will look like the following:

.. code-block:: shell

   Testing httpuv
   Testing igraph
   Error: package or namespace load failed for ‘igraph’ in dyn.load(file, DLLpath = DLLpath, ...):
   unable to load shared object '/home/abc123/R/x86_64-pc-linux-gnu-library/4.3/igraph/libs/igraph.so':
   /opt/software/gcc/8.5.0/lib64/libstdc++.so.6: version `GLIBCXX_3.4.29' not found (required by /home/abc123/R/x86_64-pc-linux-gnu-library/4.3/igraph/libs/igraph.so)
   Execution halted
   Testing isoband
   Error: package or namespace load failed for ‘isoband’ in dyn.load(file, DLLpath = DLLpath, ...):
   unable to load shared object '/home/abc123/R/x86_64-pc-linux-gnu-library/4.3/isoband/libs/isoband.so':
   /opt/software/gcc/8.5.0/lib64/libstdc++.so.6: version `GLIBCXX_3.4.29' not found (required by /home/abc123/R/x86_64-pc-linux-gnu-library/4.3/isoband/libs/isoband.so)
   Execution halted
   Testing labeling
   Testing later

Locate the error messages like the one shown above in the output and and
reinstall the affected libraries using the ``install.packages`` command:

.. code-block:: shell

   $ R
   > install.packages(c("igraph", "isoband"))

RStudio: Incorrect or invalid username/password
===============================================

Please make sure that you are entering your username in the short form
and that you have been added as a member of the ``SRV-esrumweb-users``
group (see above). If the problem persists, please :ref:`p_contact` us
for assistance.

RStudio: Logging in takes a very long time
==========================================

Similar to regular R, RStudio will automatically save the data you have
loaded into your R session and will restore it when you return later, so
that you can continue your work. However, this many result in large
amounts of data being saved and loading this data may result in a large
delay when you attempt to login at a later date.

It is therefore recommended that you regularly clean up your workspace
using the built in tools, when you no longer need to have the data
loaded in R.

You can remove individual bits of data using the ``rm`` function in R.
This works both when using regular R and when using RStudio. The
following gives two examples of using the ``rm`` function, one removing
a single variable and the other removing *all* variables in the current
session:

.. code:: r

   # 1. Remove the variable `my_variable`
   rm(my_variable)

   # 2. Remove all variables from your R session
   rm(list = ls())

Alternatively you can remove all data saved in your R session using the
broom icon on the ``Environment`` tab:

.. image:: /services/images/rstudio_gc_01.png
   :align: center

.. image:: /services/images/rstudio_gc_02.png
   :align: center

If you wish to prevent this issue in the first case, then you can also
turn off saving the data in your session on exit and/or turn off loading
the saved data on startup. This is accomplished via the ``Global
Options...`` accessible from the ``Tools`` menu:

.. image:: /services/images/rstudio_gc_03.png
   :align: center

Should your R session have grown to such a size that you simply cannot
login and clean it up, then it my be necessary to remove the files
containing the data that R/RStudio has saved. This data is stored in two
locations:

#. In the ``.RData`` file in your home (``~/.RData``). This is where R
   saves your data if you answer yes ``Save workspace image? [y/n/c]``
   when quitting R.

#. In the ``environment`` file in your RStudio session folder
   (``~/.local/share/rstudio/sessions/active/session-*/suspended-session-data/environment``).
   This is where Rstudio saves your data should your login time-out
   while using RStudio.

Please :ref:`p_contact` us and we can help you remove the correct files.

Jupyter Notebooks: Browser error when opening URL
=================================================

Depending on your browser you may receive one of the following errors.
The typical causes are listed, but the exact error message will depend
on your browser. It is therefore helpful to review all possible causes
listed here.

When using Chrome, the cause is typically listed below the line that
says "This site can't be reached".

-  "The connection was reset"

   This typically indicates that Jupyter Notebook isn't running on the
   server, or that it is running on a different port than the one you've
   forwarded. Check that Jupyter Notebook is running and make sure that
   your forwarded ports match those used by Jupyter Notebook on Esrum.

-  "localhost refused to connect" or "Unable to connect"

   This typically indicates that port forwarding isn't active, or that
   you have entered the wrong port number in your browser. Verify that
   port forwarding is active and that you are using the correct port
   number in the ``localhost`` URL.

-  "Check if there is a typo in esrumweb01fl" or "We're having trouble
   finding that site"

   You are must likely connecting from a network outside of KU. Make
   sure that you are using a wired connection at CBMR and/or that the
   VPN is activated and try again.
