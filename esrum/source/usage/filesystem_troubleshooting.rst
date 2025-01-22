The ``~/ucph`` folder or subfolders are missing
================================================

Firstly, make sure that you are not logging in GSSAPI (Kerberos) to
login. See the :ref:`p_usage_connecting` page for instructions for how
to disable this feature if you are using MobaXterm.

Once you have logged in to Esrum *without* GSSAPI enabled, and if the
folder(s) are still missing, then run the following command to create
any missing network folders:

.. code-block::

   $ bash /etc/profile.d/symlink-ucphmaps.sh

Once this is done, you should have a ``ucph`` symlink in your home
folder containing links to ``hdir`` (``H:``), ``ndir`` (``N:``), and
``sdir`` (``S:``).

``No such file or directory`` when accessing network drives
============================================================

If you get a ``No such file or directory`` error when attempting to
access the network drives (``~/ucph/hdir``, ``~/ucph/ndir``, or
``~/ucph/sdir``), then please make sure that you are not logging in
using Kerberos (GSSAPI). See the :ref:`s_network_drives_mobaxterm`
section for instructions for how to disable this feature if you are
using MobaXterm.
