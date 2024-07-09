.. _p_service_jupyter:

###################
 Jupyter Notebooks
###################

`Jupyter Notebooks`_ are available via the module system on Esrum and
may be started as follows:

.. code:: console

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

****************************************
 Port forwarding in Windows (MobaXterm)
****************************************

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
   your UCPH username. The full name of the SSH server (written in the
   top row on bottom right) is ``esrumhead01fl.unicph.domain``. Finally
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

******************************
 Port forwarding on Linux/OSX
******************************

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

   $ ssh -S none -N -L XXXXX:localhost:XXXXX abc123@esrumhead01fl.unicph.domain

Once you have port forwarding is enabled, you can open your notebook via
the ``http://localhost:XXXXX/?token=${long_text_here}`` URL that Jupyter
Notebook printed in your terminal.

.. note::

   The `-S none` option is recommended in case shared connections are
   enabled (see the `ControlMaster` section in `man ssh`), in which case
   the `ssh` command may otherwise not open the specified ports if a
   connection already exists.

.. raw:: html

   <script defer>
    document.addEventListener('DOMContentLoaded', function() {
      replaceTextContent(document.body, "XXXXX", getEphemeralPort());
    });
   </script>

*****************
 Troubleshooting
*****************

.. include:: jupyter_troubleshooting.rst

.. _argparser: https://cran.r-project.org/web/packages/argparser/index.html

.. _jupyter notebooks: https://jupyter.org/

.. _rstudio: https://posit.co/products/open-source/rstudio/
