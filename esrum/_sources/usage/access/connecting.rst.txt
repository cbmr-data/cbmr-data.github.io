.. _p_usage_connecting:

###########################
 Connecting to the cluster
###########################

The cluster is accessible via SSH_ at ``esrumhead01fl.unicph.domain``.
This is the Esrum "head" node, the entry-point to the cluster, where you
will be queuing your analyses using the Slurm job management system, as
described on the :ref:`p_usage_slurm` pages.

Additionally, the two RStudio servers are accessible at
https://esrumweb01fl/ and https://esrumweb02fl/. See the
:ref:`p_service_rstudio` page for more information.

However, to connect to any of these, you must

#. Have been granted access by the Data Analytics team. If that is not
   the case, then please see the :ref:`p_usage_access_applying` page
   before continuing

#. Be connected to the official UCPH VPN_. See below for more
   information.

#. Follow the instructions for your operating system to configure an SSH
   client:

.. list-table::
   :class: image-buttons

   -  -  :ref:`Windows <s_connecting_windows>`

         .. image:: images/os_windows.png
            :width: 128
            :target: #connecting-on-windows

      -  :ref:`OSX <s_connecting_osx>`

         .. image:: images/os_macosx.png
            :width: 128
            :target: #connecting-on-osx

      -  :ref:`Linux <s_connecting_linux>`

         .. image:: images/os_linux.png
            :width: 128
            :target: #connecting-on-linux

.. _s_connecting_windows:

***********************
 Connecting on Windows
***********************

To connect to Esrum you will first have to connect to the UCPH VPN. For
information about connecting to the VPN when using Windows, see the
support pages on KUnet in Danish_ and English_.

Windows users will additionally need to install an SSH client in order
to be able to connect to the Esrum head node. Options include
MobaXterm_, Putty_, Windows Subsystem for Linux (WSL_), and many more.

The following demonstrates how to connect using MobaXterm, but you are
welcome to use any SSH client that you prefer. If using WSL_, then see
the :ref:`s_connecting_linux` section.

.. _s_configure_mobaxterm:

Configuring MobaXterm
=====================

#. Install and open MobaXterm_.

#. Click left-most button, labeled ``Session``, on the toolbar.

   .. image:: images/mobaxterm_01.png
      :align: center

#. Click on the left-most button, labeled ``SSH``, in the resulting
   ``Session settings`` dialog

   .. image:: images/mobaxterm_02.png
      :align: center

#. Under ``Basic SSH settings``

   #. Write ``esrumhead01fl.unicph.domain`` under ``Remote Host``
   #. Click the checkbox next to ``Specify username`` and enter your
      UCPH username as shown.
   #. Select ``SCP (enhanced speed)`` on the ``SSH-browser`` type
      drop-down menu. This is required for file-uploads to work.

   .. image:: images/mobaxterm_03.png
      :align: center

#. Click on the ``Bookmark settings`` tab and

   #. Write ``Esrum`` or a name you prefer under ``Session Name``

   #. Optionally click the ``Create a desktop shortcut to this session``
      button. This will create a shortcut on your desktop that connects
      to Esrum.

   .. image:: images/mobaxterm_04.png
      :align: center

#. Click OK and you should automatically connect to the server. If not,
   then see :ref:`s_reconnecting_with_mobaxterm` below. The first time
   you connect to Esrum (or any other server), you will be asked if you
   want to proceed. Simply press ``Accept``:

   .. image:: images/mobaxterm_05.png
      :align: center

   .. warning::

      If you receive this question again later, then stop and
      double-check that you are connected via the UCPH VPN, as the
      message could indicate that you are not actually connecting to
      Esrum!

#. You should now be able to log in to the server using your UCPH
   account password:

   .. image:: images/mobaxterm_06.png
      :align: center

#. For security reasons we recommend that you decline when asked if you
   want to save your password:

.. _s_reconnecting_with_mobaxterm:

Reconnecting with MobaXterm
===========================

To connect again another time, either use the desktop shortcut (if you
created it), double-click on ``Esrum`` in the list of sessions on the
left side of MobaXterm, select ``Esrum`` from the list that appears when
clicking on the ``Sessions`` button on the main menu, or click on
``Esrum`` in the list of ``Recent sessions``.

.. image:: images/mobaxterm_07.png
   :align: center

.. _s_network_drives_mobaxterm:

Accessing network drives via MobaXterm
======================================

In order to access your UCPH network drives (``H:``, ``N:``, and ``S:``)
via Esrum, you must disable logins using Kerberos (GSSAPI). To do so,
open the ``Configuration`` dialog as shown:

.. image:: images/mobaxterm_08.png
   :align: center

Select the ``SSH`` tab and then untick the ``GSSAPI Kerberos`` checkbox
as shown. Finally, click the ``OK`` button to close the options page:

.. image:: images/mobaxterm_09.png
   :align: center

.. _s_connecting_osx:

*******************
 Connecting on OSX
*******************

To connect to Esrum you will first have to connect to the UCPH VPN. For
information about connecting to the VPN using OSX, see the support pages
on KUnet in Danish_ and English_.

.. tip::

   While we recommend using the official UCPH VPN client for connecting
   to the VPN, as described in the documentation on KUnet, it is also
   possible to use the command-line ``openconnect`` as described in the
   :ref:`s_connecting_linux` section below.

.. _s_connecting_ssh:

Connecting to Esrum using ``ssh``
=================================

Once connected to the VPN, you can connect to the cluster using the
terminal command ``ssh``, replacing ``abc123`` with your UCPH username
in the following command:

.. code-block:: console

   $ ssh abc123@esrumhead01fl.unicph.domain

You will likely be informed that the ``the authenticity of host ...
can't be established``. This is expected *the first time you connect*
(see below), and you should simply type ``yes`` and press enter to
continue. Once you've done so, you can enter your UCPH account password,
and approve the connection via the NetIQ app.

.. code-block:: console
   :emphasize-lines: 5,7

   $ ssh abc123@esrumhead01fl.unicph.domain
   The authenticity of host 'esrumhead01fl.unicph.domain (10.84.4.168)' can't be established.
   ED25519 key fingerprint is SHA256:QslJ02Z/4CrFJ2pKA64lU8WTS8Y+8pGO+748bTkrFhY.
   This key is not known by any other names.
   Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
   Warning: Permanently added 'esrumhead01fl.unicph.domain' (ED25519) to the list of known hosts.
   abc123@esrumhead01fl.unicph.domain's password: *********
        __
       /  \
      _\__/  Welcome to esrumhead01fl
     (_)     University of Copenhagen
   _____O______________________________________
   Supported by UCPH IT  it.ku.dk/english

       Documentation is available at https://cbmr-data.github.io/esrum/
           For assistance contact Data Analytics at cbmr-esrum@sund.ku.dk,
       in #data-analytics at https://cbmr.slack.com/archives/C06TF9LGD47
           or find us in room 07-8-29 (Unit 8E) at the Maersk Tower.

   Last login: Tue Apr 22 13:52:08 2025 from 10.203.180.30
   $

.. warning::

   If you get a warning about the authenticity of Esrum at a later date,
   then please double-check that you are connected to the UCPH VPN. This
   message could mean that you are connecting to an entirely different
   server!

It is recommended to add an entry for the cluster to your
``.ssh/config`` file, replacing ``abc123`` with your UCPH username:

.. code-block:: console

   $ cat ~/.ssh/config
   Host esrum esrumhead01fl esrumhead01fl.unicph.domain
       HostName esrumhead01fl.unicph.domain
       User abc123

This allows you to connect to the server using the names ``esrum``,
``esrumhead01fl``, or ``esrumhead01fl.unicph.domain``, and without
having to specify your username:

.. code-block:: console

   $ ssh esrum
   abc123@esrumhead01fl.unicph.domain's password:
        __
       /  \
      _\__/  Welcome to esrumhead01fl
     (_)     University of Copenhagen
   _____O______________________________________
   Supported by UNICPH IT  it.ku.dk/english

   Last login: Fri Oct 13 01:35:00 1980 from 127.0.0.1
   $

.. note::

   Note that the cluster *does not* support authentication through a
   public SSH key and that you therefore have to enter your password
   when connecting to the server.

.. _s_connecting_linux:

*********************
 Connecting on Linux
*********************

The official instructions for connecting to the VPN under Linux (in
Danish_ and English_) are written under the assumption that you are
using KDE5.

Alternatively, you can open https://vpn.ku.dk in your browser, log in
with your KU ID, and download the "Cisco Secure Client" for Linux. Once
downloaded, open a terminal in the folder in which you downloaded the
installer, and run the following command:

.. code-block:: console

   $ sudo bash cisco-secure-client-linux64-*.sh

Once the installer has finished running, you should be able to find the
"Cisco Secure Client" in your start menu. Enter ``vpn.ku.dk`` as the VPN
server, use your short KU ID (e.g ``abc123``) as your username.

If you prefer a command-line solution, then you can also connect using
``openconnect`` v9.10 or later, replacing ``abc123`` with your UCPH
username. You will need to enter your password and use the
authentication method you have configured (here a TOTP code generator):

.. code-block:: console
   :emphasize-lines: 7,10

   $ sudo openconnect -u abc123 --useragent=AnyConnect --no-external-auth vpn.ku.dk
   POST https://vpn.ku.dk/
   Connected to 130.225.226.54:443
   SSL negotiation with vpn.ku.dk
   Connected to HTTPS on vpn.ku.dk with ciphersuite (TLS1.2)-(RSA)-(AES-256-CBC)-(SHA1)
   XML POST enabled
   Please enter your username and password.
   Password: ****************
   POST https://vpn.ku.dk/
   Please enter the TOTP code generated on your device
   Response: ****
   POST https://vpn.ku.dk/
   Got CONNECT response: HTTP/1.1 200 OK
   CSTP connected. DPD 30, Keepalive 20
   Established DTLS connection (using GnuTLS). Ciphersuite (DTLS1.2)-(ECDHE-RSA)-(AES-256-GCM).
   Configured as 10.203.179.174, with SSL connected and DTLS connected
   Session authentication will expire at Wed May  7 09:19:45 2025

Depending on how you have configured `multifactor authentication for
UCPH <https://mfa.ku.dk>`_, you will have to authenticate the login
using one of the following methods:

-  If using NetIQ, open the app on your phone and approve the login.
-  If asked, enter the time based one-time password (TOTP) generated by
   the app you have enrolled

.. note::

   It may be possible to authenticate using additional methods, such as
   Yubikeys, but we currently cannot offer a guide to using those with
   ``openconnect``.

You will likely have to install ``openconnect`` first, in which case
please refer to the documentation for the Linux distro you are using.
OSX users can install ``openconnect`` using Homebrew_.

Once you are connected to the VPN, you can follow the instructions in
the :ref:`s_connecting_ssh` section above for connecting to Esrum
itself.

.. _s_connecting_troubleshooting:

*****************
 Troubleshooting
*****************

.. include:: connecting_troubleshooting.rst
   :start-line: 8

.. _danish: https://kunet.ku.dk/medarbejderguide/Sider/It/Fjernadgang-vpn.aspx

.. _english: https://kunet.ku.dk/employee-guide/Pages/IT/Remote-access.aspx

.. _homebrew: https://brew.sh/

.. _mobaxterm: https://mobaxterm.mobatek.net/

.. _putty: https://www.putty.org/

.. _ssh: https://en.wikipedia.org/wiki/Secure_Shell

.. _tabby: https://github.com/Eugeny/tabby

.. _vpn: en.wikipedia.org/wiki/VPN

.. _wsl: https://learn.microsoft.com/en-us/windows/wsl/about
