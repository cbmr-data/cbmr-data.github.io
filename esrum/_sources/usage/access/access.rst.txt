.. _p_usage_access_applying:

#####################
 Applying for access
#####################

The following describes how to apply for access to the Esrum cluster and
related services, projects, and datasets. You are always welcome to
:ref:`p_contact` us if you have any questions or run into any problems
applying for access to the cluster.

An official guide to the identity system used is available here_.

.. _s_applying_for_access:

************************************
 Applying for access to the cluster
************************************

#. Login at identity.ku.dk_.

#. Click on the ``Manage My Access`` button. See below if you instead
   have a ``Manage User Access`` button.

#. Search for ``SRV-esrumhead-users``.

#. Click *once* on the check mark to the left of ``SRV-esrumhead-users``
   in the resulting list. Wait for the check mark to turn green and then
   click the ``Next`` button.

   .. note::

      If you get a yellow popup with the message "Cannot Add Access
      Item. The item you are trying to select is already assigned", then
      you have already been granted access and you can simply proceed to
      the :ref:`s_applying_for_projects` section or the
      :ref:`p_usage_connecting` page.

#. Verify that you are applying for access to ``SRV-esrumhead-users``.
   Do *not* apply for access to the ``SRV-esrumhead-admin`` group. Once
   you have verified that you are applying for access the correct group,
   click the ``Submit`` button.

#. Wait for your request to be processed.

.. note::

   Users with project/group ownership will see a ``Manage User Access``
   button instead of the ``Manage User Access`` mentioned above.

   In that case, start by searching for your own UCPH username (e.g.
   ``abc123``) and then click on the check mark to the left your name
   *once*. Wait for the check mark to turn green, click the ``Next``
   button, and then proceed with the steps described above.

Once you have been granted access you will receive an email that
``Changes to your Identity were processed``. This process may take up to
a day.

Once you have been granted access and your account is ready (see below),
you may refer to the :ref:`p_usage_connecting` page for instructions on
how to connect to the cluster.

.. warning::

   Please note that your account may not be ready by the time you
   receive the email described above. In that case, logging in will
   result in a warning that your home folder does not exist. If so, then
   simply wait a few hours before trying again.

.. _s_applying_for_projects:

*********************************
 Applying for access to projects
*********************************

You can apply for access to projects using the same method as described
in `Applying for access to the cluster`_. Alternatively, the project
owner(s) can add you to their projects directly. However, the Data
Analytics Platform cannot add you to projects owned by a third party.

See :ref:`s_project_folders` for a description of the location and
file-structure of projects on Esrum.

.. warning::

   Similar to the ``-admin`` group mentioned above for the cluster, each
   project and dataset has a corresponding ``-Owners`` group. Do *not*
   apply for access to these unless explicitly instructed to do so! Your
   requests *will* be denied and that will delay your getting access to
   the actual projects/datasets.

*****************************************
 Applying for access to datasets/cohorts
*****************************************

.. warning::

   Transfer of data to the new servers has not yet been completed. You
   can still apply for access to cohorts, but you may not be granted
   access until everything is ready.

In order to apply for access to a dataset, simply follow the steps
described in the `Applying for access to the cluster`_ section and
substitute ``SRV-esrumhead-users`` with the name of your project.

.. note::

   Access to datasets managed by the Data Analytics Platform requires
   permission from the data-manager responsible for that data. The Data
   Analytics Platform will verify that you are permitted to access the
   data before granting access. You may speed up this process by having
   the data manager :ref:`p_contact` us in advance with a written
   approval.

.. _here: https://kunet.ku.dk/medarbejderguide/ITvejl/KU%20IdM%20-%20S%C3%A5dan%20anmodes%20om%20funktionsrolle.pdf

.. _identity.ku.dk: https://identity.ku.dk/

.. _wsl: https://learn.microsoft.com/en-us/windows/wsl/about
