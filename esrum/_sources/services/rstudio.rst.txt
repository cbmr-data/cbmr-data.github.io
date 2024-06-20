.. _p_service_rstudio:

#########
 RStudio
#########

The RStudio_ server can be found at http://esrumweb01fl:8787/. To
connect to this server, you must

#. Be a member of the ``SRV-esrumweb-users`` group. Simply follow the
   steps in the :ref:`s_applying_for_access` section, and apply for
   access to this group.

#. Be connected via the KU VPN (a wired connection at CBMR is *not*
   sufficient). See :ref:`p_usage_connecting` for more information.

Once you have been been made a member of the ``SRV-esrumweb-users`` and
connected using the VPN or a wired connection at CBMR, simply visit
http://esrumweb01fl:8787/ and login using your KU credentials.

For your username you should use the short form:

.. image:: images/rstudio_login.png
   :align: center

.. warning::

   The RStudio server is *only* for running R. If you need to run other
   tasks then you *must* connect to the head node and run them using
   Slurm as described in :ref:`p_usage_slurm`.

   Resource intensive tasks running on the RStudio server will likely
   negatively impact everyone using the service and we will therefore
   terminate such tasks without warning if we deem it necessary.

************************
 Preserving loaded data
************************

Data that you have loaded into R and other variables you have defined
are visible on the ``Environment`` tab in RStudio along with the amount
of memory used (here 143 MiB):

.. image:: images/rstudio_environment.png
   :align: center

By default this data will be saved to your RStudio folder on the
``/scratch`` drive when you quit your session or when it automatically
suspends after 9 hours of inactivity. This may, however, result in very
large amounts of data being saved to disk and, consequently, large of
amounts of data having to be read when you login again, resulting in
login taking a very long time.

For this reason we recommend disabling the saving and loading of
``.RData`` in the ``Global Settings`` accessible via the ``Tools Menu``
as shown:

.. image:: images/rstudio_workspace_data.png
   :align: center

This ensures that you always start with a fresh session and that you
therefore are able to login quickly to the RStudio server.

It is also recommended to keep the ``Always save history (even when not
saving .RData)`` option enabled, as the commands you type into the R
terminal will otherwise *not* be saved.

******************************
 RStudio server best practice
******************************

Since the RStudio server is a shared resource where that many users may
be using simultaneously, we ask that you show consideration towards
other users of the server.

In particular,

-  Try to limit the size of the data-sets you work with on the RStudio
   server. Since *all* data has to be read from (or written to) network
   drives, one person reading or writing a large amount of data can
   cause significant slow-downs for *everyone* using the service.

   We therefore recommend that you load a (small) subset of your data in
   Rstudio, that you use that subset of data to develop your analyses
   processes, and that you use that to process your complete dataset via
   an R-script submitted to Slurm as described in :ref:`p_usage_slurm`.

   See the :ref:`p_service_r` page for additional guidance on how to use
   R with Slurm.

-  Don't keep data in memory that you do not need. Data that you no
   longer need can be freed with the ``rm`` function or using the broom
   icon on the ``Environment`` tab in Rstudio. This also helps prevent
   RStudio from filling your home folder when your session is closed
   (see Troubleshooting below).

-  Do not run resource intensive tasks via the embedded terminal. As
   noted above, such tasks will be terminated without warning if deemed
   to have a negative impact on other users. Instead such tasks should
   be run using Slurm as described in :ref:`p_usage_slurm`.

*****************
 Troubleshooting
*****************

See also the troubleshooting steps for :ref:`p_service_r`.

.. include:: rstudio_troubleshooting.rst

.. _argparser: https://cran.r-project.org/web/packages/argparser/index.html

.. _rstudio: https://posit.co/products/open-source/rstudio/
