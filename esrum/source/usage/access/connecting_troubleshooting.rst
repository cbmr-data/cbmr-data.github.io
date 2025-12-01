######################################
 Dummy header to prevent reformatting
######################################

**************************************
 Dummy header to prevent reformatting
**************************************

If you have not already been granted access to the server, then please
see the :ref:`p_usage_access_applying` page before continuing!

Timeout while connecting to the cluster
=======================================

You may experience timeout errors when you attempt to connect to Esrum.

On Linux, this typically results in an ``Operation timed out`` message:

.. code-block:: console

   $ ssh abc123@esrumhead01fl.unicph.domain
   ssh: connect to host esrumhead01fl.unicph.domain port 22: Operation timed out

On Windows, using MobaXterm, it may result in a ``connection timed out``
message:

.. image:: /usage/access/images/connecting_mobaxterm_timeout.png
   :align: center

Firstly verify that you are correctly connected to the UCPH VPN. This is
required to connect to Esrum. See the :ref:`p_usage_connecting` page for
more information.

If you are still unable to connect to Esrum after verifying that you are
correctly connected to the UCPH network, then please try to visit either
our `Project Manager <https://cbmrcat.unicph.domain/projects/>`_ or our
`Cohort Catalog <https://cbmrcat.unicph.domain/>`_.

If you are able to visit either of the Project Manager or Cohort Catalog
pages, then you most likely do not have proper permissions to connect to
Esrum. Please :ref:`contact us <p_contact>` and we will provide further
guidance.

If you are unable to connect to the VPN or to either of the above pages
while connected to the VPN, then there may be other problems with your
account. We recommend that you either :ref:`contact us <p_contact>` for
assistance or, if you prefer, that you submit a ticket to the UCPH-IT
Serviceportal_, using the ``Research Applications Counseling and
Support`` / ``Forskningsapplikationer Rådgivning og support`` ticket
category.

File uploads using MobaXterm never start
========================================

Please make sure that your session is configured to use the ``SCP
(enhanced speed)`` browser type. See step 4 in the
:ref:`s_configure_mobaxterm` section.

Network-folders in ``~/ucph`` are not available
===============================================

Please make sure that you have disabled use of ``GSSAPI Kerberos`` as
described in the :ref:`s_configure_mobaxterm` section. Similarly, if
using Linux or OSX, then you cannot be authenticating using a Kerberos
ticket.

OpenConnect fails to perform two-factor authentication
======================================================

OpenConnect may fail to connect to the KU VPN when using the default
Configuration. In that case, when connecting, OpenConnect will make
several connection attempts, allow you to enter your password, and then
fail before you are able to use your two-factor authentication method:

.. code-block:: text

   POST https://vpn.ku.dk/
   Connected to 130.225.226.54:443
   SSL negotiation with vpn.ku.dk
   Connected to HTTPS on vpn.ku.dk with ciphersuite (TLS1.3)-(ECDHE-SECP256R1)-(RSA-PSS-RSAE-SHA256)-(AES-128-GCM)
   Got HTTP response: HTTP/1.1 404 Not Found
   Unexpected 404 result from server
   GET https://vpn.ku.dk/
   Connected to 130.225.226.54:443
   SSL negotiation with vpn.ku.dk
   Connected to HTTPS on vpn.ku.dk with ciphersuite (TLS1.3)-(ECDHE-SECP256R1)-(RSA-PSS-RSAE-SHA256)-(AES-128-GCM)
   Got HTTP response: HTTP/1.0 302 Temporary moved
   GET https://vpn.ku.dk/+webvpn+/index.html
   SSL negotiation with vpn.ku.dk
   Connected to HTTPS on vpn.ku.dk with ciphersuite (TLS1.3)-(ECDHE-SECP256R1)-(RSA-PSS-RSAE-SHA256)-(AES-128-GCM)
   Please enter your username and password.
   Password: ************
   POST https://vpn.ku.dk/+webvpn+/index.html
   Please enter the TOTP code generated on your device
   POST https://vpn.ku.dk/+webvpn+/login/challenge.html
   Please enter the TOTP code generated on your device
   POST https://vpn.ku.dk/+webvpn+/login/challenge.html
   Please enter the TOTP code generated on your device
   3 consecutive empty forms, aborting loop
   Failed to complete authentication

In this happens, then make sure that you are using the
``--useragent=AnyConnect --no-external-auth`` options as shown in the
:ref:`s_connecting_linux` section.

.. _danish: https://kunet.ku.dk/medarbejderguide/Sider/It/Fjernadgang-vpn.aspx

.. _english: https://kunet.ku.dk/employee-guide/Pages/IT/Remote-access.aspx

.. _serviceportal: https://serviceportal.ku.dk/
