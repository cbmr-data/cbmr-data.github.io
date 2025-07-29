.. _p_service_rstudio:

#########
 RStudio
#########

This page describes how to access the RStudio_ servers available to
users of Esrum. For general tips on using R, see the :ref:`p_tips_r`
page.

The Rstudio servers can be found at
   #. https://esrumweb01fl/rstudio/
   #. https://esrumweb02fl/rstudio/

To access the RStudio servers, you *must* have applied for access as
described on the :ref:`p_usage_access_applying` page, and you *must* be
connected via the UCPH VPN.

.. warning::

   If you use a non-UCPH device to access the above URLs, then you may
   receive a warning that "your connection is not private" (Chrome) or
   about a "potential security risk" (Firefox). This is due to the
   domains using certificates provided by KU-IT, that are only installed
   on KU-IT managed hardware. You can proceed by clicking the "Advanced"
   button and then clicking either the ``Proceed to esrumweb??fl
   (unsafe)`` (Chrome) link or the ``Accept the Risk and Continue``
   button (Firefox).

Once connected, use the short form of your UCPH username to log in:

.. image:: images/rstudio_login.png
   :align: center

If you have not been granted access, or if you are not connected via the
VPN, then you will likely see a browser error message like ``This site
can't be reached``. See :ref:`p_usage_connecting` for more information.

.. warning::

   The RStudio servers are *only* for running R. If you need to run
   other tasks then you *must* connect to the head node and run them
   using Slurm as described in :ref:`p_usage_slurm`.

   Resource intensive tasks running on the RStudio server will likely
   negatively impact everyone using the service, and we may therefore
   terminate such tasks without warning if we deem it necessary.

***************************************
 Accessing network drives from RStudio
***************************************

By default, you will not be able to access the network drives (``H:``,
``N:``, and ``S:``) from the RStudio nodes. For information on how to
enable access and where to find the network drives on the RStudio nodes,
see the :ref:`p_network_drives` page.

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
   RStudio, that you use that subset of data to develop your analyses
   processes, and that you use that to process your complete dataset via
   an R-script submitted to Slurm as described in :ref:`p_usage_slurm`.

   See the :ref:`p_tips_r` page for additional guidance on how to use R
   with Slurm.

-  Don't keep data in memory that you do not need. Data that you no
   longer need can be freed with the ``rm`` function or using the broom
   icon on the ``Environment`` tab in RStudio. This also helps prevent
   RStudio from filling your home folder when your session is closed
   (see Troubleshooting below).

-  Do not run resource intensive tasks via the embedded terminal. As
   noted above, such tasks will be terminated without warning if deemed
   to have a negative impact on other users. Instead, such tasks should
   be run using Slurm as described in :ref:`p_usage_slurm`.

************************
 Preserving loaded data
************************

Data that you have loaded into R and other variables you have defined
are visible on the ``Environment`` tab in RStudio along with the amount
of memory used (here 143 MiB):

.. image:: images/rstudio_environment.png
   :align: center

By default, this data will be saved to your RStudio folder on the
``/scratch`` drive when you quit your session or when it automatically
suspends after 9 hours of inactivity. This may, however, result in very
large amounts of data being saved to disk and, consequently, large of
amounts of data having to be read when you log in again, resulting in
logging in taking a very long time.

For this reason we recommend disabling the saving and loading of
``.RData`` in the ``Global Settings`` accessible via the ``Tools Menu``
as shown:

.. image:: images/rstudio_workspace_data.png
   :align: center

This ensures that you always start with a fresh session and that you
therefore are able to log in quickly to the RStudio server.

It is also recommended that the ``Always save history (even when not
saving .RData)`` option is enabled, as the commands you type into the R
terminal will otherwise *not* be saved.

.. _s_rstudio_copilot:

***********************
 Use of GitHub Copilot
***********************

You can make use of GitHub Copilot_ in RStudio, provided that you have a
valid license. Please refer to the :ref:`guidelines on use of generative
AI and LLMs <s_guidelines_llms>` before doing so.

-  To enable Copilot_, click on the ``Tools`` menu and select ``Global
   Options``:

   .. image:: images/rstudio_copilot_1.png
      :align: center

-  Open the ``Copilot`` tab and tick the ``Enable Github Copilot``
   checkbox. Then click the ``Sign In`` button:

   .. image:: images/rstudio_copilot_2.png
      :align: center

-  Finally, copy the verification code you are shown, click on the
   displayed link, and follow the instructions on Github.

*****************
 Troubleshooting
*****************

.. include:: rstudio_troubleshooting.rst

.. _copilot: https://github.com/features/copilot

.. _gcc: https://gcc.gnu.org/

.. _heads: https://heads.ku.dk/

.. _rstudio: https://posit.co/products/open-source/rstudio/
