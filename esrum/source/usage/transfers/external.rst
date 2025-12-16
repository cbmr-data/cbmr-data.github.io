.. _p_external_transfers:

#########################
 External data transfers
#########################

This page describes methods for transferring data between Esrum and
other servers, local computers such as UCPH desktops and laptops, and
external services.

.. _s_sharing_projects:

*****************************************************
 Sharing projects and datasets between UCPH clusters
*****************************************************

``/projects`` and ``/datasets`` can be shared between multiple UCPH
clusters, similarly to how these are accessible from all Esrum nodes,
and it is therefore typically not necessary to transfer data between
different UCPH clusters.

To make a ``/projects`` or ``/datasets`` available on Esrum, or on
another UCPH cluster, contact UCPH-IT via the Serviceportal_, using the
``Research Applications Counseling and Support`` /
``Forskningsapplikationer Rådgivning og support`` ticket category.

.. _s_external_updownload:

****************************************************
 Transferring data between Esrum and another server
****************************************************

If you wish to transfer data from another server to Esrum, or vice
versa, then you have two options:

#. From Esrum, you can upload data to the other server or download data
   to Esrum. This requires that you can connect to the other server from
   Esrum. This option is preferable if it is expensive or otherwise
   difficult to run transfers on the other server.

#. From the other server, you can upload data to Esrum or download data
   from Esrum. This requires that you can run transfers on that server,
   and that it has internet/SSH access, which is typically the case.
   This option is preferable if it is difficult or impossible to connect
   to the server from Esrum.

.. warning::

   Do not attempt to transfer data using ``esrumhead01fl`` as the source
   or destination; small transfers to/from your home folder are
   permitted, but your home folder is also not intended to contain data.
   Larger transfers involving ``esrumhead01fl`` will be terminated
   without warning, due to the impact on other users

.. _s_external_from_esrum:

Running transfers on Esrum
==========================

Transfers from Esrum to another server must be run on compute node,
using either an :ref:`sbatch script <p_usage_slurm_basics>` or the
:ref:`srun command <p_usage_srun>`.

-  It is recommended to use ``rsync`` when possible. Additionally, you
   will need to use the ``--no-perms`` option if transferring data from
   a ``/datasets`` folder. See the :ref:`s_rsync_basics` for more
   information.

-  If the destination server only supports SFTP, then it is recommended
   to use the ``lftp`` to perform the transfer. This tool has a built-in
   ``mirror`` command, that allows you to upload/download directories
   recursively. See the :ref:`s_sif_erda_sftp` section for example usage
   and see the `lftp manual`_ for more information.

.. _s_transfer_from_external:

Running transfers on another server, laptop, or desktop
=======================================================

If you wish to run the transfers from another server, or from a laptop
or desktop, then you can connect to the server at ``sftp.ku.dk``. This
server allows you to access your projects, datasets, and network drives,
but *not* your home folder on Esrum (i.e. ``/home/abc123``). Unlike the
head node and RStudio nodes, you do not need to be connected to the UCPH
VPN to connect to ``sftp.ku.dk``.

OSX and Linux users can use tools such as ``sftp``, ``scp``, and
``rsync``. For most part, we recommend using ``rsync`` to transfer data
to/from ``sftp.ku.dk``, as described in the :ref:`s_rsync_basics`
section. You can also use graphical SFTP clients like FileZilla_. If you
use MobaXterm_ to connect to Esrum, as described in the :ref:`connecting
using Windows <s_connecting_windows>` section, then you also have access
to its built-in file manager.

Uploading/downloading data is done as shown above, except that you have
to use 2-factor authentication when connecting to ``sftp.ku.dk``,
depending on how you have configured `UCPH two-factor authentication`_.

.. code-block:: console

   $ rsync -av my-data/ abc123@sftp.ku.dk:/projects/my-project-AUDIT/data/my-data/
   (abc123@sftp.ku.dk) Enter password
   Password: **************
   (abc123@sftp.ku.dk) Enter one-time password
   Enter one-time password: ****

Official documentation is provided on the `UCPH computing/HPC Systems`_
pages on KUnet.

.. warning::

   Not all software can be used to connect to ``sftp.ku.dk``, due to the
   use of two-factor authentication. For example, ``lftp`` is known to
   fail to log in because of this.

.. _p_transfers_computerome:

*************************************************
 Transferring data between Esrum and Computerome
*************************************************

When transferring data/to from Computerome you should *always* run the
transfer software on Esrum (or on your PC/laptop) and you should
*always* connect to Computerome via ``transfer.computerome.dk`` instead
of ``ssh.computerome.dk``. For more information, see the `official
Computerome documentation`_.

For example, to transfer data from Esrum to Computerome, you might run

.. code-block:: console

   $ srun rsync -av ./ ${USERNAME}@transfer.computerome.dk:/home/projects/ab_12345/people/${USERNAME}/

This recursively transfers the current folder to a project folder on
Computerome using ``rsync``, with ``srun`` ensuring that the transfer is
run on a compute node on Esrum. ``${USERNAME}`` in the above is your
username on Computerome. For more information, see the
:ref:`s_external_from_esrum` section.

This avoids two big issues:

#. The Computerome administrators will terminate any attempts at
   transferring data via ``ssh.computerome.dk`` and may suspend your
   account if you keep trying. This applies both to running ``rsync`` on
   ``ssh.computerome.dk`` or if you attempt upload data to or download
   data from Esrum to ``ssh.computerome.dk``.

#. While it is possible to run a transfer on Computerome by running
   ``rsync`` or similar software on a Computerome node, this means
   paying for a Computerome node for the duration of the transfer.

See :ref:`s_external_from_esrum` above for more information.

.. _filezilla: https://filezilla-project.org/

.. _lftp manual: https://lftp.yar.ru/lftp-man.html

.. _mobaxterm: https://mobaxterm.mobatek.net/

.. _official computerome documentation: https://www.computerome.dk/wiki/high-performance-computing-hpc/file-transfer

.. _serviceportal: https://serviceportal.ku.dk/

.. _ucph computing/hpc systems: https://kunet.ku.dk/work-areas/research/Research%20Infrastructure/research-it/ucph-computing-hpc-systems/Pages/default.aspx

.. _ucph two-factor authentication: https://mfa.ku.dk/
