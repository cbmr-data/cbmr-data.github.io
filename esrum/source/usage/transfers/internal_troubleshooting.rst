######################################
 Dummy header to prevent reformatting
######################################

**************************************
 Dummy header to prevent reformatting
**************************************

``rsync`` fails with ``Permission denied`` when copying from ``/datasets``
==========================================================================

If you forget to use the ``--no-perms`` option when rsync'ing data out
of a ``/datasets`` folder, then all permissions will be set to ``000``.
In other words, nobody can read, write, or execute those files and
folders.

To fix this, first run the following commands to fix the permissions,
where ``/path/to/copied/data`` is the path to the copy of the data that
you have created.

.. code-block::

   chmod -R +rX,u+w /path/to/copied/data

This will recursively mark files and folders readable for everyone, mark
folders executable for everyone (required to browse them), and mark
files and folders writable for you (and only you).

Then re-run ``rsync`` and remember to include the ``--no-perms`` option.

``Permission denied`` when accessing data copied from ``/datasets``
===================================================================

See above.
