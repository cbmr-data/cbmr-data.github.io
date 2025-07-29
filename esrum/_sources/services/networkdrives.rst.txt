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
compute node/RStudio server, then the network drives may be
inaccessible. This will typically result in ``No such file or
directory`` errors when attempting to access files/folders on the
network drives.

To (re-)authenticate and thereby enable access to the network drives,
run the ``kinit`` command and enter the password for your UCPH account:

.. code-block:: console

   $ kinit
   abc123@UNICPH.DOMAIN's password: ************
   $

See the troubleshooting section below, if you get the error message
``kinit: Unknown credential cache type while getting default ccache``.

Once you have successfully run ``kinit``, you should be able to access
the folders under ``~/ucph`` on the head node, or at their canonical
locations on other nodes (see :ref:`s_network_drives_compute_nodes`).
However, if you have tried to access these folders within the last few
minutes, before running ``kinit``, then you may have to wait a few
minutes before the folders become accessible again.

*********************************************
 Extending your access to the network drives
*********************************************

The maximum duration of your current session (Kerberos ticket) is about
10 hours, and the time at which it expires can be viewed via the
``klist`` command:

.. code-block:: console

   $ klist
   Ticket cache: KEYRING:persistent:436828696:krb_ccache_nBciOlx
   Default principal: abc123@UNICPH.DOMAIN

   Valid starting       Expires              Service principal
   07/29/2025 11:22:49  07/29/2025 21:22:49  krbtgt/UNICPH.DOMAIN@UNICPH.DOMAIN
       renew until 08/03/2025 21:55:43

In this case the current session expires at ``07/29/2025 21:22:49``, but
you can renew it for another 10 hours, until the time specified on the
``renew until`` line.

To renew your session, use the ``kinit -R`` command. Unlike the basic
``kinit`` command, this does not require that you enter your password:

.. code-block:: console

   $ kinit -R
   abc123@esrumhead01fl:~$ klist
   Ticket cache: KEYRING:persistent:436828696:krb_ccache_nBciOlx
   Default principal: abc123@UNICPH.DOMAIN

   Valid starting       Expires              Service principal
   07/29/2025 12:44:10  07/29/2025 22:44:10  krbtgt/UNICPH.DOMAIN@UNICPH.DOMAIN
    renew until 08/03/2025 21:55:43

If ``kinit -R`` fails with the message ``kinit: No credentials cache
found while renewing credentials``, then you are not authenticated and
need to run ``kinit`` without the ``-R`` as described in
:ref:`s_network_drives_reactivation`.

*****************
 Troubleshooting
*****************

.. include:: /services/networkdrives_troubleshooting.rst
