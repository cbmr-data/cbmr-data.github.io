.. _p_identity_management_system:

############################
 Identity Management System
############################

Should you need to apply for access to projects or datasets that are
*not* managed by the Data Analytics Platform, or if you need to add a
user to a project that *you* control, then this may require using the
`Identity Management System`_ (IDM).

An official guide to the identity system used is available here_.

***********************************
 Applying for access using the IDM
***********************************

If possible, we recommend simply asking the project/dataset owner to add
you to the project or dataset in question, but the following provides a
brief summary of how to apply through the IDM:

1. Log in at identity.ku.dk_.
2. Click on the ``Manage My Access`` or the ``Manage User Access``
   button. Which button you see will depend on whether you own any
   groups yourself.

   1. If you clicked on the ``Manage User Access`` button then you must
      next search for your own UCPH username (e.g. ``abc123``) and then
      click on the check mark to the left your name *once*. Wait for the
      check mark to turn green, click the ``Next`` button, and then
      proceed with the steps described above.

3. Search for and locate the group corresponding to the resource you
   wish to access. Depending on the kind of resource you wish to apply
   for access to, the names will differ somewhat:

   1. A server group will typically start with the prefix ``SRV-`` and
      end with ``-users``, for example ``SRV-esrumhead-users`` for the
      Esrum head node.
   2. A project group will typically start with ``COMP-PRJ-``, for
      example ``COMP-PRJ-cbmr_shared`` for the ``/projects/cbmr_shared``
      project.
   3. A dataset group will typically start with ``COMP-DATASET-`` and
      end with ``-ro``, for example ``COMP-DATASET-cbmr_shared-ro`` for
      the ``/datasets/cbmr_shared`` dataset containing shared resources.

   .. warning::

       In general, you should *not* be applying for access to projects
       with suffixes like ``-Owners``, ``-admin``, or ``-rw`` unless
       explicitly told to do so by the owner(s) of those resources.
       These suffixes indicate administrative groups and your requests
       will therefore be denied if you apply without reason.

4. Click *once* on the check-mark to the left of the name of the group
   in the resulting list. Wait for the check mark to turn green and then
   click the ``Next`` button. If you get a yellow popup with the message
   ``Cannot Add Access Item. The item you are trying to select is
   already assigned``, then you have already been granted access to this
   resource.

   1. If you get a ``Select Role`` popup, asking you to ``Select the
      business role to assign to this permitted role.``, then we
      recommend that you pick a ``STAFF-ORG`` role from the list.

5. Finally, click the ``Submit`` button to submit your request.
6. Wait for your request to be processed.

***************************************
 Adding users to a group using the IDM
***************************************

1. Log in at identity.ku.dk_.
2. Click on the ``Manage User Access`` button. If you instead have a
   ``Manage My Access`` button, then you do not control access to any
   groups and will not able to carry out these steps.
3. Search for the username of the user you want to add to a group, click
   *once* on the check-mark to the left of the name of the user in the
   resulting list. Wait for the check mark to turn green and then click
   the ``Next`` button.
4. Search for and locate the group corresponding to the resource you
   wish to grant access to. See the corresponding step in the previous
   guide, for a brief description of how groups are named.
5. Click *once* on the check-mark to the left of the name of the group
   in the resulting list. Wait for the check mark to turn green and then
   click the ``Next`` button. See above if you get a ``Cannot Add Access
   Item.`` or a ``Select Role`` popup.
6. Finally, click the ``Submit`` button to submit your request.
7. Wait for your request to be processed.

.. _here: https://kunet.ku.dk/medarbejderguide/ITvejl/KU%20IdM%20-%20S%C3%A5dan%20anmodes%20om%20funktionsrolle.pdf

.. _identity management system: https://identity.ku.dk/

.. _identity.ku.dk: https://identity.ku.dk/
