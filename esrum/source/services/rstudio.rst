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

R is available via the module system and modules may be installed in
your home folder using the ``install.packages`` command:

.. code:: console

   $ module load --auto R/4.3.1
   Loading R/4.3.1
     Loading requirement: gcc/11.2.0
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

See below if you get an ``libtk8.6.so: cannot open shared object file:
No such file or directory`` or similar error.

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

.. note::

   The RStudio server is managed by KU-IT and we can only provide basic
   basic support for using this service.

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

.. _jupyter notebooks: https://jupyter.org/

.. _rstudio: https://posit.co/products/open-source/rstudio/
