######################################
 Dummy header to prevent reformatting
######################################

**************************************
 Dummy header to prevent reformatting
**************************************

``Connection refused`` when running ``sacct`` / ``sacct-usage``
===============================================================

If you attempt to run ``sacct`` or ``sacct-usage`` on any other node
than the head node, then you may get an error message like this:

.. code-block:: console

   sacct: error: slurm_persist_conn_open_without_init: failed to open persistent connection to host:localhost:6819: Connection refused
   sacct: error: Sending PersistInit msg: Connection refused
   sacct: error: Problem talking to the database: Connection refused

To avoid this, only run ``sacct`` and ``sacct-usage`` on the head node.
