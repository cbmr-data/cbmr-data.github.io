.. _p_usage_rstudio:

###################################
 R, RStudio, and Jupyter Notebooks
###################################

Users of the Esrum cluster have the option of using R, RStudio or
Jupyter Notebooks to run their analyses. This section describes steps
required to use these tools.

***
 R
***

Several versions of R are available via the module system. To load
these, you need to load the version of R you want *and* a version of
gcc, which is required to install/load modules.

Compatibility with the Rstudio server
=====================================

We *highly* recommend that you always use ``gcc/8.5.0`` and ``R/4.3.2``
(or another version of ``R/4.3.x``) when loading R on the head or
compute nodes, since this ensures compatibility between all servers on
Esrum:

.. code-block:: shell

   $ module load gcc/8.5.0 R/4.3.2

Using the ``--auto`` option will instead load the latest version of gcc,
currently version ``11.2.0``.

R modules installed using versions of R other than ``4.3.x`` will simply
not be available on the RStudio server and you will need to install them
again.

.. warning::

   Using a GCC version greater than 8.x with ``R/4.3.x`` may cause
   modules you install to fail to load on the Rstudio server with the
   following error:

   See the Troubleshooting section below for more information.

Submitting R scripts using Slurm
================================

The recommended way to run R on Esrum is as non-interactive scripts
submitted to slurm. This not only ensures that your analyses do not
impact other users, but also makes make your analyses reproducible.

To run an R script on the command-line, simply use the ``Rscript``
command:

.. code-block:: shell

   $ cat my_script.R
   cat("Hello, world!\n")
   $ Rscript my_script.R
   Hello, world!

For simple scripts you can use the ``commandArgs`` function to pass
arguments to your scripts, allowing you to use them to process arbitrary
data-sets:

.. code-block:: R

   args <- commandArgs(trailingOnly = TRUE)

   cat("Hello, ", args[1], "!\n", sep="")

.. code-block:: console

   $ Rscript my_script.R world
   Hello, world!

If your script requires a heterogenous set of input files or options to
run, then it is recommended to use an argument parser such as the
argparser_ R library. To use the argparser library you must first
install it using the ``install.packages("argparser")`` command.

The following is a brief example of how you might use the ``argparser``
library and it can also be downloaded :download:`here
<scripts/argparser.R>`.

.. literalinclude:: scripts/argparser.R
   :language: R

This allows you to document your command-line options, specify default
values, and much more:

.. code-block:: shell

   $ Rscript my_script.R
   usage: my_script.R [--] [--help] [--opts OPTS] [--p-value P-VALUE]
       input_file

   This is my script!

   positional arguments:
   input_file     My data

   flags:
   -h, --help     show this help message and exit

   optional arguments:
   -x, --opts     RDS file containing argument values
   -p, --p-value  Maximum P-value [default: 0.05]

   Error in parse_args(parser) :
   Missing required arguments: expecting 1 values but got 0 values: ().
   Execution halted
   $ Rscript my_script.R my_data.tsv
   I would process the file my_data.tsv with a max P-value of 0.05

Finally, you write can write a small bash script to automatically load
the required version of R and to call your script when you submit it to
Slurm (using your preferred version of R):

.. code-block:: console

   $ cat run_rscript.sh
   #!/bin/bash

   module load gcc/8.5.0 R/4.1.2
   Rscript "${@}"

The ``"${@}"`` safely passes all your command-line arguments to
``Rscript``, even if they contain spaces. This wrapper script can then
be used to submit/call any of your R-scripts:

.. code-block:: console

   $ sbatch run_rscript.sh my_script.R my_data.tsv --p-value 0.01
   Submitted batch job 18090212
   $ cat slurm-18090212.out
   I would process the file my_data.tsv with a max P-value of 0.01

Installing R modules
====================

Modules may be installed in your home folder using the
``install.packages`` command:

.. code:: console

   $ module load gcc/8.5.0 R/4.3.1
   $ R
   > install.packages("ggplot2")
   Warning in install.packages("ggplot2") :
     'lib = "/opt/software/R/4.3.1/lib64/R/library"' is not writable
   Would you like to use a personal library instead? (yes/No/cancel) yes
   Would you like to create a personal library
   ‘/home/abc123/R/x86_64-pc-linux-gnu-library/4.3’
   to install packages into? (yes/No/cancel) yes

When asked to pick a mirror, either pick ``0-Cloud`` by entering ``1``
and pressing enter, or enter the number corresponding to a location near
you and press enter:

.. code:: console

   --- Please select a CRAN mirror for use in this session ---
   Secure CRAN mirrors

   1: 0-Cloud [https]
   [...]

   Selection: 1

.. _s_rstudio:

*********
 RStudio
*********

An RStudio_ server is made available at http://esrumweb01fl:8787/. To
use this server, you must

#. Be a member of the ``SRV-esrumweb-users`` group. Simply follow the
   steps in the :ref:`s_applying_for_access` section, and apply for
   access to this group.

#. Be connected via the KU VPN (a wired connection at CBMR is *not*
   sufficient). See :ref:`p_usage_connecting` for more information.

Once you have been been made a member of the ``SRV-esrumweb-users`` and
connected using the VPN or a wired connection at CBMR, simply visit
http://esrumweb01fl:8787/ and login using your KU credentials.

For your username you should use the short form:

.. image:: images/rstudio_login.png
   :align: center

.. warning::

   The RStudio server is *only* for running R. If you need to run other
   tasks then you *must* connect to the head node and run them using
   Slurm as described in :ref:`p_usage_slurm`.

   Resource intensive tasks running on the RStudio server will likely
   negatively impact everyone using the service and we will therefore
   terminate such tasks without warning if we deem it necessary.

RStudio server best practice
============================

Since the RStudio server is a shared resource where that many users may
be using simultaneously, we ask that you show consideration towards
other users of the server.

In particular,

-  Try to limit the size of the data-sets you work with on the RStudio
   server. Since *all* data has to be read from (or written to) network
   drives, one person reading or writing a large amount of data can
   cause significant slow-downs for *everyone* using the service.

   We therefore recommend that you load a (small) subset of your data in
   Rstudio, that you use that subset of data to develop your analyses
   processes, and that you use that to process your complete dataset via
   an R-script submitted to Slurm as described in :ref:`p_usage_slurm`.

   See also above for a brief example of how to submit R scripts to
   Slurm.

-  Don't keep data in memory that you do not need. Data that you no
   longer need can be freed with the ``rm`` function or using the broom
   icon on the ``Environment`` tab in Rstudio, as described below. This
   also helps prevent RStudio from filling your home folder when your
   session is closed (see Troubleshooting below).

-  Do not run resource intensive tasks via the embedded terminal. As
   noted above, such tasks will be terminated without warning if deemed
   to have a negative impact on other users. Instead such tasks should
   be run using Slurm as described in :ref:`p_usage_slurm`.

******************
 Jupyter notebook
******************

`Jupyter Notebooks`_ are available via the module system on Esrum and
may be started as follows:

.. code:: shell

   $ module load jupyter-notebook
   $ jupyter notebook --no-browser --port=XXXXX

.. raw:: html

   <script>
    document.write("The number used in the argument <code class=\"docutils literal notranslate\"><span class=\"pre\">--port=XXXXX</span></code> must be a value in the range 49152 to 65535, and must not be a number used by another user on Esrum. The number shown here was randomly selected for you and you can refresh this page for a different suggestion.")
   </script>
   <noscript>
   The XXXXX in the above command must be replaced with a valid port number. To avoid trouble you should pick a number in the range 49152 to 65535, and you must not pick a number used by another user on Esrum.
   </noscript>

It is also recommended that you run your notebook in a tmux session or
similar, to avoid the notebook shutting down if you lose connection to
the server. See :ref:`p_tips_tmux` for more information.

To actually connect to the notebook server, you will need to setup port
forwarding using the port-number from your command.

Port forwarding in Windows (MobaXterm)
======================================

The following instructions assume that you are using MobaXterm. If not,
then please refer to the documentation for your tool of choice.

#. Install and configure MobaXterm as described in
   :ref:`s_configure_mobaxterm`.

#. Click the middle ``Tunneling`` button on the toolbar.

   .. image:: images/mobaxterm_tunnel_01.png
      :align: center

#. Click the bottom-left ``New SSH Tunnel`` button.

   .. image:: images/mobaxterm_tunnel_02.png
      :align: center

#. Fill out the tunnel dialogue as indicated, replacing ``12356`` with
   your chosen port number (e.g. XXXXX) and replacing ``abc123`` with
   your KU username. The full name of the SSH server (written in the top
   row on bottom right) is ``esrumhead01fl.unicph.domain``. Finally
   click ``Save``:

   .. image:: images/mobaxterm_tunnel_03.png
      :align: center

#. If the tunnel does not start automatically, press either the "Play"
   button or the ``Start all tunnels`` button:

   .. image:: images/mobaxterm_tunnel_04.png
      :align: center

#. Enter your password and your SSH tunnel should now be active.

Once you have configured MobaXterm and enabled port forwarding, you can
open your notebook via the
``http://localhost:XXXXX/?token=${long_text_here}`` URL that Jupyter
Notebook printed in your terminal.

Port forwarding on Linux/OSX
============================

It is recommended to enable port forwarding using your ``~/.ssh/config``
file. This is accomplished by adding a ``LocalForward`` line to your
entry for Esrum as shown below (see also the section about
:ref:`s_connecting_linux`):

.. code:: text

   Host esrum esrumhead01fl esrumhead01fl.unicph.domain
       HostName esrumhead01fl.unicph.domain
       User abc123

       LocalForward XXXXX localhost:XXXXX

The ``LocalForward`` option consists of two parts: The port used by the
notebook on Esrum (XXXXX), and the address via which the notebook on
Esrum should be accessible on your PC (localhost:XXXXX).

Alternatively, you can start start/stop port forwarding on demand by
using an explicit SSH command. The ``-N`` option is optional and stops
ssh from starting a shell once it has connected to Esrum:

.. code:: shell

   $ ssh -N -L XXXXX:localhost:XXXXX abc123@esrumhead01fl.unicph.domain

Once you have port forwarding is enabled, you can open your notebook via
the ``http://localhost:XXXXX/?token=${long_text_here}`` URL that Jupyter
Notebook printed in your terminal.

*****************
 Troubleshooting
*****************

.. include:: rstudio_troubleshooting.rst

.. raw:: html

   <script defer>
    var random_port = getEphemeralPort();

    function updatePort(elem) {
      if (elem.childNodes.length) {
        elem.childNodes.forEach(updatePort);
      } else if (elem.textContent) {
        elem.textContent = elem.textContent.replaceAll("XXXXX", random_port);
      }

      if (elem.href && elem.href.includes("XXXXX")) {
        elem.href = elem.href.replaceAll("XXXXX", random_port);
        // open in new page
        elem.target = "_blank";
      }
    };

    document.addEventListener('DOMContentLoaded', function() {
      updatePort(document.body);
    });
   </script>

.. _argparser: https://cran.r-project.org/web/packages/argparser/index.html

.. _jupyter notebooks: https://jupyter.org/

.. _rstudio: https://posit.co/products/open-source/rstudio/
