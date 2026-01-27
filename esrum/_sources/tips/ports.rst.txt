.. _p_tips_forwarding:

#################
 Port forwarding
#################

This page describes how to set up port forwarding from your PC or
laptop, to the Esrum head node or to a compute node on Esrum. Before you
continue, please select the port you wish to forward. The following
examples will be updated to match that choice.

.. raw:: html

   <center>
     <label for="port">Port to forward:</label>
     <input id="port-input" name="port" min=1024 max=65535 type="number">
   </center>

Once you have selected a port, please select your operating system of
choice:

.. list-table::
   :class: image-buttons

   -  -  :ref:`Windows <s_ports_windows>`

         .. image:: /usage/access/images/os_windows.png
            :width: 128
            :target: #connecting-on-windows

      -  :ref:`OSX <s_ports_osx_linux>`

         .. image:: /usage/access/images/os_macosx.png
            :width: 128
            :target: #connecting-on-osx

      -  :ref:`Linux <s_ports_osx_linux>`

         .. image:: /usage/access/images/os_linux.png
            :width: 128
            :target: #connecting-on-linux

.. _s_ports_windows:

***********************************
 Port forwarding for Windows users
***********************************

The following instructions describe how to set up port forwarding to
Esrum from your laptop or PC running Windows. It is furthermore assumed
that you are using MobaXterm to connect to Esrum (see the
:ref:`s_configure_mobaxterm` section). If not, then please refer to the
documentation for your software of choice.

#. Install and configure MobaXterm as described in
   :ref:`s_configure_mobaxterm`.

#. Click the middle ``Tunneling`` button on the toolbar.

   .. image:: images/mobaxterm_tunnel_01.png
      :align: center

#. Click the bottom-left ``New SSH Tunnel`` button.

   .. image:: images/mobaxterm_tunnel_02.png
      :align: center

#. Follow these steps to configure the tunnel:

   .. raw:: html

      <p class="port-container">
        <span class="port" style="left: 58.5%;top: 22cqw;">XXXXX</span>
        <span class="port" style="left: 19.5%;top: 35.5cqw;">XXXXX</span>
        <span class="port" style="left: 77%;top: 58.5cqw;">XXXXX</span>

   .. image:: images/mobaxterm_tunnel_03.png
      :align: center

   .. raw:: html

      </p>

   #. In middle-left box, write your chosen port number as shown above.

   #. If the service you wish to connect to is running on a compute
      note, then replace ``localhost`` in the top-right pair of boxes
      with the name of that node (such as
      ``esrumcmpn07fl.unicph.domain``), and enter your chosen port
      number.

   #. In the middle-right trio of boxes, write the full name of the head
      node (``esrumhead01fl.unicph.domain``), write your UCPH username
      where the screenshot has ``abc123``, and make sure that the value
      is ``22``.

   #. Finally, click ``Save``.

#. If the tunnel does not start automatically, press either the
   Play-icon button or the ``Start all tunnels`` button:

   .. image:: images/mobaxterm_tunnel_04.png
      :align: center

#. Enter your password and your SSH tunnel should now be active.

.. _s_ports_osx_linux:

*************************************
 Port forwarding for OSX/Linux users
*************************************

The following instructions describe how to set up port forwarding to
Esrum from your laptop or PC running OSX or Linux.

This is accomplished by running the following command-line *on your
laptop or PC*, replacing ``esrumcmpn07fl`` with the name of the node to
which you want to forward a port, and replacing ``abc123`` with your
UCPH short username:

.. code-block:: console

   $ ssh -S none -N -L 'XXXXX:esrumcmpn07fl:XXXXX' abc123@esrumhead01fl.unicph.domain

If the service you wish to connect to is instead running on the head
node, then use the following command:

.. code-block:: console

   $ ssh -S none -N -L 'XXXXX:localhost:XXXXX' abc123@esrumhead01fl.unicph.domain

The ``-S none`` option ensures that SSH opens a new connection even if
shared connections are enabled (see the ``ControlMaster`` section in
``man ssh``), which is required to forward the requested ports. The
``-N`` option prevents ``ssh`` from opening a shell on Esrum, which
ensures that you do not accidentally use this terminal and then close
it, while still using the forwarded port, and the ``-L`` option
configures the actual port forwarding.

.. tip::

   If you created a ``~/.ssh/config`` file as suggested in the
   :ref:`s_connecting_linux` section, then you can use the shorter
   command ``ssh -S none -N -L 'XXXXX:esrumcmpn07fl:XXXXX' esrum``.

.. raw:: html

   <script defer>
    document.addEventListener('DOMContentLoaded', function() {
      const portInput = document.querySelector("#port-input");
      const updaters = createElementUpdaters(document.body, "XXXXX");

      portInput.addEventListener("change", (event) => {
        for (updater of updaters) {
          updater(portInput.value);
        }
      });

      portInput.value = getEphemeralPort();
      portInput.dispatchEvent(new Event("change"));
    });
   </script>
