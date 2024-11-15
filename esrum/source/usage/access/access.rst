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
additional approval from the data owners. We will guide you through this
process if you request access to a protected dataset.

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

**************************************
 Using the identity management system
**************************************

Should you need to apply for access to projects or datasets that are
*not* managed by the Data Analytics Platform, then this may require
using the `Identity Management System`_ (IDM). If possible, we recommend
simply asking the project/dataset owner to add you to the project or
dataset in question, but the following provides a brief summary of how
to apply through the IDM:

#. Login at identity.ku.dk_.

#. Click on the ``Manage My Access`` button. See below if you instead
   have a ``Manage User Access`` button.

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

#. Finally, click the ``Submit`` button to submit your request.

#. Wait for your request to be processed.

.. note::

   Users with project/group ownership will see a ``Manage User Access``
   button instead of the ``Manage User Access`` mentioned above.

   In that case, start by searching for your own UCPH username (e.g.
   ``abc123``) and then click on the check mark to the left your name
   *once*. Wait for the check mark to turn green, click the ``Next``
   button, and then proceed with the steps described above.

An official guide to the identity system used is available here_.

.. _here: https://kunet.ku.dk/medarbejderguide/ITvejl/KU%20IdM%20-%20S%C3%A5dan%20anmodes%20om%20funktionsrolle.pdf

.. _identity management system: https://identity.ku.dk/

.. _identity.ku.dk: https://identity.ku.dk/

.. _s_applying_for_projects:

.. _wsl: https://learn.microsoft.com/en-us/windows/wsl/about
