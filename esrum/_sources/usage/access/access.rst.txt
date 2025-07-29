.. _p_usage_access_applying:

#####################
 Applying for access
#####################

Access to the Esrum HPC cluster and a number of related services,
projects, and datasets are managed by the Data Analytics Platform.
Access to the cluster and non-protected (non-GDPR) data can be obtained
simply by :ref:`contacting us <p_contact>` and asking for access. If you
are an external researcher, student, guest, and otherwise collaborating
with researchers at CBMR, then you should ask for one of your
collaborators at CBMR to :ref:`contact us <p_contact>` and request for
access.

Please note that access to (GDPR) protected data managed by DAP requires
additional approval from the data owners. For more information, please
see the :ref:`p_human_cohorts` for an overview of available datasets and
for instructions on how to apply for access.

Once you have been granted access to Esrum or a related resource you
will receive an automated email that ``Changes to your Identity were
processed``. Please refer to the :ref:`p_usage_connecting` page for
further instructions on how to connect to the cluster.

.. warning::

   Note that your account may not be ready by the time you receive the
   email described above. In that case, logging in will result in a
   warning that your home folder does not exist. If so, then simply wait
   a few hours before trying again. This process may take up to a day.

.. _s_identity_management_system:

********************************************
 Using the identity management system (IDM)
********************************************

Should you need to apply for access to projects or datasets that are
*not* managed by the Data Analytics Platform, or if you need to add a
user to a project that *you* control, then this may require using the
`Identity Management System`_ (IDM).

An official guide to the identity system used is available here_.

Applying for access using the IDM
=================================

If possible, we recommend simply asking the project/dataset owner to add
you to the project or dataset in question, but the following provides a
brief summary of how to apply through the IDM:

#. Log in at identity.ku.dk_.

#. Click on the ``Manage My Access`` or the ``Manage User Access``
   button. Which button you see will depend on whether you own any
   groups yourself.

   #. If you clicked on the ``Manage User Access`` button then you must
      next search for your own UCPH username (e.g. ``abc123``) and then
      click on the check mark to the left your name *once*. Wait for the
      check mark to turn green, click the ``Next`` button, and then
      proceed with the steps described above.

#. Search for and locate the group corresponding to the resource you
   wish to access. Depending on the kind of resource you wish to apply
   for access to, the names will differ somewhat:

   #. A server group will typically start with the prefix ``SRV-`` and
      end with ``-users``, for example ``SRV-esrumhead-users`` for the
      Esrum head node.

   #. A project group will typically start with ``COMP-PRJ-``, for
      example ``COMP-PRJ-cbmr_shared`` for the ``/projects/cbmr_shared``
      project.

   #. A dataset group will typically start with ``COMP-DATASET-`` and
      end with ``-ro``, for example ``COMP-DATASET-cbmr_shared-ro`` for
      the ``/datasets/cbmr_shared`` dataset containing shared resources.

   .. warning::

      In general, you should *not* be applying for access to projects
      with suffixes like ``-Owners``, ``-admin``, or ``-rw`` unless
      explicitly told to do so by the owner(s) of those resources. These
      suffixes indicate administrative groups and your requests will
      therefore be denied if you apply without reason.

#. Click *once* on the check-mark to the left of the name of the group
   in the resulting list. Wait for the check mark to turn green and then
   click the ``Next`` button. If you get a yellow popup with the message
   ``Cannot Add Access Item. The item you are trying to select is
   already assigned``, then you have already been granted access to this
   resource.

   #. If you get a ``Select Role`` popup, asking you to ``Select the
      business role to assign to this permitted role.``, then we
      recommend that you pick a ``STAFF-ORG`` role from the list.

#. Finally, click the ``Submit`` button to submit your request.

#. Wait for your request to be processed.

Adding users to a group using the IDM
=====================================

#. Log in at identity.ku.dk_.

#. Click on the ``Manage User Access`` button. If you instead have a
   ``Manage My Access`` button, then you do not control access to any
   groups and will not able to carry out these steps.

#. Search for the username of the user you want to add to a group, click
   *once* on the check-mark to the left of the name of the user in the
   resulting list. Wait for the check mark to turn green and then click
   the ``Next`` button.

#. Search for and locate the group corresponding to the resource you
   wish to grant access to. See the corresponding step in the previous
   guide, for a brief description of how groups are named.

#. Click *once* on the check-mark to the left of the name of the group
   in the resulting list. Wait for the check mark to turn green and then
   click the ``Next`` button. See above if you get a ``Cannot Add Access
   Item.`` or a ``Select Role`` popup.

#. Finally, click the ``Submit`` button to submit your request.

#. Wait for your request to be processed.

.. _here: https://kunet.ku.dk/medarbejderguide/ITvejl/KU%20IdM%20-%20S%C3%A5dan%20anmodes%20om%20funktionsrolle.pdf

.. _identity management system: https://identity.ku.dk/

.. _identity.ku.dk: https://identity.ku.dk/

.. _s_applying_for_projects:

.. _wsl: https://learn.microsoft.com/en-us/windows/wsl/about
