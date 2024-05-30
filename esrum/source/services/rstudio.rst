.. _p_service_rstudio:

#########
 RStudio
#########

An RStudio_ server is made available at http://esrumweb01fl:8787/. To
use this server, you must

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

   See also above for a brief example of how to submit R scripts to
   Slurm.

-  Don't keep data in memory that you do not need. Data that you no
   longer need can be freed with the ``rm`` function or using the broom
   icon on the ``Environment`` tab in Rstudio, as described below. This
   also helps prevent RStudio from filling your home folder when your
   session is closed (see Troubleshooting below).

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
