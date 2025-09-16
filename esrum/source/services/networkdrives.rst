.. _p_network_drives:

#############################
 Network drives (H:, N:, S:)
#############################

When you log in to Esrum for the first time, your home folder should
contain a (link to a) single folder named ``ucph``. This folder in turn
contains (links to) your UCPH network drives:

-  ``~/ucph/hdir``: The H-drive (``H:``) is your personal drive for
   storing data that is not shared with anyone else. This may include
   personal and confidential data.

-  ``~/ucph/ndir``: The N-drive (``N:``) is used shared data that is
   neither personal nor confidential. You will have access to any number
   of sub-folders depending on your affiliations, including the
   ``SUN-CBMR-Shared-Info`` folder containing files shared across the
   entire center.

-  ``~/ucph/sdir``: The S-drive (``S:``) is meant for sharing of
   sensitive and personal data with other employees at UCPH. For more
   information, see the `official documentation
   <https://kunet.ku.dk/employee-guide/Pages/IT/S-drive.aspx>`_.

.. tip::

   You can also access your network drives online via
   https://webfile.ku.dk/.

****************************************
 Limitations on network drives on Esrum
****************************************

By default, these network drives are only accessible from the head node,
and access is furthermore limited to about 10 hours after you logged in.
Additionally, these drives may not be available if you do not log in by
typing your password.

It is therefore recommended to always copy data that you are working to
the corresponding `/projects` folder. If you don't have a `/projects`
folder, then see the :ref:`p_usage_projects` page for instructions on
how to request a new project. Never store data in your home folder and
remember that projects have to be audited (indicated by the ``-AUDIT``
suffix) if you are working on sensitive/GDPR-protected data.

Should you be missing any of these folders, or should you be unable to
access the folders from the head node, then please see the
:ref:`s_filesystem_troubleshooting` section below.

.. _s_network_drives_compute_nodes:

*********************************************
 Accessing network drives from compute nodes
*********************************************

To access network drives from compute nodes and from RStudio sessions,
you first need to authenticate as described in the
:ref:`s_network_drives_reactivation` section below. Once you have done
so, you can access the network drives at their canonical locations:

+---------+-----------------------------+
| Drive   | Location                    |
+=========+=============================+
| ``H:``  | ``/maps/hdir/${USER}``      |
+---------+-----------------------------+
| ``S:``  | ``/maps/sdir/${USER}``      |
+---------+-----------------------------+
| ``N:``  | ``/maps/groupdir/${USER}``  |
+---------+-----------------------------+

The variable ``${USER}`` refers to *your* username, in the form
``abc123``. Note that the same time-limits apply, as when accessing the
network drives from the head node. These paths work on the head node, on
compute nodes, and on the RStudio nodes, provided that you have
authenticated as described below.

.. _s_network_drives_reactivation:

*********************************************
 (Re)activating access to the network drives
*********************************************

Should your login have timed out, should you have logged on to Esrum
without having entered your password, or should you be connected to a
compute node or an RStudio server, then the network drives may be
inaccessible. This will typically result in ``No such file or
directory`` errors when attempting to access files/folders on the
network drives.

To (re-)authenticate and thereby enable access to the network drives,
run ``/usr/bin/kinit`` and enter the password for your UCPH account:

.. code-block:: console

   $ /usr/bin/kinit
   abc123@UNICPH.DOMAIN's password: ************
   $

This command *must* be run on the server from which you wish to access
the network drives:

-  **From the head node:** Simply run ``/usr/bin/kinit`` while connected
   to the head node.

-  **From a compute node:** Start an interactive session as described in
   the :ref:`s_interactive_session` section, *and then* run
   ``/usr/bin/kinit``. You will then be able to access the network
   drives *in that session*.

-  **From an RStudio server**: Log in to the RStudio server as described
   on the :ref:`p_service_rstudio` page and open the ``Terminal`` tab.
   Run the command ``/usr/bin/kinit`` in that terminal.

.. warning::

   The explicit path in ``/usr/bin/kinit`` is required to make sure that
   you call the correct executable, even if you are using a Conda
   environment or similar. Running ``kinit`` without the full path may
   otherwise result in errors like ``kinit: Unknown credential cache
   type while getting default ccache``.

Once you have successfully run ``/usr/bin/kinit``, you should be able to
access the folders under ``~/ucph`` (only on the head node), or at their
canonical locations (see :ref:`s_network_drives_compute_nodes`).
However, if you have tried to access these folders within the last few
minutes, before running ``/usr/bin/kinit``, then you may have to wait a
few minutes before the folders become accessible again.

*********************************************
 Extending your access to the network drives
*********************************************

The maximum duration of your current session (Kerberos ticket) is about
10 hours, and the time at which it expires can be viewed via the command
``/usr/bin/klist``:

.. code-block:: console

   $ /usr/bin/klist
   Ticket cache: KEYRING:persistent:436828696:krb_ccache_nBciOlx
   Default principal: abc123@UNICPH.DOMAIN

   Valid starting       Expires              Service principal
   07/29/2025 11:22:49  07/29/2025 21:22:49  krbtgt/UNICPH.DOMAIN@UNICPH.DOMAIN
       renew until 08/03/2025 21:55:43

In this case the current session expires at ``07/29/2025 21:22:49``, but
you can renew it for another 10 hours, until the time specified on the
``renew until`` line.

To renew your session, use the ``/usr/bin/kinit -R`` command. Unlike the
basic ``/usr/bin/kinit`` command, this does not require that you enter
your password:

.. code-block:: console

   $ /usr/bin/kinit -R
   $ /usr/bin/klist
   Ticket cache: KEYRING:persistent:436828696:krb_ccache_nBciOlx
   Default principal: abc123@UNICPH.DOMAIN

   Valid starting       Expires              Service principal
   07/29/2025 12:44:10  07/29/2025 22:44:10  krbtgt/UNICPH.DOMAIN@UNICPH.DOMAIN
    renew until 08/03/2025 21:55:43

If ``/usr/bin/kinit -R`` fails with the message ``kinit: No credentials
cache found while renewing credentials``, then you are not authenticated
and need to run ``/usr/bin/kinit`` without the ``-R`` as described in
:ref:`s_network_drives_reactivation`.

*****************
 Troubleshooting
*****************

.. include:: /services/networkdrives_troubleshooting.rst
   :start-line: 8
