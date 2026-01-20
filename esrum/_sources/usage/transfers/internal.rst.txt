.. _p_internal_transfers:

#########################
 Internal data transfers
#########################

This page describes how to transfer data that is already on Esrum, to
another location on Esrum. All transfers must be performed on a compute
node, as described below. Transfers running on the head node, or on the
RStudio nodes, will be terminated on sight, as these impact all users of
those nodes.

.. _p_transfer_projects_datasets:

************************************************
 Transferring data between projects or datasets
************************************************

As a rule of thumb, data should only be located in one project or
dataset folder. However, should you need to make a copy of one or more
files, then it is recommended to use the ``rsync`` command to do so. See
the :ref:`s_rsync_basics` section below for more information.

You *must* run your copy commands (whether you use ``rsync``, ``cp``, or
some other tool) on a compute node, either in an :ref:`interactive
sessions <s_interactive_session>`, or by using ``srun`` to execute the
command on a compute node, as shown in the examples below. See the
:ref:`p_usage_srun` section for more information about using ``srun``.

#. If you are copying data from a ``/projects`` folder, use the command

   .. code-block:: console

      srun rsync -av --progress /copy/this/data/ /to/this/location/

#. If you are copying data from a ``/datasets`` folder, use the command

   .. code-block:: console

      srun rsync -av --no-perms --progress /copy/this/data/
      /to/this/location/

.. include:: common_tips.rst

.. _p_transfer_network_drives:

************************************************
 Copying data to/from the H:, N:, and S: drives
************************************************

To avoid impacting other users, you must run transfers on compute nodes.
However, as described on the :ref:`p_network_drives` page, the ``H:``,
``N:``, and ``S:`` drives are not accessible from compute nodes by
default.

Therefore, you must start an interactive session, log in using the
``/usr/bin/kinit`` command, and then access the network drives via the
``/maps`` folder:

.. code-block:: bash

   # Start an interactive session
   srun --pty -- /bin/bash
   # Log in to enable the network drives
   /usr/bin/kinit
   # View my H: drive; '${USER}' corresponds to your abc123 username
   ls /maps/hdir/${USER}/

Your login will expire after about 12 hours, at which point you have to
run ``/usr/bin/kinit`` on the node again. However, while your login is
active, your network folders can be found at the following locations:

+---------+-----------------------------+
| Drive   | Location                    |
+=========+=============================+
| ``H:``  | ``/maps/hdir/${USER}``      |
+---------+-----------------------------+
| ``S:``  | ``/maps/sdir/${USER}``      |
+---------+-----------------------------+
| ``N:``  | ``/maps/groupdir/${USER}``  |
+---------+-----------------------------+

Note that these folders will be only created once you attempt to access
them, provided that you have logged in using ``/usr/bin/kinit``.

It is recommended to use ``rsync`` to copy data to/from the
network-drives, as described below, but you do *not* need to use
``srun`` in this case, as you are already working in an interactive
session if you followed the instructions above.

.. include:: common_tips.rst

.. _s_rsync_basics:

**************
 Rsync basics
**************

``rsync`` allows you to recursively copy data between two locations,
either on the same system or between two different systems (via SSH).
Unlike plain ``cp``, it is also easy to resume a transfer that has been
interrupted, simply by running ``rsync`` again.

The basic ``rsync`` command you should be using is

.. code-block:: bash

   rsync -av --progress /copy/this/data/ /to/this/location/

-  The ``-a`` option enables "archive" mode, which preserves
   meta-information such as timestamps and permissions.

-  The ``-v`` option and the ``--progress`` options are optional, but
   make ``rsync`` list the last copied file and the progress when
   copying (large) files.

-  The paths in the above example both ends in a ``/``. This is
   intentional, and makes ``rsync`` copy the content of ``data`` into
   the folder ``location``. If you instead ran ``rsync -av --progress
   /copy/this/data /to/this/location/``, then the ``data`` folder would
   be placed at ``/to/this/location/data``

However, when copying data from a ``/datasets`` it is necessary to add
the ``--no-perms`` options, since ``rsync`` would otherwise set all
permissions to ``000``, due to how access-control is implemented for
``/datasets``. See the troubleshooting section below if you forget to
add this option.

You *must* run ``rsync`` command on a compute node, either in an
:ref:`interactive sessions <s_interactive_session>`, or by using
``srun`` to automatically run the command on a compute node. See the
:ref:`p_usage_srun` section for more information about using ``srun``.

.. _s_transfer_instruments:

*************************************************
 Copying instrument data to projects or datasets
*************************************************

As the `/labs` folders are currently only accessible from the head node,
it is necessary to run the transfers directly on the head node. This is
the *only* case where it is permitted to run transfers on the head node,
and these transfers *must* be rate-limited to at most 50 MB/s (total)
using the ``rsync --bwlimit`` option:

.. code-block:: shell

   $ rsync -av --no-perms --progress=summary --bwlimit=50M /from/path/ /to/path/

.. warning::

   Similarly to ``/datasets`` folders, all files and folders on
   ``/labs`` drives have permissions ``000``, i.e. no read and no write
   access, even when you have access to the data. For this reason, you
   *must* include the ``--no-perms`` option when running ``rsync``, to
   prevent ``rsync`` from recreating these permissions. If you omit
   ``--no-perms``, then ``rsync`` normally fails during the transfer due
   not being able to write to the destination.

If you run transfers without rate limits (include using `cp` or `mv` to
copy/move data in or out of `/labs` folders), or if you run transfers
with a total rate limit above 50 MB/s, then these will be terminated to
prevent them from impacting other users of Esrum.

See :ref:`s_transfer_instruments` for more information.

*****************
 Troubleshooting
*****************

.. include:: internal_troubleshooting.rst
   :start-line: 8

.. include:: /services/networkdrives_troubleshooting.rst
   :start-line: 8
