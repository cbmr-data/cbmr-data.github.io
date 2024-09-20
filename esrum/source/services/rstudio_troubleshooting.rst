Incorrect or invalid username/password
======================================

Please make sure that you are entering your username in the short form
(i.e. ``abc123``) and that you have have applied for and been given
access to the Esrum HPC (see :ref:`s_applying_for_access`). If the
problem persists, please :ref:`p_contact` us for assistance.

Logging in takes a very long time
=================================

Similar to regular R, RStudio will automatically save the data you have
loaded into your R session and will restore it when you return later, so
that you can continue your work. However, this many result in large
amounts of data being saved and loading this data may result in a large
delay when you attempt to login at a later date.

It is therefore recommended that you regularly clean up your workspace
using the built in tools, when you no longer need to have the data
loaded in R.

You can remove individual bits of data using the ``rm`` function in R.
This works both when using regular R and when using RStudio. The
following gives two examples of using the ``rm`` function, one removing
a single variable and the other removing *all* variables in the current
session:

.. code:: r

   # 1. Remove the variable `my_variable`
   rm(my_variable)

   # 2. Remove all variables from your R session
   rm(list = ls())

Alternatively you can remove all data saved in your R session using the
broom icon on the ``Environment`` tab:

.. image:: /services/images/rstudio_gc_01.png
   :align: center

.. image:: /services/images/rstudio_gc_02.png
   :align: center

If you wish to prevent this issue in the first case, then you can also
turn off saving the data in your session on exit and/or turn off loading
the saved data on startup. This is accomplished via the ``Global
Options...`` accessible from the ``Tools`` menu:

.. image:: /services/images/rstudio_gc_03.png
   :align: center

Should your R session have grown to such a size that you simply cannot
login and clean it up, then it my be necessary to remove the files
containing the data that R/RStudio has saved. This data is stored in two
locations:

#. In the ``.RData`` file in your home (``~/.RData``). This is where R
   saves your data if you answer yes ``Save workspace image? [y/n/c]``
   when quitting R.

#. In the ``environment`` file in your RStudio session folder
   (``~/.local/share/rstudio/sessions/active/session-*/suspended-session-data/environment``).
   This is where Rstudio saves your data should your login time-out
   while using RStudio.

Please :ref:`p_contact` us and we can help you remove the correct files.

libstdc++.so.6: version ``'GLIBCXX_3.4.26'`` not found
======================================================

See the troubleshooting section on the :ref:`p_service_r` page.
