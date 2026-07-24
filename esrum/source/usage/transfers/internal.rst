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

1. If you are copying data from a ``/projects`` folder, use the command

   .. code-block:: console
       :class: remote-command

       srun rsync -av --progress /copy/this/data/ /to/this/location/

2. If you are copying data from a ``/datasets`` folder, use the command

   .. code-block:: console
       :class: remote-command

       srun rsync -av --no-group --chmod=ugo=rwX --progress /copy/this/data/
       /to/this/location/

.. warning::

    Transfers running on the head node will be terminated without
    warning, due to the impact on other users of the cluster.

.. include:: common_tips.rst

.. _p_transfer_network_drives:

************************************************
 Copying data to/from the H:, N:, and S: drives
************************************************

To avoid impacting other users, you should run transfers on compute
nodes, if at all possible.

However, as of 2026-05-05, most users are unable to access the network
drives from compute and RStudio nodes. Therefore, if the instructions in
the :ref:`p_transfer_network_drives_compute` section do not work, then
please see the :ref:`p_transfer_network_drives_head` below for how to
run the transfer on the head node.

.. _p_transfer_network_drives_compute:

Copying data to/from network drives and compute nodes
=====================================================

As described on the :ref:`p_network_drives` page, the ``H:``, ``N:``,
and ``S:`` drives are not accessible from compute nodes by default.

To access the network drives from a compute node, you must first start
an interactive session, and *then* log in using the ``/usr/bin/kinit``
command. Once you have done this, you should be able to access the
network drives via the ``/maps`` folder:

.. code-block:: console
    :class: remote-command

    # 1. Start an interactive session
    srun --pty -- /bin/bash
    # 2. Log in to enable the network drives
    /usr/bin/kinit
    # 3. View my H: drive; '${USER}' corresponds to your abc123 username
    ls /maps/hdir/${USER}/

If you get the error message that ``ls: cannot access
'maps/hdir/abc123/': No such file or directory``, then skip to the
:ref:`next section <p_transfer_network_drives_head>`. Otherwise continue
reading this section:

Your login will expire after about 12 hours, at which point you have to
run ``/usr/bin/kinit`` on the node again. However, while your login is
active, your network folders can be found at the following locations:

====== ==========================
Drive  Location
====== ==========================
``H:`` ``/maps/hdir/${USER}``
``S:`` ``/maps/sdir/${USER}``
``N:`` ``/maps/groupdir/${USER}``
====== ==========================

Note that these folders will be only appear once you attempt to access
them, so running ``ls /maps/groupdir`` will not show your folder unless
you have previously tried to ``cd`` to it, ``ls`` it directly, or
similar.

It is recommended to use ``rsync`` to copy data to/from the
network-drives, as described in the :ref:`s_rsync_basics` section below,
but you do *not* need to use ``srun`` in this case, as you are already
working in an interactive session if you followed the instructions
above.

.. tip::

    You should not use ``--bwlimit=50M`` when running transfers on a
    compute node. This limit on the rate of transfers is only required
    when performing transfers on the head node.

.. _p_transfer_network_drives_head:

Copying data to/from network drives and the head node
=====================================================

.. attention::

    If you are currently in an interactive session on a compute node,
    you need to either exit that session first, or connect to the
    head-node again, before following these instructions.

If the instructions in the :ref:`p_transfer_network_drives_compute`
section do not work, then you have to run the transfer on the head node.
However, to avoid negatively impacting other users of Esrum, we require
that these transfers are rate-limited to at most 50 MB/s (total) using
the ``rsync --bwlimit=50M`` option, and that you run no more than a
single transfer at a time:

.. code-block:: console
    :class: remote-command

    $ rsync -av --progress=summary --bwlimit=50M /from/path/ /to/path/

If you run transfers without rate limits (include using ``cp`` or
``mv``), or if you run transfers with a total rate limit above 50 MB/s,
then these will be terminated to prevent them from impacting other users
of Esrum.

If you have an urgent need to transfer data from a network drive, or if
the size of the data is so large that 50 MB/s (or roughly 6 hours per
TB) is not feasible, then please :ref:`contact us <p_contact>`.

.. include:: common_tips.rst

.. _s_transfer_instruments:

*************************************************
 Copying instrument data to projects or datasets
*************************************************

As the ``/labs`` folders are currently only accessible from the head
node, it is necessary to run the transfers directly on the head node.
These transfers *must* be rate-limited to at most 50 MB/s (total) using
the ``rsync --bwlimit=50M`` option, and you must not run more than a
single transfer at a time:

.. code-block:: console
    :class: remote-command

    $ rsync -av --no-perms --chmod=ugo=rwX --progress=summary --bwlimit=50M /from/path/ /to/path/

If you run transfers without rate limits (include using ``cp`` or
``mv``), or if you run transfers with a total rate limit above 50 MB/s,
then these will be terminated to prevent them from impacting other users
of Esrum.

If you have an urgent need to transfer instrument data, or if the size
of the data is so large that 50 MB/s (or roughly 6 hours per TB) is not
feasible, then please :ref:`contact us <p_contact>`.

.. _s_rsync_basics:

**************
 Rsync basics
**************

``rsync`` allows you to recursively copy data between two locations,
either on the same system or between two different systems (via SSH).
Unlike plain ``cp``, it is also easy to resume a transfer that has been
interrupted, simply by running ``rsync`` again.

The basic ``rsync`` command you should be using is

.. code-block:: console
    :class: generic-command

    rsync -av --progress /copy/this/data/ /to/this/location/

- The ``-a`` option enables "archive" mode, which preserves
  meta-information such as timestamps and permissions.
- The ``-v`` option and the ``--progress`` options are optional, but
  make ``rsync`` list the last copied file and the progress when copying
  (large) files.
- The paths in the above example both ends in a ``/``. This is
  intentional, and makes ``rsync`` copy the content of ``data`` into the
  folder ``location``. If you instead ran ``rsync -av --progress
  /copy/this/data /to/this/location/``, then the ``data`` folder would
  be placed at ``/to/this/location/data``

When transferring data from ``/datasets`` or from ``/labs`` you *must*
include the ``--no-perms --chmod=ugo=rwX`` options, to prevent ``rsync``
from setting the permissions on all transferred files and folders to
``000``. If that happens, then neither you nor ``rsync`` can access the
transferred data and the transfer will likely fail partway through. See
the troubleshooting section below if you forgot to add this option.

If you are running the transfer on the head node, which is only
permitted for transfers to/from the ``N:``, ``H:``, and ``S:`` drives,
or to/from the ``/labs`` folders, then you *must* use the option
``--bwlimit=50M`` to limit the rate of the transfer. Transfers running
without this limit, and simultaneous transfers adding up to more than
this limit, will be terminated.

*****************
 Troubleshooting
*****************

.. include:: internal_troubleshooting.rst
    :start-line: 8

.. include:: /usage/storage/networkdrives_troubleshooting.rst
    :start-line: 8
