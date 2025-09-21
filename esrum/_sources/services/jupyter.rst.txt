.. _p_service_jupyter:

###################
 Jupyter Notebooks
###################

`Jupyter Notebooks`_ are available via the module system on Esrum and
can be run on regular compute nodes or on the GPU/high-memory node,
depending on the kind of analyses you wish to run and the size of your
workload.

By default, Jupyter only includes support for Python notebooks, but
instructions are included :ref:`below <s_jupyter_kernels>` for how to
add support for R.

.. note::

   We are currently working on making Jupyter available along with the
   :ref:`s_service_rstudio`. We will announce when this service is
   ready.

*****************************
 Starting a Jupyter notebook
*****************************

To start a notebook on a node, run the following commands:

.. code-block:: console

   $ module load jupyter-notebook
   $ srun --pty -- jupyter notebook --no-browser --ip=0.0.0.0 --port=XXXXX

The number used in the argument ``--port=XXXXX`` must be a value in the
range 49152 to 65535, and must not be a number used by another user on
Esrum. The number shown here was randomly selected for you, and you can
refresh this page for a different suggestion.

.. raw:: html

   <noscript>
   <div class="admonition warning"><p class="admonition-title">Warning</p><p>A random port could not be selected, because Javascript is disabled. Please choose a number in the range 49152 to 65535, and use this number whenever the documentation says <code class="docutils literal notranslate"><span class="pre">XXXXX</span></code></p></div>
   </noscript>

This will allocate a single CPU and ~16 GB of RAM to your notebook. If
you need additional resources for your notebook, then please see the
:ref:`reserving_resources` section for instructions on how to reserve
additional CPUs and RAM, and the :ref:`p_usage_slurm_gpu` page for
instructions on how to reserve GPUs or large amounts of memory. The
``srun`` accepts the same options as ``sbatch``.

.. tip::

   It is recommended that you execute the ``srun`` command in a ``tmux``
   or ``screen`` session, to avoid the notebook shutting down if you
   lose connection to the head node. See :ref:`p_tips_tmux` for more
   information.

************************************
 Connecting to the Jupyter Notebook
************************************

To connect to the notebook server, you will first need to set up a
connection from your PC to the compute node on which your notebook is
running. This is called "port forwarding" and is described on the
:ref:`p_tips_forwarding` page.

However, to do so you must first determine on which compute node your
job is running. This can be done in a couple of ways:

-  Look for the URLs printed by Jupyter when you started it on Esrum:

   .. code-block:: text
      :emphasize-lines: 4

      To access the notebook, open this file in a browser:
          file:///home/abc123/.local/share/jupyter/runtime/nbserver-2082873-open.html
        Or copy and paste one of these URLs:
            http://esrumcmpn07fl.unicph.domain:XXXXX/?token=0123456789abcdefghijklmnopqrstuvwxyz
         or http://127.0.0.1:XXXXX/?token=0123456789abcdefghijklmnopqrstuvwxyz

   In this example, our notebook is running on the ``esrumcmpn07fl``
   node. All Esrum node names end with ``.unicph.domain``, but we do not
   need to include this part of the name.

-  Alternatively, run the following command on the head node in a
   separate terminal:

   .. code-block:: console

      $ squeue --me --name jupyter
      JOBID  PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
      551600 standardq  jupyter   abc123  R       8:49      1 esrumcmpn07fl

   By looking in the ``NODELIST`` column, we can see that the notebook
   is running on ``esrumcmpn07fl``, as above.

Once you've determined what node your notebook is running on, go to the
:ref:`p_tips_forwarding` page and setup port forwarding to that node and
the port you used when starting Jupyter (e.g. ``XXXXX``).

.. _s_jupyter_kernels:

*******************************
 Adding an R kernel to Jupyter
*******************************

The Jupyter module only comes with a Python kernel. If you instead wish
to use R in your Jupyter notebook, you can add an R Kernel for the
specific version of R that you wish to use.

To do so, run the following commands, replacing `R/4.3.3` with the
version of R that you wish to use:

.. code-block:: console

   $ module load jupyter-notebook/6.5.4
   $ module load --auto R/4.3.3
   $ R
   > install.packages('IRkernel')
   > name <- paste("ir", gsub("\\.", "", getRversion()), sep="")
   > displayname <- paste("R", getRversion())
   > IRkernel::installspec(name=name, displayname=displayname)
   > quit(save="no")

This will make an R kernel with the name ``R 4.3.3`` available in
Jupyter. You can repeat these commands for each version of R that you
wish to make available as a kernel. Run the command ``module purge``
between each, to ensure that you have loaded only the expected version
of R and ``gcc`` that R depends on.

Once you are done adding R versions, you start notebook as shown above:

.. code-block:: console

   $ module load jupyter-notebook/6.5.4
   $ srun --pty -- jupyter notebook --no-browser --port=XXXXX

While you do not need to load the R module first, if you only wish to
run R code, you must do so if you wish to install R libraries via the
notebook:

.. code-block:: console

   $ module load jupyter-notebook/6.5.4
   $ module load --auto R/4.3.3
   $ srun --pty -- jupyter notebook --no-browser --port=XXXXX

*****************
 Troubleshooting
*****************

.. include:: jupyter_troubleshooting.rst
   :start-line: 8

.. _jupyter notebooks: https://jupyter.org/

.. _rstudio: https://posit.co/products/open-source/rstudio/

.. raw:: html

   <script defer>
    document.addEventListener('DOMContentLoaded', function() {
      replaceTextContent(document.body, "XXXXX", getEphemeralPort());
    });
   </script>
