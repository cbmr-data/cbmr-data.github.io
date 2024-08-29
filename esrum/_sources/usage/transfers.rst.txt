.. _p_transfers:

###################
 Transferring data
###################

This section describes how to perform bulk data transfers between Esrum,
your PC/Laptop, and services such as SIF/Erda or Computerome. Several of
these sections may be useful on other systems than Esrum.

File transfers (including project-to-project transfers) should if at all
possible be run on a compute node, as high amounts of network traffic
may degrade performance on the head node for all users of the cluster.
See the :ref:`s_interactive_session` section for how to open a shell on
a compute node.

If you have an existing compute project or dataset on a UCPH-IT managed
cluster, then you may be able to connect it directly to the Esrum
cluster and thereby remove the need for transferring data entirely.
Please :ref:`p_contact` us for more information.

.. warning::

   Data must not be copied out of audited ``/datasets`` or ``/projects``
   folders without permission from the relevant data controller! See the
   :ref:`p_guidelines` for more information.

*********************************
 Transferring data to/from Esrum
*********************************

Users on a wired connection or using the VPN within CBMR can transfer
files to/from their PCs using any of the standard tools that connect via
SSH, including but not limited to ``scp``, ``sftp``, ``lftp``, and
``rsync``. Windows users may also consider graphical tools such as
FileZilla_ or MobaXterm (see the :ref:`p_usage_connecting` page).

When outside CBMR or when using the VPN is not feasible, one may instead
use the SSH/SFTP server at ``sftp.ku.dk``. Official documentation is
provided on the `UCPH computing/HPC Systems`_ pages on KUNet.

This services gives you access to all your projects and datasets:

.. code-block:: shell

   $ sftp sftp://abc123@sftp.ku.dk
   (abc123@sftp.ku.dk) Enter password
   Password: ******
   (abc123@sftp.ku.dk) Enter one-time password
   Enter one-time password: ******
   Connected to sftp.ku.dk.
   sftp> ls
   ucph
   sftp> cd ucph/
   sftp> ls
   datasets  hdir      ndir      projects

Depending on how you have configured `UCPH two-factor authentication`_,
you may either need to approve the connection attempt or (as shown
above) enter a one-time password

.. _p_tranfers_sifanderda:

************************************************
 Transferring data to/from the N: and H: drives
************************************************

As noted in the :ref:`s_ucph_network_drives` section, the `N:` and `H:`
drives are accessible via the `~/ucph` folder, but *only* from the head
node.

To avoid impacting other users, we therefore request that transfers to
or from these drives be carried out using `rsync` with rate-limiting in
place. This is accomplished using the `--bwlimit=50M` option, which
limits the transfer-rate to 50 MB/s on average (or ~20 seconds per GB).

The following command, for example, recursively copies the files in
`/from/path/` to the folder `/to/path/`, with a max transfer-rate of 50
MB/s:

.. code:: console

   $ rsync -av --progress=summary --bwlimit=50M /from/path/ /to/path/

It is furthermore recommended to run your transfer in a `tmux` (or
`screen`) instance. See the :ref:`p_tips_tmux` page for more
information. This allows your transfer to keep running after you log
off.

If you have need to transfer amounts of data that are not feasible with
this rate limit in place, then please :ref:`p_contact` us for
assistance.

.. warning::

   Transfers running on the head node, that are not rate-limited, will
   be terminated without warning due to the impact on other users of the
   cluster.

****************************************
 Transferring data to/from SIF and ERDA
****************************************

Connecting to the SIF_ or ERDA_ servers requires that the user has
successfully authenticated using Two Factor Authentication. Futhermore,
this must be done using the same IP from which the user intends to
connect, in this case from the Esrum IP.

This poses some challenges, as running a full-fledged browser over SSH
performs very poorly. This section therefore describes how to
authenticate to SIF_ or ERDA_ using a purely text-based browser
available on the cluster (Lynx_):

#. Start Lynx as follows:

         .. code:: shell

            lynx -accept_all_cookies "https://sif.ku.dk"

      .. image:: images/sif_login_01.png

#. Use the up/down arrow keys to select the ``log in`` link under ``I'm
   already signed up to SIF with my KU / UCPH account!`` and press
   ``enter``.

      .. image:: images/sif_login_02.png

#. Make sure that the ``Let me in without it, I want to try`` is
   highlighted and press enter to confirm that you wish to try login.

      .. image:: images/sif_login_03.png

#. Enter your UCPH username and password. Use the ``tab`` button to jump
   to the next field and ``Shift+Tab`` to jump to the previous field.
   Finally use ``tab`` to select the "Yes" button (appears as ``(BUTTON)
   Yes``) and press ``enter``.

      .. image:: images/sif_login_04.png

#. Enter your SIF two-factor code, press ``tab`` to select the
   ``Submit`` button, and press ``enter``.

      .. image:: images/sif_login_05.png

#. You should now see a page with the header ``SIF Project Management``,
   indicating that you have logged in:

      .. image:: images/sif_login_06.png

#. Press ``Ctrl+C`` to quit.

Once you have successfully authenticated you may connect to the SIF/ERDA
servers as normal using the tools available on Esrum.

The recommended way to transfer data to/from SIF/ERDA is using the
``lftp`` command. This allows you use the built-in ``mirror`` command to
recursively upload or download entire folders. For example, to download
the contents of the folder ``my_data`` into a project, you might run the
following:

.. code:: shell

   $ mkdir /projects/my_project-AUDIT/data/my_data
   $ cd /projects/my_project-AUDIT/data/my_data
   $ lftp sftp://sif-io.erda.dk
   > user ${YOUR_PROJECT_USERNAME}
   Password: ***********
   > set net:connection-limit 1
   > set net:max-retries 1;
   > cd my_data
   > mirror

Your project username (``${YOUR_PROJECT_USERNAME}``) is available via
the ``Setup`` page for each project once you log into SIF and typically
looks something like ``Johann.Gambolputty@sund.ku.dk@MyProject``.

.. warning::

   Remember to set a password for the project on SIF before attempting
   to login! This is done on the ``Setup`` page described above.

The two ``set`` commands are required to prevent lftp from performing
simultaneous downloads (not supported by SIF) and to prevent lftp from
re-trying repeatedly on failure. As SIF sends an email every time you
fail to login, allowing retries typically means receiving a large number
of emails if a transfer fails.

To upload a folder, simply use ``mirror -R`` instead of just ``mirror``.

.. _p_transfers_computerome:

***************************************
 Transferring data to/from Computerome
***************************************

When transferring data/to from computerome you should *always* run the
transfer software on Esrum (or on your PC/laptop) and you should
*always* connect to Computerome via ``transfer.computerome.dk`` instead
of ``ssh.computerome.dk``.

This avoids two big issues:

#. The Computerome administrators will terminate any attempts at
   transferring data via ``ssh.computerome.dk`` and may suspend your
   account if you keep trying. This applies both to running (for
   example) ``rsync`` on ``ssh.computerome.dk`` or if you attempt upload
   data to or download data from this server.

#. While it is possible to transfer data to/from Computerome from/to
   Esrum by running your software on a node, this involves paying for an
   node on computerome for the duration of the transfer.

See the `official Computerome documentation`_ for more information.

.. _erda: https://erda.ku.dk/

.. _filezilla: https://filezilla-project.org/

.. _lynx: https://en.wikipedia.org/wiki/Lynx_(web_browser)

.. _official computerome documentation: https://www.computerome.dk/wiki/high-performance-computing-hpc/file-transfer

.. _sif: https://sif.ku.dk/

.. _ucph computing/hpc systems: https://kunet.ku.dk/work-areas/research/Research%20Infrastructure/research-it/ucph-computing-hpc-systems/Pages/default.aspx

.. _ucph two-factor authentication: https://mfa.ku.dk/
