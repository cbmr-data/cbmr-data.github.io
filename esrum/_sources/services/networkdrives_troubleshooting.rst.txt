The ``~/ucph`` folder or subfolders are missing
================================================

Note that the ``~/ucph`` folder is only available on the head node
(``esrumhead01fl``), and not on the RStudio servers nor on the compute
nodes. See the :ref:`s_network_drives_compute_nodes` section for how to
access the drives elsewhere.

If you are connected to the head node, then firstly make sure that you are not using GSSAPI (Kerberos) to log in.
See the :ref:`p_usage_connecting` page for instructions for how to
disable this feature if you are using MobaXterm.

Once you have logged in to Esrum *without* GSSAPI enabled, and if the
folder(s) are still missing, then run the following command to create
any missing network folders:

.. code-block:: console

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

Note also that your login is also valid for about 10 hours, after which
you will lose access to the network drives. See the section
:ref:`s_network_drives_reactivation` for how to re-authenticate if your
access has timed out.

``kinit: Unknown credential cache type while getting default ccache``
======================================================================

The ``kinit`` command may fail if you are using a ``conda`` environment:

.. code-block:: console

   (base) $ kinit
   kinit: Unknown credential cache type while getting default ccache

In that case, run the command ``conda deactivate`` to deactivate the
current/base environment. This may require running ``conda deactivate``
multiple times; your terminal line should not start with ``(base)`` or
similar.
