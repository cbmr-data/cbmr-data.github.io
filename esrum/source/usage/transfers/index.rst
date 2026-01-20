.. _p_transfers:

###################
 Transferring data
###################

.. toctree::
   :hidden:

   internal
   external
   services
   misc

This section describes general methods and best practices for how to
transfer data to or from Esrum, as well as between different locations
*on* Esrum. In addition, advice is given for how to transfer data
between Esrum and a number of commonly used services.

.. warning::

   Data must not be copied out of audited ``/datasets`` or ``/projects``
   folders without permission from the relevant data controller. This is
   required for GDPR compliance. See the :ref:`p_guidelines` for more
   information.

Note that it is not possible to for a person without a KU account to
transfer data/to from Esrum. You furthermore must have been granted
access to Esrum and the projects, datasets, or network drives from/to
which you wish to transfer data. See the :ref:`p_usage_access_applying`
page for more information.

.. warning::

   Because large transfers can negatively impact other users of Esrum,
   we may terminate any transfer that is not done in accordance with
   this guide.

To get started, please follow the link corresponding to where your data
is located and to where you want to transfer it:

-  **My data is located on Esrum or on a network drive (H:, N:, S:)**
      -  I want to :ref:`copy data between projects or datasets
         <p_transfer_projects_datasets>`
      -  I want to :ref:`copy data to/from a network drive (H:, N:, S:)
         <p_transfer_network_drives>`
      -  I want to :ref:`copy instrument data (/labs)
         <s_transfer_instruments>`
      -  I want to :ref:`copy data to/from another UCPH cluster
         <s_sharing_projects>`
      -  I want to :ref:`download data from Esrum
         <s_external_updownload>`
      -  I want to :ref:`copy data to SIF or ERDA
         <s_transfers_sif_erda>`
      -  I want to :ref:`copy data to Computerome
         <p_transfers_computerome>`
      -  I want to :ref:`copy data to another (Linux) server
         <s_external_updownload>`

-  **My data is located somewhere else**
      -  My :ref:`data is located on another UCPH cluster
         <s_sharing_projects>`
      -  My :ref:`data is located on SIF or ERDA
         <s_transfers_sif_erda>`.
      -  My data is located on Google Drive.
      -  My data is located on AWS.
      -  My :ref:`data is located on a laptop or desktop
         <s_transfer_from_external>`
      -  My :ref:`data is located on Computerome
         <p_transfers_computerome>`
      -  My :ref:`data is located on another server
         <s_external_updownload>`

-  **Miscellaneous**
      -  I want to :ref:`email large files <s_transfers_bluewhale>`

You are always welcome to :ref:`contact us <p_contact>` if the above
does not cover your needs.

..
   *****
   Old
   *****

   -  I want to transfer data Esrum and my computer or another server
       -  I want to transfer data to/from my home folder
       -  I want to transfer data to/from projects, datasets, or network
           drives

   -  I want to transfer data from one location on Esrum to another
   location on Esrum

   -  I want to transfer data between home folders, projects and/or
       datasets
   -  I want to transfer data to/from network drives (``H:``, ``N:``,
       ``S:``)

   -  I want to transfer data to/from other service
       -  Computerome
       -  Erda or SIF
       -  Google Cloud

   -  I want to email large files
       -  Bluewhale

   This section describes how to perform bulk data transfers between Esrum,
   your PC/Laptop, repositories such as SIF/ERDA, and servers like
   Computerome. .

   File transfers (including project-to-project transfers) should, if at
   all possible, be run on a compute node, as high amounts of network
   traffic on the head node may impact all users of Esrum. This can be done
   using either a :ref:`sbatch script <p_usage_slurm_basics>`, :ref:`srun
   <p_usage_srun>` commands, or an :ref:`interactive session
   <s_interactive_session>` on a compute node.

   .. warning::

   Transfers running on the head node may be terminated without warning
   if they are found to impact the usability of the system.

   If you have an existing compute project or dataset on a UCPH-IT managed
   cluster, then you may be able to connect it directly to the Esrum
   cluster and thereby remove the need for transferring data entirely.
   Please :ref:`contact us <p_contact>` for more information.

   .. warning::

   Data must not be copied out of audited ``/datasets`` or ``/projects``
   folders without permission from the relevant data controller. This is
   required for GDPR compliance. See the :ref:`p_guidelines` for more
   information.

.. _official computerome documentation: https://www.computerome.dk/wiki/high-performance-computing-hpc/file-transfer

.. _ucph computing/hpc systems: https://kunet.ku.dk/work-areas/research/Research%20Infrastructure/research-it/ucph-computing-hpc-systems/Pages/default.aspx

.. _ucph two-factor authentication: https://mfa.ku.dk/
