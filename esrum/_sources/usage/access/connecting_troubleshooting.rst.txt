If have not already been granted access to the server, then please see
the :ref:`p_usage_access` page before continuing!

Timeout while connecting to the cluster
========================================

You may experience timeout errors when you attempt to connect to the
server:

.. image:: /usage/images/connecting_ssh_timeout.gif
   :class: gif

#. Firstly verify that you are correctly connected to the KU network:

   #. You must either use a wired connection while physically at CBMR.
   #. Or you must connect via the KU VPN.

   It is not possible to connect to using WIFI at CBMR nor is it
   possible to from outside of CBMR without the use of the VPN. See the
   official VPN documentation in Danish_ or English_ for more
   information.

#. If neither using a wired connection nor connecting the the KU VPN
   fixes the problem, you may need to create a support ticket to have KU
   IT permit you to connect to the server.

   #. Login to the KU `IT Serviceportal`_.

   #. Click the ``Create Ticket`` / ``Opret Sag`` button.

   #. Select the ``Research IT`` / ``Forsknings-IT`` category.

   #. Then select the ``Research Applications and Services`` /
      ``Forskningsapplikationer og Services`` subcategory.

   #. Finally, select ``Consultancy and Support`` / ``Rådgivning og
      support``.

   #. Write something like "SSH connection times out when attempting to
      connect to esrumhead01fl.unicph.domain" in the "Please describe"
      text-box and describe the steps you have taken to try to fix this
      problem: Tried wired connection at CBMR, tried VPN, etc.

   #. Write "esrumhead01fl.unicph.domain" in the System name text-box.

   #. Click the ``Add to cart`` button.

   #. Click the ``SUBMIT ORDER`` button.

.. warning::

   If you are not an employee at CBMR you may not have permission to
   open a ticket as described above. In that case simply
   :ref:`p_contact` us and we will forward your issue to KU-IT.


File uploads using MobaXterm never start
========================================

Please make sure that your session is configured to use the ``SCP
(enhanced speed)`` browser type. See step 4 in in the
:ref:`s_configure_mobaxterm` section.


KU network-folders in ``~/ucph`` are not available when using MobaXterm
=========================================================================

Please make sure that you have disabled use of ``GSSAPI Kerberos`` as
described in the :ref:`s_configure_mobaxterm` section.

.. _danish: https://kunet.ku.dk/medarbejderguide/Sider/It/Fjernadgang-vpn.aspx

.. _english: https://kunet.ku.dk/employee-guide/Pages/IT/Remote-access.aspx

.. _it serviceportal: https://serviceportal.ku.dk/
