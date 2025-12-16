.. _p_transfers_services:

################
 Cloud services
################

This page describes methods for transferring files between Esrum and
services such as cloud storage.

.. _s_transfers_sif_erda:

****************************************
 Transferring data to/from SIF and ERDA
****************************************

Connecting to the SIF_or ERDA_ servers requires that the user has
successfully authenticated using two-factor authentication. Furthermore,
this must be done using the same IP from which the user intends to
connect, in this case from the Esrum IP. Once authenticated, you can
transfer files using SFTP, as described below.

Authenticating on SIF
=====================

Authenticate with SIF from Esrum poses some challenges, as graphically
intensive programs like a full-fledged browser perform poorly over SSH.
Therefore, you must enable both X11-forwarding and SSH-compression
before attempting to run a browser (here Firefox):

-  Linux and OSX users can connect to Esrum using the command ``ssh -S
   none -C -X abc123@esrumhead01fl``, replacing ``abc123`` with your
   username. This ensures that we open a new connection (``-S none``),
   enables compression (``-C``), and enables X11-forwarding (``-X``).

-  Windows users using Mobaxterm should have both X11-forwarding and
   compression enabled by default. To verify this, right-click on your
   entry for Esrum in your session list and select ``Edit session``.
   Then open the ``Advanced SSH settings`` tab on the ``SSH`` page and
   verify that both the ``X11-forwarding`` and the ``Compression``
   checkboxes are checked.

As there are currently now browsers installed on Esrum, you will need to
install a copy of Firefox in your home. To do so, perform the following
steps:

.. code-block:: bash

   module load pixi/latest
   pixi global install firefox

Once you have verified that you are connected with both X11-forwarding
and compression enabled, and you have installed Firefox in your home,
start an interactive session on Esrum and start Firefox:

.. code-block:: bash

   srun --pty --x11 -- /bin/bash
   firefox "https://sif.ku.dk/"

Log in to SIF using your KU ID, once the browser window has opened, and
make sure to open the project you wish to transfer files to or from. You
will need to perform all subsequent steps in this interactive session,
or SIF will complain that you are not authenticated.

.. note::

   The Firefox browser will most likely be a bit sluggish, as a
   consequence of it running over SSH. If it is so sluggish that it is
   hard to interact with it, then double-check that you are connected
   with compression enabled.

.. _s_sif_erda_sftp:

Transferring files using SFTP
=============================

Once you have successfully authenticated you may connect to the SIF/ERDA
servers as normal using the tools available on Esrum.

The recommended way to transfer data to/from SIF/ERDA is using the
``lftp`` command. This allows you use the built-in ``mirror`` command to
recursively download entire folders. If you instead wish to upload a
folder recursively, simply use the ``mirror -R`` command instead of just
``mirror``.

For example, to download the contents of the folder ``my_data`` into a
project, you might run the following:

.. code-block:: console

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
   to log in! This is done on the ``Setup`` page described above.

The two ``set`` commands are required to prevent ``lftp`` from
performing simultaneous downloads (not supported by SIF) and to prevent
``lftp`` from re-trying repeatedly on failure. As SIF sends an email
every time you fail to log in, allowing retries typically means
receiving numerous emails if a transfer fails.

.. _s_transfers_google_cloud:

..
   ****************************************
   Transferring data to/from Google Cloud
   ****************************************

   TODO

.. _erda: https://erda.ku.dk/

.. _lynx: https://en.wikipedia.org/wiki/Lynx_(web_browser)
