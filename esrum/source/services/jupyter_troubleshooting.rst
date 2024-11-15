Jupyter Notebooks: Browser error when opening URL
=================================================

Depending on your browser you may receive one of the following errors.
The typical causes are listed, but the exact error message will depend
on your browser. It is therefore helpful to review all possible causes
listed here.

When using Chrome, the cause is typically listed below the line that
says "This site can't be reached".

-  "The connection was reset"

   This typically indicates that Jupyter Notebook isn't running on the
   server, or that it is running on a different port than the one you've
   forwarded. Check that Jupyter Notebook is running and make sure that
   your forwarded ports match those used by Jupyter Notebook on Esrum.

-  "Localhost refused to connect" or "Unable to connect"

   This typically indicates that port forwarding isn't active, or that
   you have entered the wrong port number in your browser. Verify that
   port forwarding is active and that you are using the correct port
   number in the ``localhost`` URL.

-  "Check if there is a typo in esrumweb01fl" or "We're having trouble
   finding that site"

   You are most likely connecting from a network outside UCPH. Make sure
   that you are using a wired connection at CBMR and/or that the VPN is
   activated and try again.
