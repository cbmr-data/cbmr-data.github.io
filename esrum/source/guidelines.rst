.. _p_guidelines:

#########################
 Guidelines and policies
#########################

The following describes the general guidelines for using the Esrum
cluster. Failure to follow these guidelines may result in your tasks
being terminated and may even result in your access to the cluster being
revoked.

Please also see the general KU resources for handling `GDPR sensitive
data`_.

****************
 Basic security
****************

-  Your account on Esrum is strictly personal and must not be shared.
-  Never leave your computer unsecured while logged onto the cluster.
   Your computer *must* be locked or turned off whenever you leave it.

**************
 Data storage
**************

-  GDPR protected data *must* be stored in audited folders. These can be
   recognized by the ``-AUDIT`` suffix, for example
   ``/projects/name-AUDIT`` or ``/datasets/name-AUDIT``.

-  Directory names and file names *must not* contain GDPR protected data
   or other confidential information, even if placed in an audited
   folder. This is because common operations expose this information to
   *all* users of the cluster. For the same reason, *do not* include
   such information in command-line arguments.

-  Data *must not* be copied out of audited ``/datasets`` or
   ``/projects`` folders without permission from the relevant data
   controller. Instead use symbolic links if you need the data to be
   located in a more convenient location.

-  Data must not leave the cluster without permission from the relevant
   data controllers.

-  Do not store data or other files related to projects in your home
   folder. Your home folder is accessible only to you, unless you have
   provided written consent to KU-IT.

See :ref:`p_usage_filesystem` for more information.

***************
 Running tasks
***************

-  Do not run big jobs on the head node (``esrumhead01fl``), as doing so
   may impact the ability of everyone to use the cluster. However, we do
   permit small jobs on the head node, meaning a few cores *in total*
   and modest memory usage.

-  Remember to be considerate to other users. For example, limit the
   number of jobs you are running simultaneously, so that others users
   can also run their jobs

-  Please remember to close interactive shells, notebooks, containers,
   and other processes that you have started via Slurm or the container
   system. Resources that you have reserved are not made available for
   other users until your tasks have finished.

See the :ref:`p_usage_slurm` page for more information about how to run
your tasks on the cluster.

***********************************
 Access to protected data by staff
***********************************

Access to protected data may be required for maintenance, data
processing, formatting, storage, indexing, curation, or to provide other
services requested from the Data Analytics Platform (DAP).

When this need arises, DAP will either

-  grant access to the relevant staff member(s), for an appropriate time
   period, after notifying the data owner. This applies to datasets and
   projects directly administrated by DAP.

-  request access to the datasets and/or projects, using the `Identity
   Management system`_. This applies to datasets and projects *not*
   administrated by DAP.

A formal data access request will also be made in cases where DAP staff
member participate in the scientific exploitation of protected data,
beyond that required to fulfill technical or service functions.

Immediate intervention under the supervision of a user with appropriate
access to protected data, for example while providing direct support, is
not considered to establish privileged access.

.. _gdpr sensitive data: https://kunet.ku.dk/work-areas/research/data/personal-data/Pages/default.aspx

.. _identity management system: https://identity.ku.dk
