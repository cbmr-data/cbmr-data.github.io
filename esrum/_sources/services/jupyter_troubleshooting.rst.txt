Jupyter Notebooks: Browser error when opening URL
=================================================

Depending on your browser you may receive one of the following errors.
The typical causes are listed, but the exact error message will depend
on your browser. It is therefore helpful to review all possible causes
listed here.

When using Chrome, the cause is typically listed below the line that
says "This site can't be reached".

-  ``The connection was reset``

   This typically indicates that Jupyter Notebook isn't running on the
   server, or that it is running on a different port than the one you've
   forwarded. Check that Jupyter Notebook is running and make sure that
   your forwarded ports match those used by Jupyter Notebook on Esrum.

-  ``Localhost refused to connect`` or ``Unable to connect``

   This typically indicates that port forwarding isn't active, or that
   you have entered the wrong port number in your browser. Therefore,

   -  Verify that port forwarding is active: On OSX/Linux that means
      verifying that an ``ssh`` command is running as described in the
      :ref:`s_ports_osx_linux` section, and on Windows that means
      activating port forwarding in MobaXterm as described in the
      :ref:`s_ports_windows` section.

   -  If using the instructions for Linux/OSX, verify that you ran the
      ``ssh`` command on your laptop or desktop, and *not* on the Esrum
      head node.

   -  Verify that either of these are using the same port number as in
      the ``jupyter`` command you ran or as in the ``http://127.0.0.1``
      URL printed by Jupyter.

   -  Verify that you are using the *second* URL that Jupyter prints on
      the terminal, namely the URL starting with
      ``http://127.0.0.1:XXXX``:

      .. code-block:: text
         :emphasize-lines: 5

         To access the notebook, open this file in a browser:
             file:///home/abc123/.local/share/jupyter/runtime/nbserver-2082873-open.html
             Or copy and paste one of these URLs:
                 http://esrumcmpn07fl.unicph.domain:XXXXX/?token=0123456789abcdefghijklmnopqrstuvwxyz
             or http://127.0.0.1:XXXXX/?token=0123456789abcdefghijklmnopqrstuvwxyz

      For security reasons it is not possible to connect directly to the
      compute nodes.
